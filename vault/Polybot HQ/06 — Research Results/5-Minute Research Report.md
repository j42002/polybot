---
polybot_auto: true
updated: 2026-11-26 01:33 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 01:06 UTC | 793 checkpoints logged | 631 graded | 148 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 100 settled rounds observed · 10 alerts (10 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/99 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1377 vs market 0.1426 on 100 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/10 · 10s 4/10 · 20s 4/10 · 30s 3/10
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 10 runs, stalls over 5s 1/16497 loops, longest BTC price gap 9.0s · checks with no market quote 64/521 (book fallback used 183) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (107 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 107 | 67.3% | 65.5% | +0.018 | -0.070 to +0.105 | $+18.93 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 107 | 63.6% | 68.5% | -0.050 | -0.138 to +0.038 | $-53.13 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 59 | 47.5% | 36.2% | +0.113 | +0.001 to +0.225 | $+66.53 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 23 | 73.9% | 47.1% | +0.268 | +0.092 to +0.444 | $+61.64 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2073 vs market 0.2148 -> **model is sharper**

## 3:30 left (117 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 117 | 71.8% | 66.1% | +0.057 | -0.022 to +0.135 | $+66.36 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 117 | 73.5% | 72.7% | +0.008 | -0.071 to +0.087 | $+9.34 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 61 | 37.7% | 31.6% | +0.062 | -0.050 to +0.173 | $+37.54 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 10 | 50.0% | 49.3% | +0.007 | -0.320 to +0.334 | $+0.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1815 vs market 0.1916 -> **model is sharper**

## 3:00 left (126 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 126 | 65.9% | 62.8% | +0.031 | -0.040 to +0.102 | $+38.65 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 126 | 75.4% | 76.7% | -0.013 | -0.084 to +0.059 | $-15.83 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 71 | 26.8% | 25.4% | +0.014 | -0.073 to +0.101 | $+10.00 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1677 vs market 0.1663 -> **market is sharper**

## 2:00 left (139 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 131 | 61.1% | 58.8% | +0.023 | -0.036 to +0.081 | $+29.63 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 128 | 86.7% | 81.6% | +0.051 | -0.008 to +0.110 | $+65.61 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 103 | 22.3% | 21.1% | +0.012 | -0.051 to +0.075 | $+12.44 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 6 | 100.0% | 73.1% | +0.269 | +0.204 to +0.335 | $+16.16 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1154 vs market 0.1174 -> **model is sharper**

## 1:00 left (142 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 101 | 50.5% | 47.7% | +0.028 | -0.030 to +0.087 | $+28.68 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 85 | 91.8% | 82.5% | +0.093 | +0.028 to +0.159 | $+79.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 114 | 14.9% | 11.5% | +0.034 | -0.010 to +0.078 | $+38.40 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0668 vs market 0.0815 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=148, bias $-0.25, sd $1.32 (set BASIS_SD near 1)
- spot at open: n=148, bias $-0.78, sd $30.58 (set BASIS_SD near 31)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 131 | 75 | 55% | 58% |
| 60%-70% | 128 | 85 | 65% | 69% |
| 70%-80% | 124 | 83 | 74% | 81% |
| 80%-90% | 237 | 115 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 100 | 451 | 0.1377 | 0.1426 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 148 (100 with decision logging, v16+)
- Markets with a signal: 30
- Alerts attempted: 10 · delivered: 10 · delivery failed: 0
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 7 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 14 markets, would have won 10, +25.96 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 7 markets, would have won 6, +26.06 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 9/10 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 109 · valid comparisons: 99
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.62, typical gap $2.75, worst $12.31
- Coinbase would have named the wrong winner: 0/99 (0.0%)
- Rounds settling within $10 of the target: 7, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 15, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 33, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 10 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 7
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 10
- Coinbase trade -> we received it: median 1146 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 30)
- Polymarket quote round trip: median 34 ms (worst 48)
- Price read -> decision made: median 88 ms (worst 105)
- Decision -> Discord accepted: median 1665 ms (worst 3027)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 4/10 | 6 | 0 | +1.17 |
| 10s | 4/10 | 6 | 0 | +1.17 |
| 20s | 4/10 | 6 | 0 | +1.17 |
| 30s | 3/10 | 7 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 10 · loops: 16497 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
