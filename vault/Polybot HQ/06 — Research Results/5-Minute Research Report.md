---
polybot_auto: true
updated: 2026-11-28 01:04 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 01:04 UTC | 3519 checkpoints logged | 3330 graded | 709 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 661 settled rounds observed · 107 alerts (105 delivered) · **24 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/648 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1633 vs market 0.1691 on 661 rounds -> model sharper
3. **Simulated profit after fees:** -21.65 on 24 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.46 to +3.65
4. **Quote available at simulated tap (size not verified):** 5s 34/105 · 10s 32/105 · 20s 27/105 · 30s 24/105
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 62 runs, stalls over 5s 4/102282 loops, longest BTC price gap 10.8s · checks with no market quote 92/3247 (book fallback used 1316) · bad close samples 14 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 24/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 24/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 64/105 delivered alerts (61%) vs average break-even 52% at the alert price.
- Same 24 tickets at every delay (right 11/24): 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 10, of which right 7/10. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (649 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 648 | 65.4% | 64.4% | +0.010 | -0.026 to +0.046 | $+64.31 | NO EDGE |
| Lean (bet the side BTC is on now) | 649 | 65.5% | 67.1% | -0.017 | -0.053 to +0.019 | $-108.01 | NO EDGE |
| Edge (model beats the ask by 3c+) | 325 | 49.2% | 42.7% | +0.065 | +0.015 to +0.116 | $+212.51 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 150 | 62.7% | 52.8% | +0.099 | +0.020 to +0.177 | $+148.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2127 vs market 0.2193 -> **model is sharper**

## 3:30 left (664 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 664 | 65.8% | 62.9% | +0.029 | -0.005 to +0.063 | $+192.31 | NO EDGE |
| Lean (bet the side BTC is on now) | 664 | 69.7% | 71.1% | -0.013 | -0.048 to +0.021 | $-89.35 | NO EDGE |
| Edge (model beats the ask by 3c+) | 374 | 39.3% | 35.2% | +0.041 | -0.003 to +0.086 | $+153.97 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 78 | 59.0% | 52.1% | +0.069 | -0.037 to +0.174 | $+53.46 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1987 vs market 0.2015 -> **model is sharper**

## 3:00 left (671 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 670 | 64.3% | 61.4% | +0.029 | -0.003 to +0.061 | $+194.46 | NO EDGE |
| Lean (bet the side BTC is on now) | 670 | 74.9% | 74.2% | +0.007 | -0.025 to +0.039 | $+47.98 | NO EDGE |
| Edge (model beats the ask by 3c+) | 408 | 35.3% | 30.7% | +0.046 | +0.006 to +0.085 | $+185.78 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 36 | 88.9% | 71.2% | +0.177 | +0.068 to +0.285 | $+63.55 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1730 vs market 0.1786 -> **model is sharper**

## 2:00 left (677 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 639 | 62.4% | 59.3% | +0.031 | +0.003 to +0.059 | $+197.90 | PASSES |
| Lean (bet the side BTC is on now) | 626 | 82.1% | 79.7% | +0.024 | -0.005 to +0.053 | $+149.32 | NO EDGE |
| Edge (model beats the ask by 3c+) | 503 | 25.0% | 22.0% | +0.031 | +0.001 to +0.060 | $+154.44 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 92.0% | 74.6% | +0.174 | +0.068 to +0.281 | $+43.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1310 vs market 0.1345 -> **model is sharper**

## 1:00 left (669 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 498 | 50.4% | 48.2% | +0.022 | -0.007 to +0.051 | $+109.70 | NO EDGE |
| Lean (bet the side BTC is on now) | 425 | 85.2% | 81.1% | +0.040 | +0.007 to +0.074 | $+171.51 | PASSES |
| Edge (model beats the ask by 3c+) | 590 | 17.1% | 12.9% | +0.042 | +0.020 to +0.064 | $+247.86 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0891 vs market 0.1013 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=709, bias $-0.05, sd $0.61 (set BASIS_SD near 1)
- spot at open: n=709, bias $-3.77, sd $22.89 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 811 | 420 | 55% | 57% |
| 60%-70% | 748 | 452 | 65% | 69% |
| 70%-80% | 632 | 415 | 75% | 79% |
| 80%-90% | 1128 | 501 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 661 | 3150 | 0.1633 | 0.1691 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 709 (661 with decision logging, v16+)
- Markets with a signal: 252
- Alerts attempted: 107 · delivered: 105 · delivery failed: 2
- Simulated fills (quote available, size not verified): 24
- Expired alerts: 81 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 106 markets, would have won 72, +59.59 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 56 markets, would have won 41, +110.52 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 98/105 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 681 · valid comparisons: 648
- Missing/untrusted: 14 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.74, typical gap $4.43, worst $20.80
- Coinbase would have named the wrong winner: 20/648 (3.1%)
- Rounds settling within $10 of the target: 99, wrong winner 19 (19%)
- Rounds settling within $25 of the target: 220, wrong winner 20 (9%)
- Rounds settling within $50 of the target: 363, wrong winner 20 (6%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 105 (goal: 300)
- Simulated paper trades: 24 · no-trade (expired/unconfirmed): 81
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 11/24 = 46% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -21.65 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 107
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 71 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 34/105 | 71 | 0 | +21.93 |
| 10s | 32/105 | 73 | 0 | -7.20 |
| 20s | 27/105 | 78 | 0 | +6.58 |
| 30s | 24/105 | 81 | 0 | -21.65 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 62 · loops: 102282 · loops over 5s: 4 (0.00%)
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
