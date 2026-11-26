---
polybot_auto: true
updated: 2026-11-26 13:07 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 13:05 UTC | 1478 checkpoints logged | 1316 graded | 290 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 242 settled rounds observed · 33 alerts (32 delivered) · **6 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/237 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 15
2. **Model vs market accuracy (Brier, lower is better):** model 0.1381 vs market 0.1477 on 242 rounds -> model sharper
3. **Simulated profit after fees:** -48.03 on 6 trades of $10 · win rate 17% vs break-even 42%, 95% range per trade -13.12 to -2.89
4. **Quote available at simulated tap (size not verified):** 5s 10/32 · 10s 10/32 · 20s 8/32 · 30s 6/32
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 23 runs, stalls over 5s 2/37939 loops, longest BTC price gap 10.7s · checks with no market quote 65/1206 (book fallback used 459) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 6/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (245 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 245 | 68.6% | 66.0% | +0.026 | -0.032 to +0.084 | $+63.89 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 245 | 66.9% | 68.4% | -0.015 | -0.073 to +0.044 | $-36.04 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 131 | 54.2% | 39.6% | +0.146 | +0.070 to +0.221 | $+191.01 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 53 | 71.7% | 50.6% | +0.211 | +0.094 to +0.328 | $+111.92 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1991 vs market 0.2189 -> **model is sharper**

## 3:30 left (256 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 256 | 72.3% | 64.7% | +0.075 | +0.024 to +0.127 | $+192.83 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 256 | 76.2% | 72.7% | +0.035 | -0.018 to +0.088 | $+89.77 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 148 | 42.6% | 34.2% | +0.084 | +0.014 to +0.153 | $+123.62 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 28 | 64.3% | 52.1% | +0.122 | -0.050 to +0.294 | $+34.14 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1746 vs market 0.1879 -> **model is sharper**

## 3:00 left (265 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 265 | 66.8% | 61.4% | +0.054 | +0.007 to +0.101 | $+143.71 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 265 | 78.9% | 75.4% | +0.035 | -0.013 to +0.082 | $+91.55 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 164 | 32.9% | 28.1% | +0.049 | -0.008 to +0.105 | $+79.61 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 10 | 100.0% | 71.1% | +0.289 | +0.247 to +0.331 | $+28.91 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1509 vs market 0.1585 -> **model is sharper**

## 2:00 left (275 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 256 | 63.7% | 60.3% | +0.033 | -0.007 to +0.073 | $+85.54 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 251 | 88.0% | 80.9% | +0.072 | +0.032 to +0.111 | $+180.10 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 207 | 21.7% | 20.6% | +0.012 | -0.030 to +0.053 | $+24.13 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 13 | 100.0% | 75.1% | +0.249 | +0.216 to +0.283 | $+32.43 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1098 vs market 0.1088 -> **market is sharper**

## 1:00 left (275 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 203 | 47.3% | 45.5% | +0.018 | -0.021 to +0.057 | $+36.47 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 167 | 91.6% | 83.4% | +0.082 | +0.037 to +0.127 | $+137.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 238 | 14.3% | 11.5% | +0.028 | -0.002 to +0.057 | $+65.87 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0680 vs market 0.0768 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=290, bias $-0.13, sd $0.95 (set BASIS_SD near 1)
- spot at open: n=290, bias $-1.71, sd $24.40 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 288 | 155 | 55% | 60% |
| 60%-70% | 284 | 176 | 65% | 72% |
| 70%-80% | 247 | 168 | 75% | 85% |
| 80%-90% | 486 | 224 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 242 | 1136 | 0.1381 | 0.1477 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 290 (242 with decision logging, v16+)
- Markets with a signal: 86
- Alerts attempted: 33 · delivered: 32 · delivery failed: 1
- Simulated fills (quote available, size not verified): 6
- Expired alerts: 26 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 41 markets, would have won 31, +58.65 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 18 markets, would have won 16, +69.64 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 3 markets, would have won 3, +11.53 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 31/32 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 252 · valid comparisons: 237
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 8 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.31, typical gap $2.98, worst $12.31
- Coinbase would have named the wrong winner: 3/237 (1.3%)
- Rounds settling within $10 of the target: 30, wrong winner 3 (10%)
- Rounds settling within $25 of the target: 62, wrong winner 3 (5%)
- Rounds settling within $50 of the target: 108, wrong winner 3 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 32 (goal: 300)
- Simulated paper trades: 6 · no-trade (expired/unconfirmed): 26
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/6 = 17% vs break-even 42.3% (price paid + fee)
- Paper P&L after fees: -48.03 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 33
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1386 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 10/32 | 22 | 0 | -4.02 |
| 10s | 10/32 | 22 | 0 | -4.02 |
| 20s | 8/32 | 24 | 0 | -26.59 |
| 30s | 6/32 | 26 | 0 | -48.03 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 23 · loops: 37939 · loops over 5s: 2 (0.01%)
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
