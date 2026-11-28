# polybot report

Updated 2026-11-28 10:18 UTC | 4033 checkpoints logged | 3839 graded | 814 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 766 settled rounds observed · 127 alerts (124 delivered) · **30 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 21/750 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1604 vs market 0.1646 on 766 rounds -> model sharper
3. **Simulated profit after fees:** -6.29 on 30 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -4.19 to +3.77
4. **Quote available at simulated tap (size not verified):** 5s 42/124 · 10s 40/124 · 20s 35/124 · 30s 30/124
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 72 runs, stalls over 5s 13/118764 loops, longest BTC price gap 21.8s · checks with no market quote 98/3761 (book fallback used 1537) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 30/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 30/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 78/124 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 30 tickets at every delay (right 15/30): 5s -12.55 · 10s -14.48 · 20s -9.39 · 30s -6.29. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (752 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 750 | 66.3% | 64.6% | +0.017 | -0.016 to +0.050 | $+128.13 | NO EDGE |
| Lean (bet the side BTC is on now) | 752 | 66.6% | 67.0% | -0.003 | -0.037 to +0.030 | $-25.72 | NO EDGE |
| Edge (model beats the ask by 3c+) | 374 | 50.3% | 42.5% | +0.077 | +0.031 to +0.124 | $+289.41 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 177 | 65.5% | 52.6% | +0.130 | +0.059 to +0.201 | $+229.65 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2088 vs market 0.2164 -> **model is sharper**

## 3:30 left (766 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 763 | 66.7% | 63.4% | +0.033 | +0.001 to +0.064 | $+249.56 | PASSES |
| Lean (bet the side BTC is on now) | 766 | 70.2% | 71.1% | -0.009 | -0.040 to +0.023 | $-67.76 | NO EDGE |
| Edge (model beats the ask by 3c+) | 430 | 38.4% | 35.3% | +0.031 | -0.010 to +0.072 | $+132.53 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 88 | 55.7% | 52.5% | +0.032 | -0.069 to +0.133 | $+28.14 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1957 vs market 0.1967 -> **model is sharper**

## 3:00 left (773 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 772 | 65.2% | 62.1% | +0.030 | +0.001 to +0.060 | $+233.61 | PASSES |
| Lean (bet the side BTC is on now) | 772 | 75.3% | 74.2% | +0.010 | -0.019 to +0.040 | $+81.02 | NO EDGE |
| Edge (model beats the ask by 3c+) | 470 | 35.7% | 31.3% | +0.044 | +0.008 to +0.080 | $+206.78 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 44 | 88.6% | 71.9% | +0.168 | +0.070 to +0.265 | $+73.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1705 vs market 0.1751 -> **model is sharper**

## 2:00 left (778 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 738 | 61.1% | 58.8% | +0.023 | -0.003 to +0.049 | $+168.17 | NO EDGE |
| Lean (bet the side BTC is on now) | 724 | 82.9% | 79.7% | +0.031 | +0.005 to +0.058 | $+226.27 | PASSES |
| Edge (model beats the ask by 3c+) | 579 | 24.5% | 21.9% | +0.027 | -0.000 to +0.053 | $+153.45 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1282 vs market 0.1288 -> **model is sharper**

## 1:00 left (770 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 572 | 50.9% | 48.9% | +0.020 | -0.006 to +0.047 | $+115.11 | NO EDGE |
| Lean (bet the side BTC is on now) | 488 | 85.7% | 82.0% | +0.037 | +0.006 to +0.068 | $+179.92 | PASSES |
| Edge (model beats the ask by 3c+) | 681 | 15.9% | 12.3% | +0.036 | +0.015 to +0.056 | $+242.87 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0874 vs market 0.0966 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=814, bias $-0.05, sd $0.57 (set BASIS_SD near 1)
- spot at open: n=814, bias $-3.90, sd $22.49 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 932 | 484 | 55% | 57% |
| 60%-70% | 873 | 529 | 65% | 70% |
| 70%-80% | 725 | 478 | 75% | 80% |
| 80%-90% | 1298 | 578 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 766 | 3659 | 0.1604 | 0.1646 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 814 (766 with decision logging, v16+)
- Markets with a signal: 293
- Alerts attempted: 127 · delivered: 124 · delivery failed: 3
- Simulated fills (quote available, size not verified): 30
- Expired alerts: 94 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 123 markets, would have won 83, +70.37 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 61 markets, would have won 45, +121.90 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 112/124 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 791 · valid comparisons: 750
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.94, typical gap $4.29, worst $20.80
- Coinbase would have named the wrong winner: 21/750 (2.8%)
- Rounds settling within $10 of the target: 112, wrong winner 20 (18%)
- Rounds settling within $25 of the target: 272, wrong winner 21 (8%)
- Rounds settling within $50 of the target: 437, wrong winner 21 (5%)

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

- Runs: 72 · loops: 118764 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
