---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 08:27 UTC | 3926 checkpoints logged | 3729 graded | 791 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 743 settled rounds observed · 124 alerts (121 delivered) · **27 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/727 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1606 vs market 0.1650 on 743 rounds -> model sharper
3. **Simulated profit after fees:** -11.35 on 27 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.69 to +3.84
4. **Quote available at simulated tap (size not verified):** 5s 40/121 · 10s 38/121 · 20s 33/121 · 30s 28/121
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 70 runs, stalls over 5s 13/115464 loops, longest BTC price gap 21.8s · checks with no market quote 98/3654 (book fallback used 1486) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 27/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 27/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 75/120 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 27 tickets at every delay (right 13/27): 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (729 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 728 | 66.2% | 64.5% | +0.017 | -0.016 to +0.051 | $+125.96 | NO EDGE |
| Lean (bet the side BTC is on now) | 729 | 66.7% | 67.0% | -0.003 | -0.037 to +0.031 | $-21.65 | NO EDGE |
| Edge (model beats the ask by 3c+) | 366 | 50.3% | 42.7% | +0.075 | +0.029 to +0.122 | $+275.95 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 174 | 65.5% | 52.7% | +0.128 | +0.056 to +0.199 | $+222.33 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2092 vs market 0.2167 -> **model is sharper**

## 3:30 left (743 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 740 | 66.6% | 63.2% | +0.034 | +0.002 to +0.066 | $+251.67 | PASSES |
| Lean (bet the side BTC is on now) | 743 | 70.1% | 71.1% | -0.010 | -0.042 to +0.022 | $-73.34 | NO EDGE |
| Edge (model beats the ask by 3c+) | 418 | 38.8% | 35.4% | +0.034 | -0.008 to +0.076 | $+140.66 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 85 | 56.5% | 52.4% | +0.041 | -0.062 to +0.143 | $+34.73 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1967 vs market 0.1979 -> **model is sharper**

## 3:00 left (751 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 750 | 65.3% | 62.1% | +0.032 | +0.002 to +0.062 | $+240.46 | PASSES |
| Lean (bet the side BTC is on now) | 750 | 75.3% | 74.3% | +0.011 | -0.019 to +0.041 | $+79.74 | NO EDGE |
| Edge (model beats the ask by 3c+) | 460 | 36.1% | 31.4% | +0.047 | +0.010 to +0.083 | $+214.45 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 44 | 88.6% | 71.9% | +0.168 | +0.070 to +0.265 | $+73.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1708 vs market 0.1756 -> **model is sharper**

## 2:00 left (757 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 719 | 60.9% | 58.6% | +0.023 | -0.003 to +0.049 | $+164.47 | NO EDGE |
| Lean (bet the side BTC is on now) | 705 | 83.0% | 79.8% | +0.032 | +0.006 to +0.059 | $+227.24 | PASSES |
| Edge (model beats the ask by 3c+) | 562 | 24.7% | 22.0% | +0.027 | -0.000 to +0.055 | $+154.12 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 92.3% | 74.3% | +0.180 | +0.077 to +0.283 | $+46.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1283 vs market 0.1298 -> **model is sharper**

## 1:00 left (749 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 557 | 50.8% | 48.6% | +0.022 | -0.004 to +0.049 | $+125.28 | NO EDGE |
| Lean (bet the side BTC is on now) | 476 | 85.7% | 82.0% | +0.037 | +0.006 to +0.068 | $+176.85 | PASSES |
| Edge (model beats the ask by 3c+) | 663 | 16.0% | 12.5% | +0.035 | +0.015 to +0.056 | $+233.04 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0869 vs market 0.0956 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=791, bias $-0.05, sd $0.58 (set BASIS_SD near 1)
- spot at open: n=791, bias $-3.86, sd $22.70 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 900 | 468 | 55% | 57% |
| 60%-70% | 847 | 515 | 65% | 70% |
| 70%-80% | 703 | 462 | 75% | 80% |
| 80%-90% | 1268 | 565 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 743 | 3549 | 0.1606 | 0.165 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 791 (743 with decision logging, v16+)
- Markets with a signal: 286
- Alerts attempted: 124 · delivered: 121 · delivery failed: 3
- Simulated fills (quote available, size not verified): 28
- Expired alerts: 93 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 120 markets, would have won 82, +77.03 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 61 markets, would have won 45, +121.90 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 110/121 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 769 · valid comparisons: 727
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 25 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.91, typical gap $4.34, worst $20.80
- Coinbase would have named the wrong winner: 20/727 (2.8%)
- Rounds settling within $10 of the target: 109, wrong winner 19 (17%)
- Rounds settling within $25 of the target: 262, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 421, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 120 (goal: 300)
- Simulated paper trades: 27 · no-trade (expired/unconfirmed): 93
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 13/27 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -11.35 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 124
- Coinbase trade -> we received it: median 966 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 39/120 | 81 | 0 | +52.66 |
| 10s | 37/120 | 83 | 0 | +23.53 |
| 20s | 32/120 | 88 | 0 | +37.31 |
| 30s | 27/120 | 93 | 0 | -11.35 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 70 · loops: 115464 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
