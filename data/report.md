# polybot report

Updated 2026-11-27 13:59 UTC | 2889 checkpoints logged | 2719 graded | 580 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 532 settled rounds observed · 84 alerts (83 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/520 valid rounds (1.9%) where Coinbase points at the wrong winner · missing 29
2. **Model vs market accuracy (Brier, lower is better):** model 0.1598 vs market 0.1660 on 532 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/83 · 10s 20/83 · 20s 17/83 · 30s 15/83
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 50 runs, stalls over 5s 3/82487 loops, longest BTC price gap 10.7s · checks with no market quote 73/2617 (book fallback used 1084) · bad close samples 13 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (527 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 527 | 64.7% | 64.3% | +0.004 | -0.036 to +0.044 | $+22.80 | NO EDGE |
| Lean (bet the side BTC is on now) | 527 | 64.7% | 67.1% | -0.024 | -0.064 to +0.016 | $-127.72 | NO EDGE |
| Edge (model beats the ask by 3c+) | 265 | 47.9% | 40.9% | +0.070 | +0.015 to +0.125 | $+185.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 116 | 63.8% | 52.2% | +0.116 | +0.027 to +0.205 | $+134.68 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2127 vs market 0.2212 -> **model is sharper**

## 3:30 left (540 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 540 | 64.6% | 62.6% | +0.021 | -0.017 to +0.058 | $+110.84 | NO EDGE |
| Lean (bet the side BTC is on now) | 540 | 70.7% | 70.8% | -0.001 | -0.039 to +0.037 | $-4.44 | NO EDGE |
| Edge (model beats the ask by 3c+) | 299 | 40.8% | 35.1% | +0.057 | +0.008 to +0.107 | $+171.69 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1953 vs market 0.2014 -> **model is sharper**

## 3:00 left (548 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 547 | 65.6% | 61.9% | +0.037 | +0.002 to +0.072 | $+202.70 | PASSES |
| Lean (bet the side BTC is on now) | 547 | 75.7% | 74.3% | +0.014 | -0.021 to +0.049 | $+75.21 | NO EDGE |
| Edge (model beats the ask by 3c+) | 325 | 32.9% | 29.5% | +0.034 | -0.009 to +0.077 | $+111.20 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1694 vs market 0.1739 -> **model is sharper**

## 2:00 left (555 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 521 | 63.1% | 60.0% | +0.031 | +0.000 to +0.062 | $+161.89 | PASSES |
| Lean (bet the side BTC is on now) | 512 | 83.6% | 80.2% | +0.034 | +0.003 to +0.065 | $+175.84 | PASSES |
| Edge (model beats the ask by 3c+) | 412 | 23.5% | 21.4% | +0.022 | -0.009 to +0.053 | $+89.50 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1269 vs market 0.1286 -> **model is sharper**

## 1:00 left (549 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 408 | 49.5% | 47.9% | +0.016 | -0.015 to +0.047 | $+65.84 | NO EDGE |
| Lean (bet the side BTC is on now) | 345 | 86.7% | 82.3% | +0.043 | +0.007 to +0.080 | $+149.74 | PASSES |
| Edge (model beats the ask by 3c+) | 482 | 16.6% | 12.5% | +0.041 | +0.018 to +0.065 | $+197.71 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0841 vs market 0.0961 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=580, bias $-0.06, sd $0.68 (set BASIS_SD near 1)
- spot at open: n=580, bias $-2.55, sd $22.29 (set BASIS_SD near 22)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 658 | 346 | 55% | 57% |
| 60%-70% | 604 | 366 | 65% | 69% |
| 70%-80% | 526 | 349 | 75% | 80% |
| 80%-90% | 920 | 419 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 532 | 2539 | 0.1598 | 0.166 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 580 (532 with decision logging, v16+)
- Markets with a signal: 201
- Alerts attempted: 84 · delivered: 83 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 68 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 85 markets, would have won 57, +38.27 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 44 markets, would have won 34, +109.84 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 79/83 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 549 · valid comparisons: 520
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.32, typical gap $3.14, worst $12.47
- Coinbase would have named the wrong winner: 10/520 (1.9%)
- Rounds settling within $10 of the target: 80, wrong winner 10 (12%)
- Rounds settling within $25 of the target: 168, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 280, wrong winner 10 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 83 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 68
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 84
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 73 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/83 | 61 | 0 | +25.17 |
| 10s | 20/83 | 63 | 0 | -1.27 |
| 20s | 17/83 | 66 | 0 | -13.40 |
| 30s | 15/83 | 68 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 50 · loops: 82487 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
