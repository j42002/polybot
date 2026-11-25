"""Phase 1: historical (exploratory) test of the "12-minute rule" on Kalshi BTC 15m. Read-only, $0.

Rules are frozen in data/15m/PREREG.md. This script only implements them.
Outputs (data/15m/):
  markets.csv   one row per settled market: target, outcome, BTC at T and T-60, asks after T, flags
  report.md     the full results, every exclusion counted
Run: python backtest15.py            (resumes: markets already in markets.csv are not refetched)
"""
import csv
import hashlib
import json
import math
import os
import sys
import time
from datetime import datetime, timezone, timedelta

import requests

KALSHI = "https://external-api.kalshi.com/trade-api/v2"
COINBASE = "https://api.exchange.coinbase.com/products/BTC-USD/candles"
US_GATEWAY = "https://gateway.polymarket.us/v1"
SERIES = "KXBTC15M"
OUT = os.path.join("data", "15m")
MARKETS = os.path.join(OUT, "markets.csv")
REPORT = os.path.join(OUT, "report.md")
PREREG = os.path.join(OUT, "PREREG.md")
HDR = {"User-Agent": "polybot-research/1.0 (paper only)"}
DECISION_S = 720
WINDOW_S = 900
STAKE = 10.0
FIELDS = ["ticker", "open_ts", "close_ts", "target", "final", "result", "settle_check",
          "ask_up_close", "ask_dn_close", "ask_up_open", "ask_dn_open", "vol_minute", "candle_status"]

session = requests.Session()
session.headers.update(HDR)


def get(url, params=None, tries=6):
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


# ---------------- data fetch ----------------

def settled_markets():
    out, cursor = [], ""
    while True:
        p = {"series_ticker": SERIES, "status": "settled", "limit": 1000}
        if cursor:
            p["cursor"] = cursor
        r = get(f"{KALSHI}/markets", p)
        if r is None or r.status_code != 200:
            print(f"markets page failed ({getattr(r, 'status_code', 'no response')}) after {len(out)}")
            break
        j = r.json()
        out += j.get("markets", [])
        cursor = j.get("cursor")
        if not cursor or not j.get("markets"):
            break
        time.sleep(0.1)
    return out


def fee_multiplier():
    r = get(f"{KALSHI}/series/{SERIES}")
    try:
        s = r.json()["series"]
        m = s.get("fee_multiplier")
        return (float(m) if m is not None else 1.0), s.get("fee_type", "")
    except Exception:
        return 1.0, "unknown"


def market_row(m):
    """Market metadata + the one candle we need: [T, T+60). Only asks, never mid."""
    o, c = ts(m["open_time"]), ts(m["close_time"])
    target, final = num(m.get("floor_strike")), num(m.get("expiration_value"))
    res = m.get("result", "")
    check = ""
    if target is not None and final is not None and res in ("yes", "no"):
        check = "ok" if (final >= target) == (res == "yes") else "MISMATCH"
    row = {"ticker": m["ticker"], "open_ts": o, "close_ts": c, "target": target, "final": final,
           "result": res, "settle_check": check, "ask_up_close": "", "ask_dn_close": "",
           "ask_up_open": "", "ask_dn_open": "", "vol_minute": "", "candle_status": ""}
    if c - o != WINDOW_S:
        row["candle_status"] = "bad_window"
        return row
    T = o + DECISION_S
    r = get(f"{KALSHI}/series/{SERIES}/markets/{m['ticker']}/candlesticks",
            {"start_ts": T, "end_ts": T + 60, "period_interval": 1})
    if r is None or r.status_code != 200:
        row["candle_status"] = f"http_{getattr(r, 'status_code', 'none')}"
        return row
    cs = [x for x in r.json().get("candlesticks", []) if int(x.get("end_period_ts", 0)) == T + 60]
    if not cs:
        row["candle_status"] = "no_candle"
        return row
    x = cs[0]
    ya, yb = x.get("yes_ask") or {}, x.get("yes_bid") or {}
    up_c, bid_c = num(ya.get("close_dollars")), num(yb.get("close_dollars"))
    up_o, bid_o = num(ya.get("open_dollars")), num(yb.get("open_dollars"))
    row.update(ask_up_close=up_c, ask_dn_close=(round(1 - bid_c, 4) if bid_c is not None else ""),
               ask_up_open=up_o, ask_dn_open=(round(1 - bid_o, 4) if bid_o is not None else ""),
               vol_minute=num(x.get("volume_fp")), candle_status="ok")
    return row


