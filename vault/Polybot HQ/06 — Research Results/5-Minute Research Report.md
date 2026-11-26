---
polybot_auto: true
updated: 2026-11-26 09:24 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 09:24 UTC | 1271 checkpoints logged | 1110 graded | 248 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 200 settled rounds observed · 29 alerts (28 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/199 valid rounds (0.5%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1349 vs market 0.1451 on 200 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/28 · 10s 8/28 · 20s 6/28 · 30s 4/28
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 19 runs, stalls over 5s 2/31340 loops, longest BTC price gap 10.7s · checks with no market quote 64/999 (book fallback used 379) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (206 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 206 | 70.4% | 66.1% | +0.043 | -0.019 to +0.105 | $+88.57 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 206 | 68.0% | 68.8% | -0.008 | -0.071 to +0.055 | $-16.38 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 115 | 52.2% | 39.9% | +0.123 | +0.042 to +0.204 | $+141.19 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 48 | 70.8% | 49.9% | +0.209 | +0.083 to +0.335 | $+100.36 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1952 vs market 0.2118 -> **model is sharper**

## 3:30 left (215 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 215 | 72.6% | 65.2% | +0.074 | +0.018 to +0.130 | $+158.79 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 215 | 76.3% | 72.9% | +0.034 | -0.023 to +0.090 | $+72.08 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 121 | 38.8% | 32.8% | +0.060 | -0.015 to +0.136 | $+72.83 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 20 | 60.0% | 51.5% | +0.085 | -0.132 to +0.301 | $+16.97 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1728 vs market 0.1822 -> **model is sharper**

## 3:00 left (223 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 223 | 69.1% | 61.9% | +0.071 | +0.021 to +0.122 | $+159.23 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 223 | 80.3% | 75.3% | +0.050 | -0.001 to +0.101 | $+111.10 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 140 | 35.0% | 29.0% | +0.060 | -0.001 to +0.122 | $+84.62 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 9 | 100.0% | 71.2% | +0.288 | +0.241 to +0.335 | $+25.92 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1474 vs market 0.1567 -> **model is sharper**

## 2:00 left (233 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 218 | 61.0% | 58.9% | +0.021 | -0.023 to +0.066 | $+46.78 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 214 | 87.9% | 80.8% | +0.071 | +0.027 to +0.115 | $+151.36 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 177 | 23.7% | 21.6% | +0.021 | -0.025 to +0.068 | $+37.92 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 12 | 100.0% | 74.6% | +0.254 | +0.219 to +0.289 | $+30.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1098 vs market 0.1129 -> **model is sharper**

## 1:00 left (233 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 170 | 45.9% | 45.0% | +0.009 | -0.035 to +0.052 | $+15.02 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 137 | 91.2% | 82.5% | +0.087 | +0.036 to +0.138 | $+119.78 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 199 | 15.1% | 11.5% | +0.035 | +0.003 to +0.068 | $+70.55 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0677 vs market 0.0807 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=248, bias $-0.15, sd $1.03 (set BASIS_SD near 1)
- spot at open: n=248, bias $-1.23, sd $26.12 (set BASIS_SD near 26)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 231 | 126 | 55% | 60% |
| 60%-70% | 238 | 147 | 65% | 73% |
| 70%-80% | 213 | 146 | 75% | 84% |
| 80%-90% | 417 | 194 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 200 | 930 | 0.1349 | 0.1451 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 248 (200 with decision logging, v16+)
- Markets with a signal: 72
- Alerts attempted: 29 · delivered: 28 · delivery failed: 1
- Simulated fills (quote available, size not verified): 4
- Expired alerts: 24 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 36 markets, would have won 27, +49.22 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 14 markets, would have won 12, +51.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 3 markets, would have won 3, +11.53 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 27/28 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 208 · valid comparisons: 199
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.09, typical gap $2.85, worst $12.31
- Coinbase would have named the wrong winner: 1/199 (0.5%)
- Rounds settling within $10 of the target: 20, wrong winner 1 (5%)
- Rounds settling within $25 of the target: 44, wrong winner 1 (2%)
- Rounds settling within $50 of the target: 84, wrong winner 1 (1%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 27 (goal: 300)
- Simulated paper trades: 4 · no-trade (expired/unconfirmed): 23
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/4 = 25% vs break-even 43.9% (price paid + fee)
- Paper P&L after fees: -26.83 at $10 a trade · max drawdown: -26.83

## Ticket speed (measured, not assumed)

- Tickets: 29
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 33 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 8/27 | 19 | 0 | +16.97 |
| 10s | 8/27 | 19 | 0 | +16.97 |
| 20s | 6/27 | 21 | 0 | -5.60 |
| 30s | 4/27 | 23 | 0 | -26.83 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 19 · loops: 31340 · loops over 5s: 2 (0.01%)
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
