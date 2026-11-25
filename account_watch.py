"""polybot account watcher - READ-ONLY view of Jacob's Polymarket US account.

Only ever sends GET requests: account balances and portfolio activity.
It has no code path that creates, changes or cancels an order.

Setup (GitHub repo secrets, added by Jacob himself):
  POLYMARKET_KEY_ID      the Key ID from polymarket.us/developer
  POLYMARKET_SECRET_KEY  the Secret Key shown once when the key is created

Privacy: this repo is PUBLIC (logs and data/ are visible to anyone), so the
watcher never prints balances or trades to the log and never writes them to
data/. It only keeps SHA-256 fingerprints of activity IDs it has already
posted (data/account_seen.txt), which reveal nothing. Account details go to
Discord only.

Auth (docs.polymarket.us/api-reference/authentication): headers
X-PM-Access-Key, X-PM-Timestamp (ms), X-PM-Signature = base64(Ed25519 sign of
f"{timestamp}{METHOD}{path}") using the first 32 bytes of the base64 secret.
"""
import base64
import hashlib
import json
import os
import time

API = "https://api.polymarket.us"
SEEN = os.path.join("data", "account_seen.txt")
KEY_ID = os.getenv("POLYMARKET_KEY_ID", "")
SECRET = os.getenv("POLYMARKET_SECRET_KEY", "")


def enabled():
    return bool(KEY_ID and SECRET)


def _signer():
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    raw = base64.b64decode(SECRET.strip())
    return Ed25519PrivateKey.from_private_bytes(raw[:32])


def sign_headers(method, path, key=None, ts=None):
    ts = str(ts or int(time.time() * 1000))
    sig = (key or _signer()).sign(f"{ts}{method}{path}".encode())
    return {"X-PM-Access-Key": KEY_ID, "X-PM-Timestamp": ts,
            "X-PM-Signature": base64.b64encode(sig).decode(), "Content-Type": "application/json"}


def get(session, path, query=""):
    """Signed GET. Path is signed without the query string."""
    r = session.get(API + path + (f"?{query}" if query else ""), headers=sign_headers("GET", path), timeout=10)
    if r.status_code >= 400:
        raise RuntimeError(f"{path} -> HTTP {r.status_code}")
    return r.json()


# ---------- tolerant field pickers (response shapes vary by type) ----------

def _unwrap(v):
    if isinstance(v, dict) and "value" in v and len(v) <= 3:
        return v["value"]
    return v


def pick(obj, *names, depth=0):
    """First value whose key matches one of names (case-insensitive), searched depth-first."""
    want = {n.lower() for n in names}
    if depth > 5:
        return None
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.lower() in want and v not in (None, "", [], {}):
                return _unwrap(v)
        for v in obj.values():
            found = pick(v, *names, depth=depth + 1)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for v in obj:
            found = pick(v, *names, depth=depth + 1)
            if found is not None:
                return found
    return None


def first_list(obj):
    """The activity list, wherever the response nests it."""
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    if isinstance(obj, dict):
        for k in ("activities", "data", "items", "results"):
            if isinstance(obj.get(k), list):
                return [x for x in obj[k] if isinstance(x, dict)]
        for v in obj.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v
    return []


def fingerprint(a):
    ident = a.get("id") or pick(a, "id", "activityId", "tradeId", "orderId") or json.dumps(a, sort_keys=True)
    return hashlib.sha256(str(ident).encode()).hexdigest()[:24]


def money(v):
    try:
        return f"${float(v):,.2f}"
    except (TypeError, ValueError):
        return str(v)


def event_link(slug):
    if not slug:
        return None
    slug = str(slug)
    if slug.startswith("cpc-"):
        slug = slug[4:]
    return f"https://polymarket.us/event/{slug}"


def describe(a):
    """One Discord embed for one activity, built from whatever fields exist."""
    kind = str(pick(a, "type", "activityType", "kind") or "ACTIVITY").replace("ACTIVITY_TYPE_", "").replace("_", " ").title()
    slug = pick(a, "marketSlug", "slug")
    side = pick(a, "intent", "side", "outcome", "outcomeSide")
    qty = pick(a, "quantity", "qty", "shares", "filledQuantity", "size")
    px = pick(a, "price", "avgPx", "fillPrice", "executionPrice")
    amt = pick(a, "amount", "cost", "notional", "payout", "realizedPnl", "netAmount")
    lines = []
    if slug:
        lines.append(f"**{str(slug).replace('cpc-', '')}**")
    if side:
        sv = str(side).upper()
        word = ("Up" if "LONG" in sv or sv in ("YES", "UP") else
                "Down" if "SHORT" in sv or sv in ("NO", "DOWN") else str(side).title())
        verb = "Sold" if "SELL" in sv else "Bought"
        lines.append(f"{verb} **{word}**")
    if qty is not None and px is not None:
        try:
            lines.append(f"{float(qty):g} shares @ {float(px) * 100:.0f}%")
        except (TypeError, ValueError):
            lines.append(f"{qty} @ {px}")
    if amt is not None:
        lines.append(f"Amount: {money(amt)}")
    e = {"title": f"\U0001F4D2 YOUR ACCOUNT · {kind}", "description": "\n".join(lines) or "new activity",
         "color": 0x6096FF}
    link = event_link(slug)
    if link:
        e["url"] = link
    return e


def balance_line(bal):
    cur = pick(bal, "currentBalance", "balance", "cashBalance", "totalBalance")
    bp = pick(bal, "buyingPower", "availableBalance", "available")
    parts = []
    if cur is not None:
        parts.append(f"Balance **{money(cur)}**")
    if bp is not None:
        parts.append(f"buying power {money(bp)}")
    return " · ".join(parts) or "balance: (no fields recognized)"


def load_seen():
    try:
        with open(SEEN, encoding="utf-8") as f:
            return set(x.strip() for x in f if x.strip())
    except FileNotFoundError:
        return None          # first run ever


def save_seen(seen):
    os.makedirs("data", exist_ok=True)
    with open(SEEN, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(seen)[-2000:]) + "\n")


def check(session, post):
    """Fetch balance + recent activity; post anything new to Discord via post(payload).
    First run: posts one 'connected' card and marks history as seen (no spam)."""
    if not enabled():
        return
    acts = first_list(get(session, "/v1/portfolio/activities", "limit=50"))
    seen = load_seen()
    new = [a for a in acts if fingerprint(a) not in (seen or set())]
    if seen is None:
        bal = get(session, "/v1/account/balances")
        post({"username": "polybot", "embeds": [{
            "title": "\U0001F4D2 Account connected (read-only watcher)",
            "description": f"{balance_line(bal)}\nWatching your trades and results from now on. "
                           f"{len(acts)} past activities skipped.",
            "color": 0x6096FF}]})
        save_seen({fingerprint(a) for a in acts})
        print("account watcher: connected")        # no account details in the public log
        return
    if not new:
        return
    bal = get(session, "/v1/account/balances")
    for a in reversed(new[:10]):                     # oldest first, cap 10 per check
        e = describe(a)
        e["footer"] = {"text": "read-only watcher"}
        post({"username": "polybot", "embeds": [e]})
    post({"username": "polybot", "content": f"\U0001F4D2 {balance_line(bal)}"})
    save_seen(seen | {fingerprint(a) for a in acts})
    print(f"account watcher: posted {len(new[:10])} new item(s)")
