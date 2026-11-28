# polybot report

Updated 2026-11-28 07:31 UTC | 3874 checkpoints logged | 3678 graded | 780 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 732 settled rounds observed · 121 alerts (118 delivered) · **27 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/716 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1614 vs market 0.1658 on 732 rounds -> model sharper
3. **Simulated profit after fees:** -11.35 on 27 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.69 to +3.84
4. **Quote available at simulated tap (size not verified):** 5s 39/118 · 10s 37/118 · 20s 32/118 · 30s 27/118
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 69 runs, stalls over 5s 13/113814 loops, longest BTC price gap 21.8s · checks with no market quote 98/3602 (book fallback used 1468) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 27/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 27/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 74/118 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 27 tickets at every delay (right 13/27): 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (718 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 717 | 66.0% | 64.5% | +0.015 | -0.019 to +0.049 | $+105.09 | NO EDGE |
| Lean (bet the side BTC is on now) | 718 | 66.3% | 67.0% | -0.007 | -0.041 to +0.027 | $-49.13 | NO EDGE |
| Edge (model beats the ask by 3c+) | 359 | 50.1% | 42.6% | +0.075 | +0.027 to +0.123 | $+269.21 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 170 | 64.7% | 52.5% | +0.122 | +0.049 to +0.195 | $+206.73 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2099 vs market 0.2174 -> **model is sharper**

## 3:30 left (733 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 730 | 66.7% | 63.2% | +0.035 | +0.003 to +0.067 | $+254.22 | PASSES |
| Lean (bet the side BTC is on now) | 733 | 70.0% | 71.2% | -0.012 | -0.044 to +0.020 | $-86.90 | NO EDGE |
| Edge (model beats the ask by 3c+) | 413 | 38.7% | 35.2% | +0.035 | -0.007 to +0.077 | $+145.25 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 82 | 57.3% | 52.2% | +0.052 | -0.052 to +0.155 | $+42.23 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1970 vs market 0.1983 -> **model is sharper**

## 3:00 left (741 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 740 | 65.1% | 61.9% | +0.032 | +0.002 to +0.062 | $+240.08 | PASSES |
| Lean (bet the side BTC is on now) | 740 | 75.3% | 74.2% | +0.011 | -0.019 to +0.041 | $+79.37 | NO EDGE |
| Edge (model beats the ask by 3c+) | 455 | 35.8% | 31.2% | +0.046 | +0.009 to +0.083 | $+209.38 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 42 | 88.1% | 71.6% | +0.165 | +0.063 to +0.266 | $+69.20 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1715 vs market 0.1762 -> **model is sharper**

## 2:00 left (747 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 709 | 61.4% | 58.9% | +0.024 | -0.002 to +0.051 | $+171.07 | NO EDGE |
| Lean (bet the side BTC is on now) | 696 | 82.8% | 79.8% | +0.030 | +0.003 to +0.057 | $+208.99 | PASSES |
| Edge (model beats the ask by 3c+) | 557 | 24.8% | 22.0% | +0.028 | +0.000 to +0.056 | $+155.91 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 92.3% | 74.3% | +0.180 | +0.077 to +0.283 | $+46.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1291 vs market 0.1308 -> **model is sharper**

## 1:00 left (739 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 551 | 50.6% | 48.3% | +0.023 | -0.004 to +0.050 | $+128.29 | NO EDGE |
| Lean (bet the side BTC is on now) | 470 | 85.5% | 81.9% | +0.036 | +0.005 to +0.068 | $+170.84 | PASSES |
| Edge (model beats the ask by 3c+) | 653 | 16.1% | 12.5% | +0.036 | +0.015 to +0.057 | $+234.92 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0879 vs market 0.0968 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=780, bias $-0.05, sd $0.58 (set BASIS_SD near 1)
- spot at open: n=780, bias $-3.89, sd $22.82 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 893 | 463 | 55% | 57% |
| 60%-70% | 835 | 509 | 65% | 70% |
| 70%-80% | 691 | 453 | 75% | 80% |
| 80%-90% | 1248 | 555 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 732 | 3498 | 0.1614 | 0.1658 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 780 (732 with decision logging, v16+)
- Markets with a signal: 279
- Alerts attempted: 121 · delivered: 118 · delivery failed: 3
- Simulated fills (quote available, size not verified): 27
- Expired alerts: 91 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 117 markets, would have won 80, +74.62 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 59 markets, would have won 43, +114.34 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 107/118 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 758 · valid comparisons: 716
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 25 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.95, typical gap $4.35, worst $20.80
- Coinbase would have named the wrong winner: 20/716 (2.8%)
- Rounds settling within $10 of the target: 108, wrong winner 19 (18%)
- Rounds settling within $25 of the target: 259, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 415, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 118 (goal: 300)
- Simulated paper trades: 27 · no-trade (expired/unconfirmed): 91
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 13/27 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -11.35 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 121
- Coinbase trade -> we received it: median 966 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 39/118 | 79 | 0 | +52.66 |
| 10s | 37/118 | 81 | 0 | +23.53 |
| 20s | 32/118 | 86 | 0 | +37.31 |
| 30s | 27/118 | 91 | 0 | -11.35 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 69 · loops: 113814 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
