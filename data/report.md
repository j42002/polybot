# polybot report

Updated 2026-11-28 16:45 UTC | 4402 checkpoints logged | 4204 graded | 889 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 841 settled rounds observed · 144 alerts (141 delivered) · **34 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/821 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 47
2. **Model vs market accuracy (Brier, lower is better):** model 0.1594 vs market 0.1631 on 841 rounds -> model sharper
3. **Simulated profit after fees:** +5.73 on 34 trades of $10 · win rate 50% vs break-even 49%, 95% range per trade -3.69 to +4.03
4. **Quote available at simulated tap (size not verified):** 5s 48/141 · 10s 46/141 · 20s 39/141 · 30s 34/141
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 79 runs, stalls over 5s 13/130313 loops, longest BTC price gap 21.8s · checks with no market quote 101/4130 (book fallback used 1664) · bad close samples 20 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 34/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 34/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 87/141 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 34 tickets at every delay (right 17/34): 5s -0.53 · 10s -2.46 · 20s +2.63 · 30s +5.73. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (823 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 821 | 66.4% | 64.6% | +0.018 | -0.014 to +0.049 | $+143.96 | NO EDGE |
| Lean (bet the side BTC is on now) | 823 | 66.3% | 66.9% | -0.006 | -0.037 to +0.026 | $-47.88 | NO EDGE |
| Edge (model beats the ask by 3c+) | 424 | 50.0% | 43.0% | +0.070 | +0.027 to +0.114 | $+298.27 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 200 | 64.5% | 52.3% | +0.122 | +0.056 to +0.189 | $+244.51 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2089 vs market 0.2147 -> **model is sharper**

## 3:30 left (839 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 835 | 66.6% | 63.6% | +0.030 | +0.000 to +0.060 | $+250.32 | PASSES |
| Lean (bet the side BTC is on now) | 839 | 70.3% | 71.1% | -0.008 | -0.038 to +0.022 | $-68.27 | NO EDGE |
| Edge (model beats the ask by 3c+) | 478 | 38.9% | 35.3% | +0.036 | -0.003 to +0.075 | $+172.42 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 98 | 58.2% | 52.2% | +0.060 | -0.035 to +0.155 | $+58.80 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1938 vs market 0.1958 -> **model is sharper**

## 3:00 left (847 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 845 | 65.8% | 62.2% | +0.036 | +0.008 to +0.064 | $+305.56 | PASSES |
| Lean (bet the side BTC is on now) | 846 | 75.4% | 74.4% | +0.010 | -0.018 to +0.038 | $+87.44 | NO EDGE |
| Edge (model beats the ask by 3c+) | 516 | 35.7% | 31.1% | +0.046 | +0.011 to +0.080 | $+235.71 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 48 | 89.6% | 71.8% | +0.178 | +0.088 to +0.267 | $+85.25 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1689 vs market 0.1738 -> **model is sharper**

## 2:00 left (853 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 809 | 61.2% | 58.7% | +0.025 | +0.001 to +0.050 | $+202.53 | PASSES |
| Lean (bet the side BTC is on now) | 795 | 82.9% | 80.0% | +0.029 | +0.004 to +0.054 | $+232.10 | PASSES |
| Edge (model beats the ask by 3c+) | 631 | 23.6% | 21.4% | +0.022 | -0.003 to +0.048 | $+141.76 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 28 | 92.9% | 73.8% | +0.190 | +0.094 to +0.287 | $+53.23 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1266 vs market 0.1266 -> **model is sharper**

## 1:00 left (842 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 630 | 49.2% | 47.7% | +0.015 | -0.010 to +0.040 | $+95.17 | NO EDGE |
| Lean (bet the side BTC is on now) | 533 | 85.2% | 81.7% | +0.035 | +0.006 to +0.064 | $+186.47 | PASSES |
| Edge (model beats the ask by 3c+) | 748 | 15.6% | 12.2% | +0.034 | +0.015 to +0.053 | $+253.79 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0883 vs market 0.0958 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=889, bias $-0.04, sd $0.55 (set BASIS_SD near 1)
- spot at open: n=889, bias $-4.09, sd $21.93 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 1027 | 530 | 55% | 56% |
| 60%-70% | 944 | 570 | 65% | 69% |
| 70%-80% | 788 | 519 | 75% | 81% |
| 80%-90% | 1434 | 633 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 841 | 4024 | 0.1594 | 0.1631 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 889 (841 with decision logging, v16+)
- Markets with a signal: 328
- Alerts attempted: 144 · delivered: 141 · delivery failed: 3
- Simulated fills (quote available, size not verified): 34
- Expired alerts: 107 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 135 markets, would have won 93, +104.78 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 68 markets, would have won 50, +137.82 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 127/141 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 868 · valid comparisons: 821
- Missing/untrusted: 20 sampling gaps (>6s hole or <20 samples), 27 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.13, typical gap $4.22, worst $20.80
- Coinbase would have named the wrong winner: 25/821 (3.0%)
- Rounds settling within $10 of the target: 122, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 301, wrong winner 25 (8%)
- Rounds settling within $50 of the target: 485, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 141 (goal: 300)
- Simulated paper trades: 34 · no-trade (expired/unconfirmed): 107
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 17/34 = 50% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: +5.73 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 144
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 48/141 | 93 | 0 | +91.11 |
| 10s | 46/141 | 95 | 0 | +61.98 |
| 20s | 39/141 | 102 | 0 | +54.39 |
| 30s | 34/141 | 107 | 0 | +5.73 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 79 · loops: 130313 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
