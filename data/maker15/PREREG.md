# Pre-registration: maker (limit-order) paper test on Kalshi BTC 15m

Frozen before any result. Requested by Jacob 2026-11-26. Separate from the 5m v18 experiment (agent.py, grade.py)
and the 15m Phase 1 backtest (backtest15.py); neither is changed. Paper only: nothing places orders, no keys.
Changing anything below after results exist = a new, separately labelled test.

## Data (public, no key, $0)
- Markets: Kalshi `KXBTC15M`, read live from the public API (`/markets`, `/markets/{ticker}`).
- Fills: Kalshi public trade prints (`/markets/trades`: price, size, time, block flag).
- BTC: Coinbase BTC-USD 1-minute candles (signal only).

## Order rule (no look-ahead)
- One order per 15-minute window, posted at 12:00 elapsed (3:00 left). Live: only if posted within 60s of that time.
- Side = the Phase 1 AGREE signal: LEAN (BTC vs the window's target) and MOMENTUM (last 1m BTC move) agree. No agreement = no order.
- Limit = the chosen side's current ask minus 2 cents (a resting buy below the ask). Up ask = yes ask, Down ask = no ask.
  No order if the ask is outside 0.01 to 0.99 or the limit would be under 0.02.
- Size: $10. Contracts = floor(10 / limit).

## Fill rule (strict)
- Filled only if on-book trades (block trades excluded) after the order time and before the close printed
  STRICTLY better than the limit for a seller (our side's price below the limit; touching does not count),
  and those prints add up to at least our full size. Less than full size = PARTIAL, not counted.
- Unfilled orders cancel at the close. Filled orders are held to settlement (no exit fee).

## Fees
- Kalshi fee schedule (effective 2026-07-07): resting orders pay a maker fee of round-up(M x 0.0175 x C x P x (1-P))
  only on series in its Maker Fees list. KXBTC15M is not listed, and its series `fee_type` read "quadratic" in Phase 1.
  The script re-reads `fee_type` at grading time and applies the maker fee if the series ever gains one.
- Every result is also shown as if the 0.0175 maker fee applied (stress line, not the verdict).

## Scoring and verdict
- Report: orders, fills, fill rate, partial-only, win rate of fills, break-even (limit + fee per contract),
  P&L after fees, and the win rate of orders that never filled (adverse-selection check).
- Verdict on the first 100 live fills by order time, then frozen: PASSED only if win rate >= average break-even + 3 points.
  Otherwise FAILED.
- A historical replay (`python maker15.py replay N`) may be run as an exploratory preview. It uses 1-minute candle
  quotes, is reported separately and never counts toward the verdict.
