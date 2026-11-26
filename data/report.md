# polybot report

Updated 2026-11-26 11:14 UTC | 1378 checkpoints logged | 1216 graded | 270 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 222 settled rounds observed · 30 alerts (29 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/219 valid rounds (0.5%) where Coinbase points at the wrong winner · missing 11
2. **Model vs market accuracy (Brier, lower is better):** model 0.1332 vs market 0.1420 on 222 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/29 · 10s 8/29 · 20s 6/29 · 30s 4/29
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 21 runs, stalls over 5s 2/34640 loops, longest BTC price gap 10.7s · checks with no market quote 65/1106 (book fallback used 418) · bad close samples 6 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (225 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 225 | 71.1% | 66.1% | +0.050 | -0.009 to +0.109 | $+113.44 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 225 | 68.9% | 68.8% | +0.001 | -0.058 to +0.061 | $+3.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 122 | 52.5% | 39.6% | +0.128 | +0.050 to +0.206 | $+156.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 50 | 72.0% | 50.2% | +0.218 | +0.097 to +0.339 | $+108.90 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1919 vs market 0.2095 -> **model is sharper**

## 3:30 left (236 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 236 | 72.5% | 65.1% | +0.074 | +0.021 to +0.127 | $+173.64 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 236 | 76.7% | 72.9% | +0.038 | -0.016 to +0.091 | $+88.54 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 133 | 39.8% | 33.2% | +0.066 | -0.005 to +0.138 | $+87.96 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 24 | 62.5% | 52.0% | +0.105 | -0.085 to +0.296 | $+25.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1708 vs market 0.1815 -> **model is sharper**

## 3:00 left (245 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 245 | 66.5% | 61.1% | +0.055 | +0.006 to +0.103 | $+134.10 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 245 | 80.4% | 75.5% | +0.049 | +0.001 to +0.098 | $+120.29 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 153 | 34.0% | 28.5% | +0.055 | -0.004 to +0.114 | $+84.20 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 9 | 100.0% | 71.2% | +0.288 | +0.241 to +0.335 | $+25.92 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1462 vs market 0.1550 -> **model is sharper**

## 2:00 left (255 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 238 | 62.2% | 59.4% | +0.027 | -0.014 to +0.069 | $+65.45 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 233 | 88.4% | 80.7% | +0.078 | +0.037 to +0.118 | $+180.58 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 192 | 22.4% | 21.2% | +0.012 | -0.031 to +0.055 | $+22.44 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 13 | 100.0% | 75.1% | +0.249 | +0.216 to +0.283 | $+32.43 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1081 vs market 0.1078 -> **market is sharper**

## 1:00 left (255 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 187 | 46.0% | 44.8% | +0.012 | -0.028 to +0.052 | $+22.26 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 153 | 91.5% | 82.9% | +0.086 | +0.039 to +0.132 | $+131.23 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 219 | 14.6% | 11.7% | +0.029 | -0.001 to +0.060 | $+63.84 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0675 vs market 0.0755 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=270, bias $-0.14, sd $0.99 (set BASIS_SD near 1)
- spot at open: n=270, bias $-1.46, sd $25.14 (set BASIS_SD near 25)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 258 | 139 | 55% | 60% |
| 60%-70% | 260 | 161 | 65% | 74% |
| 70%-80% | 231 | 156 | 75% | 85% |
| 80%-90% | 456 | 209 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 222 | 1036 | 0.1332 | 0.142 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 270 (222 with decision logging, v16+)
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

- Rounds with a logged close: 230 · valid comparisons: 219
- Missing/untrusted: 6 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.09, typical gap $2.91, worst $12.31
- Coinbase would have named the wrong winner: 1/219 (0.5%)
- Rounds settling within $10 of the target: 26, wrong winner 1 (4%)
- Rounds settling within $25 of the target: 55, wrong winner 1 (2%)
- Rounds settling within $50 of the target: 98, wrong winner 1 (1%)

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

- Runs: 21 · loops: 34640 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
