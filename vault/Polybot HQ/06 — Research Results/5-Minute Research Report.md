---
polybot_auto: true
updated: 2026-11-28 13:59 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 13:59 UTC | 4249 checkpoints logged | 4054 graded | 858 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 810 settled rounds observed · 137 alerts (134 delivered) · **33 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/793 valid rounds (3.2%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1600 vs market 0.1641 on 810 rounds -> model sharper
3. **Simulated profit after fees:** -9.33 on 33 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.16 to +3.59
4. **Quote available at simulated tap (size not verified):** 5s 47/134 · 10s 45/134 · 20s 38/134 · 30s 33/134
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 76 runs, stalls over 5s 13/125363 loops, longest BTC price gap 21.8s · checks with no market quote 98/3977 (book fallback used 1612) · bad close samples 18 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 33/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 33/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 83/134 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 33 tickets at every delay (right 16/33): 5s -15.59 · 10s -17.52 · 20s -12.43 · 30s -9.33. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (794 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 792 | 66.4% | 64.6% | +0.018 | -0.014 to +0.051 | $+146.06 | NO EDGE |
| Lean (bet the side BTC is on now) | 794 | 66.5% | 66.9% | -0.004 | -0.036 to +0.028 | $-30.99 | NO EDGE |
| Edge (model beats the ask by 3c+) | 404 | 50.5% | 42.9% | +0.076 | +0.031 to +0.120 | $+306.16 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 191 | 64.4% | 52.3% | +0.121 | +0.052 to +0.189 | $+231.05 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2092 vs market 0.2161 -> **model is sharper**

## 3:30 left (810 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 807 | 66.5% | 63.6% | +0.029 | -0.001 to +0.060 | $+236.45 | NO EDGE |
| Lean (bet the side BTC is on now) | 810 | 70.0% | 71.2% | -0.012 | -0.042 to +0.019 | $-95.63 | NO EDGE |
| Edge (model beats the ask by 3c+) | 459 | 39.0% | 35.4% | +0.036 | -0.004 to +0.076 | $+164.53 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 94 | 56.4% | 52.1% | +0.042 | -0.055 to +0.140 | $+39.81 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1954 vs market 0.1974 -> **model is sharper**

## 3:00 left (817 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 816 | 65.6% | 62.1% | +0.035 | +0.006 to +0.063 | $+282.16 | PASSES |
| Lean (bet the side BTC is on now) | 816 | 75.2% | 74.4% | +0.009 | -0.020 to +0.037 | $+72.04 | NO EDGE |
| Edge (model beats the ask by 3c+) | 500 | 36.2% | 31.0% | +0.052 | +0.016 to +0.087 | $+258.17 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 46 | 89.1% | 71.8% | +0.173 | +0.080 to +0.267 | $+79.75 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1697 vs market 0.1757 -> **model is sharper**

## 2:00 left (822 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 780 | 61.3% | 58.9% | +0.024 | -0.001 to +0.049 | $+188.13 | NO EDGE |
| Lean (bet the side BTC is on now) | 766 | 83.0% | 80.0% | +0.030 | +0.005 to +0.056 | $+232.63 | PASSES |
| Edge (model beats the ask by 3c+) | 611 | 24.1% | 21.5% | +0.025 | -0.001 to +0.052 | $+154.69 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1263 vs market 0.1267 -> **model is sharper**

## 1:00 left (811 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 604 | 49.7% | 48.0% | +0.017 | -0.009 to +0.043 | $+103.04 | NO EDGE |
| Lean (bet the side BTC is on now) | 513 | 85.4% | 81.7% | +0.036 | +0.007 to +0.066 | $+186.92 | PASSES |
| Edge (model beats the ask by 3c+) | 721 | 15.5% | 12.3% | +0.033 | +0.013 to +0.052 | $+236.37 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0881 vs market 0.0953 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=858, bias $-0.04, sd $0.56 (set BASIS_SD near 1)
- spot at open: n=858, bias $-4.14, sd $22.15 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 988 | 513 | 55% | 57% |
| 60%-70% | 915 | 553 | 65% | 69% |
| 70%-80% | 760 | 502 | 75% | 81% |
| 80%-90% | 1380 | 612 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 810 | 3874 | 0.16 | 0.1641 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 858 (810 with decision logging, v16+)
- Markets with a signal: 314
- Alerts attempted: 137 · delivered: 134 · delivery failed: 3
- Simulated fills (quote available, size not verified): 33
- Expired alerts: 101 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 129 markets, would have won 87, +79.92 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 66 markets, would have won 48, +128.35 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 122/134 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 835 · valid comparisons: 793
- Missing/untrusted: 18 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.09, typical gap $4.26, worst $20.80
- Coinbase would have named the wrong winner: 25/793 (3.2%)
- Rounds settling within $10 of the target: 118, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 291, wrong winner 25 (9%)
- Rounds settling within $50 of the target: 466, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 134 (goal: 300)
- Simulated paper trades: 33 · no-trade (expired/unconfirmed): 101
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 16/33 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -9.33 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 137
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 26 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 47/134 | 87 | 0 | +76.05 |
| 10s | 45/134 | 89 | 0 | +46.92 |
| 20s | 38/134 | 96 | 0 | +39.33 |
| 30s | 33/134 | 101 | 0 | -9.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 76 · loops: 125363 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
