---
polybot_auto: true
updated: 2026-11-28 04:45 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-28 04:45 UTC | 3722 checkpoints logged | 3533 graded | 750 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 702 settled rounds observed · 116 alerts (113 delivered) · **26 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/685 valid rounds (2.9%) where Coinbase points at the wrong winner · missing 40
2. **Model vs market accuracy (Brier, lower is better):** model 0.1614 vs market 0.1661 on 702 rounds -> model sharper
3. **Simulated profit after fees:** -20.88 on 26 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.17 to +3.56
4. **Quote available at simulated tap (size not verified):** 5s 37/113 · 10s 35/113 · 20s 30/113 · 30s 26/113
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 66 runs, stalls over 5s 13/108864 loops, longest BTC price gap 21.8s · checks with no market quote 92/3450 (book fallback used 1418) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 26/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 26/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 70/113 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 26 tickets at every delay (right 12/26): 5s -23.63 · 10s -25.56 · 20s -20.47 · 30s -20.88. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 11, of which right 8/11. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (689 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 688 | 65.8% | 64.6% | +0.012 | -0.022 to +0.047 | $+84.88 | NO EDGE |
| Lean (bet the side BTC is on now) | 689 | 66.3% | 67.1% | -0.008 | -0.042 to +0.027 | $-51.85 | NO EDGE |
| Edge (model beats the ask by 3c+) | 344 | 49.7% | 42.8% | +0.069 | +0.020 to +0.117 | $+236.64 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 163 | 64.4% | 52.8% | +0.116 | +0.042 to +0.191 | $+189.55 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2108 vs market 0.2176 -> **model is sharper**

## 3:30 left (704 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 702 | 66.5% | 63.2% | +0.033 | +0.001 to +0.066 | $+233.27 | PASSES |
| Lean (bet the side BTC is on now) | 704 | 70.2% | 71.2% | -0.010 | -0.043 to +0.023 | $-71.45 | NO EDGE |
| Edge (model beats the ask by 3c+) | 396 | 38.4% | 35.0% | +0.034 | -0.009 to +0.077 | $+135.58 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 81 | 56.8% | 52.1% | +0.047 | -0.058 to +0.151 | $+37.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1969 vs market 0.1987 -> **model is sharper**

## 3:00 left (712 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 711 | 65.0% | 61.8% | +0.032 | +0.002 to +0.063 | $+228.26 | PASSES |
| Lean (bet the side BTC is on now) | 711 | 75.2% | 74.3% | +0.010 | -0.021 to +0.040 | $+68.12 | NO EDGE |
| Edge (model beats the ask by 3c+) | 434 | 35.5% | 31.1% | +0.043 | +0.006 to +0.081 | $+188.66 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 41 | 87.8% | 71.5% | +0.163 | +0.059 to +0.267 | $+66.69 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1716 vs market 0.1763 -> **model is sharper**

## 2:00 left (718 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 680 | 62.1% | 59.0% | +0.030 | +0.003 to +0.057 | $+205.30 | PASSES |
| Lean (bet the side BTC is on now) | 667 | 82.9% | 79.9% | +0.030 | +0.002 to +0.057 | $+198.64 | PASSES |
| Edge (model beats the ask by 3c+) | 533 | 24.6% | 21.7% | +0.028 | +0.000 to +0.057 | $+151.31 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 92.0% | 74.6% | +0.174 | +0.068 to +0.281 | $+43.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1284 vs market 0.1309 -> **model is sharper**

## 1:00 left (710 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 530 | 50.2% | 48.2% | +0.020 | -0.007 to +0.048 | $+107.76 | NO EDGE |
| Lean (bet the side BTC is on now) | 451 | 85.6% | 81.6% | +0.040 | +0.008 to +0.072 | $+179.82 | PASSES |
| Edge (model beats the ask by 3c+) | 624 | 16.3% | 12.6% | +0.038 | +0.016 to +0.059 | $+234.12 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0876 vs market 0.0975 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=750, bias $-0.05, sd $0.60 (set BASIS_SD near 1)
- spot at open: n=750, bias $-3.94, sd $22.43 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 846 | 441 | 55% | 57% |
| 60%-70% | 802 | 485 | 65% | 69% |
| 70%-80% | 671 | 440 | 75% | 80% |
| 80%-90% | 1203 | 533 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 702 | 3353 | 0.1614 | 0.1661 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 750 (702 with decision logging, v16+)
- Markets with a signal: 269
- Alerts attempted: 116 · delivered: 113 · delivery failed: 3
- Simulated fills (quote available, size not verified): 26
- Expired alerts: 87 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 113 markets, would have won 76, +57.48 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 59 markets, would have won 43, +114.34 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 102/113 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 725 · valid comparisons: 685
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 23 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.84, typical gap $4.37, worst $20.80
- Coinbase would have named the wrong winner: 20/685 (2.9%)
- Rounds settling within $10 of the target: 104, wrong winner 19 (18%)
- Rounds settling within $25 of the target: 242, wrong winner 20 (8%)
- Rounds settling within $50 of the target: 394, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 113 (goal: 300)
- Simulated paper trades: 26 · no-trade (expired/unconfirmed): 87
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 12/26 = 46% vs break-even 49.3% (price paid + fee)
- Paper P&L after fees: -20.88 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 116
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 72 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 37/113 | 76 | 0 | +35.41 |
| 10s | 35/113 | 78 | 0 | +6.28 |
| 20s | 30/113 | 83 | 0 | +20.06 |
| 30s | 26/113 | 87 | 0 | -20.88 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 66 · loops: 108864 · loops over 5s: 13 (0.01%)
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
