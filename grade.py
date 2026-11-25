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
VERSION = "polybot grader v7"

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


def breakeven(price, fee_rate=None):
    """Win rate needed to break even at this price AFTER the taker fee: cost per share = price + fee."""
    fr = fee_rate if fee_rate is not None else FEE_RATE
    return price + fr * price * (1 - price)


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
             f"{SHARES} shares per bet. Breakeven = win rate needed after the fee (price + fee).", ""]
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
                    prices.append(breakeven(price, fnum(r.get("fee_rate"))))
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
    best, info = fit_sigma(graded, res)
    tune = tune_lines(best, info)
    lines += calibration_lines(graded, res) + ["", "## Model tuning", ""] + tune + honest_lines() + latency_lines() + loop_lines() + team_lines()
    lines += ["", f"_{VERSION}_"]
    return "\n".join(lines)


def jj_stats(rows, results, key="jj"):
    res = {r["slug"]: r for r in results}
    pnls, prices, wins, seen = [], [], 0, set()
    for r in sorted(rows, key=lambda r: -fnum(r.get("secs_left")) if fnum(r.get("secs_left")) is not None else 0):
        if r["slug"] not in res or r.get("quote_src") not in GOOD_QUOTES or r["slug"] in seen:
            continue
        side, price = r.get(f"{key}_side"), fnum(r.get(f"{key}_price"))
        pnl = bet_pnl(side, price, res[r["slug"]]["winner"], fnum(r.get("fee_rate")))
        if pnl is not None:                                # one bet per market: checkpoints in a round aren't independent
            seen.add(r["slug"])
            pnls.append(pnl); prices.append(breakeven(price, fnum(r.get("fee_rate")))); wins += side == res[r["slug"]]["winner"]
    s = summarize(pnls, prices, wins)
    if not s:
        return {"n": 0}
    return {"n": s["n"], "hit": round(s["hit"], 4), "breakeven": round(s["avg_price"], 4),
            "pnl": round(s["mean"] * s["n"], 2), "verdict": s["verdict"]}


TUNE = os.path.join("data", "model_tune.json")
TUNE_MIN_MARKETS = 60              # train markets needed before a fit is even tried (plus half that to test)
DEFAULT_MULT = 1.4
US_FEE = 0.095                     # tickets are Polymarket US: feeCoefficient 0.095


def split_markets(graded, train_frac=0.7):
    """Chronological split BY MARKET: the oldest 70% of rounds train, the newest 30% test.
    All checkpoints of one round stay on the same side, so nothing leaks between them."""
    start = {}
    for r in graded:
        t = fnum(r.get("t_start"))
        if t is not None:
            start[r["slug"]] = min(t, start.get(r["slug"], t))
    order = sorted(start, key=start.get)
    cut = int(len(order) * train_frac)
    return set(order[:cut]), set(order[cut:])


def fit_sigma(graded, res):
    """Fit the volatility multiplier on OLD markets, judge it only on NEW markets it never saw.
    It replaces the default only if it beats the default out of sample."""
    import agent
    train_s, test_s = split_markets(graded)
    def rows_for(slugs):
        out = []
        for r in graded:
            if r["slug"] not in slugs:
                continue
            spot, ptb, sig, left = fnum(r.get("spot")), fnum(r.get("ptb_proxy")), fnum(r.get("sigma")), fnum(r.get("secs_left"))
            if None in (spot, ptb, sig, left):
                continue
            mid = None
            ua, ub = fnum(r.get("up_ask")), fnum(r.get("up_bid"))
            if ua is not None:
                mid = (ua + ub) / 2 if ub is not None else ua
            out.append((spot, ptb, sig, left, 1.0 if res[r["slug"]]["winner"] == "Up" else 0.0, mid))
        return out
    train, test = rows_for(train_s), rows_for(test_s)
    info = {"train_markets": len(train_s), "test_markets": len(test_s), "train_rows": len(train), "test_rows": len(test)}
    if len(train_s) < TUNE_MIN_MARKETS or len(test_s) < TUNE_MIN_MARKETS // 2:
        with open(TUNE, "w", encoding="utf-8") as f:           # overwrite any old in-sample fit with the default
            json.dump({"sigma_mult": DEFAULT_MULT, "adopted": False, "reason": "not enough markets", **info}, f)
        return None, info
    score = lambda rows, k: sum((agent.model_p_up(sp, pt, sg, lf, mult=k, cap=agent.PROB_CAP) - y) ** 2
                                for sp, pt, sg, lf, y, _ in rows) / len(rows)
    best_k = min((x / 10 for x in range(8, 31)), key=lambda k: score(train, k))
    info.update(fit=best_k, test_brier_fit=round(score(test, best_k), 4),
                test_brier_default=round(score(test, DEFAULT_MULT), 4))
    mk = [(m, y) for *_, y, m in test if m is not None]
    info["test_brier_market"] = round(brier(mk), 4) if mk else None
    info["adopted"] = info["test_brier_fit"] < info["test_brier_default"]
    with open(TUNE, "w", encoding="utf-8") as f:
        json.dump({"sigma_mult": best_k if info["adopted"] else DEFAULT_MULT, **info}, f)
    return best_k, info


