# polybot report

Updated 2026-11-28 06:36 UTC | 3823 checkpoints logged | 3627 graded | 769 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 721 settled rounds observed · 120 alerts (117 delivered) · **27 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/705 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1612 vs market 0.1656 on 721 rounds -> model sharper
3. **Simulated profit after fees:** -11.35 on 27 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.69 to +3.84
4. **Quote available at simulated tap (size not verified):** 5s 39/117 · 10s 37/117 · 20s 32/117 · 30s 27/117
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 68 runs, stalls over 5s 13/112164 loops, longest BTC price gap 21.8s · checks with no market quote 98/3551 (book fallback used 1447) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 27/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 27/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 73/117 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 27 tickets at every delay (right 13/27): 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (707 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 706 | 65.9% | 64.6% | +0.013 | -0.021 to +0.047 | $+92.01 | NO EDGE |
| Lean (bet the side BTC is on now) | 707 | 66.3% | 67.0% | -0.007 | -0.041 to +0.027 | $-49.31 | NO EDGE |
| Edge (model beats the ask by 3c+) | 353 | 50.1% | 42.8% | +0.074 | +0.026 to +0.122 | $+260.63 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 169 | 64.5% | 52.6% | +0.119 | +0.046 to +0.192 | $+201.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2103 vs market 0.2177 -> **model is sharper**

## 3:30 left (723 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 721 | 66.7% | 63.2% | +0.035 | +0.003 to +0.067 | $+251.39 | PASSES |
| Lean (bet the side BTC is on now) | 723 | 69.8% | 71.2% | -0.013 | -0.046 to +0.019 | $-97.31 | NO EDGE |
| Edge (model beats the ask by 3c+) | 407 | 38.8% | 35.2% | +0.037 | -0.006 to +0.079 | $+149.38 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 81 | 56.8% | 52.1% | +0.047 | -0.058 to +0.151 | $+37.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1974 vs market 0.1989 -> **model is sharper**

## 3:00 left (731 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 730 | 65.2% | 61.9% | +0.033 | +0.003 to +0.063 | $+239.24 | PASSES |
| Lean (bet the side BTC is on now) | 730 | 75.2% | 74.2% | +0.010 | -0.020 to +0.041 | $+75.21 | NO EDGE |
| Edge (model beats the ask by 3c+) | 448 | 35.9% | 31.2% | +0.047 | +0.010 to +0.084 | $+211.23 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 42 | 88.1% | 71.6% | +0.165 | +0.063 to +0.266 | $+69.20 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1717 vs market 0.1768 -> **model is sharper**

## 2:00 left (737 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 699 | 61.7% | 58.8% | +0.028 | +0.002 to +0.055 | $+197.98 | PASSES |
| Lean (bet the side BTC is on now) | 686 | 82.8% | 79.8% | +0.030 | +0.003 to +0.057 | $+204.49 | PASSES |
| Edge (model beats the ask by 3c+) | 550 | 24.5% | 21.8% | +0.027 | -0.000 to +0.055 | $+150.23 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 92.3% | 74.3% | +0.180 | +0.077 to +0.283 | $+46.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1283 vs market 0.1301 -> **model is sharper**

## 1:00 left (729 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 544 | 50.4% | 48.4% | +0.020 | -0.007 to +0.047 | $+108.65 | NO EDGE |
| Lean (bet the side BTC is on now) | 464 | 85.8% | 81.7% | +0.040 | +0.009 to +0.072 | $+187.37 | PASSES |
| Edge (model beats the ask by 3c+) | 643 | 16.0% | 12.6% | +0.034 | +0.014 to +0.055 | $+220.35 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0868 vs market 0.0952 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=769, bias $-0.05, sd $0.59 (set BASIS_SD near 1)
- spot at open: n=769, bias $-4.02, sd $22.23 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 878 | 456 | 55% | 57% |
| 60%-70% | 823 | 500 | 65% | 70% |
| 70%-80% | 682 | 447 | 75% | 80% |
| 80%-90% | 1233 | 548 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 721 | 3447 | 0.1612 | 0.1656 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 769 (721 with decision logging, v16+)
- Markets with a signal: 277
- Alerts attempted: 120 · delivered: 117 · delivery failed: 3
- Simulated fills (quote available, size not verified): 27
- Expired alerts: 90 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 116 markets, would have won 79, +69.16 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 59 markets, would have won 43, +114.34 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 106/117 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 747 · valid comparisons: 705
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 25 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.94, typical gap $4.37, worst $20.80
- Coinbase would have named the wrong winner: 20/705 (2.8%)
- Rounds settling within $10 of the target: 106, wrong winner 19 (18%)
- Rounds settling within $25 of the target: 253, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 408, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 117 (goal: 300)
- Simulated paper trades: 27 · no-trade (expired/unconfirmed): 90
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 13/27 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -11.35 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 120
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 39/117 | 78 | 0 | +52.66 |
| 10s | 37/117 | 80 | 0 | +23.53 |
| 20s | 32/117 | 85 | 0 | +37.31 |
| 30s | 27/117 | 90 | 0 | -11.35 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 68 · loops: 112164 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
