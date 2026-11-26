# polybot report

Updated 2026-11-26 14:55 UTC | 1578 checkpoints logged | 1416 graded | 310 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 262 settled rounds observed · 36 alerts (35 delivered) · **6 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/257 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 17
2. **Model vs market accuracy (Brier, lower is better):** model 0.1397 vs market 0.1480 on 262 rounds -> model sharper
3. **Simulated profit after fees:** -48.03 on 6 trades of $10 · win rate 17% vs break-even 42%, 95% range per trade -13.12 to -2.89
4. **Quote available at simulated tap (size not verified):** 5s 10/35 · 10s 10/35 · 20s 8/35 · 30s 6/35
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 25 runs, stalls over 5s 3/41237 loops, longest BTC price gap 10.7s · checks with no market quote 65/1306 (book fallback used 511) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 6/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (265 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 265 | 67.9% | 65.3% | +0.026 | -0.030 to +0.082 | $+68.70 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 265 | 67.2% | 68.1% | -0.009 | -0.065 to +0.047 | $-23.71 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 138 | 53.6% | 40.0% | +0.137 | +0.063 to +0.210 | $+188.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 56 | 71.4% | 51.3% | +0.202 | +0.087 to +0.316 | $+112.84 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1985 vs market 0.2151 -> **model is sharper**

## 3:30 left (276 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 276 | 71.0% | 64.6% | +0.064 | +0.014 to +0.115 | $+177.38 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 276 | 76.4% | 72.4% | +0.041 | -0.010 to +0.092 | $+112.52 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 159 | 42.1% | 34.3% | +0.079 | +0.012 to +0.146 | $+125.37 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 31 | 61.3% | 51.3% | +0.100 | -0.067 to +0.266 | $+30.85 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1749 vs market 0.1897 -> **model is sharper**

## 3:00 left (285 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 285 | 66.3% | 61.7% | +0.046 | +0.001 to +0.092 | $+132.18 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 285 | 78.6% | 75.3% | +0.033 | -0.012 to +0.079 | $+94.34 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 180 | 31.7% | 28.2% | +0.035 | -0.020 to +0.089 | $+62.60 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 11 | 100.0% | 71.1% | +0.289 | +0.251 to +0.327 | $+31.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1515 vs market 0.1563 -> **model is sharper**

## 2:00 left (295 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 275 | 61.5% | 59.3% | +0.021 | -0.018 to +0.061 | $+58.35 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 270 | 86.7% | 80.5% | +0.062 | +0.023 to +0.101 | $+167.48 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 223 | 22.4% | 21.6% | +0.008 | -0.033 to +0.049 | $+17.62 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1141 vs market 0.1121 -> **market is sharper**

## 1:00 left (295 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 218 | 49.5% | 46.9% | +0.026 | -0.011 to +0.063 | $+56.61 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 182 | 91.8% | 82.8% | +0.090 | +0.048 to +0.132 | $+163.66 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 255 | 14.5% | 11.6% | +0.029 | +0.001 to +0.058 | $+74.87 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0688 vs market 0.0771 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=310, bias $-0.12, sd $0.92 (set BASIS_SD near 1)
- spot at open: n=310, bias $-2.14, sd $23.88 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 318 | 168 | 55% | 60% |
| 60%-70% | 306 | 189 | 65% | 73% |
| 70%-80% | 267 | 181 | 75% | 85% |
| 80%-90% | 514 | 236 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 262 | 1236 | 0.1397 | 0.148 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 310 (262 with decision logging, v16+)
- Markets with a signal: 94
- Alerts attempted: 36 · delivered: 35 · delivery failed: 1
- Simulated fills (quote available, size not verified): 6
- Expired alerts: 29 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 45 markets, would have won 33, +54.49 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 18 markets, would have won 16, +69.64 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 4 markets, would have won 4, +14.81 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 33/35 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 274 · valid comparisons: 257
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.53, typical gap $2.98, worst $12.31
- Coinbase would have named the wrong winner: 3/257 (1.2%)
- Rounds settling within $10 of the target: 32, wrong winner 3 (9%)
- Rounds settling within $25 of the target: 72, wrong winner 3 (4%)
- Rounds settling within $50 of the target: 122, wrong winner 3 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 35 (goal: 300)
- Simulated paper trades: 6 · no-trade (expired/unconfirmed): 29
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/6 = 17% vs break-even 42.3% (price paid + fee)
- Paper P&L after fees: -48.03 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 36
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 10/35 | 25 | 0 | -4.02 |
| 10s | 10/35 | 25 | 0 | -4.02 |
| 20s | 8/35 | 27 | 0 | -26.59 |
| 30s | 6/35 | 29 | 0 | -48.03 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 25 · loops: 41237 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
