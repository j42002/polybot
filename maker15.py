"""Paper-only MAKER (limit-order) test on Kalshi BTC 15-minute Up/Down markets. Never places orders, needs no keys.

Separate experiment: it does not touch agent.py/grade.py (5m v18) or backtest15.py (15m Phase 1).
Rules are frozen in data/maker15/PREREG.md. This file only implements them.

Modes:
  python maker15.py live       watch open windows for RUN_MINUTES; at 12:00 elapsed log one simulated limit order
  python maker15.py grade      grade pending orders (trade-through fills + settlement), rewrite report.md
  python maker15.py replay N   exploratory preview: same rules on the last N settled markets. Never counts.
  python maker15.py selftest   offline checks of the fill / fee / grading logic on made-up trades

Outputs (data/maker15/): orders.csv (live, judged), replay.csv (exploratory), report.md
"""
import csv
import math
import os
import sys
import time
from datetime import datetime, timezone

import requests

KALSHI = "https://external-api.kalshi.com/trade-api/v2"
COINBASE = "https://api.exchange.coinbase.com/products/BTC-USD/candles"
SERIES = "KXBTC15M"
OUT = os.path.join("data", "maker15")
ORDERS = os.path.join(OUT, "orders.csv")
REPLAY = os.path.join(OUT, "replay.csv")
REPORT = os.path.join(OUT, "report.md")
HDR = {"User-Agent": "polybot-research/1.0 (paper only)"}

DECISION_S = 720          # post the order at 12:00 elapsed (3:00 left)
POST_GRACE_S = 60         # live: only post if we are within 60s of the decision time
WINDOW_S = 900
STAKE = 10.0              # $ per order
IMPROVE = 0.02            # limit = ask - 2c
MAKER_RATE = 0.0175       # Kalshi maker coefficient, charged only on series with maker fees
JUDGE_N = 100             # verdict on the first 100 live fills
MARGIN = 0.03             # win rate must beat break-even by 3 points

FIELDS = ["ticker", "open_ts", "close_ts", "order_ts", "target", "btc_T", "btc_T60", "lean", "mom", "side",
          "ask", "bid", "limit", "contracts", "status", "through_vol", "first_through_ts", "result", "won",
          "fee", "fee_stress", "pnl", "pnl_stress", "breakeven", "fee_type", "fee_mult", "graded_utc"]
# status: NO_DATA | NO_SIGNAL | NO_QUOTE | PENDING | FILLED | PARTIAL | UNFILLED | NO_RESULT

session = requests.Session()
session.headers.update(HDR)


# ---------------- helpers ----------------

def get(url, params=None, tries=5):
    for i in range(tries):
        try:
            r = session.get(url, params=params, timeout=20)
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(1.5 * (i + 1))
                continue
            return r
        except requests.RequestException:
            time.sleep(1.5 * (i + 1))
    return None


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def ts(iso):
    return int(datetime.fromisoformat(str(iso).replace("Z", "+00:00")).timestamp())


