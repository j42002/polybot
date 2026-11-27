# polybot report

Updated 2026-11-27 19:32 UTC | 3197 checkpoints logged | 3022 graded | 643 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 595 settled rounds observed · 92 alerts (90 delivered) · **16 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 13/582 valid rounds (2.2%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1612 vs market 0.1682 on 595 rounds -> model sharper
3. **Simulated profit after fees:** -29.13 on 16 trades of $10 · win rate 44% vs break-even 50%, 95% range per trade -7.27 to +3.63
4. **Quote available at simulated tap (size not verified):** 5s 24/90 · 10s 22/90 · 20s 19/90 · 30s 17/90
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 56 runs, stalls over 5s 4/92382 loops, longest BTC price gap 10.8s · checks with no market quote 75/2925 (book fallback used 1228) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 16/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (589 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 589 | 65.0% | 64.5% | +0.005 | -0.033 to +0.043 | $+28.36 | NO EDGE |
| Lean (bet the side BTC is on now) | 589 | 65.4% | 67.3% | -0.019 | -0.057 to +0.019 | $-111.55 | NO EDGE |
| Edge (model beats the ask by 3c+) | 297 | 49.5% | 41.7% | +0.078 | +0.026 to +0.130 | $+231.55 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 132 | 65.2% | 52.5% | +0.126 | +0.043 to +0.209 | $+166.46 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2121 vs market 0.2207 -> **model is sharper**

## 3:30 left (601 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 601 | 65.9% | 62.9% | +0.030 | -0.006 to +0.066 | $+179.79 | NO EDGE |
| Lean (bet the side BTC is on now) | 601 | 70.5% | 71.2% | -0.007 | -0.042 to +0.029 | $-39.22 | NO EDGE |
| Edge (model beats the ask by 3c+) | 335 | 40.6% | 34.6% | +0.060 | +0.014 to +0.107 | $+202.28 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 69 | 59.4% | 52.2% | +0.072 | -0.039 to +0.184 | $+49.83 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1958 vs market 0.2013 -> **model is sharper**

## 3:00 left (608 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 607 | 64.6% | 61.2% | +0.034 | +0.001 to +0.067 | $+207.00 | PASSES |
| Lean (bet the side BTC is on now) | 607 | 75.6% | 74.4% | +0.012 | -0.022 to +0.045 | $+71.96 | NO EDGE |
| Edge (model beats the ask by 3c+) | 366 | 34.7% | 29.7% | +0.050 | +0.008 to +0.091 | $+181.37 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 33 | 87.9% | 70.8% | +0.171 | +0.053 to +0.289 | $+56.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1717 vs market 0.1777 -> **model is sharper**

## 2:00 left (615 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 579 | 63.4% | 59.8% | +0.035 | +0.006 to +0.065 | $+204.82 | PASSES |
| Lean (bet the side BTC is on now) | 568 | 82.9% | 79.9% | +0.031 | +0.001 to +0.061 | $+173.49 | PASSES |
| Edge (model beats the ask by 3c+) | 462 | 25.1% | 21.9% | +0.032 | +0.002 to +0.062 | $+149.17 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 23 | 95.7% | 75.3% | +0.204 | +0.113 to +0.294 | $+46.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1279 vs market 0.1318 -> **model is sharper**

## 1:00 left (609 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 449 | 49.9% | 48.0% | +0.018 | -0.012 to +0.049 | $+82.61 | NO EDGE |
| Lean (bet the side BTC is on now) | 383 | 85.4% | 81.6% | +0.038 | +0.003 to +0.073 | $+146.14 | PASSES |
| Edge (model beats the ask by 3c+) | 537 | 17.1% | 12.5% | +0.047 | +0.024 to +0.069 | $+250.45 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0872 vs market 0.1002 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=643, bias $-0.06, sd $0.64 (set BASIS_SD near 1)
- spot at open: n=643, bias $-3.19, sd $23.71 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 727 | 379 | 55% | 57% |
| 60%-70% | 674 | 410 | 65% | 69% |
| 70%-80% | 590 | 385 | 75% | 79% |
| 80%-90% | 1020 | 462 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 595 | 2842 | 0.1612 | 0.1682 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 643 (595 with decision logging, v16+)
- Markets with a signal: 223
- Alerts attempted: 92 · delivered: 90 · delivery failed: 2
- Simulated fills (quote available, size not verified): 17
- Expired alerts: 73 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 97 markets, would have won 67, +60.88 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 51 markets, would have won 39, +120.63 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 85/90 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 615 · valid comparisons: 582
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.17, typical gap $4.15, worst $20.80
- Coinbase would have named the wrong winner: 13/582 (2.2%)
- Rounds settling within $10 of the target: 89, wrong winner 13 (15%)
- Rounds settling within $25 of the target: 182, wrong winner 13 (7%)
- Rounds settling within $50 of the target: 308, wrong winner 13 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 89 (goal: 300)
- Simulated paper trades: 16 · no-trade (expired/unconfirmed): 73
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 7/16 = 44% vs break-even 50.2% (price paid + fee)
- Paper P&L after fees: -29.13 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 92
- Coinbase trade -> we received it: median 890 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1563 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 23/89 | 66 | 0 | +31.19 |
| 10s | 21/89 | 68 | 0 | +4.75 |
| 20s | 18/89 | 71 | 0 | -7.38 |
| 30s | 16/89 | 73 | 0 | -29.13 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 56 · loops: 92382 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
