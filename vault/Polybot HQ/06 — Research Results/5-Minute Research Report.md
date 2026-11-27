---
polybot_auto: true
updated: 2026-11-27 09:37 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 09:23 UTC | 2624 checkpoints logged | 2455 graded | 526 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 478 settled rounds observed · 77 alerts (76 delivered) · **13 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/469 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1534 vs market 0.1609 on 478 rounds -> model sharper
3. **Simulated profit after fees:** -13.94 on 13 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -7.43 to +5.28
4. **Quote available at simulated tap (size not verified):** 5s 19/76 · 10s 17/76 · 20s 15/76 · 30s 13/76
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 45 runs, stalls over 5s 3/74237 loops, longest BTC price gap 10.7s · checks with no market quote 73/2352 (book fallback used 970) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 13/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (475 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 475 | 65.9% | 64.6% | +0.013 | -0.029 to +0.054 | $+59.99 | NO EDGE |
| Lean (bet the side BTC is on now) | 475 | 66.1% | 67.3% | -0.012 | -0.053 to +0.030 | $-54.65 | NO EDGE |
| Edge (model beats the ask by 3c+) | 241 | 49.8% | 40.9% | +0.089 | +0.031 to +0.146 | $+214.20 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 106 | 67.0% | 51.9% | +0.151 | +0.061 to +0.241 | $+160.16 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2073 vs market 0.2176 -> **model is sharper**

## 3:30 left (487 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 487 | 66.3% | 63.3% | +0.031 | -0.008 to +0.070 | $+148.73 | NO EDGE |
| Lean (bet the side BTC is on now) | 487 | 71.7% | 71.0% | +0.007 | -0.032 to +0.046 | $+32.68 | NO EDGE |
| Edge (model beats the ask by 3c+) | 273 | 41.0% | 35.0% | +0.061 | +0.010 to +0.112 | $+165.43 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 59 | 62.7% | 51.9% | +0.108 | -0.010 to +0.227 | $+63.91 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1867 vs market 0.1953 -> **model is sharper**

## 3:00 left (494 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 493 | 65.1% | 61.8% | +0.033 | -0.003 to +0.069 | $+162.30 | NO EDGE |
| Lean (bet the side BTC is on now) | 493 | 76.5% | 74.5% | +0.019 | -0.017 to +0.055 | $+95.64 | NO EDGE |
| Edge (model beats the ask by 3c+) | 301 | 32.9% | 29.6% | +0.032 | -0.011 to +0.076 | $+97.57 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 88.5% | 70.9% | +0.176 | +0.045 to +0.306 | $+45.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1630 vs market 0.1681 -> **model is sharper**

## 2:00 left (501 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 470 | 62.6% | 59.9% | +0.026 | -0.006 to +0.058 | $+122.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 462 | 84.6% | 80.5% | +0.042 | +0.010 to +0.074 | $+192.77 | PASSES |
| Edge (model beats the ask by 3c+) | 369 | 23.8% | 21.1% | +0.028 | -0.005 to +0.060 | $+101.62 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1221 vs market 0.1249 -> **model is sharper**

## 1:00 left (498 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 369 | 49.6% | 48.0% | +0.016 | -0.016 to +0.048 | $+59.12 | NO EDGE |
| Lean (bet the side BTC is on now) | 310 | 87.7% | 82.9% | +0.049 | +0.011 to +0.086 | $+150.88 | PASSES |
| Edge (model beats the ask by 3c+) | 438 | 16.2% | 12.2% | +0.040 | +0.016 to +0.064 | $+174.34 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0806 vs market 0.0926 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=526, bias $-0.07, sd $0.71 (set BASIS_SD near 1)
- spot at open: n=526, bias $-1.91, sd $22.55 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 584 | 308 | 55% | 56% |
| 60%-70% | 548 | 332 | 65% | 71% |
| 70%-80% | 464 | 314 | 75% | 83% |
| 80%-90% | 848 | 385 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 478 | 2275 | 0.1534 | 0.1609 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 526 (478 with decision logging, v16+)
- Markets with a signal: 181
- Alerts attempted: 77 · delivered: 76 · delivery failed: 1
- Simulated fills (quote available, size not verified): 13
- Expired alerts: 63 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 76 markets, would have won 52, +46.86 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 40 markets, would have won 33, +117.26 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 72/76 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 494 · valid comparisons: 469
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.07, typical gap $2.98, worst $12.31
- Coinbase would have named the wrong winner: 6/469 (1.3%)
- Rounds settling within $10 of the target: 69, wrong winner 6 (9%)
- Rounds settling within $25 of the target: 143, wrong winner 6 (4%)
- Rounds settling within $50 of the target: 244, wrong winner 6 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 76 (goal: 300)
- Simulated paper trades: 13 · no-trade (expired/unconfirmed): 63
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/13 = 46% vs break-even 48.8% (price paid + fee)
- Paper P&L after fees: -13.94 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 77
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 28 ms (worst 75)
- Price read -> decision made: median 74 ms (worst 168)
- Decision -> Discord accepted: median 1538 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 19/76 | 57 | 0 | +56.50 |
| 10s | 17/76 | 59 | 0 | +30.06 |
| 20s | 15/76 | 61 | 0 | +7.50 |
| 30s | 13/76 | 63 | 0 | -13.94 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 45 · loops: 74237 · loops over 5s: 3 (0.00%)
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
