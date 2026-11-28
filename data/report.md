# polybot report

Updated 2026-11-28 17:40 UTC | 4452 checkpoints logged | 4254 graded | 899 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 851 settled rounds observed · 144 alerts (141 delivered) · **34 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/831 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 48
2. **Model vs market accuracy (Brier, lower is better):** model 0.1592 vs market 0.1626 on 851 rounds -> model sharper
3. **Simulated profit after fees:** +5.73 on 34 trades of $10 · win rate 50% vs break-even 49%, 95% range per trade -3.69 to +4.03
4. **Quote available at simulated tap (size not verified):** 5s 48/141 · 10s 46/141 · 20s 39/141 · 30s 34/141
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 80 runs, stalls over 5s 13/131963 loops, longest BTC price gap 21.8s · checks with no market quote 101/4180 (book fallback used 1699) · bad close samples 20 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 34/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 34/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 87/141 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 34 tickets at every delay (right 17/34): 5s -0.53 · 10s -2.46 · 20s +2.63 · 30s +5.73. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (833 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 831 | 66.4% | 64.6% | +0.018 | -0.013 to +0.049 | $+150.05 | NO EDGE |
| Lean (bet the side BTC is on now) | 833 | 66.4% | 66.9% | -0.005 | -0.036 to +0.026 | $-41.78 | NO EDGE |
| Edge (model beats the ask by 3c+) | 431 | 50.1% | 43.0% | +0.071 | +0.028 to +0.114 | $+306.23 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 204 | 64.2% | 52.2% | +0.120 | +0.054 to +0.186 | $+244.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2087 vs market 0.2147 -> **model is sharper**

## 3:30 left (849 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 845 | 67.0% | 63.6% | +0.033 | +0.004 to +0.063 | $+281.65 | PASSES |
| Lean (bet the side BTC is on now) | 849 | 70.4% | 71.1% | -0.007 | -0.037 to +0.023 | $-58.84 | NO EDGE |
| Edge (model beats the ask by 3c+) | 483 | 38.5% | 35.2% | +0.033 | -0.006 to +0.072 | $+159.74 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 100 | 57.0% | 51.9% | +0.051 | -0.044 to +0.145 | $+50.65 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1936 vs market 0.1951 -> **model is sharper**

## 3:00 left (857 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 855 | 65.8% | 62.2% | +0.037 | +0.009 to +0.064 | $+313.68 | PASSES |
| Lean (bet the side BTC is on now) | 856 | 75.4% | 74.4% | +0.010 | -0.018 to +0.038 | $+83.27 | NO EDGE |
| Edge (model beats the ask by 3c+) | 522 | 35.2% | 31.0% | +0.043 | +0.009 to +0.077 | $+224.13 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 48 | 89.6% | 71.8% | +0.178 | +0.088 to +0.267 | $+85.25 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1687 vs market 0.1733 -> **model is sharper**

## 2:00 left (863 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 819 | 61.2% | 58.7% | +0.024 | +0.000 to +0.049 | $+199.72 | PASSES |
| Lean (bet the side BTC is on now) | 804 | 82.8% | 80.0% | +0.029 | +0.004 to +0.053 | $+230.19 | PASSES |
| Edge (model beats the ask by 3c+) | 640 | 23.4% | 21.3% | +0.021 | -0.005 to +0.046 | $+134.17 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 28 | 92.9% | 73.8% | +0.190 | +0.094 to +0.287 | $+53.23 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1264 vs market 0.1260 -> **market is sharper**

## 1:00 left (852 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 637 | 49.0% | 47.5% | +0.015 | -0.010 to +0.040 | $+93.35 | NO EDGE |
| Lean (bet the side BTC is on now) | 539 | 85.2% | 81.7% | +0.035 | +0.005 to +0.064 | $+186.89 | PASSES |
| Edge (model beats the ask by 3c+) | 756 | 15.5% | 12.2% | +0.033 | +0.014 to +0.052 | $+249.79 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0883 vs market 0.0953 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=899, bias $-0.04, sd $0.54 (set BASIS_SD near 1)
- spot at open: n=899, bias $-4.11, sd $21.83 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 1047 | 537 | 55% | 56% |
| 60%-70% | 952 | 575 | 65% | 69% |
| 70%-80% | 795 | 525 | 75% | 81% |
| 80%-90% | 1449 | 640 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 851 | 4074 | 0.1592 | 0.1626 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 899 (851 with decision logging, v16+)
- Markets with a signal: 334
- Alerts attempted: 144 · delivered: 141 · delivery failed: 3
- Simulated fills (quote available, size not verified): 34
- Expired alerts: 107 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 140 markets, would have won 94, +90.53 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 69 markets, would have won 51, +143.80 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 127/141 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 879 · valid comparisons: 831
- Missing/untrusted: 20 sampling gaps (>6s hole or <20 samples), 28 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.15, typical gap $4.21, worst $20.80
- Coinbase would have named the wrong winner: 25/831 (3.0%)
- Rounds settling within $10 of the target: 123, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 306, wrong winner 25 (8%)
- Rounds settling within $50 of the target: 493, wrong winner 25 (5%)

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

- Runs: 80 · loops: 131963 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
