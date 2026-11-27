"""Team relay ($0): ChatGPT <-> Claude through GitHub issue comments, Jacob kept informed on Discord.

How messages move
- ChatGPT posts comments on issues (through Jacob's GitHub connection, so they show as j42002).
  It marks them with a header like "## ChatGPT → Claude" or the signature "— ChatGPT".
- `inbound` (GitHub Actions, on every new comment, every new issue, and every 30 min): each ChatGPT request
  (comment, or an issue ChatGPT opened) gets ONE status card in #ai-team-chat. The card is edited in place
  as the status moves, so there are no duplicate messages:
     📨 Received (the relay delivered it; NOT a Claude review)  🧠 Under review  ✅ Reviewed  ⚠️ Blocked
  Ages and timestamps use Discord's own <t:…> format, so "received 2 hours ago" stays current by itself.
- Claude answers either instantly (claude-fast.yml, if Jacob added CLAUDE_CODE_OAUTH_TOKEN) or from the hourly
  scheduled task. `pending` lists what still needs a reply. Claude writes JSON files in lab/outbox/:
  a "status" item (🧠 / ⚠️) and the reply itself.
- `outbound` (GitHub Actions, on push to lab/outbox/): posts the reply as an issue comment (as the
  GitHub Actions bot, headed "Claude → ChatGPT") and a Discord summary: discussed / agreed / disagreed /
  next / decision needed.

Loop and duplicate guards
- lab/relay_state.json records every announced comment, every answered comment, every sent outbox item.
  Nothing is announced or posted twice.
- Claude answers each ChatGPT comment at most once, never answers Claude/bot comments, and posts at most
  CLAUDE_DAILY_MAX comments a day. Once an issue has had MAX_AI_ROUNDS ChatGPT↔Claude exchanges in 24h, it
  waits for Jacob.
- Comments posted with the built-in GITHUB_TOKEN do not trigger workflows, so a reply can't set off a reply.
- ChatGPT only posts when Jacob opens a ChatGPT session; it does not run on its own.
Decisions: replies may agree, disagree or propose. Changes to experiments, rules or stages wait for Jacob.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

import requests

API = "https://api.github.com"
REPO = os.getenv("GITHUB_REPOSITORY", "j42002/polybot")
TOKEN = os.getenv("GITHUB_TOKEN", "")
# Team chat and reports have their OWN webhooks. The ticket webhook (DISCORD_WEBHOOK, #polybot) is never used here:
# if a team webhook is missing, the message waits in the queue and the run says so. It never leaks into #polybot.
TEAM_WEBHOOK = os.getenv("DISCORD_TEAM_WEBHOOK", "")
RESEARCH_WEBHOOK = os.getenv("DISCORD_RESEARCH_WEBHOOK", "")
STATE = os.path.join("lab", "relay_state.json")
OUTBOX = os.path.join("lab", "outbox")
CLAUDE_DAILY_MAX = 12
MAX_AI_ROUNDS = 3
CHATGPT_RE = re.compile(r"^\s*#{0,6}\s*\**\s*ChatGPT\s*(→|->)|—\s*ChatGPT\b", re.I | re.M)
CLAUDE_RE = re.compile(r"^\s*#{0,6}\s*\**\s*Claude\s*(→|->)", re.I | re.M)


def headers():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def gh(method, path, session=None, **kw):
    s = session or requests
    r = s.request(method, f"{API}/repos/{REPO}{path}", headers=headers(), timeout=20, **kw)
    if r.status_code >= 400:
        raise RuntimeError(f"GitHub {method} {path} -> {r.status_code}")
    return r


def load_state():
    try:
        with open(STATE, encoding="utf-8") as f:
            s = json.load(f)
    except Exception:
        s = {}
    for k, v in (("notified", []), ("answered", {}), ("sent", []), ("posted", []), ("commented", {}), ("discord_sent", []), ("requests", {})):
        s.setdefault(k, v)
    return s


def save_state(s):
    os.makedirs("lab", exist_ok=True)
    s["notified"] = s["notified"][-2000:]
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=1, sort_keys=True)


def is_chatgpt(c):
    login = (c.get("user") or {}).get("login", "")
    body = c.get("body") or ""
    # Only Jacob's account (ChatGPT posts through it). The repo is public, so anyone can comment: a stranger
    # copying the "ChatGPT →" header must not enter the queue or use up the daily cap / 3-round limit.
    return login == "j42002" and bool(CHATGPT_RE.search(body)) and not CLAUDE_RE.search(body)


def is_claude(c):
    login = (c.get("user") or {}).get("login", "")
    return login == "github-actions[bot]" and bool(CLAUDE_RE.search(c.get("body") or ""))


def issue_num(c):
    return int(c["issue_url"].rstrip("/").split("/")[-1])


def recent_comments(session=None, days=7):
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    out, page = [], 1
    while True:
        r = gh("GET", "/issues/comments", session, params={"since": since, "per_page": 100, "page": page,
                                                            "sort": "created", "direction": "asc"})
        out += r.json()
        if len(r.json()) < 100:
            return out
        page += 1


def excerpt(body, n=420):
    lines = [l.strip() for l in (body or "").splitlines() if l.strip()]
    head = next((re.sub(r"^#+\s*", "", l) for l in lines if l.startswith("#")), "")
    rest = " ".join(l.lstrip("-*# ").strip() for l in lines if not l.startswith("#"))
    rest = re.sub(r"\s+", " ", rest)
    return head, (rest[:n] + ("…" if len(rest) > n else ""))


def discord(payload, session=None, channel="team", username=None):
    """True only if Discord accepted the message (2xx). channel: 'team' -> #ai-team-chat,
    'research' -> #research-reports (falls back to the team channel, never to #polybot)."""
    hook = (RESEARCH_WEBHOOK or TEAM_WEBHOOK) if channel == "research" else TEAM_WEBHOOK
    if not hook:
        print(f"relay: no DISCORD_TEAM_WEBHOOK{' / DISCORD_RESEARCH_WEBHOOK' if channel == 'research' else ''} secret: "
              "message kept in the queue (not sent anywhere)")
        return False
    if username:
        payload = {**payload, "username": username}
    s = session or requests
    try:
        r = s.post(hook, json=payload, timeout=10)
    except requests.RequestException as e:
        print(f"relay: Discord request failed ({e.__class__.__name__}), will retry next run")
        return False
    if not 200 <= r.status_code < 300:
        print(f"relay: Discord answered HTTP {r.status_code}, will retry next run")
        return False
    return True


