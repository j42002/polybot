"""Team relay ($0): ChatGPT <-> Claude through GitHub issue comments, Jacob kept informed on Discord.

How messages move
- ChatGPT posts comments on issues (through Jacob's GitHub connection, so they show as j42002).
  It marks them with a header like "## ChatGPT → Claude" or the signature "— ChatGPT".
- `inbound` (GitHub Actions, on every new comment + every 30 min): each ChatGPT comment is announced
  ONCE in #polybot.
- Claude runs as a scheduled task every few hours: `pending` lists ChatGPT comments that still need a
  reply. Claude writes each reply as a JSON file in lab/outbox/ and pushes it.
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
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")
STATE = os.path.join("lab", "relay_state.json")
OUTBOX = os.path.join("lab", "outbox")
CLAUDE_DAILY_MAX = 8
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
    for k, v in (("notified", []), ("answered", {}), ("sent", []), ("posted", [])):
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
    return not login.endswith("[bot]") and bool(CHATGPT_RE.search(body)) and not CLAUDE_RE.search(body)


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


def discord(payload, session=None):
    if not WEBHOOK:
        print("relay: no DISCORD_WEBHOOK, skipped Discord")
        return False
    s = session or requests
    r = s.post(WEBHOOK, json=payload, timeout=10)
    return 200 <= r.status_code < 300


# ---------- inbound: announce new ChatGPT comments once ----------

def inbound(session=None):
    st = load_state()
    n = 0
    for c in recent_comments(session):
        if not is_chatgpt(c) or str(c["id"]) in st["notified"]:
            continue
        head, text = excerpt(c["body"])
        ok = discord({"embeds": [{
            "title": f"📥 ChatGPT posted on #{issue_num(c)}"[:250],
            "description": f"**{head}**\n{text}"[:3900] if head else text[:3900],
            "url": c["html_url"], "color": 0x10A37F,
            "footer": {"text": "Claude replies on GitHub within ~3 hours · paper only · $0"}}]}, session)
        if ok or not WEBHOOK:
            st["notified"].append(str(c["id"]))
            n += 1
    save_state(st)
    print(f"relay inbound: {n} new ChatGPT comment(s) announced")
    return n


# ---------- pending: what Claude still needs to answer (guards applied) ----------

def pending(session=None):
    st = load_state()
    cs = recent_comments(session, days=3)
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    claude_today = sum(1 for c in cs if is_claude(c) and c["created_at"].startswith(today))
    queued = {str(o.get("reply_to")) for o in outbox_items() if o.get("reply_to")}
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
                    "body": c["body"]})
    return out, skipped


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
    st = load_state()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    done = 0
    for o in outbox_items():
        oid = str(o["id"])
        if oid in st["sent"]:
            continue
        kind = o.get("kind", "comment+discord")
        if "comment" in kind:
            rt = str(o.get("reply_to") or "")
            if rt and rt in st["answered"]:
                print(f"relay: {oid} skipped, comment {rt} already answered")
                st["sent"].append(oid)
                continue
            posted_today = [p for p in st["posted"] if p.startswith(today)]
            if len(posted_today) >= CLAUDE_DAILY_MAX:
                print(f"relay: daily cap reached, {oid} waits")
                continue
            body = o["body"]
            if not CLAUDE_RE.search(body):
                body = "## Claude → ChatGPT\n\n" + body
            body += "\n\n_Posted by the team relay for Claude (lead developer). Paper only, $0. Major decisions wait for Jacob._"
            r = gh("POST", f"/issues/{o['issue']}/comments", session, json={"body": body})
            o["_url"] = r.json().get("html_url")
            if rt:
                st["answered"][rt] = r.json().get("id")
            st["posted"].append(f"{today} {oid}")
        if "discord" in kind:
            discord({"embeds": [summary_embed(o)]}, session)
        st["sent"].append(oid)
        save_state(st)                                 # after every item: a later failure can't cause a repeat
        done += 1
    save_state(st)
    print(f"relay outbound: {done} item(s) sent")
    return done


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "inbound":
        inbound()
    elif cmd == "outbound":
        outbound()
    elif cmd == "pending":
        items, skipped = pending()
        print(json.dumps({"pending": items, "skipped": skipped}, indent=1))
    else:
        print("usage: python relay.py inbound|outbound|pending")
