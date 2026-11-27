# polybot report

Updated 2026-11-27 04:46 UTC | 2360 checkpoints logged | 2194 graded | 470 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 422 settled rounds observed · 68 alerts (67 delivered) · **10 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/413 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1544 vs market 0.1622 on 422 rounds -> model sharper
3. **Simulated profit after fees:** -16.48 on 10 trades of $10 · win rate 40% vs break-even 47%, 95% range per trade -9.41 to +6.11
4. **Quote available at simulated tap (size not verified):** 5s 15/67 · 10s 14/67 · 20s 12/67 · 30s 10/67
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 40 runs, stalls over 5s 3/65987 loops, longest BTC price gap 10.7s · checks with no market quote 68/2088 (book fallback used 877) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 10/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (422 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 422 | 65.9% | 64.7% | +0.012 | -0.033 to +0.056 | $+49.95 | NO EDGE |
| Lean (bet the side BTC is on now) | 422 | 66.4% | 67.4% | -0.010 | -0.055 to +0.034 | $-42.80 | NO EDGE |
| Edge (model beats the ask by 3c+) | 218 | 50.5% | 41.3% | +0.092 | +0.031 to +0.153 | $+200.65 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 98 | 67.3% | 51.9% | +0.154 | +0.061 to +0.248 | $+151.18 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2068 vs market 0.2171 -> **model is sharper**

## 3:30 left (433 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 433 | 66.3% | 63.5% | +0.028 | -0.014 to +0.069 | $+119.38 | NO EDGE |
| Lean (bet the side BTC is on now) | 433 | 71.6% | 71.2% | +0.004 | -0.038 to +0.046 | $+17.08 | NO EDGE |
| Edge (model beats the ask by 3c+) | 246 | 39.8% | 34.6% | +0.052 | -0.002 to +0.106 | $+128.35 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 51 | 58.8% | 51.6% | +0.073 | -0.058 to +0.204 | $+37.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1898 vs market 0.1973 -> **model is sharper**

## 3:00 left (442 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 442 | 64.3% | 61.6% | +0.026 | -0.012 to +0.065 | $+115.75 | NO EDGE |
| Lean (bet the side BTC is on now) | 442 | 76.0% | 74.3% | +0.017 | -0.021 to +0.056 | $+75.50 | NO EDGE |
| Edge (model beats the ask by 3c+) | 268 | 34.3% | 30.1% | +0.043 | -0.005 to +0.090 | $+113.95 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 24 | 87.5% | 71.4% | +0.161 | +0.021 to +0.300 | $+38.53 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1646 vs market 0.1719 -> **model is sharper**

## 2:00 left (450 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 423 | 62.4% | 59.7% | +0.027 | -0.007 to +0.061 | $+115.60 | NO EDGE |
| Lean (bet the side BTC is on now) | 417 | 84.2% | 80.4% | +0.038 | +0.004 to +0.072 | $+158.25 | PASSES |
| Edge (model beats the ask by 3c+) | 335 | 24.2% | 21.6% | +0.026 | -0.008 to +0.061 | $+87.70 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1244 vs market 0.1273 -> **model is sharper**

## 1:00 left (447 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 335 | 50.1% | 48.2% | +0.020 | -0.014 to +0.053 | $+65.59 | NO EDGE |
| Lean (bet the side BTC is on now) | 282 | 87.9% | 82.9% | +0.050 | +0.011 to +0.089 | $+141.91 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 393 | 16.5% | 12.5% | +0.040 | +0.015 to +0.065 | $+157.68 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0800 vs market 0.0925 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=470, bias $-0.08, sd $0.75 (set BASIS_SD near 1)
- spot at open: n=470, bias $-1.67, sd $23.09 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 512 | 273 | 55% | 57% |
| 60%-70% | 494 | 301 | 65% | 70% |
| 70%-80% | 416 | 280 | 75% | 82% |
| 80%-90% | 761 | 348 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 422 | 2014 | 0.1544 | 0.1622 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 470 (422 with decision logging, v16+)
- Markets with a signal: 165
- Alerts attempted: 68 · delivered: 67 · delivery failed: 1
- Simulated fills (quote available, size not verified): 10
- Expired alerts: 57 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 71 markets, would have won 49, +45.58 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 36 markets, would have won 29, +97.60 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 63/67 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 439 · valid comparisons: 413
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.71, typical gap $2.83, worst $12.31
- Coinbase would have named the wrong winner: 5/413 (1.2%)
- Rounds settling within $10 of the target: 60, wrong winner 5 (8%)
- Rounds settling within $25 of the target: 127, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 213, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 67 (goal: 300)
- Simulated paper trades: 10 · no-trade (expired/unconfirmed): 57
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 4/10 = 40% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -16.48 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 68
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 74 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 15/67 | 52 | 0 | +38.30 |
| 10s | 14/67 | 53 | 0 | +27.53 |
| 20s | 12/67 | 55 | 0 | +4.96 |
| 30s | 10/67 | 57 | 0 | -16.48 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 40 · loops: 65987 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
