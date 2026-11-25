"""polybot agent v1 - BTC 5-minute Up/Down PAPER scout for Polymarket.

LOG-ONLY. Never places orders, never touches a wallet, needs no keys.

Every 5-minute window it:
  1. records a proxy "price to beat" from Coinbase BTC-USD (the real one is a
     Chainlink 60s TWAP that Polymarket only publishes after the window closes),
  2. at 3:00, 2:00 and 1:00 left, reads the live Polymarket odds (CLOB order
     book only) and BTC momentum/volatility,
  3. paper-bets three strategies and appends one row per checkpoint to
     data/checkpoints.csv.

grade.py later pulls the real outcome + real price to beat and scores it all.
"""
VERSION = "polybot agent v8"

import csv
import json
import math
import os
import time
from collections import deque
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests

WINDOW = 300                      # 5-minute markets
CHECKPOINTS = (240, 210, 180, 120, 60)  # seconds left when the agent decides
JJ_CHECKPOINTS = (240, 210)        # JJ strategy only enters 60-90s into the window
JJ_PRICE = (0.35, 0.70)            # ...and only at the prices the top directional traders pay
JJ_EDGE = 0.04                     # ...and only with 4c+ expected value after the fee
SAFE_CHECKPOINTS = (180, 120)      # SAFE: mid-window, never the last minute
SAFE_PROB = 0.75                   # ...only when our model gives the side 75%+
SAFE_PRICE = (0.55, 0.85)          # ...never pays more than 85c (one loss must not erase many wins)
SAFE_EDGE = 0.04                   # ...and still needs 4c+ edge after the fee
TICKET_EDGE = 0.06                 # a ticket only goes out with 6%+ edge (paper bets still log at 4%)
TICKET_BUFFER = 0.02               # card says "still good up to" the price that leaves 2% edge
TICKETS = os.path.join("data", "tickets.csv")
TICKET_FIELDS = ["t_start", "slug", "tier", "side", "price", "ev", "sent_utc", "result", "pnl10", "settled_utc"]
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")
STATS = os.path.join("data", "jj_stats.json")
ET = ZoneInfo("America/New_York")
RUN_MINUTES = float(os.getenv("RUN_MINUTES", "55"))
POLL_SEC = 2.0
VENUE = os.getenv("VENUE", "us")  # "us" = Polymarket US app (what Jacob trades); "intl" = polymarket.com
# fee per share = FEE_RATE * p * (1-p). intl BTC 5m = 0.05 (docs). US = the market's feeCoefficient (0.095 seen live).
FEE_RATE = 0.095 if VENUE == "us" else 0.05
EDGE_MIN = 0.03                   # edge strategy needs >= 3c expected value after fees
BASIS_SD = float(os.getenv("BASIS_SD", "15"))  # $ noise between Coinbase and Chainlink; grade.py measures the real value
DATA = os.path.join("data", "checkpoints.csv")

COINBASE = "https://api.exchange.coinbase.com/products/BTC-USD/ticker"
GAMMA = "https://gamma-api.polymarket.com/events"
CLOB_BOOK = "https://clob.polymarket.com/book"
US_GATEWAY = "https://gateway.polymarket.us/v1"   # public, no key: events/slug/<slug>, markets/<slug>/bbo
HEADERS = {"User-Agent": "polybot-paper/1 (research, log-only)"}

FIELDS = [
    "logged_utc", "slug", "t_start", "secs_left", "spot", "spot_open", "ptb_proxy",
    "dist", "mom60", "sigma", "model_up", "up_ask", "up_bid", "down_ask", "down_bid",
    "quote_src", "mom_side", "mom_price", "lean_side", "lean_price",
    "edge_side", "edge_price", "edge_ev", "jj_side", "jj_price", "jj_ev", "safe_side", "safe_price", "safe_ev", "pair_sum", "venue", "fee_rate", "version",
]


# ---------- pure helpers (unit-tested) ----------

