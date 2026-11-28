# polybot report

Updated 2026-11-28 13:04 UTC | 4195 checkpoints logged | 4000 graded | 847 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 799 settled rounds observed · 135 alerts (132 delivered) · **31 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/783 valid rounds (3.2%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1608 vs market 0.1649 on 799 rounds -> model sharper
3. **Simulated profit after fees:** -16.73 on 31 trades of $10 · win rate 48% vs break-even 50%, 95% range per trade -4.44 to +3.36
4. **Quote available at simulated tap (size not verified):** 5s 45/132 · 10s 43/132 · 20s 36/132 · 30s 31/132
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 75 runs, stalls over 5s 13/123713 loops, longest BTC price gap 21.8s · checks with no market quote 98/3923 (book fallback used 1595) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 31/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 31/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 82/131 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 31 tickets at every delay (right 15/31): 5s -22.99 · 10s -24.92 · 20s -19.83 · 30s -16.73. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (784 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 782 | 66.2% | 64.6% | +0.017 | -0.016 to +0.049 | $+131.57 | NO EDGE |
| Lean (bet the side BTC is on now) | 784 | 66.5% | 66.9% | -0.004 | -0.037 to +0.028 | $-34.37 | NO EDGE |
| Edge (model beats the ask by 3c+) | 398 | 51.0% | 42.9% | +0.081 | +0.036 to +0.126 | $+321.86 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 187 | 65.2% | 52.4% | +0.129 | +0.060 to +0.198 | $+240.98 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2096 vs market 0.2168 -> **model is sharper**

## 3:30 left (799 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 796 | 66.6% | 63.6% | +0.030 | -0.001 to +0.061 | $+239.64 | NO EDGE |
| Lean (bet the side BTC is on now) | 799 | 69.8% | 71.2% | -0.013 | -0.044 to +0.018 | $-105.45 | NO EDGE |
| Edge (model beats the ask by 3c+) | 452 | 38.7% | 35.3% | +0.034 | -0.007 to +0.074 | $+153.43 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 93 | 55.9% | 52.3% | +0.036 | -0.062 to +0.134 | $+33.63 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1963 vs market 0.1978 -> **model is sharper**

## 3:00 left (806 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 805 | 65.5% | 62.0% | +0.034 | +0.006 to +0.063 | $+277.72 | PASSES |
| Lean (bet the side BTC is on now) | 805 | 75.3% | 74.3% | +0.010 | -0.019 to +0.039 | $+79.99 | NO EDGE |
| Edge (model beats the ask by 3c+) | 494 | 36.0% | 31.1% | +0.049 | +0.014 to +0.085 | $+244.21 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 45 | 88.9% | 71.7% | +0.172 | +0.076 to +0.267 | $+77.24 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1705 vs market 0.1761 -> **model is sharper**

## 2:00 left (811 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 770 | 61.3% | 59.0% | +0.023 | -0.002 to +0.049 | $+179.92 | NO EDGE |
| Lean (bet the side BTC is on now) | 756 | 82.9% | 79.9% | +0.031 | +0.005 to +0.056 | $+231.69 | PASSES |
| Edge (model beats the ask by 3c+) | 602 | 24.3% | 21.7% | +0.026 | -0.001 to +0.052 | $+154.45 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1274 vs market 0.1278 -> **model is sharper**

## 1:00 left (800 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 598 | 49.7% | 48.0% | +0.017 | -0.009 to +0.043 | $+101.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 509 | 85.3% | 81.6% | +0.036 | +0.006 to +0.066 | $+184.26 | PASSES |
| Edge (model beats the ask by 3c+) | 710 | 15.8% | 12.4% | +0.034 | +0.014 to +0.054 | $+240.70 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0889 vs market 0.0964 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=847, bias $-0.04, sd $0.56 (set BASIS_SD near 1)
- spot at open: n=847, bias $-4.02, sd $22.22 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 976 | 506 | 55% | 57% |
| 60%-70% | 910 | 550 | 65% | 70% |
| 70%-80% | 751 | 494 | 75% | 80% |
| 80%-90% | 1352 | 602 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 799 | 3820 | 0.1608 | 0.1649 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 847 (799 with decision logging, v16+)
- Markets with a signal: 309
- Alerts attempted: 135 · delivered: 132 · delivery failed: 3
- Simulated fills (quote available, size not verified): 31
- Expired alerts: 101 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 128 markets, would have won 87, +84.25 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 65 markets, would have won 47, +123.79 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 120/132 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 824 · valid comparisons: 783
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.06, typical gap $4.28, worst $20.80
- Coinbase would have named the wrong winner: 25/783 (3.2%)
- Rounds settling within $10 of the target: 118, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 289, wrong winner 25 (9%)
- Rounds settling within $50 of the target: 462, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 131 (goal: 300)
- Simulated paper trades: 31 · no-trade (expired/unconfirmed): 100
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 15/31 = 48% vs break-even 50.0% (price paid + fee)
- Paper P&L after fees: -16.73 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 135
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 26 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 45/131 | 86 | 0 | +68.65 |
| 10s | 43/131 | 88 | 0 | +39.52 |
| 20s | 36/131 | 95 | 0 | +31.93 |
| 30s | 31/131 | 100 | 0 | -16.73 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 75 · loops: 123713 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
