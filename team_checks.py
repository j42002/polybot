"""Three free teammates, implemented as deterministic Python checks (no paid AI, $0, read-only).

- Data Auditor:  gaps, duplicates, missing quotes, invalid samples, settlement mismatches
- Quant Analyst: sample size, uncertainty (Wilson intervals), win rate vs break-even, model vs market
- Risk Sentinel: leaked credentials, real-order capability, paid APIs, frozen model, workflow failures

Writes lab/checks/latest.md and posts one card per role to #research-reports (DISCORD_RESEARCH_WEBHOOK,
else DISCORD_TEAM_WEBHOOK; never the #polybot ticket webhook). A role is "active" only after a real
successful run. Never changes experiments, data or settings.
"""
import csv
import math
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

import requests

DATA = "data"
OUT = os.path.join("lab", "checks")
HOOK = os.getenv("DISCORD_RESEARCH_WEBHOOK") or os.getenv("DISCORD_TEAM_WEBHOOK", "")
REPO = os.getenv("GITHUB_REPOSITORY", "j42002/polybot")
TOKEN = os.getenv("GITHUB_TOKEN", "")
EXP_MIN = 18


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ver(r):
    m = re.search(r"v(\d+)", str(r.get("version") or ""))
    return int(m.group(1)) if m else 0


def ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


# ---------------- Data Auditor ----------------

def data_auditor(now=None):
    now = now or datetime.now(timezone.utc)
    day = now - timedelta(hours=24)
    out, worst = [], "ok"

    def flag(level, msg):
        nonlocal worst
        order = {"ok": 0, "warn": 1, "fail": 2}
        if order[level] > order[worst]:
            worst = level
        out.append(("✅" if level == "ok" else "⚠️" if level == "warn" else "❌") + " " + msg)

    cp = [r for r in rows(os.path.join(DATA, "checkpoints.csv")) if ver(r) >= EXP_MIN]
    recent = [r for r in cp if (ts(r.get("logged_utc")) or now - timedelta(days=9)) >= day]
    slugs = {r["slug"] for r in recent}
    cover = len(slugs) / 288
    flag("ok" if cover >= 0.8 else "warn" if cover >= 0.4 else "fail",
         f"5m rounds observed in the last 24h: {len(slugs)}/288 ({cover:.0%})")
    keys = [(r["slug"], r.get("secs_left")) for r in cp]
    dup = len(keys) - len(set(keys))
    flag("ok" if dup == 0 else "warn", f"duplicate checkpoint rows (v{EXP_MIN}+): {dup}")
    if recent:
        noq = sum(r.get("quote_src") == "error" for r in recent)
        flag("ok" if noq / len(recent) < 0.05 else "warn" if noq / len(recent) < 0.2 else "fail",
             f"checks with no market quote (24h): {noq}/{len(recent)}")
    bad_ts = sum(ts(r.get("logged_utc")) is None for r in cp)
    flag("ok" if bad_ts == 0 else "warn", f"rows with unreadable timestamps: {bad_ts}")
    closes = [r for r in rows(os.path.join(DATA, "closes.csv")) if ver(r) >= EXP_MIN]
    if closes:
        inval = sum(str(r.get("cb_valid")) != "True" for r in closes)
        flag("ok" if inval / len(closes) < 0.1 else "warn", f"close samples with gaps (>6s hole or <20 samples): {inval}/{len(closes)}")
    t = [r for r in rows(os.path.join(DATA, "tickets.csv")) if ver(r) >= EXP_MIN]
    undeliv = sum(r.get("status") == "UNDELIVERED" for r in t)
    flag("ok" if undeliv == 0 else "warn", f"alerts that failed delivery (v{EXP_MIN}+): {undeliv}/{len(t)}")
    ls = [r for r in rows(os.path.join(DATA, "loop_stats.csv")) if ver(r) >= EXP_MIN]
    if ls:
        stalls = sum(int(float(r.get("stalls_5s") or 0)) for r in ls[-24:])
        gap = max(float(r.get("max_spot_gap_s") or 0) for r in ls[-24:])
        flag("ok" if stalls == 0 and gap <= 6 else "warn", f"loop stalls >5s (last runs): {stalls} · longest BTC price gap {gap:.1f}s")
    m15 = rows(os.path.join(DATA, "15m", "markets.csv"))
    if m15:
        mism = sum(r.get("settle_check") == "MISMATCH" for r in m15)
        nocandle = sum(r.get("candle_status") not in ("ok", "") for r in m15)
        flag("ok" if mism == 0 else "fail", f"15m backtest settlement mismatches: {mism}/{len(m15)}")
        flag("ok" if nocandle / len(m15) < 0.05 else "warn", f"15m markets without a usable candle: {nocandle}/{len(m15)}")
    return worst, out


