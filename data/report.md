# polybot report

Updated 2026-11-26 10:19 UTC | 1325 checkpoints logged | 1164 graded | 259 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 211 settled rounds observed · 30 alerts (29 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/209 valid rounds (0.5%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1327 vs market 0.1421 on 211 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/29 · 10s 8/29 · 20s 6/29 · 30s 4/29
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 20 runs, stalls over 5s 2/32990 loops, longest BTC price gap 10.7s · checks with no market quote 64/1053 (book fallback used 394) · bad close samples 5 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (216 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 216 | 71.8% | 65.9% | +0.059 | -0.002 to +0.119 | $+126.44 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 216 | 69.0% | 68.6% | +0.004 | -0.057 to +0.065 | $+8.20 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 118 | 53.4% | 40.2% | +0.132 | +0.053 to +0.212 | $+156.11 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 50 | 72.0% | 50.2% | +0.218 | +0.097 to +0.339 | $+108.90 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1921 vs market 0.2104 -> **model is sharper**

## 3:30 left (226 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 226 | 73.0% | 65.1% | +0.079 | +0.026 to +0.133 | $+179.52 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 226 | 77.0% | 72.8% | +0.041 | -0.013 to +0.096 | $+93.71 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 127 | 40.2% | 33.7% | +0.065 | -0.008 to +0.138 | $+82.41 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 24 | 62.5% | 52.0% | +0.105 | -0.085 to +0.296 | $+25.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1696 vs market 0.1801 -> **model is sharper**

## 3:00 left (234 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 234 | 67.9% | 61.5% | +0.065 | +0.016 to +0.113 | $+151.04 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 234 | 80.8% | 75.5% | +0.053 | +0.004 to +0.102 | $+123.86 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 145 | 33.8% | 28.6% | +0.052 | -0.008 to +0.112 | $+75.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 9 | 100.0% | 71.2% | +0.288 | +0.241 to +0.335 | $+25.92 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1450 vs market 0.1528 -> **model is sharper**

## 2:00 left (244 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 228 | 61.0% | 58.8% | +0.022 | -0.021 to +0.064 | $+49.06 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 223 | 88.3% | 81.0% | +0.074 | +0.032 to +0.116 | $+164.19 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 186 | 23.1% | 21.6% | +0.015 | -0.029 to +0.060 | $+28.26 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 13 | 100.0% | 75.1% | +0.249 | +0.216 to +0.283 | $+32.43 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1084 vs market 0.1092 -> **model is sharper**

## 1:00 left (244 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 179 | 45.8% | 45.0% | +0.008 | -0.034 to +0.049 | $+14.04 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 145 | 91.7% | 82.9% | +0.088 | +0.040 to +0.136 | $+127.36 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 209 | 14.8% | 11.6% | +0.032 | +0.001 to +0.064 | $+67.92 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0673 vs market 0.0777 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=259, bias $-0.14, sd $1.01 (set BASIS_SD near 1)
- spot at open: n=259, bias $-1.43, sd $25.62 (set BASIS_SD near 26)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 242 | 132 | 55% | 61% |
| 60%-70% | 248 | 153 | 65% | 74% |
| 70%-80% | 222 | 150 | 75% | 85% |
| 80%-90% | 441 | 204 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 211 | 984 | 0.1327 | 0.1421 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 259 (211 with decision logging, v16+)
- Markets with a signal: 79
- Alerts attempted: 30 · delivered: 29 · delivery failed: 1
- Simulated fills (quote available, size not verified): 4
- Expired alerts: 25 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 38 markets, would have won 28, +47.04 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 17 markets, would have won 15, +64.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 3 markets, would have won 3, +11.53 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 28/29 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 219 · valid comparisons: 209
- Missing/untrusted: 5 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.07, typical gap $2.86, worst $12.31
- Coinbase would have named the wrong winner: 1/209 (0.5%)
- Rounds settling within $10 of the target: 22, wrong winner 1 (5%)
- Rounds settling within $25 of the target: 49, wrong winner 1 (2%)
- Rounds settling within $50 of the target: 91, wrong winner 1 (1%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 29 (goal: 300)
- Simulated paper trades: 4 · no-trade (expired/unconfirmed): 25
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/4 = 25% vs break-even 43.9% (price paid + fee)
- Paper P&L after fees: -26.83 at $10 a trade · max drawdown: -26.83

## Ticket speed (measured, not assumed)

- Tickets: 30
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 33 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 8/29 | 21 | 0 | +16.97 |
| 10s | 8/29 | 21 | 0 | +16.97 |
| 20s | 6/29 | 23 | 0 | -5.60 |
| 30s | 4/29 | 25 | 0 | -26.83 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 20 · loops: 32990 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
