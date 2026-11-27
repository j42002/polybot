---
polybot_auto: true
updated: 2026-11-27 10:39 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 10:18 UTC | 2678 checkpoints logged | 2509 graded | 537 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 489 settled rounds observed · 81 alerts (80 delivered) · **14 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/480 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1534 vs market 0.1607 on 489 rounds -> model sharper
3. **Simulated profit after fees:** -24.54 on 14 trades of $10 · win rate 43% vs break-even 48%, 95% range per trade -7.78 to +4.28
4. **Quote available at simulated tap (size not verified):** 5s 21/80 · 10s 19/80 · 20s 16/80 · 30s 14/80
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 46 runs, stalls over 5s 3/75887 loops, longest BTC price gap 10.7s · checks with no market quote 73/2406 (book fallback used 987) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 14/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (486 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 486 | 65.6% | 64.5% | +0.012 | -0.030 to +0.053 | $+57.44 | NO EDGE |
| Lean (bet the side BTC is on now) | 486 | 66.3% | 67.1% | -0.009 | -0.050 to +0.033 | $-42.50 | NO EDGE |
| Edge (model beats the ask by 3c+) | 245 | 50.2% | 41.1% | +0.091 | +0.034 to +0.148 | $+223.61 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 109 | 67.0% | 52.0% | +0.149 | +0.061 to +0.238 | $+162.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2074 vs market 0.2180 -> **model is sharper**

## 3:30 left (498 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 498 | 66.1% | 63.2% | +0.029 | -0.010 to +0.067 | $+142.69 | NO EDGE |
| Lean (bet the side BTC is on now) | 498 | 71.7% | 71.0% | +0.007 | -0.031 to +0.046 | $+36.45 | NO EDGE |
| Edge (model beats the ask by 3c+) | 281 | 40.9% | 35.3% | +0.056 | +0.006 to +0.107 | $+158.66 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 63 | 60.3% | 51.9% | +0.084 | -0.031 to +0.200 | $+53.10 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1873 vs market 0.1950 -> **model is sharper**

## 3:00 left (505 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 504 | 64.9% | 61.8% | +0.031 | -0.005 to +0.066 | $+154.64 | NO EDGE |
| Lean (bet the side BTC is on now) | 504 | 76.4% | 74.6% | +0.018 | -0.017 to +0.054 | $+91.90 | NO EDGE |
| Edge (model beats the ask by 3c+) | 305 | 32.8% | 29.6% | +0.032 | -0.012 to +0.075 | $+96.91 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 88.5% | 70.9% | +0.176 | +0.045 to +0.306 | $+45.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1639 vs market 0.1687 -> **model is sharper**

## 2:00 left (512 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 481 | 63.0% | 60.2% | +0.028 | -0.003 to +0.059 | $+134.96 | NO EDGE |
| Lean (bet the side BTC is on now) | 473 | 84.8% | 80.6% | +0.042 | +0.010 to +0.073 | $+197.53 | PASSES |
| Edge (model beats the ask by 3c+) | 378 | 23.8% | 21.0% | +0.028 | -0.004 to +0.060 | $+106.41 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 20 | 100.0% | 74.8% | +0.252 | +0.227 to +0.277 | $+50.32 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1214 vs market 0.1240 -> **model is sharper**

## 1:00 left (508 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 377 | 49.3% | 48.0% | +0.014 | -0.018 to +0.045 | $+51.70 | NO EDGE |
| Lean (bet the side BTC is on now) | 317 | 88.0% | 82.9% | +0.051 | +0.014 to +0.087 | $+160.70 | PASSES |
| Edge (model beats the ask by 3c+) | 446 | 16.1% | 12.2% | +0.039 | +0.016 to +0.063 | $+175.83 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0794 vs market 0.0914 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=537, bias $-0.07, sd $0.70 (set BASIS_SD near 1)
- spot at open: n=537, bias $-2.07, sd $22.42 (set BASIS_SD near 22)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 596 | 314 | 55% | 57% |
| 60%-70% | 558 | 339 | 65% | 70% |
| 70%-80% | 480 | 323 | 75% | 83% |
| 80%-90% | 864 | 394 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 489 | 2329 | 0.1534 | 0.1607 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 537 (489 with decision logging, v16+)
- Markets with a signal: 189
- Alerts attempted: 81 · delivered: 80 · delivery failed: 1
- Simulated fills (quote available, size not verified): 14
- Expired alerts: 66 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 80 markets, would have won 55, +52.96 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 40 markets, would have won 33, +117.26 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 76/80 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 505 · valid comparisons: 480
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.16, typical gap $3.02, worst $12.31
- Coinbase would have named the wrong winner: 6/480 (1.2%)
- Rounds settling within $10 of the target: 72, wrong winner 6 (8%)
- Rounds settling within $25 of the target: 149, wrong winner 6 (4%)
- Rounds settling within $50 of the target: 253, wrong winner 6 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 80 (goal: 300)
- Simulated paper trades: 14 · no-trade (expired/unconfirmed): 66
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/14 = 43% vs break-even 48.1% (price paid + fee)
- Paper P&L after fees: -24.54 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 81
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 21/80 | 59 | 0 | +35.46 |
| 10s | 19/80 | 61 | 0 | +9.02 |
| 20s | 16/80 | 64 | 0 | -3.11 |
| 30s | 14/80 | 66 | 0 | -24.54 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 46 · loops: 75887 · loops over 5s: 3 (0.00%)
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
