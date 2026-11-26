---
polybot_auto: true
updated: 2026-11-26 01:33 UTC
tags: [results, experiment/15m]
---
# 📉 15-Minute Phase 1 Report

# Phase 1 results: 12-minute rule on Kalshi BTC 15m (EXPLORATORY)

Generated 2026-11-26 00:29 UTC · rules: data/15m/PREREG.md (sha256 cba69c26b3a6)
Period: 2026-09-18 23:45Z to 2026-11-25 23:30Z · settled markets returned: 6456 · usable for the rule: 6454
Fee: Kalshi taker, multiplier 1.0 (quadratic), round up per order. Entry = ask ~60s after the decision.

**This cannot prove profitability. It decides only whether Phase 2 (forward paper test) is worth running.**

## Primary: AGREE

| Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|
| 2022 | 78.1% | 80.9% | -632.13 | -0.313 (-0.713 to +0.088) | -3.85 | -768.38 | 4 |

- Windows where LEAN and MOMENTUM disagreed (no trade): 2694 · momentum flat: 121 · signal but no usable ask (<=1c or >=99c): 1617

## Sensitivity (primary rule)

| Variant | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| Entry ~0s after decision (candle open) | 1978 | 77.7% | 80.7% | -744.98 | -0.377 (-0.622 to -0.131) | -3.60 | -746.46 | 4 |
| No fee | 2022 | 78.1% | 80.1% | -348.34 | -0.172 (-0.573 to +0.228) | -2.72 | -532.68 | 4 |
| Fee x1.5 | 2022 | 78.1% | 81.3% | -774.03 | -0.383 (-0.783 to +0.017) | -4.43 | -887.02 | 4 |
| As registered (entry ~60s, fee x1) | 2022 | 78.1% | 80.9% | -632.13 | -0.313 (-0.713 to +0.088) | -3.85 | -768.38 | 4 |

## By entry price (primary)

| Ask bucket | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| 1%-60% | 371 | 35.0% | 39.5% | -166.93 | -0.450 (-2.482 to +1.582) | -1.85 | -401.33 | 10 |
| 60%-75% | 213 | 63.8% | 70.0% | -182.27 | -0.856 (-1.772 to +0.061) | -1.96 | -194.61 | 4 |
| 75%-85% | 209 | 79.4% | 81.2% | -47.72 | -0.228 (-0.892 to +0.435) | -0.67 | -83.18 | 3 |
| 85%-92% | 273 | 83.9% | 89.5% | -164.19 | -0.601 (-1.075 to -0.128) | -3.03 | -169.69 | 2 |
| 92%-99% | 956 | 96.1% | 96.9% | -71.02 | -0.074 (-0.195 to +0.047) | -1.33 | -95.97 | 2 |

## Stability over time (primary)

| Period | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| First half | 1011 | 78.5% | 81.3% | -483.27 | -0.478 (-0.888 to -0.068) | -2.73 | -537.96 | 4 |
| Second half | 1011 | 77.7% | 80.5% | -148.87 | -0.147 (-0.835 to +0.541) | -2.71 | -442.77 | 4 |
| 2026-W38 | 64 | 68.8% | 79.1% | -64.31 | -1.005 (-3.086 to +1.076) | -2.51 | -107.56 | 3 |
| 2026-W39 | 195 | 77.9% | 81.3% | -138.28 | -0.709 (-1.540 to +0.121) | -1.50 | -142.82 | 4 |
| 2026-W40 | 235 | 81.3% | 82.9% | -58.71 | -0.250 (-1.081 to +0.581) | -0.82 | -186.70 | 3 |
| 2026-W41 | 213 | 80.8% | 81.2% | -20.43 | -0.096 (-0.959 to +0.767) | -0.20 | -109.04 | 2 |
| 2026-W42 | 194 | 76.8% | 80.5% | -92.69 | -0.478 (-1.575 to +0.619) | -1.56 | -158.36 | 3 |
| 2026-W43 | 213 | 77.0% | 78.4% | +18.56 | +0.087 (-1.740 to +1.915) | -0.62 | -190.43 | 3 |
| 2026-W44 | 196 | 78.6% | 80.3% | -68.65 | -0.350 (-1.463 to +0.762) | -0.78 | -146.69 | 4 |
| 2026-W45 | 231 | 77.5% | 79.9% | -92.57 | -0.401 (-1.496 to +0.694) | -1.09 | -219.86 | 3 |
| 2026-W46 | 191 | 77.5% | 83.1% | -198.91 | -1.041 (-1.839 to -0.244) | -2.53 | -219.04 | 3 |
| 2026-W47 | 196 | 81.1% | 81.7% | +217.33 | +1.109 (-1.129 to +3.347) | -0.24 | -81.71 | 3 |
| 2026-W48 | 94 | 72.3% | 79.5% | -133.47 | -1.420 (-2.737 to -0.102) | -2.09 | -140.02 | 3 |

## By market condition: BTC volatility in the hour before (primary)

| Volatility | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| Calm (lowest third) | 674 | 78.8% | 80.9% | -69.33 | -0.103 (-0.826 to +0.620) | -1.73 | -231.30 | 3 |
| Normal | 674 | 76.1% | 80.2% | -312.27 | -0.463 (-1.286 to +0.359) | -3.32 | -457.59 | 4 |
| Wild (highest third) | 674 | 79.5% | 81.5% | -250.54 | -0.372 (-0.866 to +0.122) | -1.62 | -301.92 | 3 |

## By time of day, UTC (primary)

| Session | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| Asia 00-08 | 682 | 80.4% | 81.0% | -110.13 | -0.161 (-0.740 to +0.417) | -0.55 | -178.45 | 4 |
| Europe 08-13 | 424 | 77.4% | 81.0% | -96.05 | -0.227 (-1.312 to +0.859) | -2.27 | -391.33 | 5 |
| US 13-21 | 649 | 77.5% | 81.0% | -437.17 | -0.674 (-1.180 to -0.167) | -2.79 | -443.23 | 4 |
| Late US 21-24 | 267 | 75.3% | 80.2% | +11.22 | +0.042 (-1.546 to +1.630) | -2.40 | -136.93 | 3 |

## Secondary rules (multiple-testing warning: these cannot confirm anything)

| Rule | Trades | Win rate | Break-even | P&L ($10/trade) | Mean per trade (95% CI) | z vs break-even | Max drawdown | Worst losing streak |
|---|---|---|---|---|---|---|---|---|
| LEAN only (secondary) | 3854 | 77.5% | 80.1% | -1864.83 | -0.484 (-0.738 to -0.230) | -5.14 | -2006.43 | 4 |
| MOMENTUM only (secondary) | 3809 | 52.1% | 53.4% | -1684.34 | -0.442 (-1.426 to +0.542) | -2.47 | -2112.29 | 11 |

## Missing or excluded data (all counted)

- bad_window: 0
- no_candle: 0
- candle_http: 0
- no_target: 0
- no_btc: 2
- settle_mismatch: 0
- unsettled: 0

## Cross-platform check: Kalshi vs Polymarket US, same 15m window

- Windows checked: 700 (most recent) · found on Polymarket US: 696
- Start price (target) difference: median $0.00, max $0.00, exact matches 696/696
- End price difference: median $0.00, max $0.00 · same winner 696/696

## How to read this

- Win rate alone means nothing: compare it with break-even (price + fee).
- z vs break-even above +2 would be a hint, not proof: this is one look at past data, prices are 1-minute
  candle closes (not guaranteed fills, no size), and BTC comes from Coinbase, not BRTI.
- Only the Phase 2 forward paper test (300 trades) can confirm.

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
