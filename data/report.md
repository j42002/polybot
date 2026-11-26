# polybot report

Updated 2026-11-26 19:32 UTC | 1839 checkpoints logged | 1674 graded | 364 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 316 settled rounds observed · 45 alerts (44 delivered) · **7 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/311 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1485 vs market 0.1561 on 316 rounds -> model sharper
3. **Simulated profit after fees:** -41.74 on 7 trades of $10 · win rate 29% vs break-even 45%, 95% range per trade -11.86 to -0.07
4. **Quote available at simulated tap (size not verified):** 5s 11/44 · 10s 11/44 · 20s 9/44 · 30s 7/44
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 30 runs, stalls over 5s 3/49487 loops, longest BTC price gap 10.7s · checks with no market quote 65/1567 (book fallback used 632) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 7/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (319 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 319 | 66.5% | 64.8% | +0.017 | -0.034 to +0.068 | $+54.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 319 | 66.1% | 67.7% | -0.016 | -0.067 to +0.035 | $-50.87 | NO EDGE |
| Edge (model beats the ask by 3c+) | 166 | 51.8% | 40.6% | +0.112 | +0.044 to +0.180 | $+186.72 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 69 | 68.1% | 51.2% | +0.169 | +0.060 to +0.279 | $+116.89 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2063 vs market 0.2178 -> **model is sharper**

## 3:30 left (328 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 328 | 69.2% | 64.4% | +0.048 | +0.000 to +0.095 | $+156.12 | PASSES |
| Lean (bet the side BTC is on now) | 328 | 72.9% | 71.9% | +0.010 | -0.038 to +0.058 | $+32.90 | NO EDGE |
| Edge (model beats the ask by 3c+) | 184 | 41.3% | 34.5% | +0.068 | +0.005 to +0.131 | $+125.29 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 35 | 57.1% | 51.2% | +0.060 | -0.098 to +0.217 | $+20.84 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1836 vs market 0.1955 -> **model is sharper**

## 3:00 left (337 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 337 | 65.9% | 61.4% | +0.044 | +0.002 to +0.087 | $+149.83 | PASSES |
| Lean (bet the side BTC is on now) | 337 | 77.2% | 74.7% | +0.024 | -0.019 to +0.067 | $+82.06 | NO EDGE |
| Edge (model beats the ask by 3c+) | 209 | 32.1% | 28.4% | +0.036 | -0.016 to +0.089 | $+76.15 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 12 | 91.7% | 71.2% | +0.205 | +0.037 to +0.374 | $+24.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1578 vs market 0.1640 -> **model is sharper**

## 2:00 left (345 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 321 | 61.7% | 58.8% | +0.028 | -0.009 to +0.066 | $+91.02 | NO EDGE |
| Lean (bet the side BTC is on now) | 316 | 85.8% | 80.3% | +0.055 | +0.017 to +0.092 | $+173.56 | PASSES |
| Edge (model beats the ask by 3c+) | 263 | 24.0% | 22.0% | +0.019 | -0.019 to +0.058 | $+51.24 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 16 | 100.0% | 75.2% | +0.248 | +0.220 to +0.276 | $+39.68 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1184 vs market 0.1181 -> **market is sharper**

## 1:00 left (345 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 257 | 49.0% | 47.3% | +0.017 | -0.020 to +0.054 | $+44.28 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 215 | 89.8% | 83.1% | +0.067 | +0.024 to +0.110 | $+143.61 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 300 | 15.3% | 11.9% | +0.034 | +0.007 to +0.062 | $+103.41 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0765 vs market 0.0868 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=364, bias $-0.10, sd $0.85 (set BASIS_SD near 1)
- spot at open: n=364, bias $-1.92, sd $23.86 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 390 | 206 | 55% | 57% |
| 60%-70% | 366 | 226 | 65% | 73% |
| 70%-80% | 308 | 209 | 75% | 82% |
| 80%-90% | 599 | 272 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 316 | 1494 | 0.1485 | 0.1561 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 364 (316 with decision logging, v16+)
- Markets with a signal: 114
- Alerts attempted: 45 · delivered: 44 · delivery failed: 1
- Simulated fills (quote available, size not verified): 7
- Expired alerts: 37 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 52 markets, would have won 35, +30.72 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 23 markets, would have won 18, +64.64 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 42/44 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 329 · valid comparisons: 311
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.64, typical gap $2.85, worst $12.31
- Coinbase would have named the wrong winner: 4/311 (1.3%)
- Rounds settling within $10 of the target: 39, wrong winner 4 (10%)
- Rounds settling within $25 of the target: 86, wrong winner 4 (5%)
- Rounds settling within $50 of the target: 153, wrong winner 4 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 43 (goal: 300)
- Simulated paper trades: 7 · no-trade (expired/unconfirmed): 36
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 2/7 = 29% vs break-even 45.2% (price paid + fee)
- Paper P&L after fees: -41.74 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 45
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 78)
- Polymarket quote round trip: median 31 ms (worst 75)
- Price read -> decision made: median 80 ms (worst 168)
- Decision -> Discord accepted: median 1386 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 11/43 | 32 | 0 | +2.27 |
| 10s | 11/43 | 32 | 0 | +2.27 |
| 20s | 9/43 | 34 | 0 | -20.30 |
| 30s | 7/43 | 36 | 0 | -41.74 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 30 · loops: 49487 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
