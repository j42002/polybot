---
polybot_auto: true
updated: 2026-11-26 21:23 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 21:23 UTC | 1947 checkpoints logged | 1786 graded | 387 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 339 settled rounds observed · 53 alerts (52 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/334 valid rounds (1.5%) where Coinbase points at the wrong winner · missing 17
2. **Model vs market accuracy (Brier, lower is better):** model 0.1529 vs market 0.1615 on 339 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 13/52 · 10s 13/52 · 20s 11/52 · 30s 9/52
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 32 runs, stalls over 5s 3/52787 loops, longest BTC price gap 10.7s · checks with no market quote 65/1675 (book fallback used 690) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (342 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 342 | 65.5% | 64.3% | +0.012 | -0.038 to +0.061 | $+39.56 | NO EDGE |
| Lean (bet the side BTC is on now) | 342 | 64.9% | 67.4% | -0.025 | -0.075 to +0.025 | $-85.90 | NO EDGE |
| Edge (model beats the ask by 3c+) | 179 | 52.5% | 41.0% | +0.115 | +0.049 to +0.181 | $+206.29 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 79 | 68.4% | 51.2% | +0.171 | +0.068 to +0.274 | $+135.22 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2089 vs market 0.2200 -> **model is sharper**

## 3:30 left (351 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 351 | 68.4% | 64.1% | +0.043 | -0.003 to +0.089 | $+150.16 | NO EDGE |
| Lean (bet the side BTC is on now) | 351 | 72.1% | 71.1% | +0.009 | -0.037 to +0.056 | $+32.85 | NO EDGE |
| Edge (model beats the ask by 3c+) | 198 | 41.4% | 34.9% | +0.065 | +0.004 to +0.126 | $+128.43 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 40 | 57.5% | 51.4% | +0.061 | -0.088 to +0.210 | $+24.31 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1877 vs market 0.1979 -> **model is sharper**

## 3:00 left (360 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 360 | 65.6% | 61.5% | +0.041 | -0.002 to +0.083 | $+145.88 | NO EDGE |
| Lean (bet the side BTC is on now) | 360 | 76.7% | 74.3% | +0.023 | -0.019 to +0.066 | $+83.52 | NO EDGE |
| Edge (model beats the ask by 3c+) | 220 | 34.5% | 29.7% | +0.049 | -0.003 to +0.100 | $+107.41 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 17 | 88.2% | 71.2% | +0.171 | +0.006 to +0.335 | $+29.02 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1611 vs market 0.1701 -> **model is sharper**

## 2:00 left (367 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 343 | 61.5% | 59.2% | +0.023 | -0.014 to +0.061 | $+80.28 | NO EDGE |
| Lean (bet the side BTC is on now) | 338 | 84.6% | 80.0% | +0.046 | +0.009 to +0.084 | $+157.05 | PASSES |
| Edge (model beats the ask by 3c+) | 273 | 24.2% | 21.8% | +0.024 | -0.014 to +0.062 | $+65.58 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 16 | 100.0% | 75.2% | +0.248 | +0.220 to +0.276 | $+39.68 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1230 vs market 0.1245 -> **model is sharper**

## 1:00 left (366 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 274 | 49.3% | 47.7% | +0.016 | -0.021 to +0.053 | $+42.93 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 230 | 89.1% | 82.7% | +0.065 | +0.022 to +0.107 | $+149.01 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 318 | 15.4% | 11.8% | +0.036 | +0.008 to +0.064 | $+114.35 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0802 vs market 0.0925 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=387, bias $-0.10, sd $0.83 (set BASIS_SD near 1)
- spot at open: n=387, bias $-1.79, sd $23.27 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 427 | 225 | 55% | 57% |
| 60%-70% | 398 | 243 | 65% | 72% |
| 70%-80% | 325 | 223 | 75% | 82% |
| 80%-90% | 625 | 285 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 339 | 1606 | 0.1529 | 0.1615 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 387 (339 with decision logging, v16+)
- Markets with a signal: 129
- Alerts attempted: 53 · delivered: 52 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 43 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 58 markets, would have won 39, +31.69 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 26 markets, would have won 21, +77.44 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 49/52 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 351 · valid comparisons: 334
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.58, typical gap $2.82, worst $12.31
- Coinbase would have named the wrong winner: 5/334 (1.5%)
- Rounds settling within $10 of the target: 47, wrong winner 5 (11%)
- Rounds settling within $25 of the target: 100, wrong winner 5 (5%)
- Rounds settling within $50 of the target: 173, wrong winner 5 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 52 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 43
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 53
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 31 ms (worst 75)
- Price read -> decision made: median 80 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 13/52 | 39 | 0 | +15.83 |
| 10s | 13/52 | 39 | 0 | +15.83 |
| 20s | 11/52 | 41 | 0 | -6.74 |
| 30s | 9/52 | 43 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 32 · loops: 52787 · loops over 5s: 3 (0.01%)
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
