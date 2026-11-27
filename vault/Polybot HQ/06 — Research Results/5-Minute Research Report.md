---
polybot_auto: true
updated: 2026-11-27 21:47 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 21:23 UTC | 3303 checkpoints logged | 3124 graded | 665 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 617 settled rounds observed · 97 alerts (95 delivered) · **20 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 16/605 valid rounds (2.6%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1621 vs market 0.1688 on 617 rounds -> model sharper
3. **Simulated profit after fees:** -44.28 on 20 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -7.15 to +2.72
4. **Quote available at simulated tap (size not verified):** 5s 29/95 · 10s 27/95 · 20s 23/95 · 30s 20/95
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 58 runs, stalls over 5s 4/95682 loops, longest BTC price gap 10.8s · checks with no market quote 84/3031 (book fallback used 1259) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 20/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 20/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 58/95 delivered alerts (61%) vs average break-even 52% at the alert price.
- Same 20 tickets at every delay (right 8/20): 5s -44.85 · 10s -44.09 · 20s -43.39 · 30s -44.28. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 9, of which right 7/9. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (609 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 609 | 65.4% | 64.6% | +0.008 | -0.030 to +0.045 | $+46.16 | NO EDGE |
| Lean (bet the side BTC is on now) | 609 | 65.4% | 67.3% | -0.019 | -0.057 to +0.018 | $-117.84 | NO EDGE |
| Edge (model beats the ask by 3c+) | 306 | 49.3% | 41.9% | +0.075 | +0.023 to +0.126 | $+228.08 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 136 | 64.0% | 52.6% | +0.114 | +0.032 to +0.196 | $+154.92 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2123 vs market 0.2203 -> **model is sharper**

## 3:30 left (622 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 622 | 65.9% | 63.0% | +0.029 | -0.006 to +0.064 | $+182.87 | NO EDGE |
| Lean (bet the side BTC is on now) | 622 | 70.1% | 71.2% | -0.011 | -0.047 to +0.024 | $-70.52 | NO EDGE |
| Edge (model beats the ask by 3c+) | 347 | 39.8% | 34.7% | +0.050 | +0.004 to +0.096 | $+174.43 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 72 | 58.3% | 52.0% | +0.064 | -0.046 to +0.174 | $+45.94 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1974 vs market 0.2017 -> **model is sharper**

## 3:00 left (629 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 628 | 64.3% | 61.3% | +0.030 | -0.003 to +0.063 | $+188.95 | NO EDGE |
| Lean (bet the side BTC is on now) | 628 | 75.2% | 74.5% | +0.007 | -0.026 to +0.040 | $+44.33 | NO EDGE |
| Edge (model beats the ask by 3c+) | 382 | 34.3% | 29.9% | +0.044 | +0.004 to +0.084 | $+168.12 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 33 | 87.9% | 70.8% | +0.171 | +0.053 to +0.289 | $+56.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1730 vs market 0.1780 -> **model is sharper**

## 2:00 left (635 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 598 | 63.0% | 59.4% | +0.036 | +0.007 to +0.065 | $+215.02 | PASSES |
| Lean (bet the side BTC is on now) | 587 | 82.6% | 79.7% | +0.029 | -0.000 to +0.059 | $+172.94 | NO EDGE |
| Edge (model beats the ask by 3c+) | 475 | 25.3% | 21.9% | +0.034 | +0.004 to +0.064 | $+161.37 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 23 | 95.7% | 75.3% | +0.204 | +0.113 to +0.294 | $+46.81 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1288 vs market 0.1336 -> **model is sharper**

## 1:00 left (629 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 467 | 49.9% | 48.0% | +0.018 | -0.011 to +0.048 | $+86.38 | NO EDGE |
| Lean (bet the side BTC is on now) | 398 | 85.4% | 81.3% | +0.042 | +0.007 to +0.076 | $+165.57 | PASSES |
| Edge (model beats the ask by 3c+) | 556 | 17.3% | 12.7% | +0.046 | +0.023 to +0.068 | $+255.03 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0875 vs market 0.1006 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=665, bias $-0.06, sd $0.63 (set BASIS_SD near 1)
- spot at open: n=665, bias $-3.43, sd $23.40 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 758 | 393 | 55% | 57% |
| 60%-70% | 698 | 425 | 65% | 69% |
| 70%-80% | 603 | 394 | 75% | 79% |
| 80%-90% | 1054 | 473 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 617 | 2944 | 0.1621 | 0.1688 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 665 (617 with decision logging, v16+)
- Markets with a signal: 230
- Alerts attempted: 97 · delivered: 95 · delivery failed: 2
- Simulated fills (quote available, size not verified): 20
- Expired alerts: 75 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 98 markets, would have won 67, +56.34 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 51 markets, would have won 39, +120.63 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 90/95 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 637 · valid comparisons: 605
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.42, typical gap $4.30, worst $20.80
- Coinbase would have named the wrong winner: 16/605 (2.6%)
- Rounds settling within $10 of the target: 92, wrong winner 15 (16%)
- Rounds settling within $25 of the target: 193, wrong winner 16 (8%)
- Rounds settling within $50 of the target: 326, wrong winner 16 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 95 (goal: 300)
- Simulated paper trades: 20 · no-trade (expired/unconfirmed): 75
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 8/20 = 40% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -44.28 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 97
- Coinbase trade -> we received it: median 890 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 29/95 | 66 | 0 | +11.85 |
| 10s | 27/95 | 68 | 0 | -14.59 |
| 20s | 23/95 | 72 | 0 | -15.57 |
| 30s | 20/95 | 75 | 0 | -44.28 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 58 · loops: 95682 · loops over 5s: 4 (0.00%)
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
