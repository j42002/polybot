# polybot report

Updated 2026-11-27 14:55 UTC | 2939 checkpoints logged | 2769 graded | 590 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 542 settled rounds observed · 85 alerts (84 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/529 valid rounds (1.9%) where Coinbase points at the wrong winner · missing 31
2. **Model vs market accuracy (Brier, lower is better):** model 0.1605 vs market 0.1668 on 542 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/84 · 10s 20/84 · 20s 17/84 · 30s 15/84
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 51 runs, stalls over 5s 3/84136 loops, longest BTC price gap 10.7s · checks with no market quote 73/2667 (book fallback used 1103) · bad close samples 13 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (537 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 537 | 64.8% | 64.4% | +0.004 | -0.035 to +0.044 | $+23.66 | NO EDGE |
| Lean (bet the side BTC is on now) | 537 | 65.0% | 67.2% | -0.022 | -0.062 to +0.018 | $-117.95 | NO EDGE |
| Edge (model beats the ask by 3c+) | 269 | 47.2% | 41.0% | +0.062 | +0.007 to +0.117 | $+166.79 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 118 | 62.7% | 52.5% | +0.102 | +0.013 to +0.192 | $+120.86 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2129 vs market 0.2205 -> **model is sharper**

## 3:30 left (550 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 550 | 64.9% | 62.7% | +0.022 | -0.016 to +0.059 | $+119.65 | NO EDGE |
| Lean (bet the side BTC is on now) | 550 | 70.7% | 70.9% | -0.002 | -0.040 to +0.035 | $-11.92 | NO EDGE |
| Edge (model beats the ask by 3c+) | 306 | 40.5% | 34.7% | +0.058 | +0.009 to +0.107 | $+178.14 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1958 vs market 0.2015 -> **model is sharper**

## 3:00 left (558 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 557 | 65.4% | 61.9% | +0.034 | -0.000 to +0.069 | $+189.88 | NO EDGE |
| Lean (bet the side BTC is on now) | 557 | 75.8% | 74.3% | +0.014 | -0.020 to +0.049 | $+79.70 | NO EDGE |
| Edge (model beats the ask by 3c+) | 330 | 33.0% | 29.5% | +0.035 | -0.008 to +0.078 | $+115.03 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1706 vs market 0.1751 -> **model is sharper**

## 2:00 left (565 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 530 | 63.4% | 60.2% | +0.032 | +0.001 to +0.062 | $+167.77 | PASSES |
| Lean (bet the side BTC is on now) | 521 | 83.1% | 80.2% | +0.029 | -0.002 to +0.060 | $+150.93 | NO EDGE |
| Edge (model beats the ask by 3c+) | 420 | 23.3% | 21.4% | +0.020 | -0.011 to +0.051 | $+83.27 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1277 vs market 0.1298 -> **model is sharper**

## 1:00 left (559 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 414 | 49.8% | 48.0% | +0.017 | -0.014 to +0.048 | $+71.18 | NO EDGE |
| Lean (bet the side BTC is on now) | 350 | 86.3% | 82.4% | +0.039 | +0.002 to +0.075 | $+135.69 | PASSES |
| Edge (model beats the ask by 3c+) | 492 | 16.9% | 12.4% | +0.045 | +0.021 to +0.068 | $+220.28 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0848 vs market 0.0987 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=590, bias $-0.06, sd $0.67 (set BASIS_SD near 1)
- spot at open: n=590, bias $-2.62, sd $23.15 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 670 | 352 | 55% | 58% |
| 60%-70% | 614 | 374 | 65% | 70% |
| 70%-80% | 535 | 355 | 75% | 79% |
| 80%-90% | 939 | 427 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 542 | 2589 | 0.1605 | 0.1668 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 590 (542 with decision logging, v16+)
- Markets with a signal: 203
- Alerts attempted: 85 · delivered: 84 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 69 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 86 markets, would have won 57, +31.36 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 44 markets, would have won 34, +109.84 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 80/84 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 560 · valid comparisons: 529
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 18 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.37, typical gap $3.19, worst $12.47
- Coinbase would have named the wrong winner: 10/529 (1.9%)
- Rounds settling within $10 of the target: 81, wrong winner 10 (12%)
- Rounds settling within $25 of the target: 171, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 284, wrong winner 10 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 84 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 69
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 85
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/84 | 62 | 0 | +25.17 |
| 10s | 20/84 | 64 | 0 | -1.27 |
| 20s | 17/84 | 67 | 0 | -13.40 |
| 30s | 15/84 | 69 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 51 · loops: 84136 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
