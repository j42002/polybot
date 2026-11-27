"""Read-only QC audit of the maker15 paper test (ChatGPT QC review, PR #9, 2026-11-27).

Does NOT change maker15.py, its rules, data/maker15/ or any result. Writes only data/maker15_audit/.
  python audit_maker15.py           integrity audit (re-fetches public Kalshi trades) + statistics
  python audit_maker15.py stats     statistics only (offline, from data/maker15/orders.csv)

Integrity checks per posted order (FILLED / UNFILLED / PARTIAL):
  - trades re-fetched for [order_ts-120s, close] with NO page cap; flags any incomplete pagination
  - duplicate trade IDs, wrong ticker, block trades, out-of-order timestamps
  - fill status recomputed on the deduplicated list (same rule as maker15.check_fill) vs the recorded status
  - quote staleness: last on-book print before the order vs the recorded ask/bid; flags orders that would have
    been marketable (a print below our limit just before posting = we might have been a taker, not a maker)
  - series fee terms re-read (fee_type, fee_multiplier, every field with "fee" in its name)
Statistics: P&L per POSTED order (unfilled = $0), contract-weighted win vs break-even, fill rate conditional on
the outcome, the same orders as taker buys at the ask, splits by price and time, block-bootstrap uncertainty.
"""
import csv
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

import maker15 as M

OUT = os.path.join("data", "maker15_audit")
TAKER_RATE = 0.07          # Kalshi taker coefficient (quadratic), used only for the taker counterfactual
random.seed(7)


def utc(t):
    return datetime.fromtimestamp(int(t), timezone.utc).strftime("%Y-%m-%d %H:%M")


def et_hour(t):
    return (datetime.fromtimestamp(int(t), timezone.utc).hour - 5) % 24          # US Eastern (EST), Nov


def fetch_trades(ticker, start, end, max_pages=500):
    """All public trades, no artificial cap. Returns (trades, pages, complete, error)."""
    out, cursor, pages = [], "", 0
    while pages < max_pages:
        p = {"ticker": ticker, "min_ts": int(start), "max_ts": int(end), "limit": 1000}
        if cursor:
            p["cursor"] = cursor
        r = M.get(f"{M.KALSHI}/markets/trades", p)
        if r is None or r.status_code != 200:
            return out, pages, False, f"HTTP {getattr(r, 'status_code', 'none')}"
        j = r.json()
        pages += 1
        out += j.get("trades", [])
        cursor = j.get("cursor")
        if not cursor or not j.get("trades"):
            return out, pages, True, ""
        time.sleep(0.1)
    return out, pages, False, f"stopped at {max_pages} pages"


def series_fee_fields():
    r = M.get(f"{M.KALSHI}/series/{M.SERIES}")
    try:
        s = r.json()["series"]
        return {k: s[k] for k in s if "fee" in k.lower()}
    except Exception as e:
        return {"error": str(e)}


def audit_order(r):
    o, c = int(r["order_ts"]), int(r["close_ts"])
    side, lim, n = r["side"], float(r["limit"]), int(r["contracts"])
    trades, pages, complete, err = fetch_trades(r["ticker"], o - 120, c)
    ids = [t.get("trade_id") for t in trades]
    dup = len(ids) - len(set(ids))
    seen, uniq = set(), []
    for t in trades:
        k = t.get("trade_id")
        if k in seen:
            continue
        seen.add(k)
        uniq.append(t)
    wrong_ticker = sum(t.get("ticker") not in (None, r["ticker"]) for t in uniq)
    blocks = sum(bool(t.get("is_block_trade")) for t in uniq)
    tts = [M.ts(t["created_time"]) for t in uniq]
    ordered = tts == sorted(tts) or tts == sorted(tts, reverse=True)
    status, vol, first = M.check_fill(uniq, side, lim, n, o, c)
    before = [(M.ts(t["created_time"]), M.side_price(t, side)) for t in uniq
              if not t.get("is_block_trade") and o - 120 <= M.ts(t["created_time"]) <= o]
    before = [x for x in before if x[1] is not None]
    last_px = max(before)[1] if before else None
    last_age = (o - max(before)[0]) if before else None
    ask = M.num(r["ask"])
    flags = []
    if not complete:
        flags.append("INCOMPLETE_PAGES")
    if dup:
        flags.append(f"DUP_IDS:{dup}")
    if wrong_ticker:
        flags.append("WRONG_TICKER")
    if not ordered:
        flags.append("UNORDERED")
    if status != r["status"]:
        flags.append(f"STATUS_MISMATCH:{r['status']}->{status}")
    if last_px is not None and last_px < lim - 1e-9:
        flags.append("MARKETABLE_AT_POST")          # market already traded below our limit: we may have been a taker
    if last_px is not None and ask is not None and abs(last_px - ask) > 0.05:
        flags.append("QUOTE_FAR_FROM_LAST_PRINT")
    return {"ticker": r["ticker"], "status": r["status"], "recomputed": status, "pages": pages,
            "complete": int(complete), "error": err, "trades": len(uniq), "dup_ids": dup, "blocks": blocks,
            "through_vol_recorded": r["through_vol"], "through_vol_recomputed": round(vol, 2),
            "contracts": n, "ask": r["ask"], "limit": lim, "last_print_before": last_px,
            "last_print_age_s": last_age, "first_through_s": (first - o) if first else "",
            "flags": ";".join(flags)}