def _hook(channel):
    return (RESEARCH_WEBHOOK or TEAM_WEBHOOK) if channel == "research" else TEAM_WEBHOOK


def discord_post(payload, session=None, channel="team", username=None):
    """Post and return (ok, message_id) so the card can be edited later (Discord ?wait=true)."""
    hook = _hook(channel)
    if not hook:
        return False, None
    s = session or requests
    try:
        r = s.post(hook + ("&" if "?" in hook else "?") + "wait=true", json={**payload, "username": username or "Polybot HQ"},
                   timeout=10)
    except Exception:
        return False, None
    if not 200 <= r.status_code < 300:
        print(f"relay: Discord answered HTTP {r.status_code}, card will retry next run")
        return False, None
    try:
        return True, str(r.json().get("id") or "") or None
    except Exception:
        return True, None


def discord_edit(msg_id, payload, session=None, channel="team"):
    """Edit a card this webhook posted. Returns 'ok', 'gone' (deleted: post a new one) or 'retry'."""
    hook = _hook(channel)
    if not hook:
        return "retry"
    s = session or requests
    try:
        r = s.patch(f"{hook}/messages/{msg_id}", json=payload, timeout=10)
    except Exception:
        return "retry"
    if 200 <= r.status_code < 300:
        return "ok"
    return "gone" if r.status_code == 404 else "retry"


# ---------- request status cards ----------
STATUS = {
    "received": ("📨 Received", 0x10A37F, "The relay delivered it. Claude has **not** reviewed it yet."),
    "review": ("🧠 Under review", 0x5865F2, "Claude is working on a reply."),
    "reviewed": ("✅ Reviewed", 0x22C55E, "Claude replied on GitHub."),
    "blocked": ("⚠️ Blocked", 0xF5A623, "Claude can't finish this without something else first."),
}
ORDER = {"received": 0, "review": 1, "blocked": 1, "reviewed": 2}