def window_start(ts):
    return int(ts // WINDOW * WINDOW)


def slug_for(t_start):
    return f"btc-updown-5m-{t_start}"


def us_slug_for(t_start):
    """Polymarket US slug, e.g. btc-updown-5m-2026-11-25-1040z (window start, UTC)."""
    return "btc-updown-5m-" + datetime.fromtimestamp(t_start, timezone.utc).strftime("%Y-%m-%d-%H%Mz")


def market_url(slug):
    """Direct link to the exact contract. US slugs open polymarket.us (the US app);
    numeric slugs open polymarket.com. Both formats verified live."""
    if slug.endswith("z") and slug.count("-") >= 5:
        return f"https://polymarket.us/event/{slug}"
    return f"https://polymarket.com/event/{slug}"


def fee_per_share(p):
    return FEE_RATE * p * (1 - p)


def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def avg_between(buf, t0, t1, min_samples=10):
    vals = [p for ts, p in buf if t0 <= ts < t1]
    return sum(vals) / len(vals) if len(vals) >= min_samples else None


def price_near(buf, target, tol=6):
    best = None
    for ts, p in buf:
        if abs(ts - target) <= tol and (best is None or abs(ts - target) < abs(best[0] - target)):
            best = (ts, p)
    return best[1] if best else None


def sigma_per_sec(buf, now, lookback=600, min_samples=60):
    pts = [(ts, p) for ts, p in buf if now - lookback <= ts <= now]
    if len(pts) < min_samples:
        return None
    sq, dt = 0.0, 0.0
    for (t0, p0), (t1, p1) in zip(pts, pts[1:]):
        if t1 > t0 and p0 > 0 and p1 > 0:
            sq += math.log(p1 / p0) ** 2
            dt += t1 - t0
    return math.sqrt(sq / dt) if dt > 0 else None


def model_p_up(spot, ptb, sigma, secs_left, basis_sd=BASIS_SD):
    """P(final 60s TWAP >= price to beat) under a driftless random walk.
    The last 60s are averaged, so the effective remaining time is secs_left - 40."""
    t_eff = max(secs_left - 40.0, 1.0)
    sd = math.sqrt((spot * sigma) ** 2 * t_eff + basis_sd ** 2)
    return norm_cdf((spot - ptb) / sd) if sd > 0 else (1.0 if spot >= ptb else 0.0)


def pick_strategies(spot, ptb, mom60, p_up, q):
    """Return {strategy: (side, price, ev)} for one checkpoint. side None = no bet."""
    out = {}
    side = "Up" if mom60 and mom60 > 0 else ("Down" if mom60 and mom60 < 0 else None)
    out["mom"] = (side, q.get(f"{side.lower()}_ask") if side else None, None)
    side = "Up" if spot >= ptb else "Down"
    out["lean"] = (side, q.get(f"{side.lower()}_ask"), None)
    best = (None, None, None)
    for side, p in (("Up", p_up), ("Down", 1 - p_up)):
        ask = q.get(f"{side.lower()}_ask")
        if ask and 0 < ask < 1:
            ev = p - ask - fee_per_share(ask)
            if ev >= EDGE_MIN and (best[2] is None or ev > best[2]):
                best = (side, ask, round(ev, 4))
    out["edge"] = best
    return out


def pick_safe(p_up, q, secs_left):
    """SAFE = high win-rate tier. Only the side our model makes a 75%+ favorite,
    priced 55-85c, with 4c+ edge after the fee, at 3:00 or 2:00 left.
    Wins most of the time by design; the 85c cap keeps a loss from wiping out
    more than ~5 wins. Graded separately from JJ."""
    if secs_left not in SAFE_CHECKPOINTS:
        return (None, None, None)
    for side, p in (("Up", p_up), ("Down", 1 - p_up)):
        ask = q.get(f"{side.lower()}_ask")
        if p >= SAFE_PROB and ask and SAFE_PRICE[0] <= ask <= SAFE_PRICE[1]:
            ev = p - ask - fee_per_share(ask)
            if ev >= SAFE_EDGE:
                return (side, ask, round(ev, 4))
    return (None, None, None)


def pick_jj(p_up, q, secs_left):
    """JJ strategy, built from the top-10 BTC 5m traders' own fills (Nov 2026):
    the directional winners enter 60-120s into the window at 35-70c and never
    chase 85c+ favorites. JJ = that timing and price band, plus our model must
    beat the live ask by JJ_EDGE after the fee. One bet per window max."""
    if secs_left not in JJ_CHECKPOINTS:
        return (None, None, None)
    best = (None, None, None)
    for side, p in (("Up", p_up), ("Down", 1 - p_up)):
        ask = q.get(f"{side.lower()}_ask")
        if ask and JJ_PRICE[0] <= ask <= JJ_PRICE[1]:
            ev = p - ask - fee_per_share(ask)
            if ev >= JJ_EDGE and (best[2] is None or ev > best[2]):
                best = (side, ask, round(ev, 4))
    return best


# ---------- network ----------

def get_spot(session):
    try:
        r = session.get(COINBASE, headers=HEADERS, timeout=5)
        r.raise_for_status()
        return float(r.json()["price"])
    except Exception:
        return None


def get_market(session, slug):
    r = session.get(GAMMA, params={"slug": slug}, headers=HEADERS, timeout=8)
    r.raise_for_status()
    events = r.json()
    if not events:
        return None
    m = events[0]["markets"][0]
    outcomes = json.loads(m["outcomes"])
    tokens = json.loads(m["clobTokenIds"])
    ids = dict(zip(outcomes, tokens))
    return {"up_token": ids.get("Up"), "down_token": ids.get("Down"), "slug": slug}


def get_us_market(session, t0):
    """US event for this window: market slug + the REAL price to beat (BRTI, set at window start)."""
    slug = us_slug_for(t0)
    r = session.get(f"{US_GATEWAY}/events/slug/{slug}", headers=HEADERS, timeout=8)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    m = r.json()["event"]["markets"][0]
    terms = m.get("assetPriceTerms") or {}
    ptb = (terms.get("priceToBeat") or {}).get("value")
    return {"slug": slug, "mkt": m["slug"], "ptb": float(ptb) if ptb else None,
            "fee": float(m.get("feeCoefficient") or FEE_RATE)}


def get_us_quotes(session, mkt_slug):
    """US top of book. longQuote = price to buy Up, shortQuote = price to buy Down."""
    try:
        r = session.get(f"{US_GATEWAY}/markets/{mkt_slug}/bbo", headers=HEADERS, timeout=6)
        r.raise_for_status()
        d = r.json()["marketData"]
        val = lambda k: float(d[k]["value"]) if d.get(k) else None
        ua, da, ub, ba = val("longQuote"), val("shortQuote"), val("bestBid"), val("bestAsk")
        ok = lambda p: p if p is not None and 0 < p < 1 else None
        return {"quote_src": "us_bbo", "up_ask": ok(ua), "down_ask": ok(da),
                "up_bid": ok(ub), "down_bid": ok(round(1 - ba, 4)) if ba else None}
    except Exception as e:
        print(f"  us bbo failed ({e.__class__.__name__}) - no quotes this checkpoint")
        return {"quote_src": "error", "up_ask": None, "up_bid": None, "down_ask": None, "down_bid": None}


def book_top(session, token):
    r = session.get(CLOB_BOOK, params={"token_id": token}, headers=HEADERS, timeout=6)
    r.raise_for_status()
    b = r.json()
    asks = [float(x["price"]) for x in b.get("asks", [])]
    bids = [float(x["price"]) for x in b.get("bids", [])]
    return (min(asks) if asks else None, max(bids) if bids else None)


def get_quotes(session, mkt):
    """Live order book only. Gamma's cached bestAsk was seen 50c off the real book
    near the close, so it is never used for a bet. A side with no asks stays None
    (nothing to buy there), and every strategy skips it."""
    try:
        ua, ub = book_top(session, mkt["up_token"])
        da, db = book_top(session, mkt["down_token"])
        return {"quote_src": "clob", "up_ask": ua, "up_bid": ub, "down_ask": da, "down_bid": db}
    except Exception as e:
        print(f"  clob book failed ({e.__class__.__name__}) - no quotes this checkpoint")
        return {"quote_src": "error", "up_ask": None, "up_bid": None, "down_ask": None, "down_bid": None}


# ---------- logging ----------

def upgrade_header(path=DATA):
    """If the CSV was written by an older version with fewer columns, rewrite it
    under the current header (old rows keep their values, new columns blank)."""
    if not os.path.exists(path):
        return
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        f.seek(0)
        header = next(csv.reader(f), [])
    if header == FIELDS:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in FIELDS})
    print(f"upgraded {path} header ({len(rows)} rows kept)")


