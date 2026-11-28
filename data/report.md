# polybot report

Updated 2026-11-28 12:08 UTC | 4141 checkpoints logged | 3947 graded | 836 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 788 settled rounds observed · 132 alerts (129 delivered) · **30 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 24/772 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1609 vs market 0.1651 on 788 rounds -> model sharper
3. **Simulated profit after fees:** -6.29 on 30 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -4.19 to +3.77
4. **Quote available at simulated tap (size not verified):** 5s 44/129 · 10s 42/129 · 20s 35/129 · 30s 30/129
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 74 runs, stalls over 5s 13/122064 loops, longest BTC price gap 21.8s · checks with no market quote 98/3869 (book fallback used 1578) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 30/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 30/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 81/129 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 30 tickets at every delay (right 15/30): 5s -12.55 · 10s -14.48 · 20s -9.39 · 30s -6.29. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (774 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 772 | 66.1% | 64.6% | +0.015 | -0.018 to +0.048 | $+114.63 | NO EDGE |
| Lean (bet the side BTC is on now) | 774 | 66.4% | 67.0% | -0.006 | -0.039 to +0.027 | $-45.41 | NO EDGE |
| Edge (model beats the ask by 3c+) | 391 | 50.9% | 42.9% | +0.080 | +0.034 to +0.125 | $+311.85 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 185 | 64.9% | 52.3% | +0.125 | +0.056 to +0.195 | $+231.85 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2097 vs market 0.2169 -> **model is sharper**

## 3:30 left (788 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 785 | 66.5% | 63.5% | +0.030 | -0.001 to +0.061 | $+235.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 788 | 69.8% | 71.2% | -0.014 | -0.045 to +0.017 | $-109.18 | NO EDGE |
| Edge (model beats the ask by 3c+) | 447 | 38.7% | 35.4% | +0.033 | -0.008 to +0.074 | $+147.66 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 91 | 56.0% | 52.4% | +0.036 | -0.063 to +0.135 | $+32.99 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1964 vs market 0.1979 -> **model is sharper**

## 3:00 left (795 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 794 | 65.6% | 62.0% | +0.036 | +0.007 to +0.065 | $+284.21 | PASSES |
| Lean (bet the side BTC is on now) | 794 | 75.3% | 74.3% | +0.010 | -0.019 to +0.039 | $+82.47 | NO EDGE |
| Edge (model beats the ask by 3c+) | 488 | 35.9% | 31.1% | +0.048 | +0.012 to +0.084 | $+234.60 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 44 | 88.6% | 71.9% | +0.168 | +0.070 to +0.265 | $+73.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1703 vs market 0.1758 -> **model is sharper**

## 2:00 left (800 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 759 | 61.3% | 59.0% | +0.023 | -0.003 to +0.048 | $+171.56 | NO EDGE |
| Lean (bet the side BTC is on now) | 745 | 83.0% | 79.9% | +0.031 | +0.005 to +0.057 | $+230.50 | PASSES |
| Edge (model beats the ask by 3c+) | 596 | 24.3% | 21.8% | +0.026 | -0.001 to +0.052 | $+153.47 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1276 vs market 0.1281 -> **model is sharper**

## 1:00 left (790 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 590 | 49.7% | 48.0% | +0.017 | -0.009 to +0.043 | $+98.27 | NO EDGE |
| Lean (bet the side BTC is on now) | 501 | 85.0% | 81.6% | +0.034 | +0.004 to +0.065 | $+171.38 | PASSES |
| Edge (model beats the ask by 3c+) | 700 | 15.7% | 12.2% | +0.035 | +0.015 to +0.055 | $+243.00 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0892 vs market 0.0972 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=836, bias $-0.04, sd $0.56 (set BASIS_SD near 1)
- spot at open: n=836, bias $-3.98, sd $22.34 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 962 | 499 | 55% | 57% |
| 60%-70% | 899 | 543 | 65% | 69% |
| 70%-80% | 736 | 486 | 75% | 80% |
| 80%-90% | 1339 | 592 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 788 | 3767 | 0.1609 | 0.1651 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 836 (788 with decision logging, v16+)
- Markets with a signal: 304
- Alerts attempted: 132 · delivered: 129 · delivery failed: 3
- Simulated fills (quote available, size not verified): 30
- Expired alerts: 99 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 126 markets, would have won 85, +75.71 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 64 markets, would have won 46, +118.02 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 117/129 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 813 · valid comparisons: 772
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.02, typical gap $4.29, worst $20.80
- Coinbase would have named the wrong winner: 24/772 (3.1%)
- Rounds settling within $10 of the target: 116, wrong winner 23 (20%)
- Rounds settling within $25 of the target: 282, wrong winner 24 (9%)
- Rounds settling within $50 of the target: 452, wrong winner 24 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 129 (goal: 300)
- Simulated paper trades: 30 · no-trade (expired/unconfirmed): 99
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 15/30 = 50% vs break-even 49.8% (price paid + fee)
- Paper P&L after fees: -6.29 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 132
- Coinbase trade -> we received it: median 896 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 44/129 | 85 | 0 | +79.09 |
| 10s | 42/129 | 87 | 0 | +49.96 |
| 20s | 35/129 | 94 | 0 | +42.37 |
| 30s | 30/129 | 99 | 0 | -6.29 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 74 · loops: 122064 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