def coinbase_closes(start, end):
    """minute_start -> close, for [start, end]. 300 candles per request."""
    closes, t = {}, start
    while t < end:
        t2 = min(t + 300 * 60, end)
        r = get(COINBASE, {"granularity": 60,
                           "start": datetime.fromtimestamp(t, timezone.utc).isoformat(),
                           "end": datetime.fromtimestamp(t2, timezone.utc).isoformat()})
        if r is not None and r.status_code == 200:
            for c in r.json():
                closes[int(c[0])] = float(c[4])
        t = t2
        time.sleep(0.15)
    return closes


def polymarket_check(rows, limit=700):
    """Same window on Polymarket US 15m: compare start/end BRTI values and the winner."""
    out = []
    for r in sorted(rows, key=lambda r: -int(r["open_ts"]))[:limit]:
        slug = "btc-updown-15m-" + datetime.fromtimestamp(int(r["open_ts"]), timezone.utc).strftime("%Y-%m-%d-%H%Mz")
        g = get(f"{US_GATEWAY}/events/slug/{slug}", tries=2)
        if g is None or g.status_code != 200:
            out.append({"ticker": r["ticker"], "found": False})
            continue
        try:
            t = g.json()["event"]["markets"][0]["assetPriceTerms"]
            ptb = num((t.get("priceToBeat") or {}).get("value"))
            sp = num((t.get("settlementPrice") or {}).get("value"))
        except Exception:
            out.append({"ticker": r["ticker"], "found": False})
            continue
        out.append({"ticker": r["ticker"], "found": True, "pm_ptb": ptb, "pm_settle": sp,
                    "k_target": num(r["target"]), "k_final": num(r["final"]), "k_result": r["result"]})
        time.sleep(0.05)
    return out


# ---------------- rule + grading (pure functions, tested offline) ----------------

def decide(row, closes):
    """Signals using only data available at T. Returns (lean, mom, btc_T, btc_T60, why_missing)."""
    o = int(row["open_ts"])
    T = o + DECISION_S
    target = num(row["target"])
    b0, b1 = closes.get(T - 60), closes.get(T - 120)      # candle [T-60,T) closes at T; [T-120,T-60) at T-60
    if target is None:
        return None, None, b0, b1, "no_target"
    if b0 is None or b1 is None:
        return None, None, b0, b1, "no_btc"
    lean = "Up" if b0 >= target else "Down"
    mom = "Up" if b0 > b1 else ("Down" if b0 < b1 else None)
    return lean, mom, b0, b1, ""


def kalshi_fee(contracts, price, mult):
    return math.ceil(round(100 * mult * 0.07 * contracts * price * (1 - price), 6)) / 100.0


def trade(side, row, entry, mult, fee_scale=1.0):
    ask = num(row[f"ask_{'up' if side == 'Up' else 'dn'}_{entry}"])
    if ask is None or not 0.01 < ask < 0.99:
        return None
    c = math.floor(STAKE / ask)
    if c < 1:
        return None
    fee = kalshi_fee(c, ask, mult) * fee_scale
    won = (row["result"] == "yes") == (side == "Up")
    pnl = c * (1 - ask) - fee if won else -c * ask - fee
    return {"ask": ask, "contracts": c, "fee": fee, "won": won, "pnl": pnl,
            "breakeven": ask + fee / c}


