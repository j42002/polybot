---
polybot_auto: true
updated: 2026-11-27 22:18 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 22:18 UTC | 3357 checkpoints logged | 3170 graded | 676 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 628 settled rounds observed · 101 alerts (99 delivered) · **22 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 19/616 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1618 vs market 0.1685 on 628 rounds -> model sharper
3. **Simulated profit after fees:** -22.37 on 22 trades of $10 · win rate 45% vs break-even 49%, 95% range per trade -5.79 to +3.76
4. **Quote available at simulated tap (size not verified):** 5s 31/99 · 10s 29/99 · 20s 25/99 · 30s 22/99
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 59 runs, stalls over 5s 4/97332 loops, longest BTC price gap 10.8s · checks with no market quote 91/3085 (book fallback used 1272) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 22/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 22/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 61/98 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 22 tickets at every delay (right 10/22): 5s -20.82 · 10s -22.75 · 20s -22.05 · 30s -22.37. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 9, of which right 7/9. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (618 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 618 | 65.4% | 64.6% | +0.007 | -0.029 to +0.044 | $+46.16 | NO EDGE |
| Lean (bet the side BTC is on now) | 618 | 65.5% | 67.3% | -0.018 | -0.055 to +0.019 | $-108.34 | NO EDGE |
| Edge (model beats the ask by 3c+) | 310 | 50.0% | 42.1% | +0.079 | +0.028 to +0.129 | $+243.87 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 139 | 64.7% | 52.8% | +0.120 | +0.039 to +0.200 | $+166.45 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2119 vs market 0.2202 -> **model is sharper**

## 3:30 left (631 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 631 | 65.9% | 63.1% | +0.029 | -0.006 to +0.064 | $+181.30 | NO EDGE |
| Lean (bet the side BTC is on now) | 631 | 70.2% | 71.3% | -0.011 | -0.046 to +0.024 | $-69.99 | NO EDGE |
| Edge (model beats the ask by 3c+) | 354 | 39.8% | 34.9% | +0.050 | +0.004 to +0.095 | $+176.04 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 74 | 59.5% | 51.8% | +0.077 | -0.032 to +0.185 | $+56.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1968 vs market 0.2012 -> **model is sharper**

## 3:00 left (638 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 637 | 64.5% | 61.2% | +0.033 | +0.000 to +0.065 | $+209.68 | PASSES |
| Lean (bet the side BTC is on now) | 637 | 75.2% | 74.5% | +0.007 | -0.026 to +0.039 | $+41.99 | NO EDGE |
| Edge (model beats the ask by 3c+) | 389 | 34.7% | 29.9% | +0.048 | +0.008 to +0.088 | $+186.29 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 34 | 88.2% | 70.8% | +0.175 | +0.060 to +0.290 | $+59.38 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1719 vs market 0.1779 -> **model is sharper**

## 2:00 left (644 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 607 | 62.6% | 59.3% | +0.033 | +0.004 to +0.062 | $+200.35 | PASSES |
| Lean (bet the side BTC is on now) | 595 | 82.5% | 79.7% | +0.028 | -0.001 to +0.058 | $+168.61 | NO EDGE |
| Edge (model beats the ask by 3c+) | 480 | 25.2% | 21.8% | +0.034 | +0.004 to +0.064 | $+164.32 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 23 | 95.7% | 75.3% | +0.204 | +0.113 to +0.294 | $+46.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1287 vs market 0.1335 -> **model is sharper**

## 1:00 left (639 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 474 | 50.2% | 48.4% | +0.018 | -0.011 to +0.048 | $+86.93 | NO EDGE |
| Lean (bet the side BTC is on now) | 405 | 85.2% | 81.3% | +0.039 | +0.005 to +0.073 | $+158.23 | PASSES |
| Edge (model beats the ask by 3c+) | 566 | 17.1% | 12.9% | +0.043 | +0.020 to +0.065 | $+240.73 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0883 vs market 0.1003 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=676, bias $-0.06, sd $0.63 (set BASIS_SD near 1)
- spot at open: n=676, bias $-3.47, sd $23.27 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 766 | 398 | 55% | 57% |
| 60%-70% | 705 | 430 | 65% | 69% |
| 70%-80% | 614 | 400 | 75% | 79% |
| 80%-90% | 1074 | 481 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 628 | 2990 | 0.1618 | 0.1685 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 676 (628 with decision logging, v16+)
- Markets with a signal: 235
- Alerts attempted: 101 · delivered: 99 · delivery failed: 2
- Simulated fills (quote available, size not verified): 22
- Expired alerts: 77 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 100 markets, would have won 69, +64.09 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 51 markets, would have won 39, +120.63 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 94/99 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 648 · valid comparisons: 616
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.57, typical gap $4.41, worst $20.80
- Coinbase would have named the wrong winner: 19/616 (3.1%)
- Rounds settling within $10 of the target: 95, wrong winner 18 (19%)
- Rounds settling within $25 of the target: 199, wrong winner 19 (10%)
- Rounds settling within $50 of the target: 335, wrong winner 19 (6%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 98 (goal: 300)
- Simulated paper trades: 22 · no-trade (expired/unconfirmed): 76
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 10/22 = 45% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -22.37 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 101
- Coinbase trade -> we received it: median 890 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 31/98 | 67 | 0 | +35.88 |
| 10s | 29/98 | 69 | 0 | +6.75 |
| 20s | 25/98 | 73 | 0 | +5.77 |
| 30s | 22/98 | 76 | 0 | -22.37 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 59 · loops: 97332 · loops over 5s: 4 (0.00%)
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
