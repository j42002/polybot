---
polybot_auto: true
updated: 2026-11-28 04:09 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 03:50 UTC | 3672 checkpoints logged | 3483 graded | 740 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 692 settled rounds observed · 114 alerts (112 delivered) · **26 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/676 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 38
2. **Model vs market accuracy (Brier, lower is better):** model 0.1621 vs market 0.1669 on 692 rounds -> model sharper
3. **Simulated profit after fees:** -20.88 on 26 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.17 to +3.56
4. **Quote available at simulated tap (size not verified):** 5s 37/112 · 10s 35/112 · 20s 30/112 · 30s 26/112
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 65 runs, stalls over 5s 4/107232 loops, longest BTC price gap 10.8s · checks with no market quote 92/3400 (book fallback used 1389) · bad close samples 16 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 26/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 26/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 69/112 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 26 tickets at every delay (right 12/26): 5s -23.63 · 10s -25.56 · 20s -20.47 · 30s -20.88. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 11, of which right 8/11. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (679 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 678 | 65.6% | 64.6% | +0.011 | -0.024 to +0.046 | $+71.64 | NO EDGE |
| Lean (bet the side BTC is on now) | 679 | 66.0% | 67.1% | -0.011 | -0.047 to +0.024 | $-77.48 | NO EDGE |
| Edge (model beats the ask by 3c+) | 339 | 49.3% | 42.7% | +0.065 | +0.016 to +0.114 | $+221.05 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 159 | 63.5% | 52.8% | +0.107 | +0.031 to +0.183 | $+170.35 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2119 vs market 0.2181 -> **model is sharper**

## 3:30 left (694 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 692 | 66.2% | 63.0% | +0.032 | -0.001 to +0.065 | $+219.93 | NO EDGE |
| Lean (bet the side BTC is on now) | 694 | 69.9% | 71.1% | -0.012 | -0.045 to +0.021 | $-84.79 | NO EDGE |
| Edge (model beats the ask by 3c+) | 390 | 38.7% | 35.0% | +0.037 | -0.006 to +0.081 | $+145.43 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 80 | 57.5% | 52.0% | +0.055 | -0.049 to +0.160 | $+44.29 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1974 vs market 0.2001 -> **model is sharper**

## 3:00 left (702 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 701 | 64.9% | 61.7% | +0.033 | +0.002 to +0.063 | $+227.91 | PASSES |
| Lean (bet the side BTC is on now) | 701 | 75.0% | 74.2% | +0.008 | -0.023 to +0.039 | $+57.46 | NO EDGE |
| Edge (model beats the ask by 3c+) | 425 | 35.1% | 30.9% | +0.041 | +0.003 to +0.079 | $+175.33 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 39 | 87.2% | 71.5% | +0.157 | +0.047 to +0.266 | $+61.09 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1722 vs market 0.1767 -> **model is sharper**

## 2:00 left (708 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 670 | 62.2% | 59.2% | +0.030 | +0.003 to +0.057 | $+200.68 | PASSES |
| Lean (bet the side BTC is on now) | 657 | 82.8% | 79.8% | +0.030 | +0.002 to +0.058 | $+195.68 | PASSES |
| Edge (model beats the ask by 3c+) | 527 | 24.7% | 21.8% | +0.029 | +0.000 to +0.057 | $+150.92 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 92.0% | 74.6% | +0.174 | +0.068 to +0.281 | $+43.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1289 vs market 0.1316 -> **model is sharper**

## 1:00 left (700 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 521 | 50.3% | 48.3% | +0.020 | -0.008 to +0.048 | $+104.02 | NO EDGE |
| Lean (bet the side BTC is on now) | 442 | 85.5% | 81.4% | +0.041 | +0.009 to +0.074 | $+182.83 | PASSES |
| Edge (model beats the ask by 3c+) | 617 | 16.4% | 12.7% | +0.037 | +0.016 to +0.058 | $+228.44 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0878 vs market 0.0980 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=740, bias $-0.05, sd $0.60 (set BASIS_SD near 1)
- spot at open: n=740, bias $-3.88, sd $22.56 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 843 | 438 | 55% | 57% |
| 60%-70% | 791 | 478 | 65% | 69% |
| 70%-80% | 656 | 433 | 75% | 80% |
| 80%-90% | 1182 | 524 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 692 | 3303 | 0.1621 | 0.1669 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 740 (692 with decision logging, v16+)
- Markets with a signal: 264
- Alerts attempted: 114 · delivered: 112 · delivery failed: 2
- Simulated fills (quote available, size not verified): 26
- Expired alerts: 86 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 112 markets, would have won 75, +54.20 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 56 markets, would have won 41, +110.52 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 102/112 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 714 · valid comparisons: 676
- Missing/untrusted: 16 sampling gaps (>6s hole or <20 samples), 22 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.82, typical gap $4.39, worst $20.80
- Coinbase would have named the wrong winner: 20/676 (3.0%)
- Rounds settling within $10 of the target: 103, wrong winner 19 (18%)
- Rounds settling within $25 of the target: 237, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 386, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 112 (goal: 300)
- Simulated paper trades: 26 · no-trade (expired/unconfirmed): 86
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 12/26 = 46% vs break-even 49.3% (price paid + fee)
- Paper P&L after fees: -20.88 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 114
- Coinbase trade -> we received it: median 966 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 37/112 | 75 | 0 | +35.41 |
| 10s | 35/112 | 77 | 0 | +6.28 |
| 20s | 30/112 | 82 | 0 | +20.06 |
| 30s | 26/112 | 86 | 0 | -20.88 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 65 · loops: 107232 · loops over 5s: 4 (0.00%)
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
