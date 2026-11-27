# polybot report

Updated 2026-11-27 11:13 UTC | 2732 checkpoints logged | 2563 graded | 548 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 500 settled rounds observed · 83 alerts (82 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 9/491 valid rounds (1.8%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1574 vs market 0.1643 on 500 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/82 · 10s 20/82 · 20s 17/82 · 30s 15/82
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 47 runs, stalls over 5s 3/77537 loops, longest BTC price gap 10.7s · checks with no market quote 73/2460 (book fallback used 1018) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (497 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 497 | 65.4% | 64.5% | +0.009 | -0.032 to +0.050 | $+45.75 | NO EDGE |
| Lean (bet the side BTC is on now) | 497 | 65.6% | 67.2% | -0.016 | -0.057 to +0.025 | $-79.48 | NO EDGE |
| Edge (model beats the ask by 3c+) | 250 | 49.6% | 41.2% | +0.084 | +0.027 to +0.141 | $+210.25 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 112 | 65.2% | 52.2% | +0.130 | +0.041 to +0.219 | $+145.71 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2102 vs market 0.2197 -> **model is sharper**

## 3:30 left (509 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 509 | 65.4% | 62.9% | +0.025 | -0.014 to +0.063 | $+126.62 | NO EDGE |
| Lean (bet the side BTC is on now) | 509 | 70.7% | 70.9% | -0.002 | -0.040 to +0.037 | $-8.30 | NO EDGE |
| Edge (model beats the ask by 3c+) | 286 | 40.6% | 35.3% | +0.053 | +0.003 to +0.103 | $+151.27 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 64 | 59.4% | 51.7% | +0.076 | -0.038 to +0.191 | $+48.87 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1918 vs market 0.1978 -> **model is sharper**

## 3:00 left (516 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 515 | 64.7% | 61.7% | +0.030 | -0.006 to +0.066 | $+154.57 | NO EDGE |
| Lean (bet the side BTC is on now) | 515 | 75.7% | 74.4% | +0.013 | -0.022 to +0.049 | $+69.45 | NO EDGE |
| Edge (model beats the ask by 3c+) | 309 | 33.3% | 29.6% | +0.037 | -0.006 to +0.081 | $+115.28 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 88.5% | 70.9% | +0.176 | +0.045 to +0.306 | $+45.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1674 vs market 0.1732 -> **model is sharper**

## 2:00 left (523 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 492 | 62.6% | 60.1% | +0.025 | -0.007 to +0.057 | $+123.90 | NO EDGE |
| Lean (bet the side BTC is on now) | 484 | 83.9% | 80.3% | +0.036 | +0.004 to +0.068 | $+173.48 | PASSES |
| Edge (model beats the ask by 3c+) | 386 | 24.1% | 21.2% | +0.029 | -0.003 to +0.061 | $+112.55 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 21 | 95.2% | 75.0% | +0.202 | +0.102 to +0.302 | $+42.45 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1251 vs market 0.1287 -> **model is sharper**

## 1:00 left (518 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 385 | 49.6% | 48.2% | +0.014 | -0.017 to +0.046 | $+54.85 | NO EDGE |
| Lean (bet the side BTC is on now) | 325 | 87.1% | 82.8% | +0.043 | +0.006 to +0.080 | $+138.65 | PASSES |
| Edge (model beats the ask by 3c+) | 455 | 16.3% | 12.3% | +0.040 | +0.016 to +0.064 | $+182.46 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0830 vs market 0.0945 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=548, bias $-0.07, sd $0.70 (set BASIS_SD near 1)
- spot at open: n=548, bias $-2.12, sd $22.26 (set BASIS_SD near 22)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 611 | 322 | 55% | 57% |
| 60%-70% | 569 | 346 | 65% | 70% |
| 70%-80% | 496 | 331 | 75% | 81% |
| 80%-90% | 876 | 398 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 500 | 2383 | 0.1574 | 0.1643 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 548 (500 with decision logging, v16+)
- Markets with a signal: 194
- Alerts attempted: 83 · delivered: 82 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 67 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 81 markets, would have won 55, +45.09 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 42 markets, would have won 33, +109.01 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 78/82 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 516 · valid comparisons: 491
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.31, typical gap $3.16, worst $12.47
- Coinbase would have named the wrong winner: 9/491 (1.8%)
- Rounds settling within $10 of the target: 77, wrong winner 9 (12%)
- Rounds settling within $25 of the target: 157, wrong winner 9 (6%)
- Rounds settling within $50 of the target: 261, wrong winner 9 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 82 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 67
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 83
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/82 | 60 | 0 | +25.17 |
| 10s | 20/82 | 62 | 0 | -1.27 |
| 20s | 17/82 | 65 | 0 | -13.40 |
| 30s | 15/82 | 67 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 47 · loops: 77537 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