# ---------------- Quant Analyst ----------------

def quant_analyst():
    out, worst = [], "ok"
    t = [r for r in rows(os.path.join(DATA, "tickets.csv")) if ver(r) >= EXP_MIN]
    trades = [r for r in t if r.get("result") in ("WIN", "LOSS")]
    n, k = len(trades), sum(r["result"] == "WIN" for r in trades)
    if n:
        lo, hi = wilson(k, n)
        be = sum(float(r["fill_price"]) * (1 + 0.095 * (1 - float(r["fill_price"]))) for r in trades if r.get("fill_price")) / n
        pnl = sum(float(r.get("pnl10") or 0) for r in trades)
        verdict = ("win rate is above break-even with 95% confidence" if lo > be else
                   "win rate is below break-even with 95% confidence" if hi < be else "can't tell yet: break-even is inside the range")
        out.append(f"5m experiment: {n} simulated trades, win rate {k / n:.0%} (95% range {lo:.0%}–{hi:.0%}) vs break-even {be:.0%} → {verdict}")
        out.append(f"5m paper P&L after fees: {pnl:+.2f} at $10/trade · progress {len({r['slug'] for r in trades})}/300 separate rounds")
    else:
        out.append("5m experiment: no simulated trades yet in v18+, so nothing to judge.")
    if n < 100:
        out.append(f"⚠️ Sample too small for any conclusion (n={n}; under ~100 trades a 10-point swing in win rate is noise).")
        worst = "warn"
    rep = os.path.join(DATA, "15m", "report.md")
    if os.path.exists(rep):
        txt = open(rep, encoding="utf-8").read()
        m = re.search(r"## Primary: AGREE.*?\n\|[^\n]*\n\|[^\n]*\n(\|[^\n]*\|)", txt, re.S)
        if m:
            out.append("15m Phase 1 primary row (exploratory): " + m.group(1))
        out.append("Reminder: historical results are exploratory; only the forward test can confirm. Secondary rules carry multiple-testing risk.")
    else:
        out.append("15m Phase 1: report not published yet.")
    return worst, out


# ---------------- Risk Sentinel ----------------

