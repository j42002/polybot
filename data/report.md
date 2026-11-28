# polybot report

Updated 2026-11-28 01:59 UTC | 3572 checkpoints logged | 3383 graded | 720 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 672 settled rounds observed · 110 alerts (108 delivered) · **24 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/658 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 34
2. **Model vs market accuracy (Brier, lower is better):** model 0.1628 vs market 0.1684 on 672 rounds -> model sharper
3. **Simulated profit after fees:** -21.65 on 24 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.46 to +3.65
4. **Quote available at simulated tap (size not verified):** 5s 34/108 · 10s 32/108 · 20s 27/108 · 30s 24/108
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 63 runs, stalls over 5s 4/103932 loops, longest BTC price gap 10.8s · checks with no market quote 92/3300 (book fallback used 1348) · bad close samples 15 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 24/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 24/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 66/107 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 24 tickets at every delay (right 11/24): 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 10, of which right 7/10. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (659 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 658 | 65.8% | 64.5% | +0.013 | -0.023 to +0.048 | $+83.62 | NO EDGE |
| Lean (bet the side BTC is on now) | 659 | 65.9% | 67.2% | -0.013 | -0.049 to +0.022 | $-88.70 | NO EDGE |
| Edge (model beats the ask by 3c+) | 330 | 49.4% | 42.8% | +0.066 | +0.016 to +0.115 | $+216.74 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 153 | 63.4% | 53.0% | +0.104 | +0.026 to +0.181 | $+158.86 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2121 vs market 0.2187 -> **model is sharper**

## 3:30 left (674 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 674 | 65.9% | 62.9% | +0.030 | -0.004 to +0.063 | $+201.23 | NO EDGE |
| Lean (bet the side BTC is on now) | 674 | 69.7% | 71.1% | -0.014 | -0.048 to +0.020 | $-94.03 | NO EDGE |
| Edge (model beats the ask by 3c+) | 379 | 39.1% | 35.1% | +0.040 | -0.004 to +0.084 | $+150.80 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 79 | 58.2% | 52.1% | +0.062 | -0.043 to +0.167 | $+48.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1981 vs market 0.2009 -> **model is sharper**

## 3:00 left (682 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 681 | 64.5% | 61.5% | +0.029 | -0.002 to +0.061 | $+199.51 | NO EDGE |
| Lean (bet the side BTC is on now) | 681 | 75.0% | 74.2% | +0.008 | -0.024 to +0.040 | $+54.94 | NO EDGE |
| Edge (model beats the ask by 3c+) | 416 | 35.6% | 31.1% | +0.045 | +0.006 to +0.084 | $+187.03 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 39 | 87.2% | 71.5% | +0.157 | +0.047 to +0.266 | $+61.09 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1729 vs market 0.1782 -> **model is sharper**

## 2:00 left (688 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 650 | 62.3% | 59.2% | +0.032 | +0.004 to +0.060 | $+205.06 | PASSES |
| Lean (bet the side BTC is on now) | 637 | 82.4% | 79.7% | +0.027 | -0.001 to +0.056 | $+172.82 | NO EDGE |
| Edge (model beats the ask by 3c+) | 512 | 25.2% | 22.0% | +0.032 | +0.003 to +0.061 | $+165.30 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 92.0% | 74.6% | +0.174 | +0.068 to +0.281 | $+43.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1302 vs market 0.1340 -> **model is sharper**

## 1:00 left (680 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 506 | 50.6% | 48.4% | +0.022 | -0.006 to +0.050 | $+111.14 | NO EDGE |
| Lean (bet the side BTC is on now) | 431 | 85.4% | 81.3% | +0.041 | +0.008 to +0.074 | $+177.68 | PASSES |
| Edge (model beats the ask by 3c+) | 600 | 16.8% | 12.8% | +0.040 | +0.018 to +0.062 | $+240.52 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0884 vs market 0.1002 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=720, bias $-0.05, sd $0.61 (set BASIS_SD near 1)
- spot at open: n=720, bias $-3.76, sd $22.75 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 818 | 424 | 55% | 57% |
| 60%-70% | 762 | 461 | 65% | 69% |
| 70%-80% | 641 | 422 | 75% | 79% |
| 80%-90% | 1151 | 510 | 87% | 95% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 672 | 3203 | 0.1628 | 0.1684 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 720 (672 with decision logging, v16+)
- Markets with a signal: 257
- Alerts attempted: 110 · delivered: 108 · delivery failed: 2
- Simulated fills (quote available, size not verified): 24
- Expired alerts: 84 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 110 markets, would have won 74, +53.26 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 56 markets, would have won 41, +110.52 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 99/108 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 692 · valid comparisons: 658
- Missing/untrusted: 15 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.75, typical gap $4.41, worst $20.80
- Coinbase would have named the wrong winner: 20/658 (3.0%)
- Rounds settling within $10 of the target: 100, wrong winner 19 (19%)
- Rounds settling within $25 of the target: 223, wrong winner 20 (9%)
- Rounds settling within $50 of the target: 371, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 107 (goal: 300)
- Simulated paper trades: 24 · no-trade (expired/unconfirmed): 83
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 11/24 = 46% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -21.65 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 110
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 71 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 34/107 | 73 | 0 | +21.93 |
| 10s | 32/107 | 75 | 0 | -7.20 |
| 20s | 27/107 | 80 | 0 | +6.58 |
| 30s | 24/107 | 83 | 0 | -21.65 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 63 · loops: 103932 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
