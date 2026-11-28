"""Polybot HQ specialist agents: deterministic, read-only research checks. $0, no AI calls, no keys.

Founder-approved expansion (issues #11, #8, #2; 2026-11-27). Overlapping roles are folded together, so 16 names +
6 reliability features run as 13 checks inside the existing team-checks workflow (no new schedule):

  Velocity  (+ Expiration Guard)                 latency, quote lifetime, deadline vs later crossings
  Titan     (+ Liquidity Intelligence)           size availability, through-volume, quote freshness
  Ghost     (+ Market Stability Monitor: data)   anomalies and missing data in public market feeds
  Hawk      (+ Market Stability Monitor: regime) descriptive results by volatility / momentum regime
  Judge     (+ Confidence Auditor, Profit Validator)  independent stats, calibration, simulated-vs-executable
  Nemesis   (+ Loss Intelligence)                red-team challenges and a root-cause table of every loss
  Oracle                                         stress tests: what if the signal reverts to its history?
  Chronos                                        coverage timeline, gaps, versions, data provenance
  Mirror                                         venue definitions (fees, settlement) Kalshi vs Polymarket US
  Overwatch (+ Mechanic)                         workflow failures, data freshness, relay queue health
  Genesis                                        pre-registration template + validator for every PREREG
  Evolution                                      proposal-only hypotheses from measured patterns (never tested here)
  Cortex    (+ Archive, Nexus)                   shared registry (lab/agents/status.json) for the vault and relay

Status rule (no synthetic claims of activity): 🟢 only if the agent's synthetic-failure self-test passed in THIS run
AND its check ran on real data in THIS run. 🔵 = partly built, 🟡 = pending, 🔴 = blocked (reason given).
Nothing here changes a strategy, rule, model, order or experiment. Writes only lab/agents/.

  python hq_agents.py          self-tests + all checks, writes lab/agents/{report.md,status.json}, posts ONE card
  python hq_agents.py test     self-tests only
"""
import csv
import json
import math
import os
import random
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

import requests

OUT = os.path.join("lab", "agents")
REPO = os.getenv("GITHUB_REPOSITORY", "j42002/polybot")
TOKEN = os.getenv("GITHUB_TOKEN", "")
HOOK = os.getenv("DISCORD_RESEARCH_WEBHOOK") or os.getenv("DISCORD_TEAM_WEBHOOK", "")   # never the ticket webhook
US_FEE = 0.095            # Polymarket US fee coefficient (5m tickets)
KALSHI_TAKER = 0.07       # Kalshi quadratic taker coefficient
KALSHI_MAKER = 0.0175     # Kalshi maker coefficient (only on listed series)
NOW = time.time()


# ---------------------------------------------------------------- helpers