SECRET_PATTERNS = [
    (r"discord(?:app)?\.com/api/webhooks/\d+/[\w-]{20,}", "Discord webhook URL"),
    (r"\bsk-[A-Za-z0-9]{20,}", "OpenAI-style key"),
    (r"\bsk-ant-[A-Za-z0-9-]{20,}", "Anthropic key"),
    (r"\bAIza[0-9A-Za-z_-]{30,}", "Google API key"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
    (r"\bghp_[A-Za-z0-9]{30,}", "GitHub token"),
]
ORDER_PATTERNS = [r"/orders?\b[^\n]*\b(post|put)\b", r"\bplace_order\b", r"\bcreate_order\b", r"\bsubmit_order\b",
                  r"session\.(post|put)\([^)]*/(v1/)?orders"]


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    except Exception:
        out = []
    return [f for f in out if not f.startswith("data/") or f.endswith((".md", ".json"))]


def webhook_routing(session=None):
    """Ask Discord which channel each webhook points at. GET on a webhook URL only reads its info; it never posts.
    Expected channel IDs live in lab/channels.json (IDs aren't secret). The URLs are never printed."""
    try:
        want = json.load(open(os.path.join("lab", "channels.json"), encoding="utf-8"))
    except Exception:
        return [("warn", "webhook routing not checked (lab/channels.json missing)")]
    s, res = session or requests, []
    for env, exp in want.items():
        if env.startswith("_"):
            continue
        url = os.getenv(env, "")
        if not url:
            res.append(("warn", f"{exp['channel']}: {env} not available to this check"))
            continue
        try:
            got = str(s.get(url, timeout=10).json().get("channel_id", ""))
        except Exception as e:
            res.append(("warn", f"{exp['channel']}: couldn't read webhook ({e.__class__.__name__})"))
            continue
        res.append(("ok", f"{env} → #{exp['channel']} (verified with Discord)") if got == exp["id"] else
                   ("fail", f"{env} points at the WRONG channel (id {got or '?'}, expected #{exp['channel']})"))
    return res


def risk_sentinel(session=None):
    out, worst = [], "ok"

    def flag(level, msg):
        nonlocal worst
        order = {"ok": 0, "warn": 1, "fail": 2}
        if order[level] > order[worst]:
            worst = level
        out.append(("✅" if level == "ok" else "⚠️" if level == "warn" else "❌") + " " + msg)

    leaks, orders = [], []
    for f in tracked_files():
        if f == "team_checks.py":
            continue
        try:
            txt = open(f, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        for pat, name in SECRET_PATTERNS:
            if re.search(pat, txt):
                leaks.append(f"{name} in {f}")
        if f.endswith(".py"):
            for pat in ORDER_PATTERNS:
                if re.search(pat, txt, re.I):
                    orders.append(f)
                    break
    flag("ok" if not leaks else "fail", "no credentials committed to the repo" if not leaks else "POSSIBLE LEAK: " + "; ".join(leaks))
    flag("ok" if not orders else "fail", "no code that places real orders" if not orders else "order-placing code found in: " + ", ".join(sorted(set(orders))))
    wf = ""
    for f in os.listdir(".github/workflows") if os.path.isdir(".github/workflows") else []:
        wf += open(os.path.join(".github/workflows", f), encoding="utf-8").read()
    paid = [k for k in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "PERPLEXITY_API_KEY", "XAI_API_KEY", "GROK_API_KEY") if k in wf]
    flag("ok" if not paid else "fail", "no paid AI API keys used by any workflow ($0)" if not paid else "paid API keys referenced: " + ", ".join(paid))
    acct = "POLYMARKET_KEY_ID" in wf or "POLYMARKET_SECRET_KEY" in wf or "ACCOUNT_WATCH" in wf
    flag("ok" if not acct else "fail", "account access off (no Polymarket keys in workflows)" if not acct else "Polymarket account keys referenced in a workflow")
    try:
        src = open("agent.py", encoding="utf-8").read()
        frozen = re.search(r"^MODEL_FROZEN\s*=\s*True", src, re.M) is not None
    except Exception:
        frozen = False
    flag("ok" if frozen else "fail", "5m model still frozen (MODEL_FROZEN = True)" if frozen else "5m model is NOT frozen")
    try:
        relay = open("relay.py", encoding="utf-8").read()
        leak = re.search(r'getenv\(\s*"DISCORD_WEBHOOK"', relay) is not None
    except Exception:
        leak = False
    flag("ok" if not leak else "fail", "team relay can't post into the #polybot ticket channel" if not leak else "relay reads the ticket webhook")
    for level, msg in webhook_routing(session):
        flag(level, msg)
    if TOKEN:
        try:
            since = (datetime.now(timezone.utc) - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
            s = session or requests
            r = s.get(f"https://api.github.com/repos/{REPO}/actions/runs", timeout=20,
                      headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"},
                      params={"created": f">={since}", "per_page": 100})
            runs = r.json().get("workflow_runs", [])
            failed = [x["name"] for x in runs if x.get("conclusion") == "failure"]
            flag("ok" if not failed else "warn", f"workflow runs in 24h: {len(runs)}, failed: {len(failed)}"
                 + (f" ({', '.join(sorted(set(failed)))})" if failed else ""))
        except Exception as e:
            flag("warn", f"couldn't read workflow runs ({e.__class__.__name__})")
    return worst, out


# ---------------- report ----------------

ROLES = [("Data Auditor", data_auditor), ("Quant Analyst", quant_analyst), ("Risk Sentinel", risk_sentinel)]
ICON = {"ok": "🟢", "warn": "🟡", "fail": "🔴"}


def main():
    os.makedirs(OUT, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md = [f"# Team checks · {now}", "", "Deterministic Python checks, $0, read-only.", ""]
    results = []
    for name, fn in ROLES:
        try:
            worst, lines = fn()
        except Exception as e:
            worst, lines = "fail", [f"❌ check crashed: {e!r}"]
        results.append((name, worst, lines))
        md += [f"## {ICON[worst]} {name}", ""] + [f"- {l}" for l in lines] + [""]
    with open(os.path.join(OUT, "latest.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("\n".join(md))
    if not HOOK:
        print("team checks: no DISCORD_RESEARCH_WEBHOOK / DISCORD_TEAM_WEBHOOK, report written to lab/checks/latest.md only")
        return
    for name, worst, lines in results:
        r = requests.post(HOOK, json={"username": name, "embeds": [{
            "title": f"{ICON[worst]} {name} · {now}", "description": "\n".join(lines)[:3900],
            "color": {"ok": 0x2ECC71, "warn": 0xF1C40F, "fail": 0xE74C3C}[worst],
            "footer": {"text": "Free automated check · read-only · $0"}}]}, timeout=10)
        print(f"team checks: {name} -> Discord {r.status_code}")


if __name__ == "__main__":
    main()
