"""Polybot HQ Obsidian vault ($0): a readable, linked view of the GitHub record. GitHub stays the source of truth.

python vault_sync.py            -> (re)builds vault/Polybot HQ/ from the repo + public GitHub issues

One-way and note-safe:
- Files this script writes start with frontmatter `polybot_auto: true`. Only those are ever overwritten.
- Any note without that line (written by Jacob, ChatGPT or Claude by hand) is never touched, renamed or deleted.
- "Seed" notes (decision log, lessons, roadmap, profiles' "Notes" sections live in separate human files) are created
  once if missing and then belong to the humans.
- Daily notes: only today's note is regenerated; past days stay as they were, so history accumulates.
- Redaction: anything that looks like a webhook URL, token or key is replaced before writing. No secrets in the vault.
"""
import csv
import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone

import requests

ROOT = os.path.join("vault", "Polybot HQ")
REPO = os.getenv("GITHUB_REPOSITORY", "j42002/polybot")
TOKEN = os.getenv("GITHUB_TOKEN", "")
AUTO = "polybot_auto: true"
NOW = datetime.now(timezone.utc)
TODAY = NOW.strftime("%Y-%m-%d")

F = {k: f"{k} — {v}" for k, v in [
    ("00", "Main Dashboard"), ("01", "Polybot Brain"), ("02", "AI Team Members"), ("03", "Project History"),
    ("04", "Strategy Library"), ("05", "Active Experiments"), ("06", "Research Results"), ("07", "Team Communications"),
    ("08", "Daily Reports"), ("09", "Mistakes and Lessons"), ("10", "Security and Risk"), ("11", "Future Roadmap")]}

SECRET_RES = [
    re.compile(r"https://(?:\w+\.)?discord(?:app)?\.com/api/webhooks/\S+", re.I),
    re.compile(r"\b(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}\b"),
    re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}\b"),
]


def redact(text):
    for r in SECRET_RES:
        text = r.sub("[redacted]", text)
    return text


written = []


def write(rel, body, tags=(), title=None, seed=False):
    """Write an auto note (overwrite only if it's ours) or a seed note (only if missing)."""
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            head = f.read(400)
        if seed or AUTO not in head:
            return False                                 # a human owns this file now
    fm = ["---"]
    if not seed:
        fm.append(AUTO)
        fm.append(f"updated: {NOW.strftime('%Y-%m-%d %H:%M UTC')}")
    if tags:
        fm.append("tags: [" + ", ".join(tags) + "]")
    fm.append("---")
    note = "\n".join(fm) + "\n" + (f"# {title}\n\n" if title else "") + redact(body).rstrip() + "\n"
    if not seed:
        note += "\n---\n*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*\n"
    strip = lambda t: re.sub(r"^updated: .*$", "", t, count=1, flags=re.M)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if strip(f.read()) == strip(note):
                return False                             # content unchanged: keep the old timestamp, no churn
    with open(path, "w", encoding="utf-8") as f:
        f.write(note)
    written.append(rel)
    return True


def read(path, default=""):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return default