def rows(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def ver(r):
    m = re.search(r"v(\d+)", str(r.get("version") or ""))
    return int(m.group(1)) if m else 0


def wilson(k, n, z=1.96):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def boot(groups, stat, reps=3000, seed=7):
    """Block bootstrap over whole groups. Needs 5+ groups, otherwise an interval is meaningless."""
    keys = [k for k in groups if groups[k]]
    if len(keys) < 5:
        return None
    rnd = random.Random(seed)
    vals = sorted(v for v in (stat([x for k in rnd.choices(keys, k=len(keys)) for x in groups[k]]) for _ in range(reps))
                  if v is not None)
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def tercile(vals):
    s = sorted(v for v in vals if v is not None)
    if len(s) < 3:
        return None
    return s[len(s) // 3], s[2 * len(s) // 3]


def et_hour(t):
    return (datetime.fromtimestamp(int(t), timezone.utc).hour - 5) % 24


def fmt_ci(ci, f="{:+.2f}"):
    return (f.format(ci[0]) + " to " + f.format(ci[1])) if ci else "not shown (needs 5+ independent blocks)"


def pct(x):
    return f"{100 * x:.0f}%"


# ---------------------------------------------------------------- data

def load():
    W = {r["slug"]: (r.get("winner") or "").lower() for r in rows("data/results.csv")}
    t = [r for r in rows("data/tickets.csv") if ver(r) >= 18 and r.get("status") != "UNDELIVERED"]
    d = {"winner": W, "tickets": t, "cps": [r for r in rows("data/checkpoints.csv") if ver(r) >= 18],
         "loops": [r for r in rows("data/loop_stats.csv") if ver(r) >= 18], "closes": rows("data/closes.csv"),
         "results": rows("data/results.csv"), "m15": rows("data/maker15/orders.csv"),
         "audit": rows("data/maker15_audit/audit.csv"), "r15": read("data/15m/report.md"),
         "mirror_q": rows("data/mirror15/quotes.csv"),
         "prereg": {"15m Phase 1": read("data/15m/PREREG.md"), "maker15": read("data/maker15/PREREG.md")},
         "relay": json.loads(read("lab/relay_state.json") or "{}")}
    return d


def right(r, W):
    return W.get(r.get("slug")) == (r.get("side") or "").lower()


def m15_posted(d):
    return [r for r in d["m15"] if r.get("status") in ("FILLED", "UNFILLED", "PARTIAL")]


def m15_pnl(rs):
    return sum(num(r["pnl"]) or 0 for r in rs if r["status"] == "FILLED")


# ---------------------------------------------------------------- agents (each returns a result dict)

def velocity(d):
    """Latency, quote lifetime, Expiration Guard: is the 30s paper deadline applied consistently?"""
    t = [r for r in d["tickets"] if r.get("status_30")]
    first = Counter(r.get("expired_s") or "none by 60s" for r in t)
    after = [r for r in t if r.get("expired_s") in ("45", "60")]
    bad = [r for r in t if r.get("expired_s") in ("45", "60") and r.get("status_30") == "EXPIRED"
           and (num(r.get("ask_30")) or 0) <= (num(r.get("max_price")) or 0)]
    late = [num(r.get("ask_30_at")) - 30 for r in t if num(r.get("ask_30_at")) is not None]
    miss30 = sum(1 for r in d["tickets"] if r.get("ask_30_at") in ("", None) and r.get("status_30"))
    lag = [num(r.get("discord_ms")) for r in d["tickets"] if num(r.get("discord_ms")) is not None]
    W = d["winner"]
    g = [r for r in t if W.get(r["slug"]) in ("up", "down")]
    same = [r for r in g if all(r.get(f"status_{x}") == "FILLABLE" for x in (5, 10, 20, 30))]
    drop = [r for r in g if r.get("status_5") == "FILLABLE" and r.get("status_30") != "FILLABLE"]
    lines = [f"Delivered alerts watched: {len(t)} · first price-crossing slot: "
             + ", ".join(f"{k}s {v}" if k != "none by 60s" else f"none {v}" for k, v in sorted(first.items(), key=lambda kv: (kv[0] == 'none by 60s', num(kv[0]) or 0))),
             f"Crossed only after the 30s deadline (45/60s): {len(after)} · of those scored EXPIRED at 30s despite a 30s ask under the cap: **{len(bad)}** (must be 0)",
             f"30s check lateness: worst {max(late):+.2f}s (trusted up to +3s) · rows with no 30s check: {miss30}" if late else "No 30s checks yet",
             f"Discord delivery: median {statistics.median(lag):.0f} ms, worst {max(lag):.0f} ms" if lag else "No delivery timings",
             (f"Picks right {sum(right(r, W) for r in g)}/{len(g)} · same {len(same)} tickets at every delay: "
              + " · ".join(f"{x}s {sum(num(r.get(f'pnl10_{x}')) or 0 for r in same):+.2f}" for x in (5, 10, 20, 30))
              + f" · dropouts 5s→30s: {len(drop)} (right {sum(right(r, W) for r in drop)})") if g else "No settled alerts yet",
             "v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.",
             "v21 (Nov 28): wording only: 'model estimate' instead of 'win chance', no buy-now language, paper window close time on the card."]
    return {"ok": True, "lines": lines, "flags": len(bad), "data_n": len(t)}


def titan(d):
    """Liquidity and execution realism: are sizes known, are fills backed by volume, are quotes fresh?"""
    t = [r for r in d["tickets"] if r.get("status_30")]
    sz = Counter("size logged" if num(r.get("ask_size_30")) is not None else "no size" for r in t)
    ok30 = Counter(str(r.get("size_ok_30") or "blank") for r in t)
    P = m15_posted(d)
    F = [r for r in P if r["status"] == "FILLED"]
    ratio = sorted((num(r["through_vol"]) or 0) / int(r["contracts"]) for r in F if r.get("contracts"))
    A = d["audit"]
    stale = sum("QUOTE_FAR" in (a.get("flags") or "") for a in A)
    mk = sum("MARKETABLE" in (a.get("flags") or "") for a in A)
    lines = [f"5m: 30s ask size logged on {sz.get('size logged', 0)}/{len(t)} alerts · size >= $10 at 30s: {ok30.get('True', 0)} yes / "
             f"{ok30.get('False', 0)} no / {ok30.get('blank', 0)} unknown. **Size units are not verified against the app, so 5m P&L is quote-availability only.**",
             f"Maker: through-volume / order size on fills: min {ratio[0]:.0f}x, median {ratio[len(ratio) // 2]:.0f}x (volume never the constraint)" if ratio else "Maker: no fills yet",
             f"Maker quote freshness (from the read-only audit): recorded ask >5c from same-second prints on {stale}/{len(A)} orders; "
             f"marketable at post {mk}/{len(A)}" if A else "Maker audit not run yet"]
    return {"ok": True, "lines": lines, "flags": stale + mk, "data_n": len(t) + len(P)}


def ghost(d):
    """Anomalies and missing data in public feeds (market data only, never people)."""
    cps = d["cps"]
    noq = sum(r.get("quote_src") == "error" for r in cps)
    pair = [num(r.get("pair_sum")) for r in cps if num(r.get("pair_sum")) is not None]
    odd_pair = sum(1 for p in pair if not 0.95 <= p <= 1.15)
    W = d["winner"]
    res = {r["slug"]: r for r in d["results"]}
    mism = n = 0
    for c in d["closes"]:
        r = res.get(c.get("slug"))
        if not r or c.get("cb_valid") != "True" or num(c.get("cb_avg_last60")) is None or num(r.get("ptb_true")) is None:
            continue
        n += 1
        cb_up = num(c["cb_avg_last60"]) > num(r["ptb_true"])
        mism += cb_up != (W.get(r["slug"]) == "up")
    gaps = [num(r.get("max_spot_gap_s")) for r in d["loops"] if num(r.get("max_spot_gap_s")) is not None]
    big_gap = sum(g > 10 for g in gaps)
    A = d["audit"]
    lines = [f"5m checks with no market quote: {noq}/{len(cps)} ({noq / len(cps):.1%})" if cps else "No checkpoints",
             f"Up+Down asks outside 0.95-1.15 (broken or stale book): {odd_pair}/{len(pair)}",
             f"Coinbase proxy disagrees with the official settlement: {mism}/{n} rounds (proxy only; official winner is used for scoring)",
             f"Runs whose longest BTC price gap exceeded 10s: {big_gap}/{len(gaps)}",
             f"Maker: stale recorded quotes {sum('QUOTE_FAR' in (a.get('flags') or '') for a in A)}/{len(A)} (see Titan)" if A else "Maker audit not run yet"]
    return {"ok": True, "lines": lines, "flags": odd_pair + big_gap, "data_n": len(cps)}


def hawk(d):
    """Descriptive regime splits with counts. Not a signal; nothing adapts to this."""
    P = m15_posted(d)
    out = []
    mom = [abs((num(r["btc_T"]) or 0) - (num(r["btc_T60"]) or 0)) for r in P]
    dist = [abs((num(r["btc_T"]) or 0) - (num(r["target"]) or 0)) for r in P]
    for name, vals in (("1-min BTC move", mom), ("distance to target", dist)):
        cuts = tercile(vals)
        if not cuts:
            continue
        for lab, f in (("low", lambda v: v <= cuts[0]), ("mid", lambda v: cuts[0] < v <= cuts[1]), ("high", lambda v: v > cuts[1])):
            cell = [r for r, v in zip(P, vals) if f(v)]
            fs = [r for r in cell if r["status"] == "FILLED"]
            out.append(f"| maker | {name} {lab} | {len(cell)} | {len(fs)} | "
                       f"{(pct(sum(r['won'] == '1' for r in fs) / len(fs)) if fs else '-')} | {m15_pnl(cell) / len(cell):+.2f} |")
    W = d["winner"]
    sig = {}
    for c in d["cps"]:
        sig.setdefault(c["slug"], num(c.get("sigma")))
    t = [r for r in d["tickets"] if W.get(r["slug"]) in ("up", "down") and sig.get(r["slug"]) is not None]
    cuts = tercile([sig[r["slug"]] for r in t])
    if cuts:
        for lab, f in (("low", lambda v: v <= cuts[0]), ("mid", lambda v: cuts[0] < v <= cuts[1]), ("high", lambda v: v > cuts[1])):
            cell = [r for r in t if f(sig[r["slug"]])]
            fill = [r for r in cell if r.get("status_30") == "FILLABLE"]
            out.append(f"| 5m | BTC volatility {lab} | {len(cell)} alerts | {len(fill)} buyable at 30s | "
                       f"picks right {pct(sum(right(r, W) for r in cell) / len(cell))} | "
                       f"{sum(num(r.get('pnl10_30')) or 0 for r in fill):+.2f} total |")
    lines = ["| Test | Regime | posted | filled | win of fills | P&L per posted |", "|---|---|---|---|---|---|"] + out + \
            ["Cells are small and regimes were cut after the fact: description, not findings."]
    return {"ok": bool(out), "lines": lines, "flags": 0, "data_n": len(P) + len(t)}


def judge(d):
    """Independent statistics, calibration (Confidence Auditor) and simulated-vs-executable (Profit Validator)."""
    lines = []
    P = m15_posted(d)
    F = [r for r in P if r["status"] == "FILLED"]
    if F:
        blk = defaultdict(list)
        for r in P:
            blk[int(r["order_ts"]) // 14400].append(r)
        per = lambda rs: m15_pnl(rs) / len(rs) if rs else None
        C = sum(int(r["contracts"]) for r in F)
        cw = sum(int(r["contracts"]) for r in F if r["won"] == "1") / C
        cbe = sum(int(r["contracts"]) * num(r["breakeven"]) for r in F) / C
        k = sum(r["won"] == "1" for r in F)
        wi = wilson(k, len(F))
        be = sum(num(r["breakeven"]) for r in F) / len(F)
        lines += [f"**Maker (15m)**: {len(F)} fills / {len(P)} posted · screening {len(F)}/100 fills",
                  f"P&L {m15_pnl(F):+.2f} · **per posted order {per(P):+.2f}** (95% by 4-hour blocks: {fmt_ci(boot(blk, per))}, {len(blk)} blocks)",
                  f"Win of fills {k}/{len(F)} = {k / len(F):.1%} (95% {wi[0]:.0%}-{wi[1]:.0%}) vs break-even {be:.1%} · "
                  f"contract-weighted {cw:.1%} vs {cbe:.1%}",
                  "Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used "
                  "stale quotes on some orders; queue position unknown. Not executable-verified."]
    W = d["winner"]
    t = [r for r in d["tickets"] if r.get("status_30") and W.get(r["slug"]) in ("up", "down")]
    tr = [r for r in t if r.get("status_30") == "FILLABLE"]
    if t:
        k = sum(right(r, W) for r in tr)
        pnl = sum(num(r.get("pnl10_30")) or 0 for r in tr)
        be = (sum(num(r["fill_30"]) + US_FEE * num(r["fill_30"]) * (1 - num(r["fill_30"])) for r in tr) / len(tr)) if tr else None
        wi = wilson(k, len(tr)) if tr else None
        lines += [f"**5-minute**: {len(tr)} simulated trades from {len(t)} alerts · screening {len(tr)}/100 · research {len(tr)}/300",
                  f"P&L {pnl:+.2f} · per alert {pnl / len(t):+.3f} · win {k}/{len(tr)}" + (f" ({wi[0]:.0%}-{wi[1]:.0%}) vs break-even {be:.0%}" if tr else ""),
                  "Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified."]
    # Confidence Auditor: first checkpoint per settled v18+ round, favored side's model estimate vs outcome
    first = {}
    for c in sorted(d["cps"], key=lambda c: c.get("logged_utc") or ""):
        if W.get(c["slug"]) in ("up", "down") and num(c.get("model_up")) is not None:
            first.setdefault(c["slug"], c)
    bk = defaultdict(lambda: [0, 0])
    bri_m = bri_k = 0.0
    nb = 0
    for c in first.values():
        p = num(c["model_up"])
        y = 1.0 if W[c["slug"]] == "up" else 0.0
        fav = max(p, 1 - p)
        won = (p >= 0.5) == (y == 1.0)
        b = min(int(fav * 10) / 10, 0.9)
        bk[b][0] += won
        bk[b][1] += 1
        ua, da = num(c.get("up_ask")), num(c.get("down_ask"))
        if ua and da and ua + da > 0:
            mkt = ua / (ua + da)
            bri_m += (p - y) ** 2
            bri_k += (mkt - y) ** 2
            nb += 1
    if bk:
        cells = []
        for b in sorted(bk):
            w, n = bk[b]
            ci = wilson(w, n)
            cells.append(f"{int(b * 100)}-{int(b * 100) + 10}%: won {w}/{n} ({ci[0]:.0%}-{ci[1]:.0%})")
        lines += ["Confidence Auditor (model estimate vs outcome, 1 check per round): " + " · ".join(cells),
                  f"Brier: model {bri_m / nb:.4f} vs market {bri_k / nb:.4f} on {nb} rounds (lower = sharper; sharper is not profit)" if nb else ""]
    return {"ok": bool(lines), "lines": [l for l in lines if l], "flags": 0, "data_n": len(P) + len(t)}


def nemesis(d):
    """Red team: reasons the results may be false, plus a root-cause table of every loss (Loss Intelligence)."""
    ch, loss = [], []
    P = m15_posted(d)
    F = [r for r in P if r["status"] == "FILLED"]
    m = re.search(r"## Primary: AGREE.*?\n\|\s*(\d+)\s*\|\s*([\d.]+)%\s*\|\s*([\d.]+)%", d["r15"], re.S)
    if P:
        live = sum(r["won"] == "1" for r in P) / len(P)
        if m:
            ch.append(f"Maker signal right on {live:.0%} of {len(P)} posted orders, but the same AGREE signal won {m.group(2)}% "
                      f"(break-even {m.group(3)}%) on {m.group(1)} historical trades. Expect regression toward history.")
        wl = [r for r in P if r["won"] == "1"]
        ll = [r for r in P if r["won"] == "0"]
        if wl and ll:
            fw = sum(r["status"] == "FILLED" for r in wl) / len(wl)
            fl = sum(r["status"] == "FILLED" for r in ll) / len(ll)
            ch.append(f"Adverse selection: fill rate {fw:.0%} when right vs {fl:.0%} when wrong. Unfilled 'wins' are not earnings.")
        hi = [r for r in F if num(r["limit"]) >= 0.85]
        if hi:
            avg_w = statistics.mean([num(r["pnl"]) for r in hi if r["won"] == "1"] or [0])
            worst = min(num(r["pnl"]) for r in F)
            ch.append(f"Price risk: {len(hi)} fills at 85c+ earn about {avg_w:+.2f} each when right; one loss costs up to {worst:+.2f}. "
                      "A high win rate on expensive contracts can still lose.")
        days = len({datetime.fromtimestamp(int(r['order_ts']), timezone.utc).date() for r in P})
        ch.append(f"Independence: {len(P)} orders over {days} calendar day(s). Few independent periods: one regime can explain it all.")
        for r in sorted(F, key=lambda r: int(r["order_ts"])):
            if r["won"] == "0":
                loss.append(f"| maker | {r['ticker'][-16:]} | {r['side']} at {r['limit']} x{r['contracts']} | {num(r['pnl']):+.2f} | "
                            f"{et_hour(r['order_ts']):02d}h ET | move {abs((num(r['btc_T']) or 0) - (num(r['btc_T60']) or 0)):.0f} | "
                            f"dist {abs((num(r['btc_T']) or 0) - (num(r['target']) or 0)):.0f} | filled +{int(r['first_through_ts']) - int(r['order_ts'])}s |")
    W = d["winner"]
    t = [r for r in d["tickets"] if r.get("status_30") == "FILLABLE" and W.get(r["slug"]) in ("up", "down")]
    for r in t:
        if not right(r, W):
            loss.append(f"| 5m | {r['slug'][-10:]} | {r['side']} at {r.get('fill_30')} | {num(r.get('pnl10_30')) or 0:+.2f} | "
                        f"{et_hour(r['t_start']):02d}h ET | alert {r.get('price')} cap {r.get('max_price')} | "
                        f"{r.get('secs_left_sent') or r.get('secs_left')}s left | - |")
    g = [r for r in d["tickets"] if r.get("status_30") and W.get(r["slug"]) in ("up", "down")]
    if g:
        surv = [r for r in g if r.get("status_30") == "FILLABLE"]
        ch.append(f"5m survivorship: picks right on {pct(sum(right(r, W) for r in g) / len(g))} of all alerts but "
                  f"{pct(sum(right(r, W) for r in surv) / len(surv)) if surv else '-'} of the ones still buyable at 30s.")
    lines = ["**Challenges**"] + [f"- {c}" for c in ch] + ["", "**Every loss (Loss Intelligence)**",
             "| Test | Market | Entry | P&L | Time | Context | Context | Fill |", "|---|---|---|---|---|---|---|---|"] + loss
    return {"ok": True, "lines": lines, "flags": len(ch), "data_n": len(P) + len(t)}


def ev_per_posted(P, p_win, maker_rate=0.0):
    """Expected P&L per posted maker order if the side wins with probability p_win, keeping the observed
    outcome-conditional fill rates and price mix. Stress tool, not a forecast."""
    wl = [r for r in P if r["won"] == "1"]
    ll = [r for r in P if r["won"] == "0"]
    fw = (sum(r["status"] == "FILLED" for r in wl) / len(wl)) if wl else 0.5
    fl = (sum(r["status"] == "FILLED" for r in ll) / len(ll)) if ll else 1.0
    tot = 0.0
    for r in P:
        L, C = num(r["limit"]), int(r["contracts"])
        fee = math.ceil(round(100 * maker_rate * C * L * (1 - L), 6)) / 100 if maker_rate else 0.0
        tot += p_win * fw * (C * (1 - L) - fee) - (1 - p_win) * fl * (C * L + fee)
    return tot / len(P)


def oracle(d):
    """Stress tests and a simulated screening verdict under the historical win rate."""
    P = m15_posted(d)
    if len(P) < 10:
        return {"ok": False, "lines": ["Not enough maker orders yet (needs 10+)."], "flags": 0, "data_n": len(P)}
    live = sum(r["won"] == "1" for r in P) / len(P)
    m = re.search(r"## Primary: AGREE.*?\n\|\s*(\d+)\s*\|\s*([\d.]+)%\s*\|\s*([\d.]+)%", d["r15"], re.S)
    if not m:
        return {"ok": False, "lines": ["Historical AGREE row not found in data/15m/report.md; stress test skipped."], "flags": 0, "data_n": 0}
    hist = float(m.group(2)) / 100
    lo, hi = 0.0, 1.0
    for _ in range(40):                       # break-even win probability for this order mix
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if ev_per_posted(P, mid) < 0 else (lo, mid)
    be = (lo + hi) / 2
    rnd = random.Random(11)
    F = [r for r in P if r["status"] == "FILLED"]
    passes = 0
    for _ in range(2000):                     # 100 simulated fills at the historical win rate, same price mix
        sample = [rnd.choice(F) for _ in range(100)]
        wins = sum(rnd.random() < hist for _ in sample)
        bev = sum(num(r["breakeven"]) for r in sample) / 100
        passes += wins / 100 >= bev + 0.03
    lines = [f"Expected P&L per posted order at the live win rate ({live:.0%}): {ev_per_posted(P, live):+.2f}",
             f"…at the historical AGREE win rate ({hist:.1%}): **{ev_per_posted(P, hist):+.2f}**",
             f"…with the 0.0175 maker fee at the live rate: {ev_per_posted(P, live, KALSHI_MAKER):+.2f}",
             f"Win probability needed to break even with this price mix and these fill rates: **{be:.1%}**",
             f"If the true win rate were the historical {hist:.1%}, the frozen 100-fill screen (+3 points) would still PASS in "
             f"{passes / 20:.0f}% of 2,000 simulations: the screen is a first look, not proof.",
             "Assumes the observed fill rates (when right / when wrong) and price mix stay the same."]
    return {"ok": True, "lines": lines, "flags": 0, "data_n": len(P)}


def gaps(ts_list, step, tol=1.5):
    s = sorted(set(int(x) for x in ts_list))
    return [(a, b) for a, b in zip(s, s[1:]) if b - a > step * tol]


def chronos(d):
    """Timeline, coverage gaps, versions and provenance (where each number comes from)."""
    lines = []
    m = d["m15"]
    if m:
        g = gaps([r["open_ts"] for r in m], 900)
        span = (int(max(r["open_ts"] for r in m)) - int(min(r["open_ts"] for r in m))) / 900 + 1
        lines.append(f"Maker windows logged {len(m)} of ~{span:.0f} in its span · coverage gaps over 22 min: {len(g)}"
                     + (" (longest " + f"{max(b - a for a, b in g) / 3600:.1f} h)" if g else ""))
    res = d["results"]
    if res:
        g = gaps([r["t_start"] for r in res], 300)
        lines.append(f"5m settled rounds recorded {len(res)} · gaps over 7.5 min: {len(g)}"
                     + (" (longest " + f"{max(b - a for a, b in g) / 3600:.1f} h)" if g else ""))
    vers = Counter(r.get("version", "")[-3:] for r in d["tickets"])
    lines += [f"5m ticket versions in the experiment: {dict(vers)}",
              "Provenance: 5m prices = Polymarket US gateway (/bbo, /book fallback) · 5m winners = Polymarket US settlementPx · "
              "BTC = Coinbase · maker quotes = Kalshi /markets list · maker fills = Kalshi public trades · 15m history = Kalshi candles (Phase 1)."]
    return {"ok": bool(m or res), "lines": lines, "flags": 0, "data_n": len(m) + len(res)}


def mirror(d):
    """Venue definitions side by side, plus the live same-moment price log from mirror15.py.
    Status stays in development until real paired snapshots exist; it is descriptive only (no PASS/FAIL)."""
    import mirror15
    m = re.search(r"same winner (\d+)/(\d+)", d.get("r15", ""))
    lines = ["| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |", "|---|---|---|",
             f"| Taker fee | round-up of {KALSHI_TAKER} x C x P x (1-P) | feeCoefficient x P x (1-P) per share (5m bot assumes {US_FEE}) |",
             f"| Maker fee | only on listed series ({KALSHI_MAKER}); this series reads 'quadratic' (none) | not modelled (taker-only tests) |",
             "| Settlement | BRTI 60s average | BRTI 60s average |",
             f"| Settlement agreement (Phase 1) | {m.group(1)}/{m.group(2)} windows identical | |" if m else "| Settlement agreement | not found in report | |",
             "Matched events on two venues are the same event, not independent evidence."]
    res = mirror15.compare(d.get("mirror_q") or [], d.get("m15") or [])
    lines += mirror15.summary_lines(res)
    live = res["pairs"] > 0
    return {"ok": bool(m), "lines": lines, "flags": 0, "data_n": res["pairs"] if m else 0, "partial": not live,
            "live": res}


def gh_get(path, params=None):
    h = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    r = requests.get(f"https://api.github.com/repos/{REPO}{path}", headers=h, params=params or {}, timeout=20)
    r.raise_for_status()
    return r.json()


def overwatch_eval(runs, fresh, relay, now=None):
    """Pure evaluation (tested offline): runs = [{name, conclusion, created}], fresh = {label: (epoch, max_age_h)}."""
    now = now or NOW
    flags, lines = [], []
    by = defaultdict(list)
    for r in runs:
        by[r["name"]].append(r)
    for name, rs in sorted(by.items()):
        fails = [r for r in rs if r["conclusion"] in ("failure", "timed_out", "startup_failure")]
        if fails:
            flags.append(f"{name}: {len(fails)} failed in 24h")
    lines.append(f"Workflows active in the last 24h: {len(by)} · runs {len(runs)} · failed {sum(r['conclusion'] in ('failure', 'timed_out', 'startup_failure') for r in runs)}")
    for label, (ts, max_h) in fresh.items():
        age = (now - ts) / 3600 if ts else None
        if age is None or age > max_h:
            flags.append(f"{label} stale ({'never' if age is None else f'{age:.1f} h'}, limit {max_h} h)")
        lines.append(f"{label}: last update {'never' if age is None else f'{age:.1f} h ago'} (limit {max_h} h)")
    dirty = sum(1 for r in (relay.get("requests") or {}).values() if r.get("dirty"))
    if dirty:
        flags.append(f"{dirty} Discord status card(s) not delivered")
    lines.append(f"Relay: {len(relay.get('requests') or {})} requests tracked, {dirty} cards waiting for Discord")
    return flags, lines


def overwatch(d):
    """Workflow health, data freshness, relay queue (Mechanic folded in). Read-only GitHub API."""
    since = datetime.fromtimestamp(NOW - 86400, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        j = gh_get("/actions/runs", {"created": f">={since}", "per_page": 100})
        runs = [{"name": r["name"], "conclusion": r.get("conclusion") or r.get("status"), "created": r["created_at"]}
                for r in j.get("workflow_runs", [])]
        fresh = {}
        for label, path, max_h in (("5m tickets data", "data/tickets.csv", 6), ("maker15 orders", "data/maker15/orders.csv", 3),
                                   ("maker15 audit", "data/maker15_audit/audit.md", 6), ("vault", "vault", 6)):
            c = gh_get("/commits", {"path": path, "per_page": 1})
            fresh[label] = (datetime.fromisoformat(c[0]["commit"]["committer"]["date"].replace("Z", "+00:00")).timestamp()
                            if c else None, max_h)
    except Exception as e:
        return {"ok": False, "lines": [f"GitHub API unavailable ({e.__class__.__name__}); health not checked this run."],
                "flags": 0, "data_n": 0}
    flags, lines = overwatch_eval(runs, fresh, d["relay"])
    lines = (["**Flags:** " + "; ".join(flags)] if flags else ["No health flags."]) + lines
    return {"ok": True, "lines": lines, "flags": len(flags), "data_n": len(runs)}


PREREG_SECTIONS = {
    "data source": r"(?i)\bdata\b",
    "decision rule / no look-ahead": r"(?i)look-ahead|no look|order rule|decision",
    "entry or fill rule": r"(?i)\bfill|entry\b|ask\b",
    "fees": r"(?i)\bfee",
    "PASS/FAIL verdict rule": r"(?i)verdict|scoring|judge|passed|failed",
    "frozen before results": r"(?i)frozen|before any result",
    "kept separate from other experiments": r"(?i)separate|untouched|not change|neither is changed",
}


def genesis_check(text):
    return [name for name, rx in PREREG_SECTIONS.items() if not re.search(rx, text or "")]


def genesis(d):
    """Pre-registration template + validator. No new experiment starts without Jacob's approval."""
    os.makedirs(os.path.join("lab", "templates"), exist_ok=True)
    tpl = os.path.join("lab", "templates", "PREREG_TEMPLATE.md")
    if not os.path.exists(tpl):
        with open(tpl, "w", encoding="utf-8") as f:
            f.write("# Pre-registration: <name>\n\nFrozen before any result. Requested by <who>, approved by Jacob on <date>. "
                    "Kept separate from <other experiments>; neither is changed.\n\n## Data (public, $0)\n- \n\n## Decision rule "
                    "(no look-ahead)\n- \n\n## Entry / fill rule\n- \n\n## Fees\n- \n\n## Scoring and verdict\n- Sample size, "
                    "screening milestone vs research target, what PASS and FAIL mean.\n\n## What would change our mind\n- \n")
    lines = [f"Template: lab/templates/PREREG_TEMPLATE.md"]
    miss_total = 0
    for name, text in d["prereg"].items():
        miss = genesis_check(text)
        miss_total += len(miss)
        note = " (exploratory by design: it reports results but sets no PASS/FAIL)" if miss and re.search(r"(?i)exploratory", text) else ""
        lines.append(f"{name} PREREG: " + ("all required sections present" if not miss else "missing: " + ", ".join(miss) + note))
    return {"ok": True, "lines": lines, "flags": miss_total, "data_n": len(d["prereg"])}


def evolution(results):
    """Proposal-only hypotheses, each tied to a measured pattern. Never tested or launched here."""
    hyp = []
    v = results.get("velocity", {}).get("lines", [])
    if any("dropouts" in l for l in v):
        hyp.append("5m: correct calls are priced in within 5-30s. Hypothesis to pre-register later: alerts sent with more time "
                   "left, or faster delivery, keep more correct calls buyable. Needs a Genesis PREREG and Jacob's approval.")
    n = results.get("nemesis", {}).get("lines", [])
    if any("Adverse selection" in l for l in n):
        hyp.append("Maker: fills cluster in losing outcomes. Hypothesis: the edge, if any, is in the signal, not the resting "
                   "price; compare with a taker baseline at real prices before any new maker variant.")
    o = results.get("oracle", {}).get("lines", [])
    if any("historical AGREE" in l for l in o):
        hyp.append("Maker: profit depends on the signal staying above its historical win rate. Track the live rate against "
                   "history as fills grow; no change to the frozen test.")
    lines = [f"- {h}" for h in hyp] or ["- No measured pattern strong enough to propose anything."]
    lines.append("Proposal only. Nothing is tested, tuned or launched by Evolution. New strategy work is paused by Jacob (2026-11-26).")
    return {"ok": True, "lines": lines, "flags": 0, "data_n": len(hyp)}


# ---------------------------------------------------------------- self-tests (synthetic failure cases)

def _t_velocity():
    W = {"a": "up", "b": "up"}
    t = [{"slug": "a", "side": "Up", "status_30": "EXPIRED", "expired_s": "45", "ask_30": "0.50", "max_price": "0.60",
          "ask_30_at": "30.4", "status_5": "FILLABLE", "status_10": "FILLABLE", "status_20": "FILLABLE"},
         {"slug": "b", "side": "Up", "status_30": "FILLABLE", "expired_s": "60", "ask_30": "0.55", "max_price": "0.60",
          "ask_30_at": "30.2", "pnl10_30": "5"}]
    r = velocity({"tickets": t, "winner": W})
    return r["flags"] == 1                            # the planted mis-scored row is caught


def _t_titan():
    a = [{"flags": "QUOTE_FAR_FROM_LAST_PRINT"}, {"flags": ""}, {"flags": "MARKETABLE_AT_POST"}]
    return titan({"tickets": [], "m15": [], "audit": a})["flags"] == 2


def _t_ghost():
    cps = [{"quote_src": "us_bbo", "pair_sum": "1.50"}, {"quote_src": "error", "pair_sum": "1.01"}]
    r = ghost({"cps": cps, "results": [], "closes": [], "winner": {}, "loops": [{"max_spot_gap_s": "12"}], "audit": []})
    return r["flags"] == 2


def _t_stats():
    w = wilson(50, 100)
    return (boot({1: [1], 2: [2]}, lambda x: sum(x)) is None and abs(w[0] - 0.4038) < 0.001 and abs(w[1] - 0.5962) < 0.001
            and tercile([1, 2, 3, 4, 5, 6]) == (3, 5))


def _t_oracle():
    P = [{"won": "1", "status": "FILLED", "limit": "0.50", "contracts": "20"},
         {"won": "0", "status": "FILLED", "limit": "0.50", "contracts": "20"}]
    return abs(ev_per_posted(P, 0.5)) < 1e-9 and ev_per_posted(P, 0.6) > 0


def _t_overwatch():
    runs = [{"name": "polybot", "conclusion": "failure", "created": ""}, {"name": "relay", "conclusion": "success", "created": ""}]
    flags, _ = overwatch_eval(runs, {"maker15 orders": (1000.0, 3)}, {"requests": {"x": {"dirty": True}}}, now=1000.0 + 5 * 3600)
    return len(flags) == 3                            # failed run + stale data + undelivered card


def _t_genesis():
    return genesis_check("# x\nFrozen before any result. Data: public. Order rule. Fill rule. Verdict. Kept separate.") == ["fees"]


def _t_chronos():
    return gaps([0, 900, 1800, 4500, 5400], 900) == [(1800, 4500)]


def _t_nemesis():
    P = [{"won": "1", "status": "UNFILLED", "limit": "0.5", "contracts": "20", "order_ts": "0", "pnl": "0"},
         {"won": "0", "status": "FILLED", "limit": "0.9", "contracts": "11", "order_ts": "0", "pnl": "-9.9",
          "first_through_ts": "5", "ticker": "KXBTC15M-T", "side": "Up", "btc_T": "1", "btc_T60": "1", "target": "1"}]
    r = nemesis({"m15": P, "r15": "", "tickets": [], "winner": {}})
    return any("Adverse selection: fill rate 0% when right vs 100% when wrong" in l for l in r["lines"])


def _t_mirror():
    r15 = "- End price difference: median $0.00 · same winner 5/7"
    ok = mirror({"r15": r15})
    bad = mirror({"r15": "no such line"})
    q = [{"ticker": "A", "pm_status": "ok", "k_up_ask": "0.40", "k_dn_ask": "0.61", "pm_up_ask": "0.47", "pm_dn_ask": "0.54", "gap_s": "0.5"}]
    live = mirror({"r15": r15, "mirror_q": q, "m15": [{"ticker": "A", "side": "Up"}]})
    return (any("5/7 windows identical" in l for l in ok["lines"]) and not bad["ok"] and ok["partial"]
            and not live["partial"] and live["data_n"] == 1 and any("+7.0c" in l for l in live["lines"]))


def _t_evolution():
    empty = evolution({})                                   # no measured patterns -> proposes nothing
    full = evolution({"velocity": {"lines": ["dropouts 5s->30s: 9"]}})
    return "No measured pattern" in empty["lines"][0] and len(full["lines"]) == 2


def _t_cortex():
    reg = [{"key": "x", "name": "X", "status": "implemented", "emoji": "🟢", "self_test": "passed"}]
    bad = [{"key": "y", "name": "Y", "status": "implemented", "emoji": "🟢", "self_test": "FAILED"}]
    return cortex_valid(reg) and not cortex_valid(bad)


def cortex_valid(reg):
    """Registry rule: nothing may be marked implemented (🟢) unless its self-test passed."""
    need = {"key", "name", "status", "emoji", "self_test"}
    return all(need <= set(a) and a["emoji"] == EMOJI[a["status"]] and
               (a["status"] != "implemented" or a["self_test"] == "passed") for a in reg)


TESTS = {"velocity": _t_velocity, "titan": _t_titan, "ghost": _t_ghost, "hawk": _t_stats, "judge": _t_stats,
         "nemesis": _t_nemesis, "oracle": _t_oracle, "chronos": _t_chronos, "mirror": _t_mirror,
         "overwatch": _t_overwatch, "genesis": _t_genesis, "evolution": _t_evolution, "cortex": _t_cortex}


def selftest():
    res = {}
    for k, f in TESTS.items():
        try:
            res[k] = bool(f())
        except Exception as e:
            print(f"selftest {k}: ERROR {e!r}")
            res[k] = False
    return res


# ---------------------------------------------------------------- registry, report, card

AGENTS = [
    ("velocity", "Velocity", "Expiration Guard", "Latency, quote lifetime, 30s deadline consistency"),
    ("titan", "Titan", "Liquidity Intelligence", "Size availability, fill volume, quote freshness"),
    ("ghost", "Ghost", "Market Stability Monitor (data)", "Anomalies and missing data in public feeds"),
    ("hawk", "Hawk", "Market Stability Monitor (regimes)", "Descriptive results by volatility / momentum"),
    ("judge", "Judge", "Confidence Auditor, Profit Validator", "Independent stats, calibration, simulated vs executable"),
    ("nemesis", "Nemesis", "Loss Intelligence", "Red-team challenges, every loss explained"),
    ("oracle", "Oracle", "", "Stress tests and simulated screening outcomes"),
    ("chronos", "Chronos", "", "Coverage timeline, gaps, versions, provenance"),
    ("mirror", "Mirror", "", "Kalshi vs Polymarket US: fees, settlement and same-moment prices"),
    ("overwatch", "Overwatch", "Mechanic", "Workflow failures, data freshness, relay health"),
    ("genesis", "Genesis", "", "Pre-registration template and validator"),
    ("evolution", "Evolution", "", "Proposal-only hypotheses from measured patterns"),
    ("cortex", "Cortex", "Archive, Nexus", "Shared registry for the vault and relay (this file's output)"),
]
EXISTING = [("Data Auditor", "team_checks.py"), ("Quant Analyst", "team_checks.py"), ("Risk Sentinel", "team_checks.py"),
            ("Maker QC audit", "audit_maker15.py"), ("Relay (Nexus queue)", "relay.py"), ("Vault sync (Archive)", "vault_sync.py")]
EMOJI = {"implemented": "🟢", "development": "🔵", "pending": "🟡", "blocked": "🔴"}


def main(post=True):
    tests = selftest()
    d = load()
    fns = {"velocity": velocity, "titan": titan, "ghost": ghost, "hawk": hawk, "judge": judge, "nemesis": nemesis,
           "oracle": oracle, "chronos": chronos, "mirror": mirror, "overwatch": overwatch, "genesis": genesis}
    results = {}
    for k, f in fns.items():
        try:
            results[k] = f(d)
        except Exception as e:
            results[k] = {"ok": False, "lines": [f"check crashed: {e.__class__.__name__}: {e}"], "flags": 0, "data_n": 0}
    results["evolution"] = evolution(results)
    results["cortex"] = {"ok": True, "lines": ["Writes lab/agents/status.json (read by vault_sync for agent profiles) and "
                                              "lab/agents/report.md; the relay request queue is Nexus's coordination list."],
                         "flags": 0, "data_n": 1}
    reg = []
    for k, name, folded, job in AGENTS:
        r = results[k]
        if not tests.get(k):
            st, why = "blocked", "self-test failed this run"
        elif r.get("partial"):
            st, why = "development", "definitions done; waiting for the first live same-moment price pairs"
        elif r["ok"] and r["data_n"] > 0:
            st, why = "implemented", ""
        elif r["ok"]:
            st, why = "pending", "ran, but no real data yet"
        else:
            st, why = "pending", (r["lines"][0] if r["lines"] else "not run")
        reg.append({"key": k, "name": name, "folded_in": folded, "job": job, "status": st, "emoji": EMOJI[st],
                    "self_test": "passed" if tests.get(k) else "FAILED", "flags": r["flags"], "note": why,
                    "summary": [l for l in r["lines"] if l][:3]})
    if not cortex_valid(reg):
        raise SystemExit("agents: registry failed its own validity rule; nothing written")
    os.makedirs(OUT, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(os.path.join(OUT, "status.json"), "w", encoding="utf-8") as f:
        json.dump({"generated": stamp, "agents": reg, "existing": [{"name": n, "module": m} for n, m in EXISTING]}, f,
                  indent=1, ensure_ascii=False)
    md = ["# Polybot HQ specialist agents", "",
          f"Generated {stamp}. Deterministic Python checks, read-only, $0. Status 🟢 = self-test with planted failures passed "
          "AND the check ran on real data in this run. Nothing here changes a strategy or experiment.", "",
          "| | Agent | Folded in | Job | Self-test | Flags |", "|---|---|---|---|---|---|"]
    md += [f"| {a['emoji']} | {a['name']} | {a['folded_in'] or '-'} | {a['job']} | {a['self_test']} | {a['flags']} |" for a in reg]
    md += ["", "Existing roles keep their duties: " + ", ".join(f"{n} ({m})" for n, m in EXISTING), ""]
    for k, name, folded, job in AGENTS:
        md += [f"## {name}" + (f" (+ {folded})" if folded else ""), ""] + results[k]["lines"] + [""]
    with open(os.path.join(OUT, "report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))
    if post:
        card(reg, results, stamp)
    return reg


def card(reg, results, stamp):
    if not HOOK:
        print("agents: no research/team webhook, report written to lab/agents/ only")
        return
    grid = " ".join(f"{a['emoji']} {a['name']}" for a in reg)
    key = []
    for k in ("judge", "oracle", "velocity", "titan"):
        key += [l for l in results[k]["lines"] if l and not l.startswith("|")][:2]
    desc = (grid + "\n\n" + "\n".join("• " + re.sub(r"\*\*", "", l)[:240] for l in key[:7])
            + "\n\nFull report: lab/agents/report.md on GitHub. Paper only, $0.")[:3900]
    try:
        r = requests.post(HOOK, json={"username": "Polybot HQ agents", "embeds": [{
            "title": f"🧭 Specialist agents · {stamp}", "description": desc, "color": 0x5865F2,
            "footer": {"text": "deterministic checks · read-only · 🟢 tested 🔵 building 🟡 pending 🔴 blocked"}}]}, timeout=10)
        print(f"agents: Discord HTTP {r.status_code}")
    except requests.RequestException as e:
        print(f"agents: Discord failed ({e.__class__.__name__})")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        res = selftest()
        print(res)
        sys.exit(0 if all(res.values()) else 1)
    main(post=os.getenv("AGENTS_POST", "1") == "1")
