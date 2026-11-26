---
polybot_auto: true
updated: 2026-11-26 01:27 UTC
tags: [experiment, experiment/15m, status/negative]
---
# 🕒 15-Minute '12-Minute Rule', Phase 1

> [!failure] Phase 1 finished: negative (exploratory)
> The rule lost money after fees on 6,454 historical Kalshi rounds. Phase 2 is NOT approved. Decision pending with Jacob.

## Pre-registration (frozen before results)
# Phase 1 pre-registration: the "12-minute rule" on Kalshi BTC 15m (exploratory)

Frozen 2026-11-25 ~00:30Z, before any 15m result was computed. Approved by ChatGPT (primary = AGREE).
Changing anything below after results exist = a new, separately labelled analysis.

## Data (public, no key, $0)
- Markets: every settled Kalshi `KXBTC15M` market the public API returns. No date filtering, no exclusions
  except the data-quality rules below (each exclusion is counted and reported).
- Contract prices: Kalshi 1-minute candlesticks per market (`yes_ask`, `yes_bid` OHLC). ASK prices only, never mid.
- BTC: Coinbase BTC-USD 1-minute candles (public). Note: settlement uses CF Benchmarks BRTI, not Coinbase.
- Fees: Kalshi taker fee = round up to the next cent of `M x 0.07 x C x P x (1-P)` per order, M = the series
  fee multiplier read from the public `/series/KXBTC15M` endpoint (current value; historical changes are not
  modelled, so results are also shown at 0x and 1.5x the fee).

## Decision rule (no look-ahead)
- Window = [open_time, open_time + 900s). Decision time T = open_time + 720s (12:00 elapsed, 3:00 left).
- Target = `floor_strike` (the window's start price, shown as "Target Price" during the window).
- BTC_T = close of the Coinbase 1m candle covering [T-60, T). BTC_T-60 = close of the candle covering [T-120, T-60).
- LEAN = Up if BTC_T >= Target else Down.
- MOMENTUM = Up if BTC_T > BTC_T-60, Down if lower, none if equal.
- **PRIMARY = AGREE: trade only if LEAN and MOMENTUM point the same way.** One trade per window max.
- Secondary (reported, multiple-testing warning, cannot confirm anything): LEAN-only, MOMENTUM-only.

## Entry (ask only)
- Primary entry: the chosen side's ask at the close of the Kalshi candle covering [T, T+60): about 60s after
  the decision (conservative human delay). Up ask = `yes_ask.close`; Down ask = 1 - `yes_bid.close`.
- Secondary entry: same candle's open (about 0s delay), to show the cost of waiting.
- A quote is usable only if 0.01 < ask < 0.99; otherwise "no usable quote" (counted, no trade).
- Size: $10 per trade. Contracts C = floor(10 / ask). Fee per order as above.
- P&L: win = C x (1 - ask) - fee; loss = -C x ask - fee. Held to settlement (no exit fee).

## Outcome
- Kalshi `result` (yes = Up). Cross-checked against expiration_value >= floor_strike; mismatches counted.

## Reported (all of it, no cherry-picking)
- Trades, win rate vs break-even (ask + fee per contract), P&L after fees, mean per trade with 95% CI,
  z-test of wins vs break-even, max drawdown, longest losing streak.
- Missing data by cause. Results by week, by chronological half, by BTC volatility tercile (prior 60 min,
  known at T), by hour-of-day session, and by entry-price bucket.
- Cross-platform check: Kalshi target/settlement vs Polymarket US 15m priceToBeat/settlementPrice for the
  same windows (both BRTI 60s averages), winner agreement.

## Status
Exploratory only. It cannot prove profitability. Confirmation = Phase 2 forward paper test (300 trades).


## Result summary
| Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|
| 2022 | 78.1% | 80.9% | -632.13 | -0.313 (-0.713 to +0.088) | -3.85 | -768.38 | 4 |

- Windows where LEAN and MOMENTUM disagreed (no trade): 2694 · momentum flat: 121 · signal but no usable ask (<=1c or >=99c): 1617

Full report: [[15-Minute Phase 1 Report]] · Strategy: see [[Strategy Library]] (#1)

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
