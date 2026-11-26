---
polybot_auto: true
updated: 2026-11-26 08:42 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 08:28 UTC | 1217 checkpoints logged | 1057 graded | 237 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 189 settled rounds observed · 27 alerts (26 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/188 valid rounds (0.5%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1340 vs market 0.1448 on 189 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/26 · 10s 8/26 · 20s 6/26 · 30s 4/26
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 18 runs, stalls over 5s 2/29692 loops, longest BTC price gap 10.7s · checks with no market quote 64/945 (book fallback used 358) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (196 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 196 | 69.9% | 66.1% | +0.038 | -0.026 to +0.102 | $+74.37 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 196 | 67.9% | 68.9% | -0.011 | -0.075 to +0.054 | $-21.27 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 110 | 52.7% | 39.9% | +0.128 | +0.046 to +0.210 | $+140.79 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 46 | 71.7% | 49.6% | +0.221 | +0.094 to +0.349 | $+101.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1963 vs market 0.2120 -> **model is sharper**

## 3:30 left (204 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 204 | 73.5% | 65.6% | +0.079 | +0.022 to +0.136 | $+161.18 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 204 | 76.5% | 72.9% | +0.036 | -0.022 to +0.094 | $+73.34 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 116 | 39.7% | 33.0% | +0.066 | -0.011 to +0.144 | $+76.83 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 20 | 60.0% | 51.5% | +0.085 | -0.132 to +0.301 | $+16.97 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1716 vs market 0.1818 -> **model is sharper**

## 3:00 left (212 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 212 | 69.8% | 62.5% | +0.073 | +0.021 to +0.125 | $+154.96 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 212 | 80.2% | 75.5% | +0.047 | -0.006 to +0.099 | $+99.20 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 134 | 34.3% | 28.4% | +0.059 | -0.004 to +0.122 | $+79.10 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 7 | 100.0% | 71.7% | +0.283 | +0.224 to +0.342 | $+19.83 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1469 vs market 0.1568 -> **model is sharper**

## 2:00 left (222 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 208 | 60.6% | 58.5% | +0.021 | -0.025 to +0.066 | $+43.15 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 204 | 88.2% | 80.8% | +0.075 | +0.030 to +0.120 | $+152.43 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 168 | 23.8% | 21.6% | +0.022 | -0.025 to +0.070 | $+37.40 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 11 | 100.0% | 74.2% | +0.258 | +0.220 to +0.295 | $+28.35 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1093 vs market 0.1142 -> **model is sharper**

## 1:00 left (223 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 164 | 45.7% | 45.4% | +0.003 | -0.041 to +0.047 | $+4.71 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 132 | 91.7% | 82.3% | +0.093 | +0.042 to +0.144 | $+123.23 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 190 | 15.3% | 11.8% | +0.034 | +0.001 to +0.068 | $+64.86 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0667 vs market 0.0801 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=237, bias $-0.16, sd $1.05 (set BASIS_SD near 1)
- spot at open: n=237, bias $-1.29, sd $26.54 (set BASIS_SD near 27)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 225 | 123 | 55% | 60% |
| 60%-70% | 216 | 136 | 65% | 74% |
| 70%-80% | 204 | 138 | 75% | 83% |
| 80%-90% | 401 | 186 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 189 | 877 | 0.134 | 0.1448 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 237 (189 with decision logging, v16+)
- Markets with a signal: 67
- Alerts attempted: 27 · delivered: 26 · delivery failed: 1
- Simulated fills (quote available, size not verified): 4
- Expired alerts: 22 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 33 markets, would have won 24, +41.00 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 14 markets, would have won 12, +51.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 25/26 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 197 · valid comparisons: 188
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.13, typical gap $2.88, worst $12.31
- Coinbase would have named the wrong winner: 1/188 (0.5%)
- Rounds settling within $10 of the target: 19, wrong winner 1 (5%)
- Rounds settling within $25 of the target: 40, wrong winner 1 (2%)
- Rounds settling within $50 of the target: 80, wrong winner 1 (1%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 26 (goal: 300)
- Simulated paper trades: 4 · no-trade (expired/unconfirmed): 22
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/4 = 25% vs break-even 43.9% (price paid + fee)
- Paper P&L after fees: -26.83 at $10 a trade · max drawdown: -26.83

## Ticket speed (measured, not assumed)

- Tickets: 27
- Coinbase trade -> we received it: median 1045 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 8/26 | 18 | 0 | +16.97 |
| 10s | 8/26 | 18 | 0 | +16.97 |
| 20s | 6/26 | 20 | 0 | -5.60 |
| 30s | 4/26 | 22 | 0 | -26.83 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 18 · loops: 29692 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
