---
polybot_auto: true
updated: 2026-11-28 18:37 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 18:36 UTC | 4502 checkpoints logged | 4301 graded | 909 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 861 settled rounds observed · 145 alerts (142 delivered) · **34 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/841 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 49
2. **Model vs market accuracy (Brier, lower is better):** model 0.1591 vs market 0.1624 on 861 rounds -> model sharper
3. **Simulated profit after fees:** +5.73 on 34 trades of $10 · win rate 50% vs break-even 49%, 95% range per trade -3.69 to +4.03
4. **Quote available at simulated tap (size not verified):** 5s 48/142 · 10s 46/142 · 20s 39/142 · 30s 34/142
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 81 runs, stalls over 5s 13/133613 loops, longest BTC price gap 21.8s · checks with no market quote 104/4230 (book fallback used 1720) · bad close samples 20 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 34/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 34/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 87/141 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 34 tickets at every delay (right 17/34): 5s -0.53 · 10s -2.46 · 20s +2.63 · 30s +5.73. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (842 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 840 | 66.5% | 64.6% | +0.019 | -0.012 to +0.050 | $+160.82 | NO EDGE |
| Lean (bet the side BTC is on now) | 842 | 66.5% | 66.9% | -0.004 | -0.035 to +0.027 | $-32.71 | NO EDGE |
| Edge (model beats the ask by 3c+) | 436 | 50.2% | 43.0% | +0.073 | +0.030 to +0.115 | $+316.82 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 207 | 64.7% | 52.2% | +0.125 | +0.059 to +0.191 | $+258.83 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2084 vs market 0.2146 -> **model is sharper**

## 3:30 left (858 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 854 | 67.1% | 63.6% | +0.035 | +0.005 to +0.064 | $+296.58 | PASSES |
| Lean (bet the side BTC is on now) | 858 | 70.5% | 71.1% | -0.006 | -0.036 to +0.023 | $-52.50 | NO EDGE |
| Edge (model beats the ask by 3c+) | 490 | 38.4% | 35.2% | +0.032 | -0.007 to +0.070 | $+155.09 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 101 | 57.4% | 51.9% | +0.055 | -0.039 to +0.149 | $+55.61 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1932 vs market 0.1946 -> **model is sharper**

## 3:00 left (866 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 864 | 65.9% | 62.2% | +0.037 | +0.010 to +0.064 | $+319.29 | PASSES |
| Lean (bet the side BTC is on now) | 865 | 75.4% | 74.3% | +0.011 | -0.017 to +0.038 | $+93.08 | NO EDGE |
| Edge (model beats the ask by 3c+) | 529 | 35.2% | 31.0% | +0.041 | +0.007 to +0.075 | $+219.36 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 48 | 89.6% | 71.8% | +0.178 | +0.088 to +0.267 | $+85.25 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1686 vs market 0.1730 -> **model is sharper**

## 2:00 left (873 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 829 | 61.2% | 58.8% | +0.024 | -0.000 to +0.048 | $+197.83 | NO EDGE |
| Lean (bet the side BTC is on now) | 814 | 82.7% | 79.9% | +0.028 | +0.003 to +0.052 | $+225.92 | PASSES |
| Edge (model beats the ask by 3c+) | 646 | 23.2% | 21.4% | +0.018 | -0.007 to +0.044 | $+117.63 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 28 | 92.9% | 73.8% | +0.190 | +0.094 to +0.287 | $+53.23 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1268 vs market 0.1260 -> **market is sharper**

## 1:00 left (862 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 646 | 49.4% | 48.0% | +0.014 | -0.011 to +0.039 | $+89.84 | NO EDGE |
| Lean (bet the side BTC is on now) | 548 | 85.2% | 81.8% | +0.034 | +0.005 to +0.063 | $+184.99 | PASSES |
| Edge (model beats the ask by 3c+) | 762 | 15.5% | 12.1% | +0.034 | +0.014 to +0.053 | $+256.00 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0882 vs market 0.0955 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=909, bias $-0.04, sd $0.54 (set BASIS_SD near 1)
- spot at open: n=909, bias $-4.14, sd $21.73 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 1058 | 542 | 55% | 56% |
| 60%-70% | 966 | 582 | 65% | 69% |
| 70%-80% | 799 | 529 | 75% | 81% |
| 80%-90% | 1467 | 647 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 861 | 4121 | 0.1591 | 0.1624 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 909 (861 with decision logging, v16+)
- Markets with a signal: 338
- Alerts attempted: 145 · delivered: 142 · delivery failed: 3
- Simulated fills (quote available, size not verified): 34
- Expired alerts: 108 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 142 markets, would have won 96, +101.17 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 70 markets, would have won 52, +149.67 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 8 markets, would have won 6, +11.42 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 128/142 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 890 · valid comparisons: 841
- Missing/untrusted: 20 sampling gaps (>6s hole or <20 samples), 29 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.18, typical gap $4.21, worst $20.80
- Coinbase would have named the wrong winner: 25/841 (3.0%)
- Rounds settling within $10 of the target: 126, wrong winner 24 (19%)
- Rounds settling within $25 of the target: 311, wrong winner 25 (8%)
- Rounds settling within $50 of the target: 501, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 141 (goal: 300)
- Simulated paper trades: 34 · no-trade (expired/unconfirmed): 107
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 17/34 = 50% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: +5.73 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 145
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

- Runs: 81 · loops: 133613 · loops over 5s: 13 (0.01%)
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
