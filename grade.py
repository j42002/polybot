"""polybot grader v1 - scores the paper bets in data/checkpoints.csv.

1. For every window that has closed, pulls the REAL result from Gamma:
   winner (Up/Down), real price to beat and final price (eventMetadata).
2. Scores each strategy at each checkpoint: hit rate vs the price paid,
   paper P&L AFTER Polymarket's taker fee, 95% confidence interval.
3. Checks the model against the market (Brier score; lower = better).
4. Measures how far the Coinbase proxy is from the real Chainlink price to beat.
Writes data/results.csv (cache) and data/report.md (read this on your phone).

Verdict rules are fixed in advance so the goalposts can't move:
  under 300 bets           -> INCONCLUSIVE
  95% CI entirely above 0  -> PASSES
  95% CI entirely below 0  -> LOSES
  otherwise                -> NO EDGE
"""
VERSION = "polybot grader v5"

import csv
import json
import math
import os
import time
from datetime import datetime, timezone

import requests

GAMMA = "https://gamma-api.polymarket.com/events"
US_GATEWAY = "https://gateway.polymarket.us/v1"
GOOD_QUOTES = ("clob", "us_bbo")   # rows priced from a live order book
HEADERS = {"User-Agent": "polybot-paper/1 (research, log-only)"}
CHECKS = os.path.join("data", "checkpoints.csv")
RESULTS = os.path.join("data", "results.csv")
REPORT = os.path.join("data", "report.md")
STATS = os.path.join("data", "jj_stats.json")
FEE_RATE = 0.05
SHARES = 10            # paper size per bet, for dollar figures
MIN_BETS = 300
MAX_FETCH = 400        # Gamma lookups per run
RES_FIELDS = ["slug", "t_start", "winner", "ptb_true", "final_true", "graded_utc"]
STRATS = [("mom", "Momentum (bet the last-60s direction)"),
          ("lean", "Lean (bet the side BTC is on now)"),
          ("edge", "Edge (model beats the ask by 3c+)"),
          ("jj", "JJ (60-90s in, 35-70c ask, model +4c)"),
          ("safe", "SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left)")]


def fnum(x):
    try:
        return float(x) if x not in (None, "") else None
    except ValueError:
        return None


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_result(event):
    """Return (winner, ptb, final) from a Gamma event, or None if not resolved yet."""
    m = event["markets"][0]
    if not m.get("closed"):
        return None
    outcomes = json.loads(m["outcomes"])
    prices = [float(p) for p in json.loads(m["outcomePrices"])]
    winners = [o for o, p in zip(outcomes, prices) if p >= 0.99]
    if len(winners) != 1:
        return None
    meta = event.get("eventMetadata") or {}
    return winners[0], meta.get("priceToBeat"), meta.get("finalPrice")


def is_us(slug):
    return slug.endswith("z") and slug.count("-") >= 5


def fetch_us_result(s, slug):
    """US settles on BRTI: settlementPx 1 = Up won, 0 = Down won."""
    r = s.get(f"{US_GATEWAY}/events/slug/{slug}", headers=HEADERS, timeout=8)
    r.raise_for_status()
    m = r.json()["event"]["markets"][0]
    if not m.get("closed"):
        return None
    b = s.get(f"{US_GATEWAY}/markets/{m['slug']}/bbo", headers=HEADERS, timeout=8).json()["marketData"]
    px = float((b.get("settlementPx") or {}).get("value", "nan"))
    if px not in (0.0, 1.0):
        return None
    t = m.get("assetPriceTerms") or {}
    return ("Up" if px == 1.0 else "Down",
            (t.get("priceToBeat") or {}).get("value"), (t.get("settlementPrice") or {}).get("value"))


def fetch_results(slugs, known):
    s = requests.Session()
    new = []
    for slug, t_start in slugs:
        if slug in known or len(new) >= MAX_FETCH:
            continue
        if time.time() < int(t_start) + 300 + 180:   # give settlement ~3 min
            continue
        try:
            if is_us(slug):
                res = fetch_us_result(s, slug)
            else:
                r = s.get(GAMMA, params={"slug": slug}, headers=HEADERS, timeout=8)
                r.raise_for_status()
                ev = r.json()
                res = parse_result(ev[0]) if ev else None
        except Exception as e:
            print(f"  fetch {slug} failed: {e!r}")
            res = None
        if res:
            new.append({"slug": slug, "t_start": t_start, "winner": res[0],
                        "ptb_true": res[1], "final_true": res[2],
                        "graded_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
        time.sleep(0.15)
    return new


def bet_pnl(side, price, winner, fee_rate=None):
    """P&L per share after taker fee. None if no bet."""
    if not side or price is None or not 0 < price < 1:
        return None
    fee = (fee_rate if fee_rate is not None else FEE_RATE) * price * (1 - price)
    return (1 - price if side == winner else -price) - fee


def summarize(pnls, prices, wins):
    n = len(pnls)
    if n == 0:
        return None
    mean = sum(pnls) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in pnls) / (n - 1)) if n > 1 else 0.0
    half = 1.96 * sd / math.sqrt(n) if n > 1 else float("inf")
    lo, hi = mean - half, mean + half
    if n < MIN_BETS:
        verdict = f"INCONCLUSIVE (need {MIN_BETS}+)"
    elif lo > 0:
        verdict = "PASSES"
    elif hi < 0:
        verdict = "LOSES"
    else:
        verdict = "NO EDGE"
    return {"n": n, "hit": wins / n, "avg_price": sum(prices) / n, "mean": mean,
            "lo": lo, "hi": hi, "total": mean * n * SHARES, "verdict": verdict}