# ---------------- statistics (offline) ----------------

def taker_pnl(r):
    ask = M.num(r["ask"])
    if ask is None or not 0 < ask < 1:
        return None
    n = math.floor(M.STAKE / ask + 1e-9)
    fee = math.ceil(round(100 * float(r["fee_mult"] or 1) * TAKER_RATE * n * ask * (1 - ask), 6)) / 100.0
    return n * (1 - ask) - fee if r["won"] == "1" else -n * ask - fee


def boot_ci(groups, stat, reps=4000):
    """Block bootstrap: resample whole groups (days or 4-hour blocks) with replacement."""
    keys = list(groups)
    if len(keys) < 5:
        return None                                  # fewer than 5 blocks: an interval would be meaningless
    vals = []
    for _ in range(reps):
        sample = [x for k in random.choices(keys, k=len(keys)) for x in groups[k]]
        v = stat(sample)
        if v is not None:
            vals.append(v)
    vals.sort()
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def stats(rows):
    P = [r for r in rows if r["status"] in ("FILLED", "UNFILLED", "PARTIAL")]
    F = [r for r in P if r["status"] == "FILLED"]
    if not P:
        return ["No graded orders yet."]
    pnl_post = lambda rs: sum(float(r["pnl"]) for r in rs if r["status"] == "FILLED") / len(rs) if rs else None
    win_n = sum(r["won"] == "1" for r in P)
    fill_w = sum(1 for r in P if r["won"] == "1" and r["status"] == "FILLED")
    fill_l = sum(1 for r in P if r["won"] == "0" and r["status"] == "FILLED")
    lose_n = len(P) - win_n
    C = sum(int(r["contracts"]) for r in F)
    cw_win = sum(int(r["contracts"]) for r in F if r["won"] == "1") / C
    cw_be = sum(int(r["contracts"]) * float(r["breakeven"]) for r in F) / C
    eq_win = sum(r["won"] == "1" for r in F) / len(F)
    eq_be = sum(float(r["breakeven"]) for r in F) / len(F)
    tot = sum(float(r["pnl"]) for r in F)
    stress = sum(float(r["pnl_stress"]) for r in F)
    tk = [taker_pnl(r) for r in P]
    tk = [x for x in tk if x is not None]
    day = defaultdict(list)
    blk = defaultdict(list)
    for r in P:
        day[utc(r["order_ts"])[:10]].append(r)
        blk[int(r["order_ts"]) // (4 * 3600)].append(r)
    ci_day = boot_ci(day, pnl_post)
    ci_blk = boot_ci(blk, pnl_post)
    losses = sorted(float(r["pnl"]) for r in F if r["won"] == "0")
    eq, peak, mdd = 0.0, 0.0, 0.0
    for r in sorted(F, key=lambda r: int(r["order_ts"])):
        eq += float(r["pnl"])
        peak = max(peak, eq)
        mdd = min(mdd, eq - peak)
    f = lambda ci: f"{ci[0]:+.2f} to {ci[1]:+.2f}" if ci else "not shown (needs 5+ blocks)"
    out = [
        "## Headline numbers (unfilled orders count as $0, never as earned)",
        "",
        f"- Orders posted **{len(P)}** · filled **{len(F)}** · unfilled {len(P) - len(F)} · span {utc(min(int(r['order_ts']) for r in P))} to {utc(max(int(r['order_ts']) for r in P))} UTC ({len(day)} calendar days, {len(blk)} four-hour blocks)",
        f"- **P&L per posted order: {tot / len(P):+.2f}** (total {tot:+.2f} over {len(P)} posted). 95% range by day blocks: {f(ci_day)} · by 4-hour blocks: {f(ci_blk)}",
        f"- P&L per fill: {tot / len(F):+.2f} · if a 0.0175 maker fee applied: total {stress:+.2f}",
        f"- Equal-weight: win {eq_win:.1%} vs break-even {eq_be:.1%} ({100 * (eq_win - eq_be):+.1f} pts)",
        f"- **Contract-weighted: win {cw_win:.1%} vs break-even {cw_be:.1%} ({100 * (cw_win - cw_be):+.1f} pts)** over {C} contracts",
        f"- Worst single loss {losses[0]:+.2f} · max drawdown {mdd:+.2f}" if losses else f"- No losses yet · max drawdown {mdd:+.2f}",
        "",
        "## Adverse selection (fill rate depends on the outcome)",
        "",
        f"- Signal right on {win_n}/{len(P)} posted orders ({win_n / len(P):.0%}).",
        f"- **Fill rate when our side WON: {fill_w}/{win_n} ({fill_w / win_n:.0%}) · when it LOST: {fill_l}/{lose_n} ({(fill_l / lose_n if lose_n else 0):.0%})**",
        "- A resting buy fills when the price falls through it. Losers always fall, so they always fill; many winners never come back down.",
        "",
        "## Same orders, as taker buys at the ask (counterfactual, 0.07 quadratic taker fee)",
        "",
        f"- Taker P&L on the same {len(tk)} posted signals: **{sum(tk):+.2f}** ({sum(tk) / len(tk):+.2f} per order) vs maker {tot:+.2f}",
        "- Shows whether the cheaper price or the signal itself is doing the work. Exploratory, not part of the frozen rule.",
        "",
        "## Splits (exploratory; small cells)",
        "",
        "| Split | posted | filled | win of fills | P&L | P&L / posted |",
        "|---|---|---|---|---|---|",
    ]

    def cell(name, rs):
        fs = [r for r in rs if r["status"] == "FILLED"]
        p = sum(float(r["pnl"]) for r in fs)
        w = f"{sum(r['won'] == '1' for r in fs) / len(fs):.0%}" if fs else "-"
        out.append(f"| {name} | {len(rs)} | {len(fs)} | {w} | {p:+.2f} | {p / len(rs):+.2f} |")

    for lo, hi, name in ((0, 0.6, "ask under 60c"), (0.6, 0.85, "ask 60-85c"), (0.85, 1.0, "ask 85c+")):
        cell(name, [r for r in P if lo <= float(r["ask"]) < hi])
    for lo, hi, name in ((0, 8, "00-08 ET"), (8, 16, "08-16 ET"), (16, 24, "16-24 ET")):
        cell(name, [r for r in P if lo <= et_hour(r["order_ts"]) < hi])
    for d in sorted(day):
        cell(f"day {d}", day[d])
    out += ["", "Small cells: these splits describe the sample, they are not findings. Nothing here changes the frozen rule."]
    return out


def main(online=True):
    os.makedirs(OUT, exist_ok=True)
    rows = M.load(M.ORDERS)
    md = ["# maker15 QC audit (read-only)", "",
          f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from data/maker15/orders.csv. "
          "Does not change maker15.py, its rules or its data. Requested in ChatGPT's QC review (PR #9).", ""]
    if online:
        P = [r for r in rows if r["status"] in ("FILLED", "UNFILLED", "PARTIAL")]
        res = []
        for r in P:
            res.append(audit_order(r))
            time.sleep(0.1)
        with open(os.path.join(OUT, "audit.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(res[0].keys()) if res else ["ticker"])
            w.writeheader()
            w.writerows(res)
        fl = Counter(x.split(":")[0] for r in res for x in r["flags"].split(";") if x)
        errs = [r for r in res if r["error"]]
        mism = [r for r in res if r["status"] != r["recomputed"]]
        ages = sorted(r["last_print_age_s"] for r in res if r["last_print_age_s"] is not None)
        md += ["## Integrity audit", "",
               f"- Orders re-checked: {len(res)} · fetch errors: {len(errs)} · incomplete pagination: {fl.get('INCOMPLETE_PAGES', 0)}",
               f"- Duplicate trade IDs: {sum(r['dup_ids'] for r in res)} · wrong-ticker prints: {fl.get('WRONG_TICKER', 0)} · "
               f"block trades seen (excluded by the rule): {sum(r['blocks'] for r in res)} · unordered pages: {fl.get('UNORDERED', 0)}",
               f"- **Fill status recomputed on deduplicated, complete trade lists: {len(res) - len(mism)}/{len(res)} match the recorded status**"
               + (" · mismatches: " + ", ".join(f"{r['ticker']} {r['status']}->{r['recomputed']}" for r in mism) if mism else ""),
               f"- Marketable at post (a print below our limit in the 2 min before posting, so we might have been a taker): "
               f"**{fl.get('MARKETABLE_AT_POST', 0)}** · recorded ask more than 5c from the last print: {fl.get('QUOTE_FAR_FROM_LAST_PRINT', 0)}",
               f"- Age of the last print before posting (s): median {ages[len(ages) // 2] if ages else 'n/a'}, max {ages[-1] if ages else 'n/a'}",
               f"- Series fee fields now: `{series_fee_fields()}`",
               "", "Per-order detail: data/maker15_audit/audit.csv.", ""]
    md += stats(rows)
    with open(os.path.join(OUT, "audit.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main(online=not (len(sys.argv) > 1 and sys.argv[1] == "stats"))