def _epoch(iso):
    try:
        return int(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
    except Exception:
        return None


def _now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _dur(a, b):
    ea, eb = _epoch(a), _epoch(b)
    if ea is None or eb is None:
        return ""
    m = max(0, eb - ea) // 60
    return f"{m // 60}h {m % 60}m" if m >= 60 else f"{m} min"


def status_embed(key, r):
    label, color, meaning = STATUS.get(r["status"], STATUS["received"])
    t = lambda iso, f="f": f"<t:{_epoch(iso)}:{f}>" if _epoch(iso) else iso
    lines = [f"**#{r['issue']} · {r.get('title') or 'ChatGPT request'}**"[:300]]
    if r.get("summary"):
        lines.append(r["summary"][:300])
    lines.append(f"**Status:** {label}. {meaning}")
    lines.append(f"**Received:** {t(r['received'])} ({t(r['received'], 'R')})")
    if r["status"] == "review" and r.get("since"):
        lines.append(f"**Claude started:** {t(r['since'], 'R')}")
    if r["status"] == "blocked":
        lines.append(f"**Why:** {r.get('reason') or 'not given'}")
        if r.get("next"):
            lines.append(f"**Next:** {r['next']}")
    if r["status"] == "reviewed":
        lines.append(f"**Claude replied:** {t(r.get('since') or r['received'])}" +
                     (f" · [read the reply]({r['reply_url']})" if r.get("reply_url") else ""))
        lines.append(f"**Response time:** {_dur(r['received'], r.get('since') or r['received'])}")
    elif r["status"] != "reviewed":
        lines.append("_Claude checks for requests every hour (instantly once fast mode is on)._")
    return {"embeds": [{"title": f"{label} · ChatGPT request on #{r['issue']}"[:250], "url": r.get("url"),
                        "description": "\n".join(lines)[:4000], "color": color,
                        "footer": {"text": f"request {key} · paper only · $0 · decisions stay with Jacob"}}]}


def new_request(st, key, issue, title, summary, url, created):
    st["requests"][key] = {"issue": issue, "title": title, "summary": summary, "url": url, "received": created,
                           "status": "received", "since": created, "dirty": True, "msg": None,
                           "history": [["received", _now_iso()]]}


def set_status(st, key, status, **kw):
    """Move a request forward. Never backwards (a late 'review' can't undo 'reviewed')."""
    r = st["requests"].get(str(key))
    if not r or status not in STATUS:
        return False
    if ORDER[status] < ORDER[r["status"]]:
        return False
    if r["status"] == status and all(r.get(k) == v for k, v in kw.items()):
        return False
    r.update(kw)
    r["status"] = status
    r["since"] = kw.get("since") or _now_iso()
    r["history"].append([status, r["since"]])
    r["dirty"] = True
    return True


def sync_cards(st, session=None, max_new=10):
    """Post or edit every card whose status changed. Only a 2xx from Discord clears the 'dirty' flag."""
    new = 0
    for key, r in st["requests"].items():
        if not r.get("dirty"):
            continue
        payload = status_embed(key, r)
        if r.get("msg"):
            res = discord_edit(r["msg"], payload, session)
            if res == "ok":
                r["dirty"] = False
                continue
            if res == "retry":
                continue
        if new >= max_new:
            continue
        ok, mid = discord_post(payload, session, username="Polybot HQ")
        if ok:
            r["msg"], r["dirty"] = mid, False
            new += 1


def react(session, path, content="eyes"):
    """Small GitHub reaction (👀) on the request itself: visible proof the relay saw it. Best effort."""
    try:
        gh("POST", path, session, json={"content": content})
    except Exception:
        pass


def is_chatgpt_issue(i):
    return ("number" in i and "pull_request" not in i and (i.get("user") or {}).get("login") == "j42002"
            and bool(CHATGPT_RE.search(i.get("body") or "")))


def recent_issues(session=None, days=7):
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        r = gh("GET", "/issues", session, params={"state": "all", "since": since, "per_page": 100, "page": 1})
        return [i for i in r.json() if isinstance(i, dict) and "number" in i and "issue_url" not in i]
    except Exception as e:
        print(f"relay: could not list issues ({e})")
        return []


# ---------- inbound: one status card per ChatGPT request ----------

def inbound(session=None):
    st = load_state()
    n = 0
    for c in recent_comments(session):
        cid = str(c["id"])
        if not is_chatgpt(c) or cid in st["requests"]:
            continue
        if cid in st["answered"]:                      # older, already answered before status cards existed
            continue
        head, text = excerpt(c["body"], 280)
        new_request(st, cid, issue_num(c), head, text, c["html_url"], c["created_at"])
        react(session, f"/issues/comments/{cid}/reactions")
        if cid not in st["notified"]:
            st["notified"].append(cid)
        n += 1
    for i in recent_issues(session):
        key = f"issue-{i['number']}"
        if not is_chatgpt_issue(i) or key in st["requests"] or key in st["answered"]:
            continue
        _, text = excerpt(i.get("body"), 280)
        new_request(st, key, i["number"], i.get("title", ""), text, i.get("html_url"), i.get("created_at") or _now_iso())
        react(session, f"/issues/{i['number']}/reactions")
        n += 1
    sync_cards(st, session)
    save_state(st)
    waiting = sum(1 for r in st["requests"].values() if r.get("dirty"))
    print(f"relay inbound: {n} new ChatGPT request(s); {waiting} card(s) waiting for Discord")
    return n


# ---------- pending: what Claude still needs to answer (guards applied) ----------

def pending(session=None):
    st = load_state()
    cs = recent_comments(session, days=3)
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    claude_today = sum(1 for c in cs if is_claude(c) and c["created_at"].startswith(today))
    queued = {str(o.get("reply_to")) for o in outbox_items() if o.get("reply_to") and o.get("kind") != "status"}
    queued |= {str(a) for o in outbox_items() for a in (o.get("also_answers") or [])}
    out, skipped = [], []
    for c in cs:
        if not is_chatgpt(c):
            continue
        cid = str(c["id"])
        if cid in st["answered"] or cid in queued:
            continue
        iss = issue_num(c)
        day_ago = (now - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
        rounds = sum(1 for x in cs if is_claude(x) and issue_num(x) == iss and x["created_at"] >= day_ago)
        if rounds >= MAX_AI_ROUNDS:
            skipped.append((cid, iss, f"{rounds} AI rounds on #{iss} in 24h: waiting for Jacob"))
            continue
        if claude_today + len(out) >= CLAUDE_DAILY_MAX:
            skipped.append((cid, iss, f"daily cap {CLAUDE_DAILY_MAX} reached"))
            continue
        out.append({"comment_id": c["id"], "issue": iss, "url": c["html_url"], "created_at": c["created_at"],
                    "body": c["body"], "context": _context(cs, iss, c["id"])})
    for i in recent_issues(session, days=3):
        key = f"issue-{i['number']}"
        if not is_chatgpt_issue(i) or key in st["answered"] or key in queued:
            continue
        if claude_today + len(out) >= CLAUDE_DAILY_MAX:
            skipped.append((key, i["number"], f"daily cap {CLAUDE_DAILY_MAX} reached"))
            continue
        out.append({"comment_id": key, "issue": i["number"], "url": i.get("html_url"), "created_at": i.get("created_at"),
                    "title": i.get("title"), "body": i.get("body"), "context": _context(cs, i["number"], None)})
    return out, skipped


def _context(cs, iss, cid):
    """Earlier comments on the same issue (newest 6, trimmed) so a fresh Claude session has the thread."""
    prior = [c for c in cs if issue_num(c) == iss and c["id"] != cid]
    return [{"id": c["id"], "who": "Claude" if is_claude(c) else "ChatGPT" if is_chatgpt(c) else (c.get("user") or {}).get("login"),
             "created_at": c["created_at"], "body": (c.get("body") or "")[:1500]} for c in prior[-6:]]


def outbox_items():
    if not os.path.isdir(OUTBOX):
        return []
    items = []
    for name in sorted(os.listdir(OUTBOX)):
        if name.endswith(".json"):
            try:
                with open(os.path.join(OUTBOX, name), encoding="utf-8") as f:
                    o = json.load(f)
                o.setdefault("id", name[:-5])
                items.append(o)
            except Exception as e:
                print(f"relay: bad outbox file {name}: {e}")
    return items


# ---------- outbound: post Claude's replies + Discord summary ----------

def summary_embed(o):
    """Discord card in the founder's format: who said what, the decision, next step, budget."""
    d = o.get("discord") or {}
    lines = []
    for key, label in (("chatgpt", "ChatGPT"), ("claude", "Claude"), ("discussed", "Discussed"), ("agreed", "Agreed"),
                       ("disagreed", "Disagreed"), ("decision", "Decision"), ("next", "Next step")):
        if d.get(key):
            lines.append(f"**{label}:** {d[key]}")
    if d.get("text"):
        lines.insert(0, str(d["text"]))
    if d.get("decision_needed"):
        lines.append(f"⚠️ **Your decision needed:** {d['decision_needed']}")
    lines.append("✅ **Budget:** $0.00 · paper only")
    title = d.get("title") or "🤝 AI Team Communication"
    return {"title": title[:250], "url": o.get("_url"), "description": "\n\n".join(lines)[:4000],
            "color": 0xF5A623 if d.get("decision_needed") else 0x5865F2,
            "footer": {"text": f"Issue #{o['issue']}" if o.get("issue") else "Polybot research team"}}


def outbound(session=None):
    """Two stages per outbox item, each recorded on its own so a failure never repeats the other:
    1) GitHub comment (posted once; its URL is remembered)  2) Discord card (retried until Discord accepts it)."""
    st = load_state()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    done = 0
    for o in outbox_items():
        oid = str(o["id"])
        if oid in st["sent"]:
            continue
        kind = o.get("kind", "comment+discord")
        if kind == "status":                           # 🧠 / ⚠️ only: edits the request card, no GitHub comment
            set_status(st, o.get("reply_to"), o.get("status", "review"),
                       **{k: o[k] for k in ("reason", "next") if o.get(k)})
            st["sent"].append(oid)
            save_state(st)
            done += 1
            continue
        if "comment" in kind and oid not in st["commented"]:
            rt = str(o.get("reply_to") or "")
            if rt and rt in st["answered"]:
                print(f"relay: {oid}: comment {rt} already answered, no second comment")
                st["commented"][oid] = "skipped-duplicate"
                set_status(st, rt, "reviewed")
            else:
                posted_today = [p for p in st["posted"] if p.startswith(today)]
                if len(posted_today) >= CLAUDE_DAILY_MAX:
                    print(f"relay: daily cap reached, {oid} waits")
                    continue
                body = o["body"]
                if not CLAUDE_RE.search(body):
                    body = "## Claude → ChatGPT\n\n" + body
                body += "\n\n_Posted by the team relay for Claude (lead developer). Paper only, $0. Major decisions wait for Jacob._"
                try:
                    r = gh("POST", f"/issues/{o['issue']}/comments", session, json={"body": body})
                except Exception as e:                 # one bad item must not block the rest of the queue
                    print(f"relay: {oid}: GitHub comment failed ({e}); stays queued, other items continue")
                    continue
                st["commented"][oid] = r.json().get("html_url")
                for a in ([rt] if rt else []) + [str(x) for x in (o.get("also_answers") or [])]:
                    st["answered"][a] = r.json().get("id")
                    set_status(st, a, "reviewed", reply_url=r.json().get("html_url"))
                st["posted"].append(f"{today} {oid}")
            save_state(st)
        if "discord" in kind or "report" in kind:
            o["_url"] = st["commented"].get(oid) if str(st["commented"].get(oid, "")).startswith("http") else None
            channel = "research" if "report" in kind else "team"
            user = (o.get("discord") or {}).get("username") or ("Claude (lead developer)" if channel == "team" else "Polybot HQ")
            if not discord({"embeds": [summary_embed(o)]}, session, channel=channel, username=user):
                print(f"relay: {oid}: Discord not delivered yet, stays queued")
                continue
            st["discord_sent"].append(oid)
        st["sent"].append(oid)
        save_state(st)                                 # after every item: a later failure can't cause a repeat
        done += 1
    sync_cards(st, session)
    save_state(st)
    print(f"relay outbound: {done} item(s) fully delivered")
    return done


def validate(paths):
    """Gate for files Claude wrote in the fast workflow: only well-formed reply/status items may be committed."""
    bad = []
    for p in paths:
        try:
            o = json.load(open(p, encoding="utf-8"))
            assert os.path.dirname(os.path.abspath(p)) == os.path.abspath(OUTBOX), "outside lab/outbox"
            assert o.get("kind") in ("comment+discord", "status"), "kind must be comment+discord or status"
            assert isinstance(o.get("issue"), int) and o.get("reply_to"), "issue (int) and reply_to required"
            if o["kind"] == "status":
                assert o.get("status") in ("review", "blocked"), "status must be review or blocked"
            else:
                assert isinstance(o.get("body"), str) and len(o["body"]) < 60000, "body required"
        except Exception as e:
            bad.append(f"{p}: {e}")
    for b in bad:
        print("relay validate: REJECTED", b)
    return not bad


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "inbound":
        inbound()
    elif cmd == "outbound":
        outbound()
    elif cmd == "pending":
        items, skipped = pending()
        print(json.dumps({"pending": items, "skipped": skipped}, indent=1))
    elif cmd == "validate":
        sys.exit(0 if validate(sys.argv[2:]) else 1)
    else:
        print("usage: python relay.py inbound|outbound|pending|validate <files>")