def brier(pairs):
    return sum((p - y) ** 2 for p, y in pairs) / len(pairs) if pairs else None


def build_report(rows, results):
    res = {r["slug"]: r for r in results}
    # only rows priced from the live order book count (v1 rows priced from Gamma's stale cache are dropped)
    graded = [r for r in rows if r["slug"] in res and r.get("quote_src") in GOOD_QUOTES]
    lines = [f"# polybot report", "",
             f"Updated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | "
             f"{len(rows)} checkpoints logged | {len(graded)} graded | "
             f"{len({r['slug'] for r in graded})} windows settled", "",
             "PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes "
             f"{SHARES} shares per bet. Breakeven hit rate = avg price paid.", ""]
    for cp in sorted({int(r["secs_left"]) for r in graded}, reverse=True):
        sub = [r for r in graded if int(r["secs_left"]) == cp]
        lines += [f"## {cp // 60}:{cp % 60:02d} left ({len(sub)} windows)", "",
                  "| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |",
                  "|---|---|---|---|---|---|---|---|"]
        for key, label in STRATS:
            pnls, prices, wins = [], [], 0
            for r in sub:
                side, price = r.get(f"{key}_side"), fnum(r.get(f"{key}_price"))
                pnl = bet_pnl(side, price, res[r["slug"]]["winner"], fnum(r.get("fee_rate")))
                if pnl is not None:
                    pnls.append(pnl)
                    prices.append(price)
                    wins += side == res[r["slug"]]["winner"]
            s = summarize(pnls, prices, wins)
            if s:
                lines.append(f"| {label} | {s['n']} | {s['hit']:.1%} | {s['avg_price']:.1%} | "
                             f"{s['mean']:+.3f} | {s['lo']:+.3f} to {s['hi']:+.3f} | "
                             f"${s['total']:+.2f} | {s['verdict']} |")
            else:
                lines.append(f"| {label} | 0 | - | - | - | - | - | no bets |")
        model, market = [], []
        for r in sub:
            y = 1.0 if res[r["slug"]]["winner"] == "Up" else 0.0
            mu, ua, ub = fnum(r["model_up"]), fnum(r["up_ask"]), fnum(r["up_bid"])
            if mu is not None and ua is not None:
                mid = (ua + ub) / 2 if ub is not None else ua
                model.append((mu, y))
                market.append((mid, y))
        bm, bk = brier(model), brier(market)
        if bm is not None:
            who = "model" if bm < bk else "market"
            lines += ["", f"Brier (lower is better): model {bm:.4f} vs market {bk:.4f} -> **{who} is sharper**"]
        lines.append("")
    errs_avg, errs_spot = [], []
    for slug in {r["slug"] for r in graded}:
        r0 = next(r for r in graded if r["slug"] == slug)
        true = fnum(res[slug]["ptb_true"])
        if true is None:
            continue
        a, s = fnum(r0["ptb_proxy"]), fnum(r0["spot_open"])
        if a is not None:
            errs_avg.append(a - true)
        if s is not None:
            errs_spot.append(s - true)
    lines += ["## Price-to-beat proxy (Coinbase vs real Chainlink)", ""]
    for name, e in (("60s average", errs_avg), ("spot at open", errs_spot)):
        if len(e) > 1:
            m = sum(e) / len(e)
            sd = math.sqrt(sum((x - m) ** 2 for x in e) / (len(e) - 1))
            lines.append(f"- {name}: n={len(e)}, bias ${m:+.2f}, sd ${sd:.2f} "
                         f"(set BASIS_SD near {sd:.0f})")
    lines += ["", f"_{VERSION}_"]
    return "\n".join(lines)


def jj_stats(rows, results, key="jj"):
    res = {r["slug"]: r for r in results}
    pnls, prices, wins = [], [], 0
    for r in rows:
        if r["slug"] not in res or r.get("quote_src") not in GOOD_QUOTES:
            continue
        side, price = r.get(f"{key}_side"), fnum(r.get(f"{key}_price"))
        pnl = bet_pnl(side, price, res[r["slug"]]["winner"], fnum(r.get("fee_rate")))
        if pnl is not None:
            pnls.append(pnl); prices.append(price); wins += side == res[r["slug"]]["winner"]
    s = summarize(pnls, prices, wins)
    if not s:
        return {"n": 0}
    return {"n": s["n"], "hit": round(s["hit"], 4), "breakeven": round(s["avg_price"], 4),
            "pnl": round(s["mean"] * s["n"], 2), "verdict": s["verdict"]}


def main():
    rows = [r for r in read_csv(CHECKS) if (r.get("t_start") or "").isdigit() and r.get("secs_left")]
    if not rows:
        print("no checkpoints yet")
        return
    results = read_csv(RESULTS)
    known = {r["slug"] for r in results}
    slugs = sorted({(r["slug"], r["t_start"]) for r in rows}, key=lambda x: int(x[1]))
    new = fetch_results(slugs, known)
    if new:
        exists = os.path.exists(RESULTS)
        with open(RESULTS, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=RES_FIELDS)
            if not exists:
                w.writeheader()
            w.writerows(new)
        results += new
    print(f"{VERSION} | {len(new)} newly settled windows | {len(results)} total")
    with open(STATS, "w", encoding="utf-8") as f:
        json.dump(jj_stats(rows, results), f)
    with open(os.path.join("data", "safe_stats.json"), "w", encoding="utf-8") as f:
        json.dump(jj_stats(rows, results, "safe"), f)
    report = build_report(rows, results)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    print(report)


if __name__ == "__main__":
    main()