def tune_lines(best, info):
    out = [f"- Split by market, oldest first: train {info['train_markets']} markets ({info['train_rows']} checks), "
           f"test {info['test_markets']} markets ({info['test_rows']} checks). Test markets are never used for fitting."]
    if best is None:
        out.append(f"- Not fitted yet: needs {TUNE_MIN_MARKETS} train + {TUNE_MIN_MARKETS // 2} test markets. "
                   f"Default volatility x{DEFAULT_MULT} stays.")
        return out
    out.append(f"- Fitted on train: x{best}. Out-of-sample Brier (lower is better): fitted {info['test_brier_fit']}, "
               f"default x{DEFAULT_MULT} {info['test_brier_default']}, market {info['test_brier_market']}.")
    out.append("- " + ("Fitted value adopted: it beat the default on unseen markets." if info["adopted"]
                       else "Fit REJECTED: it did not beat the default on unseen markets."))
    return out


def calibration_lines(graded, res):
    """Is the model honest? 'When it said 85-95%, it won X%'. Uses the favored side's probability."""
    buckets = [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.01)]
    out = ["", "## Is the win chance honest? (calibration)", "",
           "| Bot said | Checks | Separate markets | Said (avg) | Actually won |", "|---|---|---|---|---|"]
    for lo, hi in buckets:
        hits = n = 0
        said, slugs = 0.0, set()
        for r in graded:
            mu = fnum(r.get("model_up"))
            if mu is None:
                continue
            p, side = (mu, "Up") if mu >= 0.5 else (1 - mu, "Down")
            if lo <= p < hi:
                n += 1
                said += p
                slugs.add(r["slug"])
                hits += res[r["slug"]]["winner"] == side
        if n:
            out.append(f"| {lo:.0%}-{min(hi, 1):.0%} | {n} | {len(slugs)} | {said / n:.0%} | {hits / n:.0%} |")
    out.append("")
    out.append("These are the live predictions as logged before each round settled, so they are out of sample.")
    out.append("Checks in one market move together: trust 'Separate markets', not 'Checks'.")
    out.append("If 'Actually won' sits well below 'Said', the model is overconfident.")
    return out


