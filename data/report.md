# polybot report

Updated 2026-11-28 09:22 UTC | 3979 checkpoints logged | 3781 graded | 802 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 754 settled rounds observed · 127 alerts (124 delivered) · **30 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/738 valid rounds (2.7%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1603 vs market 0.1644 on 754 rounds -> model sharper
3. **Simulated profit after fees:** -6.29 on 30 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -4.19 to +3.77
4. **Quote available at simulated tap (size not verified):** 5s 42/124 · 10s 40/124 · 20s 35/124 · 30s 30/124
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 71 runs, stalls over 5s 13/117114 loops, longest BTC price gap 21.8s · checks with no market quote 98/3707 (book fallback used 1510) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 30/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 30/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 77/123 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 29 tickets at every delay (right 14/29): 5s -23.78 · 10s -25.71 · 20s -20.62 · 30s -17.52. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (740 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 739 | 66.2% | 64.4% | +0.017 | -0.016 to +0.051 | $+127.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 740 | 66.5% | 66.9% | -0.004 | -0.038 to +0.029 | $-31.60 | NO EDGE |
| Edge (model beats the ask by 3c+) | 370 | 50.3% | 42.6% | +0.076 | +0.030 to +0.123 | $+282.43 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 175 | 65.7% | 52.7% | +0.130 | +0.059 to +0.202 | $+228.31 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2096 vs market 0.2172 -> **model is sharper**

## 3:30 left (754 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 751 | 66.8% | 63.3% | +0.035 | +0.003 to +0.066 | $+262.57 | PASSES |
| Lean (bet the side BTC is on now) | 754 | 70.3% | 71.1% | -0.008 | -0.040 to +0.023 | $-62.45 | NO EDGE |
| Edge (model beats the ask by 3c+) | 425 | 38.6% | 35.3% | +0.033 | -0.009 to +0.074 | $+138.82 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 87 | 56.3% | 52.4% | +0.039 | -0.062 to +0.141 | $+34.27 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1960 vs market 0.1972 -> **model is sharper**

## 3:00 left (761 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 760 | 65.7% | 62.2% | +0.035 | +0.005 to +0.064 | $+263.40 | PASSES |
| Lean (bet the side BTC is on now) | 760 | 75.5% | 74.3% | +0.013 | -0.017 to +0.042 | $+95.29 | NO EDGE |
| Edge (model beats the ask by 3c+) | 465 | 36.1% | 31.4% | +0.048 | +0.011 to +0.084 | $+221.68 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 44 | 88.6% | 71.9% | +0.168 | +0.070 to +0.265 | $+73.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1701 vs market 0.1750 -> **model is sharper**

## 2:00 left (767 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 729 | 61.0% | 58.7% | +0.024 | -0.002 to +0.050 | $+171.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 715 | 83.2% | 79.9% | +0.033 | +0.007 to +0.060 | $+239.51 | PASSES |
| Edge (model beats the ask by 3c+) | 570 | 24.4% | 21.9% | +0.025 | -0.002 to +0.052 | $+143.33 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 92.3% | 74.3% | +0.180 | +0.077 to +0.283 | $+46.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1276 vs market 0.1284 -> **model is sharper**

## 1:00 left (759 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 563 | 51.0% | 48.8% | +0.021 | -0.005 to +0.048 | $+120.92 | NO EDGE |
| Lean (bet the side BTC is on now) | 482 | 85.9% | 82.0% | +0.038 | +0.008 to +0.069 | $+185.40 | PASSES |
| Edge (model beats the ask by 3c+) | 671 | 15.8% | 12.4% | +0.034 | +0.014 to +0.054 | $+227.44 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0867 vs market 0.0948 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=802, bias $-0.05, sd $0.58 (set BASIS_SD near 1)
- spot at open: n=802, bias $-3.81, sd $22.59 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 910 | 475 | 55% | 57% |
| 60%-70% | 865 | 524 | 65% | 70% |
| 70%-80% | 714 | 470 | 75% | 80% |
| 80%-90% | 1281 | 572 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 754 | 3601 | 0.1603 | 0.1644 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 802 (754 with decision logging, v16+)
- Markets with a signal: 289
- Alerts attempted: 127 · delivered: 124 · delivery failed: 3
- Simulated fills (quote available, size not verified): 30
- Expired alerts: 94 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 120 markets, would have won 82, +77.03 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 61 markets, would have won 45, +121.90 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 112/124 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 780 · valid comparisons: 738
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 25 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.92, typical gap $4.32, worst $20.80
- Coinbase would have named the wrong winner: 20/738 (2.7%)
- Rounds settling within $10 of the target: 110, wrong winner 19 (17%)
- Rounds settling within $25 of the target: 267, wrong winner 20 (7%)
- Rounds settling within $50 of the target: 427, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 124 (goal: 300)
- Simulated paper trades: 30 · no-trade (expired/unconfirmed): 94
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 15/30 = 50% vs break-even 49.8% (price paid + fee)
- Paper P&L after fees: -6.29 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 127
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 42/124 | 82 | 0 | +57.72 |
| 10s | 40/124 | 84 | 0 | +28.59 |
| 20s | 35/124 | 89 | 0 | +42.37 |
| 30s | 30/124 | 94 | 0 | -6.29 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 71 · loops: 117114 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
