# polybot report

Updated 2026-11-26 16:47 UTC | 1680 checkpoints logged | 1517 graded | 331 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 283 settled rounds observed · 40 alerts (39 delivered) · **7 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/278 valid rounds (1.4%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1418 vs market 0.1501 on 283 rounds -> model sharper
3. **Simulated profit after fees:** -41.74 on 7 trades of $10 · win rate 29% vs break-even 45%, 95% range per trade -11.86 to -0.07
4. **Quote available at simulated tap (size not verified):** 5s 11/39 · 10s 11/39 · 20s 9/39 · 30s 7/39
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 27 runs, stalls over 5s 3/44537 loops, longest BTC price gap 10.7s · checks with no market quote 65/1408 (book fallback used 561) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 7/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (286 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 286 | 67.8% | 65.1% | +0.027 | -0.026 to +0.081 | $+78.17 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 286 | 66.8% | 68.1% | -0.013 | -0.067 to +0.041 | $-36.34 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 150 | 54.0% | 40.3% | +0.137 | +0.068 to +0.207 | $+205.98 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 61 | 72.1% | 50.8% | +0.213 | +0.104 to +0.322 | $+129.82 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1991 vs market 0.2153 -> **model is sharper**

## 3:30 left (296 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 296 | 70.6% | 64.6% | +0.060 | +0.012 to +0.109 | $+178.85 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 296 | 75.3% | 72.0% | +0.034 | -0.016 to +0.083 | $+99.20 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 170 | 41.2% | 34.1% | +0.071 | +0.006 to +0.136 | $+120.92 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 33 | 60.6% | 51.6% | +0.090 | -0.070 to +0.251 | $+29.80 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1754 vs market 0.1890 -> **model is sharper**

## 3:00 left (305 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 305 | 65.9% | 61.7% | +0.042 | -0.002 to +0.086 | $+128.21 | NO EDGE |
| Lean (bet the side BTC is on now) | 305 | 78.0% | 75.2% | +0.028 | -0.016 to +0.072 | $+84.89 | NO EDGE |
| Edge (model beats the ask by 3c+) | 193 | 30.6% | 28.3% | +0.023 | -0.029 to +0.075 | $+44.16 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 12 | 91.7% | 71.2% | +0.205 | +0.037 to +0.374 | $+24.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1528 vs market 0.1555 -> **model is sharper**

## 2:00 left (315 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 293 | 61.1% | 59.0% | +0.021 | -0.018 to +0.060 | $+61.63 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 288 | 85.8% | 80.7% | +0.051 | +0.012 to +0.090 | $+146.61 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 239 | 23.0% | 21.5% | +0.015 | -0.025 to +0.055 | $+36.44 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1163 vs market 0.1159 -> **market is sharper**

## 1:00 left (315 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 233 | 48.9% | 46.6% | +0.023 | -0.014 to +0.061 | $+54.36 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 194 | 90.7% | 82.9% | +0.078 | +0.035 to +0.122 | $+151.79 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 273 | 15.0% | 11.7% | +0.033 | +0.005 to +0.062 | $+91.34 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0718 vs market 0.0824 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=331, bias $-0.11, sd $0.89 (set BASIS_SD near 1)
- spot at open: n=331, bias $-1.86, sd $24.64 (set BASIS_SD near 25)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 347 | 183 | 55% | 58% |
| 60%-70% | 329 | 202 | 65% | 72% |
| 70%-80% | 280 | 190 | 75% | 84% |
| 80%-90% | 550 | 249 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 283 | 1337 | 0.1418 | 0.1501 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 331 (283 with decision logging, v16+)
- Markets with a signal: 102
- Alerts attempted: 40 · delivered: 39 · delivery failed: 1
- Simulated fills (quote available, size not verified): 7
- Expired alerts: 32 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 46 markets, would have won 33, +47.29 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 21 markets, would have won 18, +75.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 37/39 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 296 · valid comparisons: 278
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.57, typical gap $2.92, worst $12.31
- Coinbase would have named the wrong winner: 4/278 (1.4%)
- Rounds settling within $10 of the target: 33, wrong winner 4 (12%)
- Rounds settling within $25 of the target: 76, wrong winner 4 (5%)
- Rounds settling within $50 of the target: 131, wrong winner 4 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 38 (goal: 300)
- Simulated paper trades: 7 · no-trade (expired/unconfirmed): 31
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 2/7 = 29% vs break-even 45.2% (price paid + fee)
- Paper P&L after fees: -41.74 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 40
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 11/38 | 27 | 0 | +2.27 |
| 10s | 11/38 | 27 | 0 | +2.27 |
| 20s | 9/38 | 29 | 0 | -20.30 |
| 30s | 7/38 | 31 | 0 | -41.74 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 27 · loops: 44537 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
