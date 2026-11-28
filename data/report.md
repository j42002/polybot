# polybot report

Updated 2026-11-28 05:40 UTC | 3772 checkpoints logged | 3583 graded | 760 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 712 settled rounds observed · 118 alerts (115 delivered) · **26 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/695 valid rounds (2.9%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1611 vs market 0.1659 on 712 rounds -> model sharper
3. **Simulated profit after fees:** -20.88 on 26 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.17 to +3.56
4. **Quote available at simulated tap (size not verified):** 5s 39/115 · 10s 37/115 · 20s 32/115 · 30s 27/115
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 67 runs, stalls over 5s 13/110514 loops, longest BTC price gap 21.8s · checks with no market quote 92/3500 (book fallback used 1427) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 26/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 26/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 71/114 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 26 tickets at every delay (right 12/26): 5s -23.63 · 10s -25.56 · 20s -20.47 · 30s -20.88. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (699 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 698 | 65.8% | 64.6% | +0.011 | -0.023 to +0.046 | $+79.71 | NO EDGE |
| Lean (bet the side BTC is on now) | 699 | 66.2% | 67.1% | -0.009 | -0.043 to +0.026 | $-61.61 | NO EDGE |
| Edge (model beats the ask by 3c+) | 350 | 50.0% | 42.7% | +0.073 | +0.025 to +0.121 | $+255.83 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 166 | 64.5% | 52.6% | +0.118 | +0.044 to +0.192 | $+196.46 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2105 vs market 0.2180 -> **model is sharper**

## 3:30 left (714 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 712 | 66.7% | 63.2% | +0.035 | +0.002 to +0.067 | $+248.39 | PASSES |
| Lean (bet the side BTC is on now) | 714 | 69.9% | 71.2% | -0.013 | -0.046 to +0.020 | $-92.71 | NO EDGE |
| Edge (model beats the ask by 3c+) | 401 | 39.2% | 35.2% | +0.040 | -0.003 to +0.082 | $+158.44 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 81 | 56.8% | 52.1% | +0.047 | -0.058 to +0.151 | $+37.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1968 vs market 0.1989 -> **model is sharper**

## 3:00 left (722 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 721 | 65.2% | 61.9% | +0.033 | +0.003 to +0.063 | $+238.73 | PASSES |
| Lean (bet the side BTC is on now) | 721 | 75.3% | 74.3% | +0.010 | -0.020 to +0.041 | $+74.70 | NO EDGE |
| Edge (model beats the ask by 3c+) | 441 | 35.6% | 31.1% | +0.045 | +0.007 to +0.082 | $+197.91 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 41 | 87.8% | 71.5% | +0.163 | +0.059 to +0.267 | $+66.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1714 vs market 0.1764 -> **model is sharper**

## 2:00 left (728 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 690 | 61.7% | 58.9% | +0.029 | +0.002 to +0.056 | $+199.10 | PASSES |
| Lean (bet the side BTC is on now) | 677 | 82.9% | 79.8% | +0.030 | +0.003 to +0.058 | $+205.39 | PASSES |
| Edge (model beats the ask by 3c+) | 542 | 24.5% | 21.9% | +0.027 | -0.001 to +0.055 | $+144.40 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 26 | 92.3% | 74.3% | +0.180 | +0.077 to +0.283 | $+46.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1285 vs market 0.1304 -> **model is sharper**

## 1:00 left (720 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 538 | 50.6% | 48.5% | +0.021 | -0.006 to +0.048 | $+112.74 | NO EDGE |
| Lean (bet the side BTC is on now) | 458 | 85.8% | 81.7% | +0.041 | +0.010 to +0.073 | $+188.63 | PASSES |
| Edge (model beats the ask by 3c+) | 634 | 16.2% | 12.7% | +0.036 | +0.015 to +0.057 | $+227.98 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0871 vs market 0.0963 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=760, bias $-0.05, sd $0.59 (set BASIS_SD near 1)
- spot at open: n=760, bias $-4.02, sd $22.34 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 862 | 448 | 55% | 57% |
| 60%-70% | 814 | 492 | 65% | 69% |
| 70%-80% | 674 | 441 | 75% | 80% |
| 80%-90% | 1222 | 541 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 712 | 3403 | 0.1611 | 0.1659 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 760 (712 with decision logging, v16+)
- Markets with a signal: 273
- Alerts attempted: 118 · delivered: 115 · delivery failed: 3
- Simulated fills (quote available, size not verified): 27
- Expired alerts: 88 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 115 markets, would have won 78, +66.64 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 59 markets, would have won 43, +114.34 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 104/115 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 736 · valid comparisons: 695
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.90, typical gap $4.38, worst $20.80
- Coinbase would have named the wrong winner: 20/695 (2.9%)
- Rounds settling within $10 of the target: 106, wrong winner 19 (18%)
- Rounds settling within $25 of the target: 248, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 401, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 114 (goal: 300)
- Simulated paper trades: 26 · no-trade (expired/unconfirmed): 88
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 12/26 = 46% vs break-even 49.3% (price paid + fee)
- Paper P&L after fees: -20.88 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 118
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 38/114 | 76 | 0 | +46.64 |
| 10s | 36/114 | 78 | 0 | +17.51 |
| 20s | 31/114 | 83 | 0 | +31.29 |
| 30s | 26/114 | 88 | 0 | -20.88 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 67 · loops: 110514 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
