"""polybot agent v1 - BTC 5-minute Up/Down PAPER scout for Polymarket.

LOG-ONLY. Never places orders, never touches a wallet, needs no keys.

Every 5-minute window it:
  1. records a proxy "price to beat" from Coinbase BTC-USD (the real one is a
     Chainlink 60s TWAP that Polymarket only publishes after the window closes),
  2. at 3:00, 2:00 and 1:00 left, reads the live Polymarket odds (CLOB order
     book, Gamma fallback) and BTC momentum/volatility,
  3. paper-bets three strategies and appends one row per checkpoint to
     data/checkpoints.csv.

grade.py later pulls the real outcome + real price to beat and scores it all.
"""
VERSION = "polybot agent v1"

import csv
import json
import math
import os
import time
from collections import deque
from datetime import datetime, timezone

import requests

WINDOW = 300                      # 5-minute markets
CHECKPOINTS = (180, 120, 60)      # seconds left when the agent decides
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
    "edge_side", "edge_price", "edge_ev", "version",
]


# ---------- pure helpers (unit-tested) ----------

def window_start(ts):
    return int(ts // WINDOW * WINDOW)


def slug_for(t_start):
    return f"btc-updown-5m-{t_start}"


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


def gamma_quotes(session, slug):
    r = session.get(GAMMA, params={"slug": slug}, headers=HEADERS, timeout=8)
    r.raise_for_status()
    m = r.json()[0]["markets"][0]
    ask, bid = m.get("bestAsk"), m.get("bestBid")
    q = {"quote_src": "gamma"}
    q["up_ask"] = float(ask) if ask is not None else None
    q["up_bid"] = float(bid) if bid is not None else None
    q["down_ask"] = round(1 - q["up_bid"], 4) if q["up_bid"] is not None else None
    q["down_bid"] = round(1 - q["up_ask"], 4) if q["up_ask"] is not None else None
    return q


def book_top(session, token):
    r = session.get(CLOB_BOOK, params={"token_id": token}, headers=HEADERS, timeout=6)
    r.raise_for_status()
    b = r.json()
    asks = [float(x["price"]) for x in b.get("asks", [])]
    bids = [float(x["price"]) for x in b.get("bids", [])]
    return (min(asks) if asks else None, max(bids) if bids else None)


def get_quotes(session, mkt):
    try:
        ua, ub = book_top(session, mkt["up_token"])
        da, db = book_top(session, mkt["down_token"])
        if ua is not None and da is not None:
            return {"quote_src": "clob", "up_ask": ua, "up_bid": ub, "down_ask": da, "down_bid": db}
    except Exception as e:
        print(f"  clob book failed ({e.__class__.__name__}), using gamma")
    return gamma_quotes(session, mkt["slug"])


# ---------- logging ----------

def append_row(row, path=DATA):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k) for k in FIELDS})


def fmt(x, nd=4):
    return None if x is None else round(x, nd)


def decide(session, buf, t0, secs_left, opens, markets, now):
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
        "version": VERSION,
    }
    append_row(row)
    print(f"  {row['slug']} {secs_left}s left | dist {row['dist']:+} | model Up {p_up:.0%} "
          f"| market Up ask {q.get('up_ask')} | mom={picks['mom'][0]} lean={picks['lean'][0]} edge={picks['edge'][0]}")
    return row


def main():
    print(f"{VERSION} | paper only | running {RUN_MINUTES:g} min | checkpoints {CHECKPOINTS}s left")
    session = requests.Session()
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
                    if decide(session, buf, t0, cp, opens, markets, now):
                        rows += 1
                except Exception as e:
                    print(f"  checkpoint error {t0} {cp}s: {e!r}")
        time.sleep(max(0.0, POLL_SEC - (time.time() - tick)))
    print(f"done | {rows} checkpoint rows logged to {DATA} | price samples {len(buf)}")


if __name__ == "__main__":
    main()
