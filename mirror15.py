"""Mirror: same BTC 15-minute window, two venues, same moment. Read-only, paper research.

At each maker15 decision time (window open + 720s) this records the public top of book on
Kalshi KXBTC15M and on Polymarket US btc-updown-15m for the SAME window, read back to back.
It places nothing, changes nothing in maker15 and writes only data/mirror15/quotes.csv.
It is an observation log, not an experiment: there is no PASS/FAIL rule.

  python mirror15.py live 55     snapshot every decision time for 55 minutes
  python mirror15.py selftest    offline tests of the pure functions
  python mirror15.py summary     print the comparison from the saved files
"""
import csv
import os
import statistics
import sys
import time
from datetime import datetime, timezone

import requests

KALSHI = "https://external-api.kalshi.com/trade-api/v2"   # public, no key
US_GATEWAY = "https://gateway.polymarket.us/v1"           # public, no key
HEADERS = {"User-Agent": "polybot-paper/1 (research, log-only)"}
SERIES = "KXBTC15M"
DECISION_S = 720          # same decision time as maker15 (12:00 elapsed)
WINDOW_S = 900
SNAP_GRACE_S = 30         # only snapshot within 30s of the decision time
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "mirror15")
QUOTES = os.path.join(OUT, "quotes.csv")
ORDERS = os.path.join(HERE, "data", "maker15", "orders.csv")
FIELDS = ["ticker", "open_ts", "decision_ts", "k_ts", "k_up_ask", "k_dn_ask", "k_up_bid", "k_dn_bid", "k_target",
          "pm_slug", "pm_ts", "pm_status", "pm_src", "pm_up_ask", "pm_dn_ask", "pm_up_bid", "pm_dn_bid",
          "pm_up_size", "pm_dn_size", "pm_ptb", "pm_fee", "pm5_slug", "pm5_fee", "gap_s", "logged_utc"]


def num(x):
    if isinstance(x, dict):
        x = x.get("value")
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v


def ok(p):
    return p if p is not None and 0 < p < 1 else None


def pm_event_slug(open_ts):
    return "btc-updown-15m-" + datetime.fromtimestamp(int(open_ts), timezone.utc).strftime("%Y-%m-%d-%H%Mz")


def ts(iso):
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def get(s, url, params=None):
    try:
        return s.get(url, params=params, headers=HEADERS, timeout=8)
    except Exception as e:
        print(f"  GET failed {url.split('/v')[0]}: {e.__class__.__name__}")
        return None


def pm_quote(s, open_ts):
    """Polymarket US quote for the same 15m window. bbo first, book as fallback (same as agent.py)."""
    out = {"pm_slug": pm_event_slug(open_ts), "pm_status": "", "pm_src": ""}
    r = get(s, f"{US_GATEWAY}/events/slug/{out['pm_slug']}")
    if r is None or r.status_code != 200:
        out["pm_status"] = f"event_{getattr(r, 'status_code', 'none')}"
        return out
    try:
        m = r.json()["event"]["markets"][0]
    except Exception:
        out["pm_status"] = "event_parse"
        return out
    terms = m.get("assetPriceTerms") or {}
    out["pm_ptb"] = num(terms.get("priceToBeat")) or ""
    out["pm_fee"] = num(m.get("feeCoefficient")) or ""
    mkt = m.get("slug")
    r = get(s, f"{US_GATEWAY}/markets/{mkt}/bbo")
    if r is not None and r.status_code == 200:
        try:
            d = r.json()["marketData"]
            ba = num(d.get("bestAsk"))
            out.update(pm_src="bbo", pm_up_ask=ok(num(d.get("longQuote"))), pm_dn_ask=ok(num(d.get("shortQuote"))),
                       pm_up_bid=ok(num(d.get("bestBid"))), pm_dn_bid=ok(round(1 - ba, 4)) if ba else None,
                       pm_up_size=num(d.get("askShares")), pm_dn_size=num(d.get("bidShares")))
        except Exception:
            out["pm_src"] = ""
    if not out["pm_src"]:
        r = get(s, f"{US_GATEWAY}/markets/{mkt}/book")
        if r is None or r.status_code != 200:
            out["pm_status"] = f"quote_{getattr(r, 'status_code', 'none')}"
            return out
        try:
            d = r.json()["marketData"]
            offers = sorted((num(x.get("px")), num(x.get("qty"))) for x in d.get("offers") or [] if num(x.get("px")) is not None)
            bids = sorted(((num(x.get("px")), num(x.get("qty"))) for x in d.get("bids") or [] if num(x.get("px")) is not None),
                          key=lambda t: -t[0])
            ua, us_ = offers[0] if offers else (None, None)
            ub, bs = bids[0] if bids else (None, None)
            out.update(pm_src="book", pm_up_ask=ok(ua), pm_up_bid=ok(ub), pm_up_size=us_, pm_dn_size=bs,
                       pm_dn_ask=ok(round(1 - ub, 4)) if ub else None, pm_dn_bid=ok(round(1 - ua, 4)) if ua else None)
        except Exception:
            out["pm_status"] = "quote_parse"
            return out
    out["pm_status"] = "ok" if (out.get("pm_up_ask") or out.get("pm_dn_ask")) else "no_quote"
    return out


