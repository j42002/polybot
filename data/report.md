# polybot report

Updated 2026-11-26 14:00 UTC | 1528 checkpoints logged | 1366 graded | 300 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 252 settled rounds observed · 35 alerts (34 delivered) · **6 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/247 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 16
2. **Model vs market accuracy (Brier, lower is better):** model 0.1386 vs market 0.1485 on 252 rounds -> model sharper
3. **Simulated profit after fees:** -48.03 on 6 trades of $10 · win rate 17% vs break-even 42%, 95% range per trade -13.12 to -2.89
4. **Quote available at simulated tap (size not verified):** 5s 10/34 · 10s 10/34 · 20s 8/34 · 30s 6/34
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 24 runs, stalls over 5s 3/39587 loops, longest BTC price gap 10.7s · checks with no market quote 65/1256 (book fallback used 494) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 6/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (255 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 255 | 67.8% | 65.5% | +0.023 | -0.034 to +0.080 | $+58.82 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 255 | 67.5% | 68.2% | -0.008 | -0.065 to +0.049 | $-19.70 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 136 | 54.4% | 40.1% | +0.143 | +0.070 to +0.217 | $+194.78 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 56 | 71.4% | 51.3% | +0.202 | +0.087 to +0.316 | $+112.84 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1983 vs market 0.2173 -> **model is sharper**

## 3:30 left (266 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 266 | 71.4% | 64.4% | +0.070 | +0.019 to +0.121 | $+186.79 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 266 | 76.3% | 72.4% | +0.039 | -0.012 to +0.091 | $+104.74 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 154 | 42.2% | 34.5% | +0.077 | +0.008 to +0.145 | $+118.10 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 30 | 60.0% | 51.8% | +0.082 | -0.087 to +0.251 | $+24.67 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1748 vs market 0.1889 -> **model is sharper**

## 3:00 left (275 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 275 | 66.5% | 61.5% | +0.051 | +0.005 to +0.097 | $+139.06 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 275 | 78.9% | 75.2% | +0.037 | -0.009 to +0.083 | $+101.90 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 170 | 32.4% | 28.4% | +0.040 | -0.016 to +0.095 | $+67.53 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 11 | 100.0% | 71.1% | +0.289 | +0.251 to +0.327 | $+31.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1503 vs market 0.1565 -> **model is sharper**

## 2:00 left (285 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 266 | 62.0% | 60.1% | +0.019 | -0.021 to +0.059 | $+51.55 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 261 | 87.4% | 80.6% | +0.068 | +0.028 to +0.108 | $+177.64 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 216 | 22.7% | 21.8% | +0.009 | -0.032 to +0.050 | $+19.68 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1126 vs market 0.1118 -> **market is sharper**

## 1:00 left (285 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 212 | 49.1% | 46.4% | +0.027 | -0.012 to +0.065 | $+56.40 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 176 | 92.0% | 83.0% | +0.090 | +0.047 to +0.134 | $+158.75 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 247 | 15.0% | 11.7% | +0.033 | +0.003 to +0.062 | $+80.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0675 vs market 0.0795 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=300, bias $-0.12, sd $0.94 (set BASIS_SD near 1)
- spot at open: n=300, bias $-1.89, sd $24.07 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 301 | 161 | 55% | 60% |
| 60%-70% | 300 | 185 | 65% | 73% |
| 70%-80% | 257 | 176 | 75% | 84% |
| 80%-90% | 497 | 230 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 252 | 1186 | 0.1386 | 0.1485 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 300 (252 with decision logging, v16+)
- Markets with a signal: 93
- Alerts attempted: 35 · delivered: 34 · delivery failed: 1
- Simulated fills (quote available, size not verified): 6
- Expired alerts: 28 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 45 markets, would have won 33, +54.49 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 18 markets, would have won 16, +69.64 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 4 markets, would have won 4, +14.81 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 33/34 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 263 · valid comparisons: 247
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 9 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.44, typical gap $2.99, worst $12.31
- Coinbase would have named the wrong winner: 3/247 (1.2%)
- Rounds settling within $10 of the target: 31, wrong winner 3 (10%)
- Rounds settling within $25 of the target: 68, wrong winner 3 (4%)
- Rounds settling within $50 of the target: 117, wrong winner 3 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 34 (goal: 300)
- Simulated paper trades: 6 · no-trade (expired/unconfirmed): 28
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/6 = 17% vs break-even 42.3% (price paid + fee)
- Paper P&L after fees: -48.03 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 35
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 34)
- Polymarket quote round trip: median 31 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1445 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 10/34 | 24 | 0 | -4.02 |
| 10s | 10/34 | 24 | 0 | -4.02 |
| 20s | 8/34 | 26 | 0 | -26.59 |
| 30s | 6/34 | 28 | 0 | -48.03 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 24 · loops: 39587 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