def vol_prior_hour(closes, T):
    px = [closes.get(m) for m in range(T - 3660, T - 59, 60)]
    px = [p for p in px if p]
    if len(px) < 30:
        return None
    rets = [math.log(b / a) for a, b in zip(px, px[1:])]
    m = sum(rets) / len(rets)
    return math.sqrt(sum((x - m) ** 2 for x in rets) / max(1, len(rets) - 1))


def stats(trs):
    n = len(trs)
    if not n:
        return None
    pn = [t["pnl"] for t in trs]
    wins = sum(t["won"] for t in trs)
    mean = sum(pn) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in pn) / (n - 1)) if n > 1 else 0.0
    be = [t["breakeven"] for t in trs]
    exp_w = sum(be)
    var_w = sum(b * (1 - b) for b in be)
    z = (wins - exp_w) / math.sqrt(var_w) if var_w > 0 else 0.0
    eq = peak = dd = 0.0
    streak = worst = 0
    for t in trs:
        eq += t["pnl"]
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
        streak = streak + 1 if not t["won"] else 0
        worst = max(worst, streak)
    half = 1.96 * sd / math.sqrt(n) if n > 1 else float("nan")
    return {"n": n, "wins": wins, "win_rate": wins / n, "breakeven": exp_w / n, "avg_ask": sum(t["ask"] for t in trs) / n,
            "pnl": sum(pn), "mean": mean, "ci": (mean - half, mean + half), "z": z, "dd": dd, "streak": worst,
            "fees": sum(t["fee"] for t in trs)}


def fmt(s):
    if not s:
        return "| 0 | - | - | - | - | - | - | - |"
    return (f"| {s['n']} | {s['win_rate']:.1%} | {s['breakeven']:.1%} | {s['pnl']:+.2f} | {s['mean']:+.3f} "
            f"({s['ci'][0]:+.3f} to {s['ci'][1]:+.3f}) | {s['z']:+.2f} | -{s['dd']:.2f} | {s['streak']} |")


HEAD = ["| Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |",
        "|---|---|---|---|---|---|---|---|"]