def append_row(row, path=DATA):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k) for k in FIELDS})


def load_stats(kind="jj"):
    path = STATS if kind == "jj" else os.path.join("data", f"{kind}_stats.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def ticket_payload(row, stats):
    side, price, ev = row["jj_side"], row["jj_price"], row["jj_ev"]
    fair = row["model_up"] if side == "Up" else round(1 - row["model_up"], 4)
    left = row["secs_left"]
    t0 = datetime.fromtimestamp(row["t_start"], ET)
    t1 = datetime.fromtimestamp(row["t_start"] + WINDOW, ET)
    label = f"{t0.strftime('%I:%M').lstrip('0')}-{t1.strftime('%I:%M %p').lstrip('0')}"
    n, hit, be = stats.get("n", 0), stats.get("hit"), stats.get("breakeven")
    record = (f"JJ paper record: {n} bets, hit {hit:.0%} vs breakeven {be:.0%}, "
              f"P&L {stats.get('pnl', 0):+.2f}/share ({stats.get('verdict', '')})"
              if n and hit is not None and be is not None else "JJ paper record: no settled bets yet")
    return {
        "username": "polybot",
        "embeds": [{
            "title": f"[{row.get('tier', 'JJ')}] {'BUY UP' if side == 'Up' else 'BUY DOWN'} · BTC 5m · {left // 60}:{left % 60:02d} left",
            "url": market_url(row["slug"]),
            "description": f"Window {label} ET · [**Open this contract**]({market_url(row['slug'])})",
            "color": 0x2ECC71 if side == "Up" else 0xE74C3C,
            "fields": [
                {"name": "Ask", "value": f"{price * 100:.0f}c", "inline": True},
                {"name": "Our fair value", "value": f"{fair * 100:.0f}c", "inline": True},
                {"name": "Edge after fee", "value": f"{ev * 100:+.1f}c", "inline": True},
                {"name": "BTC vs price to beat", "value": f"${row['dist']:+,.0f}", "inline": True},
                {"name": "Last 60s", "value": f"${(row['mom60'] or 0):+,.0f}", "inline": True},
                {"name": "Window closes", "value": f"in {left}s", "inline": True},
                {"name": "Contract", "value": f"[{row['slug']}]({market_url(row['slug'])})", "inline": False},
            ],
            "footer": {"text": f"PAPER · UNVALIDATED · not advice · {record}"},
        }],
    }


def record_text(stats, kind="JJ"):
    """Paper record in plain English, e.g. 'JJ so far: won 9 of 14 (needs 52% to profit) - up $1.85 per share'."""
    n, hit, be = stats.get("n", 0), stats.get("hit"), stats.get("breakeven")
    if n and hit is not None and be is not None:
        pnl = stats.get("pnl", 0)
        return (f"{kind} so far: won {round(hit * n)} of {n} (needs {be:.0%} to make money) \u00b7 "
                f"{'up' if pnl >= 0 else 'down'} ${abs(pnl):.2f} per share")
    return f"{kind} so far: no finished bets yet"


def card_png(row, prices, stats):
    """Visual ticket (ticket_card.py). Returns PNG bytes, or None if Pillow is missing."""
    try:
        import ticket_card
    except Exception as e:
        print(f"  card renderer unavailable: {e!r}")
        return None
    side = row["jj_side"]
    t0 = datetime.fromtimestamp(row["t_start"], ET)
    t1 = datetime.fromtimestamp(row["t_start"] + WINDOW, ET)
    return ticket_card.render({
        "side": side, "price": row["jj_price"], "ev": row["jj_ev"],
        "fair": row["model_up"] if side == "Up" else round(1 - row["model_up"], 4),
        "secs_left": row["secs_left"],
        "window_label": f"{t0.strftime('%b %d').replace(' 0', ' ')} \u00b7 "
                        f"{t0.strftime('%I:%M').lstrip('0')}\u2013{t1.strftime('%I:%M %p').lstrip('0')} ET",
        "dist": row["dist"], "ptb": row["ptb_proxy"], "spot": row["spot"],
        "prices": prices, "fee_rate": row.get("fee_rate") or FEE_RATE,
        "record": record_text(stats, row.get("tier", "JJ")), "tier": row.get("tier", "JJ"),
        "max_price": round(min(row["jj_price"] + row["jj_ev"] - TICKET_BUFFER, 0.97), 2),
    })


def post_ticket(session, row, prices=None):
    if not WEBHOOK:
        print("  (no DISCORD_WEBHOOK set - ticket not sent)")
        return
    stats = load_stats(row.get("tier", "JJ").lower())
    payload = ticket_payload(row, stats)
    try:
        png = card_png(row, prices or [], stats)
        if png:
            e = payload["embeds"][0]
            e["image"] = {"url": "attachment://ticket.png"}
            e.pop("fields", None)            # the card shows the numbers
            r = session.post(WEBHOOK, data={"payload_json": json.dumps(payload)},
                             files={"files[0]": ("ticket.png", png, "image/png")}, timeout=10)
        else:
            r = session.post(WEBHOOK, json=payload, timeout=6)
        print(f"  ticket sent to Discord ({r.status_code})")
    except Exception as e:
        print(f"  ticket failed: {e!r}")


def log_ticket(row):
    os.makedirs("data", exist_ok=True)
    new = not os.path.exists(TICKETS)
    with open(TICKETS, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TICKET_FIELDS)
        if new:
            w.writeheader()
        w.writerow({"t_start": row["t_start"], "slug": row["slug"], "tier": row["tier"],
                    "side": row["jj_side"], "price": row["jj_price"], "ev": row["jj_ev"],
                    "sent_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})


def pnl_10(price, won, fee_rate=None):
    """Result of a $10 bet at this price, after the fee."""
    fr = FEE_RATE if fee_rate is None else fee_rate
    shares = 10 / price
    fee = fr * price * (1 - price) * shares
    return round(shares * (1 - price) - fee, 2) if won else round(-(10 + fee), 2)


def get_us_winner(session, slug):
    """'Up' / 'Down' once the US round has settled, else None."""
    r = session.get(f"{US_GATEWAY}/events/slug/{slug}", headers=HEADERS, timeout=8)
    r.raise_for_status()
    m = r.json()["event"]["markets"][0]
    if not m.get("closed"):
        return None
    b = session.get(f"{US_GATEWAY}/markets/{m['slug']}/bbo", headers=HEADERS, timeout=8).json()["marketData"]
    px = (b.get("settlementPx") or {}).get("value")
    if px is None:
        return None
    return "Up" if float(px) == 1.0 else ("Down" if float(px) == 0.0 else None)


def today_tally(rows):
    today = datetime.now(ET).date()
    done = [r for r in rows if r.get("result") and
            datetime.fromtimestamp(int(r["t_start"]), ET).date() == today]
    wins = sum(r["result"] == "WIN" for r in done)
    return wins, len(done) - wins, round(sum(float(r["pnl10"] or 0) for r in done), 2)


def check_results(session):
    """Post WIN/LOSS for every ticket whose round has settled (also ones left by an earlier run)."""
    if not os.path.exists(TICKETS):
        return
    with open(TICKETS, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    changed = False
    for r in rows:
        if r.get("result") or time.time() < int(r["t_start"]) + WINDOW + 45:
            continue
        try:
            winner = get_us_winner(session, r["slug"]) if VENUE == "us" else None
        except Exception as e:
            print(f"  result check failed {r['slug']}: {e!r}")
            continue
        if not winner:
            continue
        won = winner == r["side"]
        r["result"] = "WIN" if won else "LOSS"
        r["pnl10"] = pnl_10(float(r["price"]), won)
        r["settled_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        changed = True
        post_result(session, r, today_tally(rows))
    if changed:
        with open(TICKETS, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=TICKET_FIELDS)
            w.writeheader()
            w.writerows(rows)


def post_result(session, r, tally):
    won = r["result"] == "WIN"
    t0 = datetime.fromtimestamp(int(r["t_start"]), ET)
    t1 = datetime.fromtimestamp(int(r["t_start"]) + WINDOW, ET)
    when = f"{t0.strftime('%I:%M').lstrip('0')}\u2013{t1.strftime('%I:%M %p').lstrip('0')}"
    w, l, total = tally
    msg = {"username": "polybot", "embeds": [{
        "title": f"{'\u2705 WON' if won else '\u274c LOST'} \u00b7 {r['tier']} \u00b7 {r['side'].upper()} \u00b7 {when} ET",
        "description": (f"$10 at {float(r['price']) * 100:.0f}% \u2192 **{'+' if won else '-'}${abs(float(r['pnl10'])):.2f}**\n"
                        f"Today: **{w} won \u00b7 {l} lost \u00b7 {'+' if total >= 0 else '-'}${abs(total):.2f}** (paper, $10 per ticket)"),
        "color": 0x22C55E if won else 0xEF4444,
        "url": market_url(r["slug"]),
    }]}
    if not WEBHOOK:
        print(f"  result {r['slug']} {r['result']} (no webhook)")
        return
    try:
        resp = session.post(WEBHOOK, json=msg, timeout=6)
        print(f"  result posted {r['slug']} {r['result']} ({resp.status_code})")
    except Exception as e:
        print(f"  result post failed: {e!r}")


def fmt(x, nd=4):
    return None if x is None else round(x, nd)


def decide(session, buf, t0, secs_left, opens, markets, now, jj_done=None):
    if opens.get(t0) is None:
        print(f"  {t0} {secs_left}s: no open price (agent started mid-window) - skip")
        return None
    ptb, spot_open = opens[t0]
    spot = buf[-1][1]
    us = None
    if VENUE == "us":
        us = get_us_market(session, t0)
        if not us:
            print(f"  {us_slug_for(t0)} not found on Polymarket US - skip")
            return None
        if us["ptb"]:
            ptb = us["ptb"]          # real BRTI price to beat beats our Coinbase proxy
    sigma = sigma_per_sec(buf, now)
    if sigma is None:
        print(f"  {t0} {secs_left}s: not enough price history for volatility - skip")
        return None
    then = price_near(buf, now - 60)
    mom60 = spot - then if then else None
    if us:
        q = get_us_quotes(session, us["mkt"])
    else:
        if t0 not in markets:
            markets[t0] = get_market(session, slug_for(t0))
        mkt = markets[t0]
        if not mkt:
            print(f"  {slug_for(t0)} not found on Gamma - skip")
            return None
        q = get_quotes(session, mkt)
    p_up = model_p_up(spot, ptb, sigma, secs_left)
    picks = pick_strategies(spot, ptb, mom60, p_up, q)
    jj_done = jj_done if jj_done is not None else set()
    picks["jj"] = pick_jj(p_up, q, secs_left) if t0 not in jj_done else (None, None, None)
    picks["safe"] = pick_safe(p_up, q, secs_left) if ("safe", t0) not in jj_done else (None, None, None)
    row = {
        "logged_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "slug": us["slug"] if us else slug_for(t0), "t_start": t0, "secs_left": secs_left,
        "venue": VENUE, "fee_rate": FEE_RATE,
        "spot": spot, "spot_open": spot_open, "ptb_proxy": fmt(ptb, 2),
        "dist": fmt(spot - ptb, 2), "mom60": fmt(mom60, 2), "sigma": f"{sigma:.3e}",
        "model_up": fmt(p_up), "quote_src": q["quote_src"],
        "up_ask": q.get("up_ask"), "up_bid": q.get("up_bid"),
        "down_ask": q.get("down_ask"), "down_bid": q.get("down_bid"),
        "mom_side": picks["mom"][0], "mom_price": picks["mom"][1],
        "lean_side": picks["lean"][0], "lean_price": picks["lean"][1],
        "edge_side": picks["edge"][0], "edge_price": picks["edge"][1], "edge_ev": picks["edge"][2],
        "jj_side": picks["jj"][0], "jj_price": picks["jj"][1], "jj_ev": picks["jj"][2],
        "safe_side": picks["safe"][0], "safe_price": picks["safe"][1], "safe_ev": picks["safe"][2],
        "pair_sum": round(q["up_ask"] + q["down_ask"], 4) if q.get("up_ask") and q.get("down_ask") else None,
        "version": VERSION,
    }
    append_row(row)
    recent = [(ts, p) for ts, p in buf if ts >= now - 180]
    if row["jj_side"]:
        jj_done.add(t0)
    if row["safe_side"]:
        jj_done.add(("safe", t0))
    # ONE ticket per round, only the strongest, and only with a TICKET_EDGE cushion
    cands = []
    if row["jj_side"] and row["jj_ev"] >= TICKET_EDGE:
        cands.append(dict(row, tier="JJ"))
    if row["safe_side"] and row["safe_ev"] >= TICKET_EDGE:
        cands.append(dict(row, tier="SAFE", jj_side=row["safe_side"],
                          jj_price=row["safe_price"], jj_ev=row["safe_ev"]))
    if cands and ("ticket", t0) not in jj_done:
        best = max(cands, key=lambda r: r["jj_ev"])
        jj_done.add(("ticket", t0))
        post_ticket(session, best, recent)
        log_ticket(best)
    elif row["jj_side"] or row["safe_side"]:
        print("  signal below ticket bar or round already ticketed - logged, not sent")
    print(f"  {row['slug']} {secs_left}s left | dist {row['dist']:+} | model Up {p_up:.0%} "
          f"| market Up ask {q.get('up_ask')} | mom={picks['mom'][0]} lean={picks['lean'][0]} edge={picks['edge'][0]} jj={picks['jj'][0]} safe={picks['safe'][0]}")
    return row


def main():
    print(f"{VERSION} | venue {VENUE} | fee {FEE_RATE} | paper only | running {RUN_MINUTES:g} min | checkpoints {CHECKPOINTS}s left")
    upgrade_header()
    session = requests.Session()
    jj_done = set()
    buf = deque(maxlen=900)         # ~30 min of 2s samples
    opens, markets, done = {}, {}, set()
    first_window = window_start(time.time())
    stop_at = time.time() + RUN_MINUTES * 60
    rows = 0
    last_check = 0.0
    while time.time() < stop_at:
        tick = time.time()
        if tick - last_check > 20:
            last_check = tick
            try:
                check_results(session)
            except Exception as e:
                print(f"  results error: {e!r}")
        p = get_spot(session)
        now = time.time()
        if p:
            buf.append((now, p))
        t0 = window_start(now)
        left = t0 + WINDOW - now
        if t0 not in opens and now - t0 >= 1:
            # a window that started before we booted has no trustworthy open
            if t0 == first_window:
                opens[t0] = None
            else:
                opens[t0] = (avg_between(buf, t0 - 60, t0), price_near(buf, t0))
                if opens[t0][0] is None:
                    opens[t0] = None
                print(f"window {slug_for(t0)} open | ptb proxy {opens[t0] and round(opens[t0][0], 2)}")
        for cp in CHECKPOINTS:
            if (t0, cp) not in done and cp - 15 < left <= cp and buf:
                done.add((t0, cp))
                try:
                    if decide(session, buf, t0, cp, opens, markets, now, jj_done):
                        rows += 1
                except Exception as e:
                    print(f"  checkpoint error {t0} {cp}s: {e!r}")
        time.sleep(max(0.0, POLL_SEC - (time.time() - tick)))
    print(f"done | {rows} checkpoint rows logged to {DATA} | price samples {len(buf)}")


def test_ticket():
    """Send one sample ticket so you can check Discord delivery. Marked TEST."""
    import sys
    row = {"jj_side": "Up", "jj_price": 0.52, "jj_ev": 0.061, "model_up": 0.594,
           "secs_left": 240, "t_start": window_start(time.time()),
           "slug": us_slug_for(window_start(time.time())) if VENUE == "us" else slug_for(window_start(time.time())),
           "dist": 18.0, "mom60": 7.0}
    row.update(ptb_proxy=58928.09, spot=58946.09, fee_rate=FEE_RATE)
    prices = [(i * 2, 58928.09 + 18 * i / 89 + 6 * math.sin(i / 7)) for i in range(90)]
    p = ticket_payload(row, load_stats())
    p["content"] = "TEST TICKET - delivery check only, not a signal."
    if not WEBHOOK:
        sys.exit("DISCORD_WEBHOOK secret is missing")
    png = card_png(row, prices, load_stats())
    if png:
        p["embeds"][0]["image"] = {"url": "attachment://ticket.png"}
        p["embeds"][0].pop("fields", None)
        r = requests.post(WEBHOOK, data={"payload_json": json.dumps(p)},
                          files={"files[0]": ("ticket.png", png, "image/png")}, timeout=10)
    else:
        r = requests.post(WEBHOOK, json=p, timeout=8)
    print(f"test ticket -> Discord HTTP {r.status_code} (204 = delivered)")
    if r.status_code >= 300:
        sys.exit(r.text[:300])


if __name__ == "__main__":
    import sys
    test_ticket() if "--test-ticket" in sys.argv else main()