def latency_lines():
    """Ticket speed, measured stage by stage, and what each human reaction time would have made."""
    rows = read_csv(os.path.join("data", "tickets.csv"))
    rows = [r for r in rows if r.get("t_sent")]
    if not rows:
        return ["", "## Ticket speed", "", "No v10 tickets yet."]
    med = lambda xs: sorted(xs)[len(xs) // 2] if xs else None
    num = lambda r, k: float(r[k]) if r.get(k) not in (None, "") else None
    col = lambda k: [v for v in (num(r, k) for r in rows) if v is not None]
    stage = lambda a, b: [num(r, b) - num(r, a) for r in rows if num(r, a) and num(r, b)]
    out = ["", "## Ticket speed (measured, not assumed)", "", f"- Tickets: {len(rows)}"]
    for label, xs, unit in (
            ("Coinbase trade -> we received it", col("spot_lag_ms"), "ms"),
            ("Coinbase request round trip", col("spot_rtt_ms"), "ms"),
            ("Polymarket quote round trip", col("quote_rtt_ms"), "ms"),
            ("Price read -> decision made", [x * 1000 for x in stage("t_spot", "t_decide")], "ms"),
            ("Decision -> Discord accepted", [x * 1000 for x in stage("t_decide", "t_sent")], "ms")):
        if xs:
            out.append(f"- {label}: median {med(xs):.0f} {unit} (worst {max(xs):.0f})")
    left = col("secs_left_sent")
    if left:
        out.append(f"- Time left on the timer when sent: median {med(left):.0f}s")
    late = [num(r, f"ask_{k}_at") - k for r in rows for k in (5, 10, 20, 30) if num(r, f"ask_{k}_at") is not None]
    if late:
        out.append(f"- Price checks ran late by: median {med(late):.1f}s (over 3s = not trusted for a fill)")
    graded = [r for r in rows if r.get("result") in ("WIN", "LOSS", "MISSED") and r.get("status_30")]
    if graded:
        out += ["", "| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |", "|---|---|---|---|---|"]
        for d in (5, 10, 20, 30):
            st = [r.get(f"status_{d}") for r in graded]
            pnl = sum(float(r.get(f"pnl10_{d}") or 0) for r in graded)
            out.append(f"| {d}s | {st.count('FILLABLE')}/{len(st)} | {st.count('EXPIRED')} | "
                       f"{st.count('UNCONFIRMED')} | {pnl:+.2f} |")
        out.append("- Simulated quote availability, not verified fills: size at the ask is not known yet.")
        out.append("- Expired or unconfirmed = no trade.")
    return out


def honest_lines():
    """Scoreboard ChatGPT asked for: P&L after fees, win rate vs break-even, drawdown, independent markets."""
    rows = read_csv(os.path.join("data", "tickets.csv"))
    done = [r for r in rows if r.get("result") in ("WIN", "LOSS", "MISSED")]
    out = ["", "## Honest scoreboard (tickets)", ""]
    if not done:
        return out + ["No settled tickets yet."]
    trades = [r for r in done if r["result"] in ("WIN", "LOSS")]
    wins = sum(r["result"] == "WIN" for r in trades)
    eq = peak = dd = 0.0
    for r in sorted(trades, key=lambda r: int(r["t_start"])):
        eq += float(r.get("pnl10") or 0)
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    be = [breakeven(float(r["fill_price"]), US_FEE) for r in trades if r.get("fill_price")]
    out += [f"- Independent settled markets with a ticket: {len({r['slug'] for r in done})} (goal: 300)",
            f"- Simulated paper trades: {len(trades)} · no-trade (expired/unconfirmed): {len(done) - len(trades)}",
            "- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,",
            "  so this is simulated quote availability, not a proven fill.",
            f"- Win rate {wins}/{len(trades)}" + (f" = {wins / len(trades):.0%}" if trades else "") +
            (f" vs break-even {sum(be) / len(be):.1%} (price paid + fee)" if be else ""),
            f"- Paper P&L after fees: {eq:+.2f} at $10 a trade · max drawdown: -{dd:.2f}"]
    return out


def loop_lines():
    """Blocking network calls stall the 2s loop; stalls make price checks and timings late."""
    rows = read_csv(os.path.join("data", "loop_stats.csv"))
    out = ["", "## Loop health (are our timings trustworthy?)", ""]
    if not rows:
        return out + ["No loop stats yet (v15+)."]
    n = lambda k: [float(r[k]) for r in rows if r.get(k) not in (None, "")]
    ticks, stalls = sum(n("ticks")), sum(n("stalls_5s"))
    worst = {}
    for r in rows:
        if r.get("worst_part"):
            worst[r["worst_part"]] = worst.get(r["worst_part"], 0) + 1
    out += [f"- Runs: {len(rows)} · loops: {ticks:.0f} · loops over 5s: {stalls:.0f} ({stalls / ticks:.2%})" if ticks else "",
            f"- Worst single loop: {max(n('max_ms')) / 1000:.1f}s · longest gap between BTC prices: {max(n('max_spot_gap_s')):.1f}s",
            f"- Most common stall cause: {max(worst, key=worst.get)}" if worst else "- No stalls recorded.",
            "- A tick or price check during a stall is late; price checks over 3s late never count as a fill."]
    return out


def team_lines():
    """Is Gemini's second opinion worth listening to? Compare tickets it agreed with vs passed on."""
    rows = [r for r in read_csv(os.path.join("data", "tickets.csv"))
            if r.get("ai_verdict") in ("AGREE", "PASS") and r.get("result") in ("WIN", "LOSS")]
    out = ["", "## Gemini second opinion", ""]
    if not rows:
        return out + ["No graded tickets with a Gemini opinion yet."]
    for v in ("AGREE", "PASS"):
        g = [r for r in rows if r["ai_verdict"] == v]
        if g:
            w = sum(r["result"] == "WIN" for r in g)
            pnl = sum(float(r.get("pnl10") or 0) for r in g)
            out.append(f"- Gemini said {v}: {len(g)} tickets, won {w} ({w / len(g):.0%}), $10 each = {pnl:+.2f}")
    out.append("- If PASS tickets lose money and AGREE tickets make money, Gemini is adding value.")
    return out


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
