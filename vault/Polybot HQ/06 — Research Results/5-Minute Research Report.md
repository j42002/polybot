---
polybot_auto: true
updated: 2026-11-26 18:44 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 18:37 UTC | 1786 checkpoints logged | 1621 graded | 353 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 305 settled rounds observed · 40 alerts (39 delivered) · **7 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/300 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1465 vs market 0.1547 on 305 rounds -> model sharper
3. **Simulated profit after fees:** -41.74 on 7 trades of $10 · win rate 29% vs break-even 45%, 95% range per trade -11.86 to -0.07
4. **Quote available at simulated tap (size not verified):** 5s 11/39 · 10s 11/39 · 20s 9/39 · 30s 7/39
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 29 runs, stalls over 5s 3/47837 loops, longest BTC price gap 10.7s · checks with no market quote 65/1514 (book fallback used 611) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 7/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (308 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 308 | 66.9% | 65.0% | +0.018 | -0.033 to +0.070 | $+56.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 308 | 66.6% | 68.0% | -0.014 | -0.066 to +0.038 | $-43.39 | NO EDGE |
| Edge (model beats the ask by 3c+) | 157 | 53.5% | 40.2% | +0.133 | +0.064 to +0.202 | $+208.88 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 63 | 71.4% | 50.9% | +0.205 | +0.097 to +0.314 | $+129.35 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2025 vs market 0.2171 -> **model is sharper**

## 3:30 left (317 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 317 | 69.1% | 64.6% | +0.045 | -0.003 to +0.093 | $+143.15 | NO EDGE |
| Lean (bet the side BTC is on now) | 317 | 74.1% | 71.9% | +0.022 | -0.026 to +0.070 | $+69.81 | NO EDGE |
| Edge (model beats the ask by 3c+) | 178 | 41.0% | 34.3% | +0.067 | +0.004 to +0.131 | $+119.98 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 35 | 57.1% | 51.2% | +0.060 | -0.098 to +0.217 | $+20.84 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1800 vs market 0.1930 -> **model is sharper**

## 3:00 left (326 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 326 | 65.6% | 61.8% | +0.039 | -0.004 to +0.082 | $+126.55 | NO EDGE |
| Lean (bet the side BTC is on now) | 326 | 77.3% | 75.1% | +0.022 | -0.022 to +0.065 | $+70.57 | NO EDGE |
| Edge (model beats the ask by 3c+) | 201 | 31.3% | 28.4% | +0.030 | -0.023 to +0.082 | $+59.66 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 12 | 91.7% | 71.2% | +0.205 | +0.037 to +0.374 | $+24.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1561 vs market 0.1596 -> **model is sharper**

## 2:00 left (335 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 312 | 61.9% | 59.0% | +0.029 | -0.009 to +0.067 | $+90.73 | NO EDGE |
| Lean (bet the side BTC is on now) | 307 | 86.0% | 80.6% | +0.054 | +0.016 to +0.092 | $+165.55 | PASSES |
| Edge (model beats the ask by 3c+) | 255 | 23.5% | 21.5% | +0.020 | -0.019 to +0.060 | $+51.91 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1182 vs market 0.1189 -> **model is sharper**

## 1:00 left (335 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 250 | 48.8% | 47.2% | +0.016 | -0.021 to +0.054 | $+40.75 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 208 | 89.4% | 83.1% | +0.064 | +0.020 to +0.108 | $+132.44 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 290 | 15.2% | 11.6% | +0.036 | +0.007 to +0.064 | $+103.82 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0780 vs market 0.0884 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=353, bias $-0.11, sd $0.86 (set BASIS_SD near 1)
- spot at open: n=353, bias $-1.73, sd $24.09 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 375 | 199 | 55% | 57% |
| 60%-70% | 355 | 217 | 65% | 74% |
| 70%-80% | 298 | 202 | 75% | 83% |
| 80%-90% | 582 | 263 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 305 | 1441 | 0.1465 | 0.1547 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 353 (305 with decision logging, v16+)
- Markets with a signal: 106
- Alerts attempted: 40 · delivered: 39 · delivery failed: 1
- Simulated fills (quote available, size not verified): 7
- Expired alerts: 32 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 49 markets, would have won 33, +32.50 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 21 markets, would have won 18, +75.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 37/39 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 318 · valid comparisons: 300
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.56, typical gap $2.85, worst $12.31
- Coinbase would have named the wrong winner: 4/300 (1.3%)
- Rounds settling within $10 of the target: 38, wrong winner 4 (11%)
- Rounds settling within $25 of the target: 84, wrong winner 4 (5%)
- Rounds settling within $50 of the target: 145, wrong winner 4 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 39 (goal: 300)
- Simulated paper trades: 7 · no-trade (expired/unconfirmed): 32
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
| 5s | 11/39 | 28 | 0 | +2.27 |
| 10s | 11/39 | 28 | 0 | +2.27 |
| 20s | 9/39 | 30 | 0 | -20.30 |
| 30s | 7/39 | 32 | 0 | -41.74 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 29 · loops: 47837 · loops over 5s: 3 (0.01%)
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
