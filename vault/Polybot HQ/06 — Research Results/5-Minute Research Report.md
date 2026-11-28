---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 00:08 UTC | 3465 checkpoints logged | 3277 graded | 698 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 650 settled rounds observed · 105 alerts (103 delivered) · **24 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/638 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1639 vs market 0.1696 on 650 rounds -> model sharper
3. **Simulated profit after fees:** -21.65 on 24 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.46 to +3.65
4. **Quote available at simulated tap (size not verified):** 5s 34/103 · 10s 32/103 · 20s 27/103 · 30s 24/103
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 61 runs, stalls over 5s 4/100632 loops, longest BTC price gap 10.8s · checks with no market quote 92/3193 (book fallback used 1291) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 24/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 24/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 63/103 delivered alerts (61%) vs average break-even 52% at the alert price.
- Same 24 tickets at every delay (right 11/24): 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 10, of which right 7/10. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (639 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 638 | 65.4% | 64.6% | +0.008 | -0.029 to +0.044 | $+49.71 | NO EDGE |
| Lean (bet the side BTC is on now) | 639 | 65.1% | 67.3% | -0.022 | -0.058 to +0.015 | $-137.82 | NO EDGE |
| Edge (model beats the ask by 3c+) | 321 | 48.9% | 42.6% | +0.063 | +0.013 to +0.114 | $+202.54 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 146 | 62.3% | 52.9% | +0.095 | +0.014 to +0.175 | $+138.05 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2135 vs market 0.2201 -> **model is sharper**

## 3:30 left (653 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 653 | 66.0% | 62.9% | +0.031 | -0.003 to +0.065 | $+203.03 | NO EDGE |
| Lean (bet the side BTC is on now) | 653 | 69.5% | 71.1% | -0.016 | -0.051 to +0.018 | $-104.74 | NO EDGE |
| Edge (model beats the ask by 3c+) | 369 | 39.3% | 35.2% | +0.041 | -0.004 to +0.086 | $+151.15 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 77 | 59.7% | 52.2% | +0.076 | -0.030 to +0.182 | $+58.19 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1991 vs market 0.2019 -> **model is sharper**

## 3:00 left (660 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 659 | 64.2% | 61.4% | +0.028 | -0.004 to +0.060 | $+186.15 | NO EDGE |
| Lean (bet the side BTC is on now) | 659 | 74.5% | 74.3% | +0.002 | -0.030 to +0.035 | $+16.16 | NO EDGE |
| Edge (model beats the ask by 3c+) | 402 | 34.8% | 30.6% | +0.043 | +0.003 to +0.082 | $+171.17 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 35 | 88.6% | 71.0% | +0.176 | +0.064 to +0.288 | $+61.60 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1743 vs market 0.1794 -> **model is sharper**

## 2:00 left (666 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 628 | 62.9% | 59.5% | +0.034 | +0.005 to +0.063 | $+213.42 | PASSES |
| Lean (bet the side BTC is on now) | 615 | 82.1% | 79.6% | +0.025 | -0.004 to +0.054 | $+152.51 | NO EDGE |
| Edge (model beats the ask by 3c+) | 496 | 25.0% | 21.9% | +0.031 | +0.002 to +0.061 | $+155.43 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 24 | 91.7% | 74.8% | +0.169 | +0.058 to +0.279 | $+40.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1311 vs market 0.1349 -> **model is sharper**

## 1:00 left (659 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 490 | 50.6% | 48.5% | +0.022 | -0.007 to +0.051 | $+105.87 | NO EDGE |
| Lean (bet the side BTC is on now) | 417 | 85.4% | 81.1% | +0.042 | +0.009 to +0.076 | $+176.62 | PASSES |
| Edge (model beats the ask by 3c+) | 585 | 17.1% | 12.9% | +0.042 | +0.019 to +0.064 | $+243.11 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0889 vs market 0.1012 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=698, bias $-0.05, sd $0.62 (set BASIS_SD near 1)
- spot at open: n=698, bias $-3.77, sd $23.05 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 795 | 413 | 55% | 56% |
| 60%-70% | 737 | 446 | 65% | 69% |
| 70%-80% | 626 | 410 | 75% | 79% |
| 80%-90% | 1108 | 494 | 87% | 95% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 650 | 3097 | 0.1639 | 0.1696 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 698 (650 with decision logging, v16+)
- Markets with a signal: 245
- Alerts attempted: 105 · delivered: 103 · delivery failed: 2
- Simulated fills (quote available, size not verified): 24
- Expired alerts: 79 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 104 markets, would have won 70, +52.28 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 53 markets, would have won 39, +107.59 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 98/103 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 670 · valid comparisons: 638
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.74, typical gap $4.46, worst $20.80
- Coinbase would have named the wrong winner: 20/638 (3.1%)
- Rounds settling within $10 of the target: 98, wrong winner 19 (19%)
- Rounds settling within $25 of the target: 214, wrong winner 20 (9%)
- Rounds settling within $50 of the target: 353, wrong winner 20 (6%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 103 (goal: 300)
- Simulated paper trades: 24 · no-trade (expired/unconfirmed): 79
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 11/24 = 46% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -21.65 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 105
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1556 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 34/103 | 69 | 0 | +21.93 |
| 10s | 32/103 | 71 | 0 | -7.20 |
| 20s | 27/103 | 76 | 0 | +6.58 |
| 30s | 24/103 | 79 | 0 | -21.65 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 61 · loops: 100632 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
