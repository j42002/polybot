# polybot report

Updated 2026-11-27 23:13 UTC | 3411 checkpoints logged | 3223 graded | 687 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 639 settled rounds observed · 102 alerts (100 delivered) · **23 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/627 valid rounds (3.2%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1634 vs market 0.1696 on 639 rounds -> model sharper
3. **Simulated profit after fees:** -11.14 on 23 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -5.17 to +4.20
4. **Quote available at simulated tap (size not verified):** 5s 32/100 · 10s 30/100 · 20s 26/100 · 30s 23/100
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 60 runs, stalls over 5s 4/98982 loops, longest BTC price gap 10.8s · checks with no market quote 92/3139 (book fallback used 1286) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 23/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 23/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 63/100 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 23 tickets at every delay (right 11/23): 5s -13.98 · 10s -15.91 · 20s -10.82 · 30s -11.14. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 9, of which right 7/9. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (628 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 628 | 65.4% | 64.6% | +0.009 | -0.028 to +0.045 | $+55.20 | NO EDGE |
| Lean (bet the side BTC is on now) | 628 | 65.3% | 67.3% | -0.020 | -0.057 to +0.017 | $-126.19 | NO EDGE |
| Edge (model beats the ask by 3c+) | 316 | 49.7% | 42.4% | +0.073 | +0.022 to +0.124 | $+230.68 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 143 | 63.6% | 52.8% | +0.108 | +0.028 to +0.189 | $+155.14 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2129 vs market 0.2203 -> **model is sharper**

## 3:30 left (642 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 642 | 66.2% | 63.1% | +0.031 | -0.003 to +0.066 | $+201.30 | NO EDGE |
| Lean (bet the side BTC is on now) | 642 | 69.8% | 71.3% | -0.015 | -0.049 to +0.020 | $-94.49 | NO EDGE |
| Edge (model beats the ask by 3c+) | 362 | 39.8% | 35.1% | +0.047 | +0.002 to +0.092 | $+169.91 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 76 | 60.5% | 52.1% | +0.084 | -0.022 to +0.190 | $+64.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1984 vs market 0.2019 -> **model is sharper**

## 3:00 left (649 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 648 | 64.2% | 61.4% | +0.028 | -0.004 to +0.061 | $+182.38 | NO EDGE |
| Lean (bet the side BTC is on now) | 648 | 74.7% | 74.4% | +0.002 | -0.030 to +0.035 | $+15.79 | NO EDGE |
| Edge (model beats the ask by 3c+) | 393 | 34.9% | 30.1% | +0.047 | +0.007 to +0.087 | $+185.28 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 35 | 88.6% | 71.0% | +0.176 | +0.064 to +0.288 | $+61.60 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1738 vs market 0.1795 -> **model is sharper**

## 2:00 left (655 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 618 | 62.6% | 59.5% | +0.031 | +0.002 to +0.060 | $+192.35 | PASSES |
| Lean (bet the side BTC is on now) | 605 | 82.1% | 79.7% | +0.025 | -0.005 to +0.054 | $+148.61 | NO EDGE |
| Edge (model beats the ask by 3c+) | 489 | 25.2% | 21.9% | +0.033 | +0.003 to +0.062 | $+160.25 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 24 | 91.7% | 74.8% | +0.169 | +0.058 to +0.279 | $+40.48 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1308 vs market 0.1351 -> **model is sharper**

## 1:00 left (649 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 482 | 50.6% | 48.5% | +0.022 | -0.008 to +0.051 | $+104.01 | NO EDGE |
| Lean (bet the side BTC is on now) | 411 | 85.2% | 81.2% | +0.040 | +0.005 to +0.074 | $+162.44 | PASSES |
| Edge (model beats the ask by 3c+) | 576 | 17.2% | 13.0% | +0.042 | +0.020 to +0.065 | $+243.18 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0889 vs market 0.1011 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=687, bias $-0.05, sd $0.62 (set BASIS_SD near 1)
- spot at open: n=687, bias $-3.72, sd $23.20 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 781 | 405 | 55% | 56% |
| 60%-70% | 717 | 438 | 65% | 69% |
| 70%-80% | 617 | 403 | 75% | 79% |
| 80%-90% | 1097 | 488 | 87% | 95% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 639 | 3043 | 0.1634 | 0.1696 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 687 (639 with decision logging, v16+)
- Markets with a signal: 241
- Alerts attempted: 102 · delivered: 100 · delivery failed: 2
- Simulated fills (quote available, size not verified): 23
- Expired alerts: 77 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 103 markets, would have won 70, +56.92 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 53 markets, would have won 39, +107.59 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 95/100 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 659 · valid comparisons: 627
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.70, typical gap $4.48, worst $20.80
- Coinbase would have named the wrong winner: 20/627 (3.2%)
- Rounds settling within $10 of the target: 96, wrong winner 19 (20%)
- Rounds settling within $25 of the target: 206, wrong winner 20 (10%)
- Rounds settling within $50 of the target: 343, wrong winner 20 (6%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 100 (goal: 300)
- Simulated paper trades: 23 · no-trade (expired/unconfirmed): 77
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 11/23 = 48% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -11.14 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 102
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1563 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 32/100 | 68 | 0 | +42.72 |
| 10s | 30/100 | 70 | 0 | +13.59 |
| 20s | 26/100 | 74 | 0 | +17.00 |
| 30s | 23/100 | 77 | 0 | -11.14 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 60 · loops: 98982 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
