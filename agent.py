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
VERSION = "polybot agent v4"

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
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")
STATS = os.path.join("data", "jj_stats.json")
ET = ZoneInfo("America/New_York")
RUN_MINUTES = float(os.getenv("RUN_MINUTES", "55"))
POLL_SEC = 2.0
FEE_RATE = 0.05                   # Polymarket BTC 5m taker fee: C * 0.05 * p * (1-p)
EDGE_MIN = 0.03                   # edge strategy needs >= 3c expected value after fees
BASIS_SD = float(os.getenv("BASIS_SD", "15"))  # $ noise between Coinbase and Chainlink; grade.py measures the real value
DATA = os.path.join("data", "checkpoints.csv")

COINBASE = "https://api.exchange.coinbase.com/products/BTC-USD/ticker"
GAMMA = "https://gamma-api.polymarket.com/events"
CLOB_BOOK = "https://clob.polymarket.com/book"
HEADERS = {"User-Agent": "polybot-paper/1 (research, log-only)"}

FIELDS = [
    "logged_utc", "slug", "t_start", "secs_left", "spot", "spot_open", "ptb_proxy",
    "dist", "mom60", "sigma", "model_up", "up_ask", "up_bid", "down_ask", "down_bid",
    "quote_src", "mom_side", "mom_price", "lean_side", "lean_price",
    "edge_side", "edge_price", "edge_ev", "jj_side", "jj_price", "jj_ev", "version",
]


# ---------- pure helpers (unit-tested) ----------

def window_start(ts):
    return int(ts // WINDOW * WINDOW)


def slug_for(t_start):
    return f"btc-updown-5m-{t_start}"


def market_url(slug):
    """Direct link to the exact 5m contract (verified format: polymarket.com/event/<slug>)."""
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


def load_stats():
    try:
        with open(STATS, encoding="utf-8") as f:
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
            "title": f"{'BUY UP' if side == 'Up' else 'BUY DOWN'} · BTC 5m · {left // 60}:{left % 60:02d} left",
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


def post_ticket(session, row):
    if not WEBHOOK:
        print("  (no DISCORD_WEBHOOK set - ticket not sent)")
        return
    try:
        r = session.post(WEBHOOK, json=ticket_payload(row, load_stats()), timeout=6)
        print(f"  ticket sent to Discord ({r.status_code})")
    except Exception as e:
        print(f"  ticket failed: {e!r}")


def fmt(x, nd=4):
    return None if x is None else round(x, nd)


def decide(session, buf, t0, secs_left, opens, markets, now, jj_done=None):
    if opens.get(t0) is None:
        print(f"  {t0} {secs_left}s: no open price (agent started mid-window) - skip")
        return None
    ptb, spot_open = opens[t0]
    spot = buf[-1][1]
    sigma = sigma_per_sec(buf, now)
    if sigma is None:
        print(f"  {t0} {secs_left}s: not enough price history for volatility - skip")
        return None
    then = price_near(buf, now - 60)
    mom60 = spot - then if then else None
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
    row = {
        "logged_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "slug": slug_for(t0), "t_start": t0, "secs_left": secs_left,
        "spot": spot, "spot_open": spot_open, "ptb_proxy": fmt(ptb, 2),
        "dist": fmt(spot - ptb, 2), "mom60": fmt(mom60, 2), "sigma": f"{sigma:.3e}",
        "model_up": fmt(p_up), "quote_src": q["quote_src"],
        "up_ask": q.get("up_ask"), "up_bid": q.get("up_bid"),
        "down_ask": q.get("down_ask"), "down_bid": q.get("down_bid"),
        "mom_side": picks["mom"][0], "mom_price": picks["mom"][1],
        "lean_side": picks["lean"][0], "lean_price": picks["lean"][1],
        "edge_side": picks["edge"][0], "edge_price": picks["edge"][1], "edge_ev": picks["edge"][2],
        "jj_side": picks["jj"][0], "jj_price": picks["jj"][1], "jj_ev": picks["jj"][2],
        "version": VERSION,
    }
    append_row(row)
    if row["jj_side"]:
        jj_done.add(t0)
        post_ticket(session, row)
    print(f"  {row['slug']} {secs_left}s left | dist {row['dist']:+} | model Up {p_up:.0%} "
          f"| market Up ask {q.get('up_ask')} | mom={picks['mom'][0]} lean={picks['lean'][0]} edge={picks['edge'][0]} jj={picks['jj'][0]}")
    return row


def main():
    print(f"{VERSION} | paper only | running {RUN_MINUTES:g} min | checkpoints {CHECKPOINTS}s left")
    upgrade_header()
    session = requests.Session()
    jj_done = set()
    buf = deque(maxlen=900)         # ~30 min of 2s samples
    opens, markets, done = {}, {}, set()
    first_window = window_start(time.time())
    stop_at = time.time() + RUN_MINUTES * 60
    rows = 0
    while time.time() < stop_at:
        tick = time.time()
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
           "secs_left": 240, "t_start": window_start(time.time()), "slug": "TEST-ticket-not-a-real-bet",
           "dist": 18.0, "mom60": 7.0}
    p = ticket_payload(row, load_stats())
    p["content"] = "TEST TICKET - delivery check only, not a signal."
    if not WEBHOOK:
        sys.exit("DISCORD_WEBHOOK secret is missing")
    r = requests.post(WEBHOOK, json=p, timeout=8)
    print(f"test ticket -> Discord HTTP {r.status_code} (204 = delivered)")
    if r.status_code >= 300:
        sys.exit(r.text[:300])


if __name__ == "__main__":
    import sys
    test_ticket() if "--test-ticket" in sys.argv else main()