def pm5_fee(s, now):
    """Read-only: feeCoefficient of the current Polymarket US BTC 5m market (the 5m bot scores with 0.095)."""
    t5 = now // 300 * 300
    slug = "btc-updown-5m-" + datetime.fromtimestamp(t5, timezone.utc).strftime("%Y-%m-%d-%H%Mz")
    r = get(s, f"{US_GATEWAY}/events/slug/{slug}")
    try:
        return {"pm5_slug": slug, "pm5_fee": num(r.json()["event"]["markets"][0].get("feeCoefficient")) or ""}
    except Exception:
        return {"pm5_slug": slug, "pm5_fee": ""}


def fee_set(quotes, key):
    return sorted({num(q.get(key)) for q in quotes if num(q.get(key)) is not None})


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    os.makedirs(OUT, exist_ok=True)
    with open(QUOTES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in FIELDS})


def live(minutes):
    s = requests.Session()
    rows = {r["ticker"]: r for r in load(QUOTES)}
    stop = time.time() + 60 * minutes
    print(f"mirror live: {minutes} min, {len(rows)} snapshots on file")
    while time.time() < stop:
        now = time.time()
        r = get(s, f"{KALSHI}/markets", {"series_ticker": SERIES, "status": "open", "limit": 50})
        opens = r.json().get("markets", []) if r is not None and r.status_code == 200 else []
        for m in opens:
            try:
                o, c = ts(m["open_time"]), ts(m["close_time"])
            except Exception:
                continue
            T = o + DECISION_S
            if c - o != WINDOW_S or m["ticker"] in rows or not T <= now < T + SNAP_GRACE_S:
                continue
            k_ts = time.time()                         # Kalshi read: re-fetch this market right now
            km = get(s, f"{KALSHI}/markets/{m['ticker']}")
            km = (km.json().get("market") if km is not None and km.status_code == 200 else None) or m
            row = {"ticker": m["ticker"], "open_ts": o, "decision_ts": T, "k_ts": round(k_ts, 2),
                   "k_up_ask": ok(num(km.get("yes_ask_dollars"))), "k_dn_ask": ok(num(km.get("no_ask_dollars"))),
                   "k_up_bid": ok(num(km.get("yes_bid_dollars"))), "k_dn_bid": ok(num(km.get("no_bid_dollars"))),
                   "k_target": num(km.get("floor_strike"))}
            pm_ts = time.time()
            row |= pm_quote(s, o)
            row["pm_ts"] = round(pm_ts, 2)
            row["gap_s"] = round(pm_ts - k_ts, 2)
            row |= pm5_fee(s, int(time.time()))      # fee check only: the live 5m market's feeCoefficient
            row["logged_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            rows[m["ticker"]] = row
            save(list(rows.values()))
            print(f"  {m['ticker']} kalshi up/dn {row['k_up_ask']}/{row['k_dn_ask']} · "
                  f"polymarket {row['pm_status']} {row.get('pm_up_ask')}/{row.get('pm_dn_ask')} · gap {row['gap_s']}s")
        nxt = min([ts(m["open_time"]) + DECISION_S for m in opens if ts(m["open_time"]) + DECISION_S > now] or [now + 30])
        time.sleep(max(2, min(30, nxt - time.time() + 1)))


def compare(quotes, orders):
    """Pure. Pairs both venues' asks at the same decision time.
    diff = Polymarket ask - Kalshi ask for the side maker15 chose (negative = Polymarket cheaper).
    Fees differ per venue; this is the quoted price before fees."""
    side_of = {o["ticker"]: o.get("side") for o in orders if o.get("side") in ("Up", "Down")}
    pairs, both_up, missing = [], [], {}
    for q in quotes:
        if q.get("pm_status") != "ok":
            missing[q.get("pm_status") or "blank"] = missing.get(q.get("pm_status") or "blank", 0) + 1
            continue
        ku, pu = num(q.get("k_up_ask")), num(q.get("pm_up_ask"))
        if ku is not None and pu is not None:
            both_up.append(pu - ku)
        side = side_of.get(q["ticker"])
        if side:
            k = num(q.get("k_up_ask" if side == "Up" else "k_dn_ask"))
            p = num(q.get("pm_up_ask" if side == "Up" else "pm_dn_ask"))
            if k is not None and p is not None:
                pairs.append({"ticker": q["ticker"], "side": side, "k": k, "pm": p, "diff": round(p - k, 4),
                              "gap_s": num(q.get("gap_s"))})
    diffs = [p["diff"] for p in pairs]
    gaps = [num(q.get("gap_s")) for q in quotes if num(q.get("gap_s")) is not None]
    res = {"snapshots": len(quotes), "pm_ok": len(quotes) - sum(missing.values()), "missing": missing,
           "pairs": len(pairs), "up_pairs": len(both_up),
           "up_diff_median": round(statistics.median(both_up), 4) if both_up else None,
           "side_diff_median": round(statistics.median(diffs), 4) if diffs else None,
           "side_diff_mean": round(statistics.mean(diffs), 4) if diffs else None,
           "pm_cheaper": sum(d < 0 for d in diffs), "same": sum(d == 0 for d in diffs), "k_cheaper": sum(d > 0 for d in diffs),
           "abs_ge_5c": sum(abs(d) >= 0.05 for d in diffs),
           "gap_max": max(gaps) if gaps else None, "fee15": fee_set(quotes, "pm_fee"), "fee5": fee_set(quotes, "pm5_fee")}
    return res


def summary_lines(res):
    if not res["snapshots"]:
        return ["Live comparison: no snapshots yet (collector runs alongside each maker15 run)."]
    L = [f"Live snapshots at the maker decision time: {res['snapshots']} · Polymarket US quote found: {res['pm_ok']}"
         + (f" · missing {res['missing']}" if res["missing"] else ""),
         f"Same moment: the two reads are at most {res['gap_max']}s apart." if res["gap_max"] is not None else ""]
    if res["pairs"]:
        L += [f"Maker's chosen side, ask on both venues: {res['pairs']} pairs · Polymarket minus Kalshi: median "
              f"{res['side_diff_median'] * 100:+.1f}c, mean {res['side_diff_mean'] * 100:+.1f}c · Polymarket cheaper "
              f"{res['pm_cheaper']}, same {res['same']}, Kalshi cheaper {res['k_cheaper']} · gaps of 5c or more: {res['abs_ge_5c']}",
              "Quoted prices before fees. Small sample: descriptive only, no PASS/FAIL rule."]
    if res.get("fee15"):
        L.append(f"Polymarket US feeCoefficient seen live: 15m {res['fee15']}"
                 + (f" · 5m {res['fee5']}" if res.get("fee5") else " · 5m not read yet")
                 + " (the 5m bot scores with 0.095)")
    return [x for x in L if x]


def selftest():
    assert pm_event_slug(1795703400) == "btc-updown-15m-2026-11-26-1430z", pm_event_slug(1795703400)
    assert ok(0.0) is None and ok(1.0) is None and ok(0.42) == 0.42 and num({"value": "0.5"}) == 0.5
    q = [{"ticker": "A", "pm_status": "ok", "k_up_ask": "0.40", "k_dn_ask": "0.61", "pm_up_ask": "0.37", "pm_dn_ask": "0.64", "gap_s": "0.4", "pm_fee": "0.11", "pm5_fee": "0.095"},
         {"ticker": "B", "pm_status": "ok", "k_up_ask": "0.70", "k_dn_ask": "0.31", "pm_up_ask": "0.72", "pm_dn_ask": "0.30", "gap_s": "0.6"},
         {"ticker": "C", "pm_status": "event_404", "k_up_ask": "0.5", "k_dn_ask": "0.5", "gap_s": "0.2"},
         {"ticker": "D", "pm_status": "ok", "k_up_ask": "0.55", "k_dn_ask": "0.46", "pm_up_ask": "0.55", "pm_dn_ask": "0.46", "gap_s": "0.3"},
         {"ticker": "E", "pm_status": "ok", "k_up_ask": "0.50", "k_dn_ask": "0.51", "pm_up_ask": "0.50", "pm_dn_ask": "0.52", "gap_s": "0.5"}]
    o = [{"ticker": "A", "side": "Up"}, {"ticker": "B", "side": "Down"}, {"ticker": "C", "side": "Up"}, {"ticker": "D", "side": ""},
         {"ticker": "E", "side": "Up"}]
    r = compare(q, o)
    assert r["snapshots"] == 5 and r["pm_ok"] == 4 and r["missing"] == {"event_404": 1}, r
    assert r["pairs"] == 3 and r["pm_cheaper"] == 2 and r["same"] == 1 and r["k_cheaper"] == 0, r   # A, B cheaper; E tie
    assert r["side_diff_median"] == -0.01 and r["up_pairs"] == 4 and r["gap_max"] == 0.6, r
    assert compare([], [])["snapshots"] == 0 and "no snapshots" in summary_lines(compare([], []))[0]
    assert any("3 pairs" in x for x in summary_lines(r))
    assert r["fee15"] == [0.11] and r["fee5"] == [0.095], r
    assert any("15m [0.11] · 5m [0.095]" in x for x in summary_lines(r)), summary_lines(r)
    print("MIRROR SELFTEST OK")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "live":
        live(float(sys.argv[2]) if len(sys.argv) > 2 else 55)
    elif cmd == "selftest":
        selftest()
    else:
        print("\n".join(summary_lines(compare(load(QUOTES), load(ORDERS)))))
