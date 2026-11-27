---
polybot_auto: true
updated: 2026-11-27 20:30 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 20:27 UTC | 3250 checkpoints logged | 3070 graded | 653 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 605 settled rounds observed · 95 alerts (93 delivered) · **18 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 15/593 valid rounds (2.5%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1611 vs market 0.1675 on 605 rounds -> model sharper
3. **Simulated profit after fees:** -50.17 on 18 trades of $10 · win rate 39% vs break-even 50%, 95% range per trade -7.78 to +2.21
4. **Quote available at simulated tap (size not verified):** 5s 27/93 · 10s 25/93 · 20s 22/93 · 30s 19/93
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 57 runs, stalls over 5s 4/94032 loops, longest BTC price gap 10.8s · checks with no market quote 80/2978 (book fallback used 1241) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 18/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (599 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 599 | 65.1% | 64.6% | +0.006 | -0.032 to +0.043 | $+33.02 | NO EDGE |
| Lean (bet the side BTC is on now) | 599 | 65.4% | 67.3% | -0.018 | -0.056 to +0.019 | $-109.18 | NO EDGE |
| Edge (model beats the ask by 3c+) | 302 | 49.7% | 42.0% | +0.076 | +0.025 to +0.128 | $+230.38 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 135 | 64.4% | 52.6% | +0.119 | +0.037 to +0.201 | $+160.36 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2118 vs market 0.2203 -> **model is sharper**

## 3:30 left (611 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 611 | 65.8% | 62.9% | +0.029 | -0.006 to +0.065 | $+179.12 | NO EDGE |
| Lean (bet the side BTC is on now) | 611 | 70.5% | 71.2% | -0.007 | -0.042 to +0.029 | $-41.38 | NO EDGE |
| Edge (model beats the ask by 3c+) | 340 | 40.3% | 34.8% | +0.055 | +0.009 to +0.101 | $+187.55 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 70 | 58.6% | 52.2% | +0.064 | -0.047 to +0.175 | $+44.60 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1957 vs market 0.2005 -> **model is sharper**

## 3:00 left (618 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 617 | 64.5% | 61.2% | +0.033 | -0.000 to +0.066 | $+203.05 | NO EDGE |
| Lean (bet the side BTC is on now) | 617 | 75.5% | 74.4% | +0.011 | -0.022 to +0.044 | $+66.52 | NO EDGE |
| Edge (model beats the ask by 3c+) | 373 | 34.6% | 30.0% | +0.046 | +0.006 to +0.087 | $+172.15 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 33 | 87.9% | 70.8% | +0.171 | +0.053 to +0.289 | $+56.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1717 vs market 0.1770 -> **model is sharper**

## 2:00 left (624 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 587 | 63.4% | 59.8% | +0.036 | +0.007 to +0.065 | $+210.44 | PASSES |
| Lean (bet the side BTC is on now) | 576 | 83.0% | 79.9% | +0.031 | +0.001 to +0.061 | $+178.04 | PASSES |
| Edge (model beats the ask by 3c+) | 466 | 24.9% | 21.8% | +0.031 | +0.001 to +0.061 | $+145.40 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 23 | 95.7% | 75.3% | +0.204 | +0.113 to +0.294 | $+46.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1279 vs market 0.1315 -> **model is sharper**

## 1:00 left (618 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 458 | 49.8% | 48.0% | +0.018 | -0.012 to +0.047 | $+80.93 | NO EDGE |
| Lean (bet the side BTC is on now) | 390 | 85.4% | 81.6% | +0.038 | +0.003 to +0.072 | $+146.60 | PASSES |
| Edge (model beats the ask by 3c+) | 546 | 16.8% | 12.5% | +0.044 | +0.021 to +0.066 | $+239.34 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0872 vs market 0.0990 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=653, bias $-0.06, sd $0.64 (set BASIS_SD near 1)
- spot at open: n=653, bias $-3.31, sd $23.55 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 741 | 385 | 55% | 57% |
| 60%-70% | 683 | 416 | 65% | 69% |
| 70%-80% | 595 | 388 | 75% | 79% |
| 80%-90% | 1040 | 468 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 605 | 2890 | 0.1611 | 0.1675 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 653 (605 with decision logging, v16+)
- Markets with a signal: 227
- Alerts attempted: 95 · delivered: 93 · delivery failed: 2
- Simulated fills (quote available, size not verified): 19
- Expired alerts: 74 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 98 markets, would have won 67, +56.34 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 51 markets, would have won 39, +120.63 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 88/93 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 626 · valid comparisons: 593
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.32, typical gap $4.25, worst $20.80
- Coinbase would have named the wrong winner: 15/593 (2.5%)
- Rounds settling within $10 of the target: 90, wrong winner 14 (16%)
- Rounds settling within $25 of the target: 187, wrong winner 15 (8%)
- Rounds settling within $50 of the target: 315, wrong winner 15 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 92 (goal: 300)
- Simulated paper trades: 18 · no-trade (expired/unconfirmed): 74
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 7/18 = 39% vs break-even 49.8% (price paid + fee)
- Paper P&L after fees: -50.17 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 95
- Coinbase trade -> we received it: median 890 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 26/92 | 66 | 0 | +17.11 |
| 10s | 24/92 | 68 | 0 | -9.33 |
| 20s | 21/92 | 71 | 0 | -21.46 |
| 30s | 18/92 | 74 | 0 | -50.17 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 57 · loops: 94032 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
