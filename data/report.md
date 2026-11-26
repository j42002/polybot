# polybot report

Updated 2026-11-26 15:51 UTC | 1629 checkpoints logged | 1466 graded | 320 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 272 settled rounds observed · 38 alerts (37 delivered) · **6 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/267 valid rounds (1.1%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1394 vs market 0.1470 on 272 rounds -> model sharper
3. **Simulated profit after fees:** -48.03 on 6 trades of $10 · win rate 17% vs break-even 42%, 95% range per trade -13.12 to -2.89
4. **Quote available at simulated tap (size not verified):** 5s 10/37 · 10s 10/37 · 20s 8/37 · 30s 6/37
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 26 runs, stalls over 5s 3/42887 loops, longest BTC price gap 10.7s · checks with no market quote 65/1357 (book fallback used 534) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 6/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (275 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 275 | 68.4% | 65.5% | +0.029 | -0.025 to +0.083 | $+79.79 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 275 | 66.9% | 68.3% | -0.013 | -0.068 to +0.041 | $-37.02 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 144 | 54.2% | 40.2% | +0.140 | +0.069 to +0.211 | $+201.12 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 58 | 72.4% | 51.2% | +0.212 | +0.100 to +0.324 | $+123.00 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1975 vs market 0.2140 -> **model is sharper**

## 3:30 left (286 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 286 | 71.3% | 64.6% | +0.067 | +0.018 to +0.116 | $+191.55 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 286 | 75.9% | 72.2% | +0.037 | -0.013 to +0.087 | $+105.50 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 165 | 41.8% | 34.0% | +0.078 | +0.012 to +0.144 | $+128.80 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 31 | 61.3% | 51.3% | +0.100 | -0.067 to +0.266 | $+30.85 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1742 vs market 0.1886 -> **model is sharper**

## 3:00 left (295 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 295 | 66.1% | 61.6% | +0.045 | +0.001 to +0.090 | $+133.80 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 295 | 78.3% | 75.3% | +0.030 | -0.015 to +0.075 | $+88.87 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 187 | 31.0% | 28.0% | +0.030 | -0.022 to +0.083 | $+56.90 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 11 | 100.0% | 71.1% | +0.289 | +0.251 to +0.327 | $+31.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1518 vs market 0.1557 -> **model is sharper**

## 2:00 left (305 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 284 | 61.3% | 59.0% | +0.023 | -0.016 to +0.062 | $+64.72 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 279 | 86.7% | 80.6% | +0.061 | +0.023 to +0.100 | $+170.88 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 232 | 22.4% | 21.7% | +0.007 | -0.033 to +0.047 | $+16.81 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1136 vs market 0.1114 -> **market is sharper**

## 1:00 left (305 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 225 | 49.3% | 46.8% | +0.026 | -0.011 to +0.062 | $+57.66 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 188 | 92.0% | 82.9% | +0.091 | +0.050 to +0.132 | $+171.55 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 265 | 14.3% | 11.7% | +0.027 | -0.001 to +0.055 | $+71.08 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0684 vs market 0.0754 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=320, bias $-0.12, sd $0.91 (set BASIS_SD near 1)
- spot at open: n=320, bias $-1.55, sd $24.56 (set BASIS_SD near 25)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 331 | 174 | 55% | 59% |
| 60%-70% | 317 | 195 | 65% | 73% |
| 70%-80% | 272 | 184 | 75% | 85% |
| 80%-90% | 535 | 243 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 272 | 1286 | 0.1394 | 0.147 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 320 (272 with decision logging, v16+)
- Markets with a signal: 96
- Alerts attempted: 38 · delivered: 37 · delivery failed: 1
- Simulated fills (quote available, size not verified): 6
- Expired alerts: 31 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 45 markets, would have won 33, +54.49 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 18 markets, would have won 16, +69.64 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 4 markets, would have won 4, +14.81 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 35/37 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 285 · valid comparisons: 267
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.59, typical gap $2.96, worst $12.31
- Coinbase would have named the wrong winner: 3/267 (1.1%)
- Rounds settling within $10 of the target: 32, wrong winner 3 (9%)
- Rounds settling within $25 of the target: 74, wrong winner 3 (4%)
- Rounds settling within $50 of the target: 127, wrong winner 3 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 37 (goal: 300)
- Simulated paper trades: 6 · no-trade (expired/unconfirmed): 31
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/6 = 17% vs break-even 42.3% (price paid + fee)
- Paper P&L after fees: -48.03 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 38
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 10/37 | 27 | 0 | -4.02 |
| 10s | 10/37 | 27 | 0 | -4.02 |
| 20s | 8/37 | 29 | 0 | -26.59 |
| 30s | 6/37 | 31 | 0 | -48.03 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 26 · loops: 42887 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
