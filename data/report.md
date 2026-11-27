# polybot report

Updated 2026-11-27 08:27 UTC | 2570 checkpoints logged | 2397 graded | 514 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 466 settled rounds observed · 75 alerts (74 delivered) · **13 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/457 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1543 vs market 0.1617 on 466 rounds -> model sharper
3. **Simulated profit after fees:** -13.94 on 13 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -7.43 to +5.28
4. **Quote available at simulated tap (size not verified):** 5s 19/74 · 10s 17/74 · 20s 15/74 · 30s 13/74
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 44 runs, stalls over 5s 3/72587 loops, longest BTC price gap 10.7s · checks with no market quote 73/2298 (book fallback used 950) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 13/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (463 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 463 | 65.7% | 64.6% | +0.010 | -0.032 to +0.053 | $+48.25 | NO EDGE |
| Lean (bet the side BTC is on now) | 463 | 66.1% | 67.4% | -0.013 | -0.055 to +0.030 | $-58.69 | NO EDGE |
| Edge (model beats the ask by 3c+) | 237 | 50.2% | 41.0% | +0.093 | +0.035 to +0.151 | $+219.32 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 103 | 68.0% | 52.1% | +0.159 | +0.068 to +0.250 | $+163.56 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2076 vs market 0.2184 -> **model is sharper**

## 3:30 left (475 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 475 | 66.1% | 63.1% | +0.030 | -0.009 to +0.070 | $+143.81 | NO EDGE |
| Lean (bet the side BTC is on now) | 475 | 71.6% | 71.0% | +0.006 | -0.034 to +0.046 | $+27.76 | NO EDGE |
| Edge (model beats the ask by 3c+) | 264 | 40.5% | 34.7% | +0.058 | +0.006 to +0.110 | $+153.59 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 58 | 62.1% | 51.7% | +0.104 | -0.017 to +0.224 | $+60.04 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1873 vs market 0.1955 -> **model is sharper**

## 3:00 left (482 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 481 | 65.1% | 61.8% | +0.033 | -0.004 to +0.069 | $+157.75 | NO EDGE |
| Lean (bet the side BTC is on now) | 481 | 76.3% | 74.4% | +0.019 | -0.018 to +0.055 | $+89.76 | NO EDGE |
| Edge (model beats the ask by 3c+) | 292 | 33.6% | 29.9% | +0.037 | -0.008 to +0.081 | $+107.10 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 88.5% | 70.9% | +0.176 | +0.045 to +0.306 | $+45.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1637 vs market 0.1696 -> **model is sharper**

## 2:00 left (490 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 459 | 62.3% | 60.0% | +0.023 | -0.009 to +0.056 | $+106.17 | NO EDGE |
| Lean (bet the side BTC is on now) | 452 | 84.5% | 80.3% | +0.042 | +0.009 to +0.075 | $+190.37 | PASSES |
| Edge (model beats the ask by 3c+) | 361 | 23.8% | 21.2% | +0.026 | -0.007 to +0.059 | $+93.89 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1234 vs market 0.1258 -> **model is sharper**

## 1:00 left (487 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 361 | 50.1% | 48.6% | +0.015 | -0.017 to +0.048 | $+55.57 | NO EDGE |
| Lean (bet the side BTC is on now) | 304 | 87.5% | 83.0% | +0.045 | +0.007 to +0.083 | $+137.77 | PASSES |
| Edge (model beats the ask by 3c+) | 428 | 16.1% | 12.2% | +0.039 | +0.015 to +0.063 | $+167.91 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0818 vs market 0.0930 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=514, bias $-0.07, sd $0.72 (set BASIS_SD near 1)
- spot at open: n=514, bias $-1.75, sd $22.60 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 568 | 300 | 55% | 56% |
| 60%-70% | 538 | 325 | 65% | 71% |
| 70%-80% | 453 | 306 | 75% | 83% |
| 80%-90% | 827 | 375 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 466 | 2217 | 0.1543 | 0.1617 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 514 (466 with decision logging, v16+)
- Markets with a signal: 177
- Alerts attempted: 75 · delivered: 74 · delivery failed: 1
- Simulated fills (quote available, size not verified): 13
- Expired alerts: 61 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 74 markets, would have won 51, +46.12 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 40 markets, would have won 33, +117.26 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 70/74 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 483 · valid comparisons: 457
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.94, typical gap $2.89, worst $12.31
- Coinbase would have named the wrong winner: 6/457 (1.3%)
- Rounds settling within $10 of the target: 67, wrong winner 6 (9%)
- Rounds settling within $25 of the target: 140, wrong winner 6 (4%)
- Rounds settling within $50 of the target: 239, wrong winner 6 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 74 (goal: 300)
- Simulated paper trades: 13 · no-trade (expired/unconfirmed): 61
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/13 = 46% vs break-even 48.8% (price paid + fee)
- Paper P&L after fees: -13.94 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 75
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 28 ms (worst 75)
- Price read -> decision made: median 74 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 19/74 | 55 | 0 | +56.50 |
| 10s | 17/74 | 57 | 0 | +30.06 |
| 20s | 15/74 | 59 | 0 | +7.50 |
| 30s | 13/74 | 61 | 0 | -13.94 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 44 · loops: 72587 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