def rows(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []


def gh(path, params=None):
    h = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    out, page = [], 1
    while True:
        r = requests.get(f"https://api.github.com/repos/{REPO}{path}", headers=h, timeout=20,
                         params={**(params or {}), "per_page": 100, "page": page})
        r.raise_for_status()
        j = r.json()
        if not isinstance(j, list):
            return j
        out += j
        if len(j) < 100:
            return out
        page += 1


def safe(name):
    return re.sub(r'[\\/:*?"<>|#^\[\]]', "", name).strip()[:90]


def who(c):
    body = c.get("body") or ""
    login = (c.get("user") or {}).get("login", "")
    if re.search(r"^\s*#{0,6}\s*\**\s*Claude\s*(→|->)", body, re.M):
        return "Claude"
    if re.search(r"^\s*#{0,6}\s*\**\s*ChatGPT\s*(→|->)|—\s*ChatGPT\b", body, re.M):
        return "ChatGPT"
    if "Gemini" in body[:200] and login.endswith("[bot]"):
        return "Gemini"
    return "Jacob" if login == "j42002" else login


def section(md, heading):
    """Text under '## heading' up to the next heading of the same or higher level."""
    m = re.search(rf"^(#+)\s*{re.escape(heading)}.*?$", md, re.M)
    if not m:
        return ""
    level = len(m.group(1))
    rest = md[m.end():]
    n = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[:n.start()].strip() if n else rest.strip()


# ---------------------------------------------------------------- data
def load():
    d = {"issues": [], "comments": defaultdict(list), "gh_ok": False}
    try:
        for i in gh("/issues", {"state": "all"}):
            if "pull_request" in i:
                continue
            d["issues"].append(i)
        for c in gh("/issues/comments", {"sort": "created", "direction": "asc"}):
            d["comments"][int(c["issue_url"].rstrip("/").split("/")[-1])].append(c)
        d["gh_ok"] = True
    except Exception as e:
        print(f"vault: GitHub API unavailable ({e}); issue notes kept as they were")
    d["issues"].sort(key=lambda i: i["number"])
    d["report"] = read(os.path.join("data", "report.md"))
    d["r15"] = read(os.path.join("data", "15m", "report.md"))
    d["prereg"] = read(os.path.join("data", "15m", "PREREG.md"))
    d["m15"] = read(os.path.join("data", "maker15", "report.md"))
    d["m15pre"] = read(os.path.join("data", "maker15", "PREREG.md"))
    d["m15audit"] = read(os.path.join("data", "maker15_audit", "audit.md"))
    d["checks"] = read(os.path.join("lab", "checks", "latest.md"))
    d["readme"] = read(os.path.join("lab", "README.md"))
    d["relay"] = json.loads(read(os.path.join("lab", "relay_state.json"), "{}") or "{}")
    try:
        log = subprocess.run(["git", "log", "--reverse", "--date=short", "--format=%ad\t%h\t%s"],
                             capture_output=True, text=True, timeout=30).stdout.splitlines()
    except Exception:
        log = []
    noise = re.compile(r"^(polybot data|relay state|team checks|backtest15 data|lab sync|relay: |Merge |polybot-|share state)", re.I)
    d["log"] = [l.split("\t", 2) for l in log if l.count("\t") == 2 and not noise.match(l.split("\t", 2)[2])]
    return d


def labels(i):
    return [l["name"] for l in i.get("labels", [])]


def kind(i):
    t = i.get("title", "")
    return "strategy" if t.startswith("[Strategy]") else "ops" if t.startswith("[Team ops]") else "other"


def short(i):
    t = re.sub(r"^\[(Strategy|Team ops)\]\s*", "", i.get("title", ""))
    return safe(f"Issue {i['number']} — {t}")


def stage(i):
    s = [l for l in labels(i) if l.startswith(("stage:", "verdict:", "evidence:"))]
    return ", ".join(s) or ("closed" if i.get("state") == "closed" else "open")


# ---------------------------------------------------------------- notes
TEAM = [
    ("Jacob", "Founder", "👑", "Owns Polybot. Approves every stage change, experiment and real-world action.",
     "GitHub app, Discord, ChatGPT", "Human", ["Final say on decisions", "Shares ChatGPT sessions", "Paper only, $0 budget"]),
    ("Claude", "Lead Developer", "🛠️", "Builds and tests the code, runs the relay, answers ChatGPT on GitHub.",
     "Claude (scheduled tasks hourly; fast mode once the token is set)", "Active, verified",
     ["Writes experiments only after approval", "Replies as 'Claude → ChatGPT'", "Never changes a frozen experiment"]),
    ("ChatGPT", "Research Director", "🧭", "Sets research priorities, reviews designs and results, posts on GitHub.",
     "ChatGPT through Jacob's GitHub connection (posts show as j42002)", "Active, verified (when Jacob opens a session)",
     ["Approves designs and pre-registrations", "Asks for evidence, not hype", "Can't change experiments by comment alone"]),
    ("Grok", "Strategy Scout", "🔭", "Finds what traders publicly claim works (X, TikTok, YouTube).",
     "Free app; output carried into GitHub issues", "Manual, not automated",
     ["Submits claims as L0", "Uses lab/prompts/grok.md"]),
    ("Perplexity", "Fact-Checker", "🔎", "Finds original sources, exact rules and counter-evidence.",
     "Free app; output pasted as issue comments", "Manual, not automated", ["Moves claims to L1 when sourced"]),
    ("Gemini", "Independent Reviewer", "♊", "Automatic first review of new strategies and second opinions on tickets.",
     "Free API tier inside GitHub Actions", "Not active yet (free GEMINI_API_KEY not set)", ["150 calls/day cap, stops on 429"]),
    ("Data Auditor", "Data integrity", "🧮", "Checks coverage, duplicates, missing quotes, timestamps, delivery.",
     "Python in GitHub Actions (team_checks.py)", "Active, tested", ["Daily card in #research-reports"]),
    ("Quant Analyst", "Statistics", "📐", "Win rate vs break-even with uncertainty ranges; flags small samples.",
     "Python in GitHub Actions (team_checks.py)", "Active, tested", ["Never calls anything proven under 300 trades"]),
    ("Risk Sentinel", "Safety", "🛡️", "Checks for credentials, real-order code, paid APIs, frozen model, routing leaks.",
     "Python in GitHub Actions (team_checks.py)", "Active, tested", ["Fails loudly if a safety rule breaks"]),
    ("Polybot HQ relay", "Messenger", "📡", "Moves messages between GitHub and Discord. Status cards, no duplicates.",
     "GitHub Actions + Discord webhooks", "Active, tested", ["📨 → 🧠 → ✅ / ⚠️ cards edited in place"]),
]


def team_notes():
    for name, role, icon, what, how, status, duties in TEAM:
        body = (f"> [!info] {icon} {role}\n> {what}\n\n| | |\n|---|---|\n| **Status** | {status} |\n| **Runs on** | {how} |\n"
                f"| **Cost** | $0 |\n\n## Responsibilities\n" + "\n".join(f"- {x}" for x in duties) +
                f"\n\n## Works with\n- [[Team Overview]] · [[Brain Overview]] · [[Start Here]]\n")
        write(f"{F['02']}/{name}.md", body, tags=["team", f"team/{safe(name).lower().replace(' ', '-')}"], title=f"{icon} {name}")
    table = "| | Member | Role | Status |\n|---|---|---|---|\n" + "\n".join(
        f"| {ic} | [[{n}]] | {r} | {s} |" for n, r, ic, _, _, s, _ in TEAM)
    flow = ("```mermaid\nflowchart LR\n  G[Grok: finds claims] --> P[Perplexity: checks sources]\n  P --> C[ChatGPT: reviews]\n"
            "  C --> Cl[Claude: builds paper test]\n  Cl --> A[Auditor / Quant / Risk: check]\n  A --> J{Jacob decides}\n"
            "  C <-->|GitHub issues| Cl\n```\n")
    write(f"{F['02']}/Team Overview.md", f"{table}\n\n## How work flows\n{flow}\nProfiles are auto-generated. Add your own notes in a new file.",
          tags=["team"], title="🤝 Team Overview")


def strategy_notes(d):
    lines = []
    for i in d["issues"]:
        if kind(i) != "strategy":
            continue
        cs = d["comments"].get(i["number"], [])
        verdict = next((l.split(":", 1)[1] for l in labels(i) if l.startswith("verdict:")), "")
        tag_v = [f"verdict/{verdict}"] if verdict else []
        body = (f"> [!abstract] Status\n> **{stage(i)}** · [open on GitHub]({i['html_url']}) · {len(cs)} comments\n\n"
                f"## Submission\n{(i.get('body') or '').strip()[:6000]}\n\n## Discussion\n"
                f"Full thread: [[{short(i)} (thread)]]\n\n## Related\n- [[Strategy Library]] · [[Experiment Registry]] · [[Evidence Levels]]\n")
        write(f"{F['04']}/{short(i)}.md", body, tags=["strategy"] + tag_v, title=short(i))
        lines.append(f"| [[{short(i)}]] | {stage(i)} | {len(cs)} |")
    if lines:
        write(f"{F['04']}/Strategy Library.md",
              "Every trading idea is a GitHub issue first. No strategy is trusted because a trader claims it works.\n\n"
              "| Strategy | Stage / evidence | Comments |\n|---|---|---|\n" + "\n".join(lines) +
              "\n\nNew idea? Use [[Strategy Template]] or the GitHub *Strategy submission* form.",
              tags=["strategy", "index"], title="📚 Strategy Library")


def thread_notes(d):
    idx = []
    for i in d["issues"]:
        cs = d["comments"].get(i["number"], [])
        parts = [f"> [!note] [#{i['number']} on GitHub]({i['html_url']}) · opened {i['created_at'][:10]} by {who(i)} · {i['state']}\n"]
        parts.append(f"## Opening post ({who(i)}, {i['created_at'][:16].replace('T', ' ')} UTC)\n{(i.get('body') or '').strip()[:8000]}\n")
        for c in cs:
            parts.append(f"## {who(c)} · {c['created_at'][:16].replace('T', ' ')} UTC\n{(c.get('body') or '').strip()[:8000]}\n")
        link = f"\nStrategy note: [[{short(i)}]]\n" if kind(i) == "strategy" else ""
        write(f"{F['07']}/{short(i)} (thread).md", "\n".join(parts) + link, tags=["communication", kind(i)], title=f"💬 {short(i)}")
        idx.append(f"| [[{short(i)} (thread)]] | {kind(i)} | {len(cs)} | {(cs[-1]['created_at'] if cs else i['created_at'])[:10]} |")
    reqs = d["relay"].get("requests", {})
    stat = {"received": "📨", "review": "🧠", "reviewed": "✅", "blocked": "⚠️"}
    rq = "\n".join(f"| #{r['issue']} | {stat.get(r['status'], r['status'])} {r['status']} | {r['received'][:16].replace('T', ' ')} | {r.get('title', '')[:70]} |"
                   for _, r in sorted(reqs.items(), key=lambda kv: kv[1]["received"], reverse=True)[:25])
    write(f"{F['07']}/Communications Index.md",
          "ChatGPT and Claude talk on GitHub issues. Discord #ai-team-chat shows a status card per request.\n\n"
          "## ChatGPT requests (newest first)\n| Issue | Status | Received (UTC) | Topic |\n|---|---|---|---|\n" + (rq or "| | | | |") +
          "\n\n## All threads\n| Thread | Type | Comments | Last activity |\n|---|---|---|---|\n" + "\n".join(idx),
          tags=["communication", "index"], title="💬 Team Communications")


def experiment_notes(d):
    rr = section(d["report"], "Research report: experiment v18+ only")
    upd = re.search(r"Updated (.+?UTC)", d["report"])
    prog = re.search(r"(?:Progress:|research target) (\d+)/300", d["report"])
    write(f"{F['05']}/5-Minute Experiment v18.md",
          "> [!success] Running · paper only · model frozen\n"
          f"> Progress **{prog.group(1) if prog else '?'} / 300** separate settled simulated trades. Nothing is judged before 300.\n\n"
          "## What it tests\nPolymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?\n\n"
          "## Frozen settings\n- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.\n"
          "- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.\n"
          "- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.\n\n"
          f"## Latest numbers ({upd.group(1) if upd else 'see report'})\n{rr}\n\n"
          "Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]",
          tags=["experiment", "experiment/5m", "status/running"], title="⏱️ 5-Minute Experiment (v18, frozen)")
    head = section(d["r15"], "Primary") or d["r15"][:1800]
    write(f"{F['05']}/15-Minute 12-Minute Rule (Phase 1).md",
          "> [!failure] Phase 1 finished: negative (exploratory)\n"
          "> The rule lost money after fees on 6,454 historical Kalshi rounds. Phase 2 is NOT approved. Decision pending with Jacob.\n\n"
          "## Pre-registration (frozen before results)\n" + d["prereg"][:5000] +
          f"\n\n## Result summary\n{head[:3000]}\n\nFull report: [[15-Minute Phase 1 Report]] · Strategy: see [[Strategy Library]] (#1)",
          tags=["experiment", "experiment/15m", "status/negative"], title="🕒 15-Minute '12-Minute Rule', Phase 1")
    write(f"{F['01']}/Experiment Registry.md",
          "| Experiment | Status | Evidence | Rules |\n|---|---|---|---|\n"
          f"| [[5-Minute Experiment v18]] | running, {prog.group(1) if prog else '?'}/300 | too early | model frozen, v18+ only |\n"
          "| [[15-Minute 12-Minute Rule (Phase 1)]] | refuted (Jacob, 2026-11-26) | L2-negative (exploratory) | PREREG frozen 2026-11-25 |\n"
          "| [[15-Minute Maker Test (paper)]] | running, paper | screening (100 fills) | PREREG frozen 2026-11-26, PR #9 |\n\n"
          "Every experiment is pre-registered; changing rules after results = a new, separately labelled analysis.",
          tags=["brain", "experiment", "index"], title="🧪 Experiment Registry")


def maker_notes(d):
    if not d["m15"]:
        return
    head = re.search(r"\*\*Verdict: (.+?)\*\*", d["m15"])
    write(f"{F['05']}/15-Minute Maker Test (paper).md",
          "> [!warning] Running · paper only · rules frozen (data/maker15/PREREG.md)\n"
          f"> {head.group(1) if head else 'see report'} The 100-fill verdict is a **screening** rule, not proof.\n\n"
          "## What it tests\nA resting buy limit 2c below the ask on the 12-minute AGREE side (Kalshi BTC 15m). "
          "Fills only when later public trades print strictly through the limit for the full size.\n\n"
          "## Known caveats (QC review, PR #9)\n- **Adverse selection:** losing orders always fill; many winners never do. "
          "Unfilled hypothetical wins are not earned P&L.\n- Same signal as the refuted 12-minute rule (2,022 historical trades, negative). "
          "Compare live results with the taker counterfactual in the audit.\n- Few independent days so far.\n\n"
          f"## Latest report\n{d['m15']}\n\nAudit: [[Maker Test QC Audit]] · Merged via PR #9 (2026-11-26).",
          tags=["experiment", "experiment/maker15", "status/running"], title="🪤 15-Minute Maker (limit-order) Test")
    write(f"{F['06']}/Maker Test QC Audit.md", d["m15audit"] or "_audit not run yet_", tags=["results", "experiment/maker15", "audit"],
          title="🔍 Maker Test QC Audit")


def result_notes(d):
    write(f"{F['06']}/5-Minute Research Report.md", d["report"] or "_report not generated yet_", tags=["results", "experiment/5m"],
          title="📈 5-Minute Research Report (all detail)")
    write(f"{F['06']}/15-Minute Phase 1 Report.md", d["r15"] or "_not run_", tags=["results", "experiment/15m"],
          title="📉 15-Minute Phase 1 Report")
    write(f"{F['06']}/Team Checks (latest).md", d["checks"] or "_no checks yet_", tags=["results", "checks"],
          title="🧮 Team Checks (latest)")
    write(f"{F['06']}/Results Index.md",
          "| Result | What it says |\n|---|---|\n| [[5-Minute Research Report]] | live paper experiment, too early (under 300 trades) |\n"
          "| [[15-Minute Phase 1 Report]] | 12-minute rule loses after fees (exploratory, negative) |\n"
          "| [[Team Checks (latest)]] | Data Auditor, Quant Analyst, Risk Sentinel |\n\n"
          "Reading rule: historical tests are exploratory. Only a pre-registered forward test with 300+ independent trades counts as evidence.",
          tags=["results", "index"], title="📊 Research Results")


def history_notes(d):
    by_day = defaultdict(list)
    for day, h, msg in d["log"]:
        by_day[day].append(f"- `{h}` {msg}")
    body = "\n\n".join(f"## {day}\n" + "\n".join(v) for day, v in sorted(by_day.items(), reverse=True))
    write(f"{F['03']}/Timeline.md", "Built from the git history (routine data commits left out). Newest first.\n\n" + body,
          tags=["history"], title="🗓️ Project Timeline")


def daily_note(d):
    upd = re.search(r"\*\*Data:\*\*(.+)", d["report"])
    prog = re.search(r"(?:Progress:|research target) (\d+)/300", d["report"])
    pnl = re.search(r"Simulated profit after fees:\*\* (.+)", d["report"])
    reqs = d["relay"].get("requests", {})
    today_reqs = [r for r in reqs.values() if r["received"].startswith(TODAY)]
    body = (f"## 5-minute experiment\n- {upd.group(1).strip() if upd else 'no data'}\n- Progress {prog.group(1) if prog else '?'}/300\n"
            f"- {pnl.group(1).strip() if pnl else ''}\n\n## Team requests today\n" +
            ("\n".join(f"- #{r['issue']} {r['status']}: {r.get('title', '')[:80]}" for r in today_reqs) or "- none") +
            f"\n\n## Checks\n{d['checks'][:2500]}\n\nPrevious days: see the [[Daily Reports Index]].")
    write(f"{F['08']}/{TODAY}.md", body, tags=["daily"], title=f"📅 {TODAY}")
    days = sorted([f[:-3] for f in os.listdir(os.path.join(ROOT, F["08"])) if re.match(r"\d{4}-\d{2}-\d{2}\.md$", f)], reverse=True)
    write(f"{F['08']}/Daily Reports Index.md", "\n".join(f"- [[{x}]]" for x in days), tags=["daily", "index"], title="📅 Daily Reports")


def brain_notes(d):
    ev = section(d["readme"], "Evidence levels")
    write(f"{F['01']}/Evidence Levels.md", ev + "\n\nPipeline stages and red flags: see [[Brain Overview]].",
          tags=["brain", "rules"], title="🎚️ Evidence Levels")
    pipe = section(d["readme"], "Pipeline (stage labels)")
    flags = section(d["readme"], "Red flags (check every submission)")
    write(f"{F['01']}/Brain Overview.md",
          "> [!quote] Polybot Brain = shared memory + evidence + coordination. Not a trading bot, not a trained model.\n\n"
          "## Six parts (design v1, issue #8)\n1. **Memory**: GitHub issues, reports, decisions, lessons. This vault is the readable view.\n"
          "2. **Retrieval**: search these notes (Obsidian search / graph); later a free local index.\n"
          "3. **Reasoning and evidence**: independent reviews + deterministic checks. Agreement is not evidence.\n"
          "4. **Coordination**: request status cards, task queue, founder approval gates.\n"
          "5. **Safety**: paper only, no keys, no paid services, no automatic strategy changes.\n"
          "6. **Learning**: [[Lessons Log]] keeps what failed and why. Nothing is retrained automatically.\n\n"
          f"## Pipeline\n{pipe}\n\n## Red flags\n{flags}\n\n"
          "Related: [[Evidence Levels]] · [[Experiment Registry]] · [[Decision Log]] · [[Team Overview]]",
          tags=["brain"], title="🧠 Polybot Brain")


def security_notes(d):
    risk = section(d["checks"], "🟡 Risk Sentinel") or section(d["checks"], "Risk Sentinel") or ""
    write(f"{F['10']}/Security Rules.md",
          "> [!danger] Non-negotiable\n> Paper trading only · $0 budget · no trading credentials · no real orders.\n\n"
          "## Rules\n- No passwords, API keys, tokens or webhook URLs in this vault, the repo, issues or chats.\n"
          "- Secrets live only in GitHub → Settings → Secrets. Names only, never values: `DISCORD_WEBHOOK` (#polybot tickets), "
          "`DISCORD_TEAM_WEBHOOK` (#ai-team-chat), `DISCORD_RESEARCH_WEBHOOK` (#research-reports), optional `GEMINI_API_KEY`, "
          "optional `CLAUDE_CODE_OAUTH_TOKEN` (fast mode).\n- Polymarket keys were revoked on 2026-11-25. The account watcher is off.\n"
          "- The repo is public: everything here is public.\n- ChatGPT posts through Jacob's account, so no experiment, rule or stage change "
          "happens from a GitHub comment alone. Jacob confirms directly.\n- #polybot carries tickets only.\n\n"
          f"## Risk Sentinel (latest automatic check)\n{risk}\n\nSee [[Team Checks (latest)]].",
          tags=["security"], title="🛡️ Security and Risk")


def dashboard(d):
    prog = re.search(r"(?:Progress:|research target) (\d+)/300", d["report"])
    pnl = re.search(r"Simulated profit after fees:\*\* (.+?) ·", d["report"])
    reqs = d["relay"].get("requests", {})
    open_reqs = [r for r in reqs.values() if r["status"] != "reviewed"]
    strat = [i for i in d["issues"] if kind(i) == "strategy"]
    folders = "\n".join(f"| {k} | [[{v}|{F[k]}]] |" for k, v in [
        ("01", "Brain Overview"), ("02", "Team Overview"), ("03", "Timeline"), ("04", "Strategy Library"),
        ("05", "Experiment Registry"), ("06", "Results Index"), ("07", "Communications Index"), ("08", "Daily Reports Index"),
        ("09", "Lessons Log"), ("10", "Security Rules"), ("11", "Roadmap")])
    body = (
        "> [!tip] Welcome to Polybot HQ\n> The long-term library of the Polybot research team. GitHub is the source of truth; "
        "this vault is the readable, linked view. Paper trading only · $0.\n\n"
        "## Right now\n"
        f"> [!example] ⏱️ 5-minute experiment\n> **{prog.group(1) if prog else '?'} / 300** separate settled trades · P&L {pnl.group(1) if pnl else '?'} · too early to judge\n> → [[5-Minute Experiment v18]]\n\n"
        "> [!failure] 🕒 15-minute '12-minute rule'\n> Phase 1 negative after fees (exploratory). Phase 2 not approved.\n> → [[15-Minute 12-Minute Rule (Phase 1)]]\n\n"
        f"> [!question] 📨 Open team requests: {len(open_reqs)}\n" +
        ("\n".join(f"> - #{r['issue']} {r['status']}: {r.get('title', '')[:70]}" for r in open_reqs[:6]) or "> - none") +
        "\n> → [[Communications Index]]\n\n"
        f"## Map\n| | Folder |\n|---|---|\n{folders}\n\n"
        f"## Strategies ({len(strat)})\n" + "\n".join(f"- [[{short(i)}]]: {stage(i)}" for i in strat) +
        "\n\n## Team\n" + " · ".join(f"[[{n}]]" for n, *_ in TEAM) +
        "\n\n## Quick links\n- [[Decision Log]] · [[Discoveries and Wins]] · [[Lessons Log]] · [[Roadmap]] · [[Security Rules]]\n"
        "- Templates: [[Strategy Template]] · [[Decision Template]] · [[Lesson Template]] · [[Daily Template]]\n\n"
        "> [!info] Tip: open **Graph view** (left sidebar) to see how everything connects. Colors = folders.\n")
    write(f"{F['00']}/Start Here.md", body, tags=["dashboard"], title="🏠 Polybot HQ")


def seeds():
    write(f"{F['03']}/Decision Log.md", """Team decisions, newest first. Add new ones with [[Decision Template]]. Each line: date · decision · who decided · source.

| Date | Decision | Decided by | Source |
|---|---|---|---|
| 2026-11-25 | Polybot HQ Discord: #ai-team-chat (team), #research-reports (reports), #polybot (tickets only) | Jacob + ChatGPT | GitHub #6 |
| 2026-11-25 | Strategy #5 (halfway leader) on hold at L0 until a source exists | ChatGPT + Claude | GitHub #5 |
| 2026-11-25 | 15m Phase 1 pre-registered: AGREE rule primary, asks not mids, no look-ahead | ChatGPT, Jacob | PREREG.md |
| 2026-11-25 | Research phase approved; model frozen (`rw-m1.4-c0.88-b15`), experiment counts v18+ only | ChatGPT, Jacob | data/report.md |
| 2026-11-25 | Polymarket API keys revoked; account watcher off; paper only | Jacob | — |
| 2026-11-25 | Budget $0: Gemini free tier only, no paid APIs | Jacob | — |
| pending | Mark the 12-minute rule `verdict:refuted` and skip Phase 2 | **Jacob to decide** | GitHub #1 |
""", tags=["history", "decisions"], title="⚖️ Decision Log", seed=True)
    write(f"{F['09']}/Lessons Log.md", """What went wrong, what we learned, what changed. Add new ones with [[Lesson Template]]. Failures stay on the record.

| Date | What happened | Lesson | Fix |
|---|---|---|---|
| 2026-11-25 | An HTTP 500 Discord error was counted as a filled, winning ticket (+13.26) | A ticket that wasn't delivered can't be a trade | v16: only delivered (2xx + message id) and FILLABLE tickets count |
| 2026-11-25 | Two runs saved data at once and one overwrote the other (lost rows, erased team board entry) | Parallel jobs need merge-safe saving | sync_data.py merges against a snapshot; boards merge by entry |
| 2026-11-25 | Model tuned on 155 correlated checkpoints from the same markets (in-sample) | Checkpoints in one market aren't independent; tuning on them overfits | split by market, then froze the model |
| 2026-11-25 | Break-even ignored the fee | Fees decide whether a "winning" rule makes money | break-even = price + fee·p·(1-p) everywhere |
| 2026-11-25 | Polymarket /bbo returned 404 on ~31% of live checks | Don't trust one endpoint | v19: /book fallback, source recorded |
| 2026-11-25 | 12-minute rule: won 78% but needed 81% to break even | A rule that wins "most of the time" can still lose money: the price already includes the trend | judged by fee-inclusive break-even, pre-registered |
| 2026-11-26 | A scoreboard landed in #polybot after rerouting | A run started on old code keeps old settings until it ends | audit in-flight runs after routing changes |
| 2026-11-26 | Scoreboard counted every checkpoint and every market ever, mixing old and new | Count separate rounds, not checks; same snapshot as the report | 1 pre-specified check per v18+ round |
""", tags=["lessons"], title="🧩 Mistakes and Lessons", seed=True)
    write(f"{F['06']}/Discoveries and Wins.md", """What the team found out and what it shipped. A discovery is a measured fact, not proof of profit.

## Discoveries
| Date | Finding | Strength | Source |
|---|---|---|---|
| 2026-11-25 | Kalshi and Polymarket US settle BTC 15m on identical BRTI values: 696/696 windows matched | measured, strong | [[15-Minute Phase 1 Report]] |
| 2026-11-25 | The 12-minute rule's trend side wins 78% but the price already demands 81%: no edge after fees | exploratory, negative | [[15-Minute Phase 1 Report]] |
| 2026-11-25 | Polymarket /book is reliable when /bbo returns 404 | measured | [[Lessons Log]] |
| 2026-11-26 | Frozen 5m model slightly sharper than the market price (Brier 0.138 vs 0.143, 100 rounds) | early, not evidence of profit | [[5-Minute Research Report]] |

## Wins (shipped)
| Date | What | Why it matters |
|---|---|---|
| 2026-11-25 | Merge-safe data saving | no more lost rows |
| 2026-11-25 | Honest scoreboard: only delivered, fillable tickets count; fee-inclusive break-even | numbers we can trust |
| 2026-11-25 | Research lab + strategy database on GitHub issues | every claim gets checked, not trusted |
| 2026-11-26 | Polybot HQ Discord + request status cards (📨 🧠 ✅ ⚠️) | Jacob sees the team work without copy-paste |
| 2026-11-26 | This vault, rebuilt from GitHub every 3 hours | long-term memory for Polybot Brain |
""", tags=["results", "discoveries", "wins"], title="🏆 Discoveries and Wins", seed=True)
    write(f"{F['11']}/Roadmap.md", """Planned work. Nothing here changes an experiment without Jacob's approval.

## Now
- [ ] 5-minute experiment: keep collecting until 300 separate settled trades (paper)
- [ ] Jacob: decide on #1 (refute the 12-minute rule, skip Phase 2?)
- [ ] Fresh #polybot channel (tickets only), old one archived
- [ ] Optional: fast mode (Claude replies within minutes) once `CLAUDE_CODE_OAUTH_TOKEN` is added

## Next (Polybot Brain, issue #8)
- [ ] Phase A: inventory + architecture doc + machine-readable schema (no experiment edits)
- [ ] Phase B: free local search index over the vault + source-linked daily briefing
- [ ] Phase C: task queue, deterministic auditors, tests (duplicates ignored, unsupported claims stay unverified, strategy changes can't auto-execute)

## Later
- [ ] Gemini free key for automatic reviews
- [ ] Red Team / Archivist / Research Coordinator roles (deterministic first)
""", tags=["roadmap"], title="🗺️ Future Roadmap", seed=True)
    tpl = {
        "Strategy Template": "---\ntags: [strategy]\nissue: \nstage: stage:1-submitted\nevidence: evidence:L0-claim\n---\n# {{title}}\n\n## Claim\n\n## Original source\n\n## Exact rules\n\n## Fees and delay considered?\n\n## Red flags\n\n## Test plan\n\n## Links\n- [[Strategy Library]]\n",
        "Decision Template": "---\ntags: [decisions]\ndate: {{date}}\n---\n# Decision: {{title}}\n\n- **Decision:**\n- **Decided by:** (Jacob approves experiment/rule changes)\n- **Evidence:**\n- **Source:** GitHub #\n- **Alternatives considered:**\n\nAdd a row to [[Decision Log]].\n",
        "Lesson Template": "---\ntags: [lessons]\ndate: {{date}}\n---\n# Lesson: {{title}}\n\n- **What happened:**\n- **Impact:**\n- **Root cause:**\n- **Lesson:**\n- **Fix / guard added:**\n\nAdd a row to [[Lessons Log]].\n",
        "Daily Template": "---\ntags: [daily]\ndate: {{date}}\n---\n# {{date}}\n\n## What moved\n\n## Decisions\n\n## Problems\n\n## Tomorrow\n",
    }
    for name, body in tpl.items():
        path = os.path.join(ROOT, "_templates", f"{name}.md")
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(body)
            written.append(f"_templates/{name}.md")


def obsidian_config():
    """Core settings only: templates folder, graph colors per folder. Created once; Jacob's later changes win."""
    cfg = os.path.join(ROOT, ".obsidian")
    os.makedirs(cfg, exist_ok=True)
    colors = [0x7C3AED, 0xEC4899, 0x06B6D4, 0x64748B, 0xF59E0B, 0x22C55E, 0x3B82F6, 0x10B981, 0x94A3B8, 0xEF4444, 0xF97316, 0xA3E635]
    files = {
        "templates.json": {"folder": "_templates"},
        "core-plugins.json": ["file-explorer", "global-search", "switcher", "graph", "backlink", "outgoing-link", "tag-pane",
                              "page-preview", "templates", "note-composer", "command-palette", "outline", "word-count", "file-recovery"],
        "app.json": {"newFileLocation": "folder", "newFileFolderPath": "00 — Main Dashboard", "showFrontmatter": False},
        "graph.json": {"colorGroups": [{"query": f'path:"{F[k]}"', "color": {"a": 1, "rgb": c}} for k, c in zip(F, colors)],
                       "showTags": True, "showArrow": True},
        "workspace.json": None,
    }
    for name, data in files.items():
        p = os.path.join(cfg, name)
        if data is None or os.path.exists(p):
            continue
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    d = load()
    for v in F.values():
        os.makedirs(os.path.join(ROOT, v), exist_ok=True)
    obsidian_config()
    seeds()
    team_notes()
    brain_notes(d)
    experiment_notes(d)
    result_notes(d)
    maker_notes(d)
    history_notes(d)
    security_notes(d)
    if d["gh_ok"]:
        strategy_notes(d)
        thread_notes(d)
    daily_note(d)
    dashboard(d)
    leaks = [p for p in written if any(r.search(read(os.path.join(ROOT, p))) for r in SECRET_RES)]
    if leaks:
        raise SystemExit(f"vault: secret-looking text survived redaction in {leaks}")
    print(f"vault: wrote {len(written)} notes under {ROOT}")


if __name__ == "__main__":
    main()