def utc(t=None):
    return datetime.fromtimestamp(t if t is not None else time.time(), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(path, rows):
    os.makedirs(OUT, exist_ok=True)
    rows = sorted(rows, key=lambda r: int(r["open_ts"]))
    with open(path + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    os.replace(path + ".tmp", path)


# ---------------- pure rule functions (tested offline) ----------------

def decide(target, b0, b1):
    """Phase 1 AGREE signal, copied (not imported) so later edits to backtest15.py can't change this test.
    b0 = BTC close of the 1m candle [T-60,T), b1 = close of [T-120,T-60). Returns side or None."""
    if target is None or b0 is None or b1 is None:
        return None, None, None
    lean = "Up" if b0 >= target else "Down"
    mom = "Up" if b0 > b1 else ("Down" if b0 < b1 else None)
    return lean, mom, (lean if lean == mom else None)


def limit_price(ask):
    """Resting buy limit 2c below the current ask on the chosen side. None if there is no usable quote."""
    if ask is None or not 0.01 < ask < 0.99:
        return None
    lim = round(ask - IMPROVE, 2)
    return lim if lim >= 0.02 else None


def contracts_for(lim):
    return math.floor(STAKE / lim + 1e-9)


def side_price(trade, side):
    """Price of the side we are buying, in dollars, for one Kalshi trade print."""
    y = num(trade.get("yes_price_dollars"))
    if y is None and trade.get("yes_price") is not None:      # older integer-cents schema
        y = num(trade.get("yes_price")) / 100.0
    if y is None:
        return None
    if side == "Up":
        return y
    n = num(trade.get("no_price_dollars"))
    return n if n is not None else round(1 - y, 4)


def trade_count(trade):
    c = num(trade.get("count_fp"))
    return c if c is not None else num(trade.get("count")) or 0.0


def check_fill(trades, side, lim, contracts, order_ts, close_ts):
    """A fill counts only if on-book prints traded STRICTLY through our limit (touching is not enough)
    after we posted and before the close, and that through-volume covers our whole size.
    Returns (status, through_volume, first_through_ts)."""
    vol, first = 0.0, None
    for t in trades:
        if t.get("is_block_trade"):
            continue                                            # off-book, can't hit a resting order
        tt = ts(t["created_time"])
        if not order_ts < tt < close_ts:
            continue
        p = side_price(t, side)
        if p is None or not p < lim - 1e-9:
            continue
        vol += trade_count(t)
        first = tt if first is None else min(first, tt)
    if vol >= contracts:
        return "FILLED", vol, first
    return ("PARTIAL" if vol > 0 else "UNFILLED"), vol, first


def maker_fee(contracts, price, rate, mult):
    """Kalshi formula: round up to the next cent of M x rate x C x P x (1-P)."""
    if rate <= 0:
        return 0.0
    return math.ceil(round(100 * mult * rate * contracts * price * (1 - price), 6)) / 100.0


def settle(lim, contracts, won, fee):
    pnl = contracts * (1 - lim) - fee if won else -contracts * lim - fee
    return round(pnl, 4), round(lim + fee / contracts, 4)


def verdict(filled):
    """filled = graded FILLED rows. Judged once, on the first JUDGE_N by order time, then frozen."""
    rows = sorted(filled, key=lambda r: int(r["order_ts"]))
    if len(rows) < JUDGE_N:
        return "PENDING", rows
    rows = rows[:JUDGE_N]
    win = sum(r["won"] == "1" for r in rows) / len(rows)
    be = sum(float(r["breakeven"]) for r in rows) / len(rows)
    return ("PASSED" if win >= be + MARGIN - 1e-9 else "FAILED"), rows


# ---------------- data fetch ----------------

def fee_terms():
    r = get(f"{KALSHI}/series/{SERIES}")
    try:
        s = r.json()["series"]
        ft = s.get("fee_type", "") or "unknown"
        m = num(s.get("fee_multiplier"))
        return ft, (m if m is not None else 1.0)
    except Exception:
        return "unknown", 1.0


def maker_rate(fee_type):
    """Published schedule: resting orders pay nothing unless the series is on the Maker Fees list."""
    return MAKER_RATE if "maker" in fee_type else 0.0


def all_trades(ticker, start, end):
    out, cursor = [], ""
    for _ in range(50):
        p = {"ticker": ticker, "min_ts": int(start), "max_ts": int(end), "limit": 1000}
        if cursor:
            p["cursor"] = cursor
        r = get(f"{KALSHI}/markets/trades", p)
        if r is None or r.status_code != 200:
            return None
        j = r.json()
        out += j.get("trades", [])
        cursor = j.get("cursor")
        if not cursor or not j.get("trades"):
            break
        time.sleep(0.1)
    return out


def market(ticker):
    r = get(f"{KALSHI}/markets/{ticker}")
    if r is None or r.status_code != 200:
        return None
    return r.json().get("market")


def btc_closes(start, end):
    """minute_start -> Coinbase BTC-USD 1m close, for [start, end]."""
    r = get(COINBASE, {"granularity": 60, "start": utc(start), "end": utc(end)})
    if r is None or r.status_code != 200:
        return {}
    return {int(c[0]): float(c[4]) for c in r.json()}


def new_row(m):
    o, c = ts(m["open_time"]), ts(m["close_time"])
    return {k: "" for k in FIELDS} | {"ticker": m["ticker"], "open_ts": o, "close_ts": c,
                                      "target": num(m.get("floor_strike"))}


def place(row, closes, ask_up, ask_dn, bid_up, bid_dn, order_ts):
    """Fill in the simulated order (or why there is none). Uses only data known at order time."""
    T = int(row["open_ts"]) + DECISION_S
    b0, b1 = closes.get(T - 60), closes.get(T - 120)
    lean, mom, side = decide(num(row["target"]), b0, b1)
    row.update(btc_T=b0 or "", btc_T60=b1 or "", lean=lean or "", mom=mom or "", order_ts=order_ts)
    if b0 is None or b1 is None:
        row["status"] = "NO_DATA"                               # BTC candles missing: not a signal decision
        return row
    if side is None:
        row["status"] = "NO_SIGNAL"
        return row
    ask, bid = (ask_up, bid_up) if side == "Up" else (ask_dn, bid_dn)
    lim = limit_price(ask)
    row.update(side=side, ask=ask if ask is not None else "", bid=bid if bid is not None else "")
    if lim is None:
        row["status"] = "NO_QUOTE"
        return row
    row.update(limit=lim, contracts=contracts_for(lim), status="PENDING")
    return row


def grade_row(row, fee_type, mult):
    """After the close: did the market trade through us, and who won. Leaves PENDING if data isn't there yet."""
    m = market(row["ticker"])
    if not m or m.get("result") not in ("yes", "no"):
        if m and time.time() > int(row["close_ts"]) + 6 * 3600:
            row["status"] = "NO_RESULT"
        return row
    trades = all_trades(row["ticker"], int(row["order_ts"]), int(row["close_ts"]))
    if trades is None:
        return row
    lim, c = float(row["limit"]), int(row["contracts"])
    status, vol, first = check_fill(trades, row["side"], lim, c, int(row["order_ts"]), int(row["close_ts"]))
    won = (m["result"] == "yes") == (row["side"] == "Up")
    fee = maker_fee(c, lim, maker_rate(fee_type), mult)
    fee_s = maker_fee(c, lim, MAKER_RATE, mult)
    pnl, be = settle(lim, c, won, fee)
    pnl_s, _ = settle(lim, c, won, fee_s)
    row.update(status=status, through_vol=round(vol, 2), first_through_ts=first or "", result=m["result"],
               won="1" if won else "0", fee=fee, fee_stress=fee_s, pnl=pnl, pnl_stress=pnl_s, breakeven=be,
               fee_type=fee_type, fee_mult=mult, graded_utc=utc())
    return row


# ---------------- modes ----------------

def live(minutes):
    rows = {r["ticker"]: r for r in load(ORDERS)}
    stop = time.time() + 60 * minutes
    print(f"live: {minutes} min, {len(rows)} orders on file")
    while time.time() < stop:
        now = time.time()
        r = get(f"{KALSHI}/markets", {"series_ticker": SERIES, "status": "open", "limit": 50})
        opens = (r.json().get("markets", []) if r is not None and r.status_code == 200 else [])
        for m in opens:
            try:
                o, c = ts(m["open_time"]), ts(m["close_time"])
            except Exception:
                continue
            T = o + DECISION_S
            if c - o != WINDOW_S or m["ticker"] in rows or not T <= now < T + POST_GRACE_S:
                continue
            closes = btc_closes(T - 240, T)
            row = place(new_row(m), closes, num(m.get("yes_ask_dollars")), num(m.get("no_ask_dollars")),
                        num(m.get("yes_bid_dollars")), num(m.get("no_bid_dollars")), int(time.time()))
            rows[m["ticker"]] = row
            save(ORDERS, list(rows.values()))
            print(f"{utc()} {m['ticker']} {row['status']} side={row['side']} ask={row['ask']} limit={row['limit']}")
        # sleep to the next decision time (windows open every 15 min), polling a little early
        nxt = min([ts(m["open_time"]) + DECISION_S for m in opens if ts(m["open_time"]) + DECISION_S > now] or [now + 30])
        time.sleep(max(2, min(30, nxt - time.time() + 1)))


def grade(path=ORDERS):
    rows = load(path)
    if not rows:
        return rows
    fee_type, mult = fee_terms()
    now = time.time()
    for r in rows:
        if r["status"] == "PENDING" and now > int(r["close_ts"]) + 60:
            grade_row(r, fee_type, mult)
            time.sleep(0.1)
    save(path, rows)
    return rows


def replay(n):
    """Exploratory: last n settled markets. Quote = 1m candle [T-60,T) close (asks, never mid). Never judged."""
    ms, cursor = [], ""
    while len(ms) < n:
        p = {"series_ticker": SERIES, "status": "settled", "limit": 1000}
        if cursor:
            p["cursor"] = cursor
        r = get(f"{KALSHI}/markets", p)
        if r is None or r.status_code != 200:
            break
        j = r.json()
        ms += j.get("markets", [])
        cursor = j.get("cursor")
        if not cursor or not j.get("markets"):
            break
    ms = sorted(ms, key=lambda m: ts(m["open_time"]))[-n:]
    if not ms:
        print("replay: no markets")
        return []
    o0, o1 = ts(ms[0]["open_time"]), ts(ms[-1]["open_time"])
    closes, t = {}, o0 - 600
    while t < o1 + DECISION_S:
        closes |= btc_closes(t, min(t + 290 * 60, o1 + DECISION_S))
        t += 290 * 60
        time.sleep(0.15)
    done = {r["ticker"]: r for r in load(REPLAY)}
    fee_type, mult = fee_terms()
    for m in ms:
        if m["ticker"] in done:
            continue
        row = new_row(m)
        T = int(row["open_ts"]) + DECISION_S
        cr = get(f"{KALSHI}/series/{SERIES}/markets/{m['ticker']}/candlesticks",
                 {"start_ts": T - 60, "end_ts": T, "period_interval": 1})
        cs = [x for x in (cr.json().get("candlesticks", []) if cr is not None and cr.status_code == 200 else [])
              if int(x.get("end_period_ts", 0)) == T]
        ya, yb = (cs[0].get("yes_ask") or {}, cs[0].get("yes_bid") or {}) if cs else ({}, {})
        au, bu = num(ya.get("close_dollars")), num(yb.get("close_dollars"))
        place(row, closes, au, (round(1 - bu, 4) if bu is not None else None),
              bu, (round(1 - au, 4) if au is not None else None), T)
        if row["status"] == "PENDING":
            grade_row(row, fee_type, mult)
        done[m["ticker"]] = row
        time.sleep(0.1)
    save(REPLAY, list(done.values()))
    return list(done.values())


# ---------------- report ----------------

def summary(rows):
    placed = [r for r in rows if r["status"] in ("FILLED", "PARTIAL", "UNFILLED")]
    filled = [r for r in placed if r["status"] == "FILLED"]
    unfilled = [r for r in placed if r["status"] != "FILLED"]
    s = {"windows": len(rows), "no_signal": sum(r["status"] == "NO_SIGNAL" for r in rows),
         "no_quote": sum(r["status"] in ("NO_QUOTE", "NO_DATA") for r in rows),
         "pending": sum(r["status"] == "PENDING" for r in rows), "placed": len(placed),
         "filled": len(filled), "partial": sum(r["status"] == "PARTIAL" for r in rows), "rows": filled}
    if filled:
        s["win"] = sum(r["won"] == "1" for r in filled) / len(filled)
        s["be"] = sum(float(r["breakeven"]) for r in filled) / len(filled)
        s["pnl"] = sum(float(r["pnl"]) for r in filled)
        s["pnl_stress"] = sum(float(r["pnl_stress"]) for r in filled)
        s["fee_type"] = filled[-1]["fee_type"]
    if unfilled:
        s["unfilled_win"] = sum(r["won"] == "1" for r in unfilled) / len(unfilled)
        s["unfilled_n"] = len(unfilled)
    return s


def block(title, s):
    out = [f"## {title}", ""]
    if s["placed"] == 0:
        out += [f"- Windows seen {s['windows']}, no orders graded yet (no signal {s['no_signal']}, "
                f"no quote {s['no_quote']}, waiting for close {s['pending']}).", ""]
        return out
    fr = s["filled"] / s["placed"]
    out.append(f"- Orders posted {s['placed']} · **filled {s['filled']}** ({fr:.0%} fill rate) · partial only "
               f"{s['partial']} (not counted) · no signal {s['no_signal']} · no quote or data {s['no_quote']} · waiting {s['pending']}")
    if s["filled"]:
        out.append(f"- Win rate **{s['win']:.1%}** vs break-even {s['be']:.1%} "
                   f"({100 * (s['win'] - s['be']):+.1f} points; needs +{100 * MARGIN:.0f})")
        out.append(f"- P&L after fees **{s['pnl']:+.2f}** on {s['filled']} fills of ${STAKE:.0f} "
                   f"(maker fee as published for this series: {s['fee_type']}). "
                   f"If a 0.0175 maker fee applied: {s['pnl_stress']:+.2f}")
    if s.get("unfilled_n"):
        out.append(f"- Orders that never filled would have won {s['unfilled_win']:.0%} of {s['unfilled_n']}. "
                   f"A big gap vs the filled win rate = fills come mostly when price runs against you.")
    if s["filled"] < 30:
        out.append("- Sample too small to mean anything yet.")
    out.append("")
    return out


def report():
    live_rows, rep = load(ORDERS), load(REPLAY)
    s = summary(live_rows)
    v, judged = verdict(s["rows"])
    out = ["# Maker (limit-order) paper test, Kalshi BTC 15m", "",
           f"Generated {utc()}. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.", ""]
    if v == "PENDING":
        out.append(f"**Verdict: PENDING. {s['filled']}/{JUDGE_N} filled trades, {JUDGE_N - s['filled']} to go.**")
    else:
        w = sum(r["won"] == "1" for r in judged) / JUDGE_N
        be = sum(float(r["breakeven"]) for r in judged) / JUDGE_N
        p = sum(float(r["pnl"]) for r in judged)
        out.append(f"**Verdict: {v}.** First {JUDGE_N} fills: win {w:.1%} vs break-even {be:.1%} "
                   f"({100 * (w - be):+.1f} points, needed +{100 * MARGIN:.0f}), P&L after fees {p:+.2f}.")
    out += ["", "Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades "
            "print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.", ""]
    out += block("Live forward test (judged)", s)
    if rep:
        out += block("Historical replay (exploratory preview, never judged)", summary(rep))
        out.append("Replay quotes come from 1-minute candles, so they are rougher than the live book read.")
    os.makedirs(OUT, exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))


# ---------------- offline self-test ----------------

def selftest():
    iso = lambda t: utc(t)
    assert decide(100, 101, 100.5)[2] == "Up" and decide(100, 99, 99.5)[2] == "Down"
    assert decide(100, 101, 102)[2] is None and decide(100, 101, 101)[2] is None
    assert limit_price(0.62) == 0.60 and limit_price(0.03) is None and limit_price(0.995) is None
    assert contracts_for(0.60) == 16 and contracts_for(0.25) == 40
    o, c = 1000, 1180
    tr = [{"created_time": iso(1010), "yes_price_dollars": "0.6000", "no_price_dollars": "0.4000", "count_fp": "50"},  # touch only
          {"created_time": iso(990), "yes_price_dollars": "0.5000", "no_price_dollars": "0.5000", "count_fp": "50"},   # before post
          {"created_time": iso(1020), "yes_price_dollars": "0.5800", "no_price_dollars": "0.4200", "count_fp": "10",
           "is_block_trade": True}]                                                                                    # block
    assert check_fill(tr, "Up", 0.60, 16, o, c)[0] == "UNFILLED"
    tr.append({"created_time": iso(1030), "yes_price_dollars": "0.5900", "no_price_dollars": "0.4100", "count_fp": "10"})
    assert check_fill(tr, "Up", 0.60, 16, o, c)[:2] == ("PARTIAL", 10.0)
    tr.append({"created_time": iso(1100), "yes_price_dollars": "0.5700", "no_price_dollars": "0.4300", "count_fp": "6"})
    assert check_fill(tr, "Up", 0.60, 16, o, c) == ("FILLED", 16.0, 1030)
    tr.append({"created_time": iso(1200), "yes_price_dollars": "0.1000", "no_price_dollars": "0.9000", "count_fp": "99"})
    assert check_fill(tr, "Up", 0.60, 16, o, c)[1] == 16.0                                                            # after close
    # Down side reads the no price: no at 0.41 is through a 0.42 Down limit, no at 0.42 is a touch
    assert check_fill([{"created_time": iso(1050), "yes_price": 59, "count": 30}], "Down", 0.42, 23, o, c)[0] == "FILLED"
    assert check_fill([{"created_time": iso(1050), "yes_price": 58, "count": 30}], "Down", 0.42, 23, o, c)[0] == "UNFILLED"
    assert maker_fee(16, 0.60, 0.0, 1.0) == 0.0 and maker_fee(16, 0.60, 0.0175, 1.0) == 0.07
    assert settle(0.60, 16, True, 0.0) == (6.4, 0.6) and settle(0.60, 16, False, 0.07) == (-9.67, 0.6044)
    mk = lambda i, w, be: {"order_ts": str(i), "won": "1" if w else "0", "breakeven": str(be)}
    assert verdict([mk(i, i % 2 == 0, 0.5) for i in range(99)])[0] == "PENDING"
    assert verdict([mk(i, i % 100 < 53, 0.5) for i in range(100)])[0] == "PASSED"       # 53% vs 50% BE
    assert verdict([mk(i, i % 100 < 52, 0.5) for i in range(100)])[0] == "FAILED"       # 52% vs 50% BE
    assert verdict([mk(i, i < 100, 0.5) for i in range(150)])[1][-1]["order_ts"] == "99"  # frozen on first 100
    row = place({k: "" for k in FIELDS} | {"open_ts": 0, "target": 100.0}, {660: 101.0, 600: 100.5},
                0.62, 0.40, 0.60, 0.38, 720)
    assert (row["side"], row["limit"], row["contracts"], row["status"]) == ("Up", 0.60, 16, "PENDING")
    print("selftest: all checks passed")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if mode == "selftest":
        selftest()
    elif mode == "live":
        live(float(os.getenv("RUN_MINUTES", "55")))
    elif mode == "grade":
        grade()
        report()
    elif mode == "replay":
        replay(int(sys.argv[2]) if len(sys.argv) > 2 else 500)
        report()
    else:
        sys.exit(__doc__)