def build(rows, closes, mult, fee_type, pm):
    rows = sorted(rows, key=lambda r: int(r["open_ts"]))
    miss = {"bad_window": 0, "no_candle": 0, "candle_http": 0, "no_target": 0, "no_btc": 0,
            "settle_mismatch": 0, "unsettled": 0}
    rules = {"AGREE (primary)": [], "LEAN only (secondary)": [], "MOMENTUM only (secondary)": []}
    entry0, fee0, fee15 = [], [], []
    no_quote = no_signal = disagree = 0
    graded = 0
    for r in rows:
        if r["result"] not in ("yes", "no"):
            miss["unsettled"] += 1
            continue
        if r["settle_check"] == "MISMATCH":
            miss["settle_mismatch"] += 1
            continue
        st = r["candle_status"]
        if st != "ok":
            key = "bad_window" if st == "bad_window" else ("no_candle" if st == "no_candle" else "candle_http")
            miss[key] += 1
            continue
        lean, mom, b0, b1, why = decide(r, closes)
        if why:
            miss[why] += 1
            continue
        graded += 1
        T = int(r["open_ts"]) + DECISION_S
        meta = {"open_ts": int(r["open_ts"]), "vol": vol_prior_hour(closes, T)}
        for name, side in (("LEAN only (secondary)", lean), ("MOMENTUM only (secondary)", mom)):
            if side:
                t = trade(side, r, "close", mult)
                if t:
                    rules[name].append({**t, **meta})
        if mom is None:
            no_signal += 1
            continue
        if lean != mom:
            disagree += 1
            continue
        t = trade(lean, r, "close", mult)
        if not t:
            no_quote += 1
            continue
        rules["AGREE (primary)"].append({**t, **meta})
        for lst, kw in ((entry0, {"entry": "open"}), (fee0, {"fee_scale": 0.0}), (fee15, {"fee_scale": 1.5})):
            x = trade(lean, r, kw.get("entry", "close"), mult, kw.get("fee_scale", 1.0))
            if x:
                lst.append({**x, **meta})
    P = rules["AGREE (primary)"]
    d0 = datetime.fromtimestamp(int(rows[0]["open_ts"]), timezone.utc) if rows else None
    d1 = datetime.fromtimestamp(int(rows[-1]["open_ts"]), timezone.utc) if rows else None
    prereg_hash = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()[:12] if os.path.exists(PREREG) else "missing"
    L = [f"# Phase 1 results: 12-minute rule on Kalshi BTC 15m (EXPLORATORY)", "",
         f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · rules: data/15m/PREREG.md (sha256 {prereg_hash})",
         f"Period: {d0:%Y-%m-%d %H:%MZ} to {d1:%Y-%m-%d %H:%MZ} · settled markets returned: {len(rows)} · "
         f"usable for the rule: {graded}" if rows else "No markets.",
         f"Fee: Kalshi taker, multiplier {mult} ({fee_type or 'n/a'}), round up per order. Entry = ask ~60s after the decision.",
         "", "**This cannot prove profitability. It decides only whether Phase 2 (forward paper test) is worth running.**", "",
         "## Primary: AGREE", ""] + HEAD + [fmt(stats(P)), "",
         f"- Windows where LEAN and MOMENTUM disagreed (no trade): {disagree} · momentum flat: {no_signal} · "
         f"signal but no usable ask (<=1c or >=99c): {no_quote}"]
    # sensitivity
    L += ["", "## Sensitivity (primary rule)", ""] + ["| Variant |" + HEAD[0][1:], "|---" + HEAD[1]]
    for label, lst in (("Entry ~0s after decision (candle open)", entry0), ("No fee", fee0), ("Fee x1.5", fee15),
                       ("As registered (entry ~60s, fee x1)", P)):
        L.append(f"| {label} " + fmt(stats(lst)))
    # by price bucket
    L += ["", "## By entry price (primary)", "", "| Ask bucket |" + HEAD[0][1:], "|---" + HEAD[1]]
    for lo, hi in ((0.01, 0.6), (0.6, 0.75), (0.75, 0.85), (0.85, 0.92), (0.92, 0.99)):
        L.append(f"| {lo:.0%}-{hi:.0%} " + fmt(stats([t for t in P if lo <= t["ask"] < hi])))
    # chronological halves + weeks
    L += ["", "## Stability over time (primary)", "", "| Period |" + HEAD[0][1:], "|---" + HEAD[1]]
    h = len(P) // 2
    L.append("| First half " + fmt(stats(P[:h])))
    L.append("| Second half " + fmt(stats(P[h:])))
    weeks = {}
    for t in P:
        k = datetime.fromtimestamp(t["open_ts"], timezone.utc).strftime("%G-W%V")
        weeks.setdefault(k, []).append(t)
    for k in sorted(weeks):
        L.append(f"| {k} " + fmt(stats(weeks[k])))
    # volatility terciles (prior hour, known at T)
    vs = sorted(t["vol"] for t in P if t["vol"] is not None)
    if len(vs) >= 9:
        a, b = vs[len(vs) // 3], vs[2 * len(vs) // 3]
        L += ["", "## By market condition: BTC volatility in the hour before (primary)", "", "| Volatility |" + HEAD[0][1:], "|---" + HEAD[1]]
        L.append("| Calm (lowest third) " + fmt(stats([t for t in P if t["vol"] is not None and t["vol"] < a])))
        L.append("| Normal " + fmt(stats([t for t in P if t["vol"] is not None and a <= t["vol"] < b])))
        L.append("| Wild (highest third) " + fmt(stats([t for t in P if t["vol"] is not None and t["vol"] >= b])))
    # sessions
    L += ["", "## By time of day, UTC (primary)", "", "| Session |" + HEAD[0][1:], "|---" + HEAD[1]]
    for label, lo, hi in (("Asia 00-08", 0, 8), ("Europe 08-13", 8, 13), ("US 13-21", 13, 21), ("Late US 21-24", 21, 24)):
        L.append(f"| {label} " + fmt(stats([t for t in P if lo <= datetime.fromtimestamp(t['open_ts'], timezone.utc).hour < hi])))
    # secondary
    L += ["", "## Secondary rules (multiple-testing warning: these cannot confirm anything)", "", "| Rule |" + HEAD[0][1:], "|---" + HEAD[1]]
    for name in ("LEAN only (secondary)", "MOMENTUM only (secondary)"):
        L.append(f"| {name} " + fmt(stats(rules[name])))
    # missing data
    L += ["", "## Missing or excluded data (all counted)", ""] + [f"- {k}: {v}" for k, v in miss.items()]
    # cross-platform
    found = [x for x in pm if x.get("found")]
    L += ["", "## Cross-platform check: Kalshi vs Polymarket US, same 15m window", "",
          f"- Windows checked: {len(pm)} (most recent) · found on Polymarket US: {len(found)}"]
    both = [x for x in found if x["pm_ptb"] is not None and x["k_target"] is not None]
    if both:
        d = sorted(abs(x["pm_ptb"] - x["k_target"]) for x in both)
        L.append(f"- Start price (target) difference: median ${d[len(d) // 2]:.2f}, max ${d[-1]:.2f}, exact matches {sum(v < 0.005 for v in d)}/{len(d)}")
    fin = [x for x in found if x["pm_settle"] is not None and x["k_final"] is not None and x["pm_ptb"] is not None]
    if fin:
        d = sorted(abs(x["pm_settle"] - x["k_final"]) for x in fin)
        agree = sum(((x["pm_settle"] >= x["pm_ptb"]) == (x["k_result"] == "yes")) for x in fin)
        L.append(f"- End price difference: median ${d[len(d) // 2]:.2f}, max ${d[-1]:.2f} · same winner {agree}/{len(fin)}")
    L += ["", "## How to read this", "",
          "- Win rate alone means nothing: compare it with break-even (price + fee).",
          "- z vs break-even above +2 would be a hint, not proof: this is one look at past data, prices are 1-minute",
          "  candle closes (not guaranteed fills, no size), and BTC comes from Coinbase, not BRTI.",
          "- Only the Phase 2 forward paper test (300 trades) can confirm."]
    return "\n".join(L) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    have = {}
    if os.path.exists(MARKETS):
        with open(MARKETS, newline="", encoding="utf-8") as f:
            have = {r["ticker"]: r for r in csv.DictReader(f)}
    mult, fee_type = fee_multiplier()
    print(f"fee multiplier {mult} ({fee_type})")
    ms = settled_markets()
    print(f"settled markets returned: {len(ms)} (already have {len(have)})")
    todo = [m for m in ms if m["ticker"] not in have or have[m["ticker"]].get("candle_status", "").startswith("http")]
    budget = float(os.getenv("BUDGET_MIN", "300")) * 60
    t_start = time.time()
    for i, m in enumerate(todo):
        if time.time() - t_start > budget:
            print(f"time budget reached after {i} markets; rerun to continue")
            break
        try:
            have[m["ticker"]] = market_row(m)
        except Exception as e:
            print(f"  {m.get('ticker')}: {e!r}")
        if i % 250 == 0:
            print(f"  {i}/{len(todo)} markets")
            save(have)
        time.sleep(0.07)
    save(have)
    rows = list(have.values())
    if not rows:
        print("no data")
        return
    o = [int(r["open_ts"]) for r in rows]
    closes = coinbase_closes(min(o) - 3700, max(o) + WINDOW_S)
    print(f"coinbase minutes: {len(closes)}")
    pm = polymarket_check(rows)
    rep = build(rows, closes, mult, fee_type, pm)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(rep)
    print(rep)


def save(have):
    with open(MARKETS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(have.values(), key=lambda r: int(r["open_ts"])):
            w.writerow(r)


if __name__ == "__main__":
    main()
