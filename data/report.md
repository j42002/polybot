# polybot report

Updated 2026-11-28 02:54 UTC | 3622 checkpoints logged | 3433 graded | 730 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 682 settled rounds observed · 111 alerts (109 delivered) · **24 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/667 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 36
2. **Model vs market accuracy (Brier, lower is better):** model 0.1623 vs market 0.1677 on 682 rounds -> model sharper
3. **Simulated profit after fees:** -21.65 on 24 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.46 to +3.65
4. **Quote available at simulated tap (size not verified):** 5s 34/109 · 10s 32/109 · 20s 27/109 · 30s 24/109
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 64 runs, stalls over 5s 4/105582 loops, longest BTC price gap 10.8s · checks with no market quote 92/3350 (book fallback used 1359) · bad close samples 16 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 24/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 24/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 67/109 delivered alerts (61%) vs average break-even 52% at the alert price.
- Same 24 tickets at every delay (right 11/24): 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 10, of which right 7/10. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (669 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 668 | 65.6% | 64.6% | +0.010 | -0.025 to +0.045 | $+66.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 669 | 65.9% | 67.2% | -0.013 | -0.048 to +0.023 | $-85.10 | NO EDGE |
| Edge (model beats the ask by 3c+) | 333 | 49.5% | 42.9% | +0.067 | +0.017 to +0.116 | $+222.74 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 156 | 63.5% | 52.9% | +0.106 | +0.029 to +0.182 | $+164.86 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2118 vs market 0.2185 -> **model is sharper**

## 3:30 left (684 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 683 | 66.0% | 62.9% | +0.031 | -0.002 to +0.064 | $+212.18 | NO EDGE |
| Lean (bet the side BTC is on now) | 684 | 69.9% | 71.2% | -0.013 | -0.046 to +0.021 | $-87.30 | NO EDGE |
| Edge (model beats the ask by 3c+) | 383 | 39.2% | 35.1% | +0.041 | -0.003 to +0.085 | $+157.57 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 79 | 58.2% | 52.1% | +0.062 | -0.043 to +0.167 | $+48.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1975 vs market 0.2006 -> **model is sharper**

## 3:00 left (692 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 691 | 64.5% | 61.6% | +0.030 | -0.001 to +0.061 | $+206.53 | NO EDGE |
| Lean (bet the side BTC is on now) | 691 | 75.1% | 74.3% | +0.009 | -0.023 to +0.040 | $+59.18 | NO EDGE |
| Edge (model beats the ask by 3c+) | 419 | 35.3% | 30.9% | +0.044 | +0.005 to +0.082 | $+183.47 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 39 | 87.2% | 71.5% | +0.157 | +0.047 to +0.266 | $+61.09 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1725 vs market 0.1776 -> **model is sharper**

## 2:00 left (698 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 660 | 62.3% | 59.2% | +0.030 | +0.003 to +0.058 | $+200.38 | PASSES |
| Lean (bet the side BTC is on now) | 647 | 82.7% | 79.8% | +0.029 | +0.001 to +0.057 | $+189.26 | PASSES |
| Edge (model beats the ask by 3c+) | 520 | 25.0% | 21.9% | +0.031 | +0.002 to +0.059 | $+159.97 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 92.0% | 74.6% | +0.174 | +0.068 to +0.281 | $+43.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1295 vs market 0.1328 -> **model is sharper**

## 1:00 left (690 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 513 | 50.5% | 48.5% | +0.020 | -0.008 to +0.048 | $+103.33 | NO EDGE |
| Lean (bet the side BTC is on now) | 438 | 85.4% | 81.3% | +0.041 | +0.008 to +0.074 | $+180.09 | PASSES |
| Edge (model beats the ask by 3c+) | 607 | 16.6% | 12.8% | +0.038 | +0.017 to +0.060 | $+233.01 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0881 vs market 0.0992 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=730, bias $-0.05, sd $0.60 (set BASIS_SD near 1)
- spot at open: n=730, bias $-3.85, sd $22.69 (set BASIS_SD near 23)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 828 | 430 | 55% | 57% |
| 60%-70% | 776 | 468 | 65% | 69% |
| 70%-80% | 648 | 427 | 75% | 79% |
| 80%-90% | 1170 | 517 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 682 | 3253 | 0.1623 | 0.1677 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 730 (682 with decision logging, v16+)
- Markets with a signal: 260
- Alerts attempted: 111 · delivered: 109 · delivery failed: 2
- Simulated fills (quote available, size not verified): 24
- Expired alerts: 85 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 111 markets, would have won 75, +58.63 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 56 markets, would have won 41, +110.52 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 100/109 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 703 · valid comparisons: 667
- Missing/untrusted: 16 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.78, typical gap $4.40, worst $20.80
- Coinbase would have named the wrong winner: 20/667 (3.0%)
- Rounds settling within $10 of the target: 101, wrong winner 19 (19%)
- Rounds settling within $25 of the target: 229, wrong winner 20 (9%)
- Rounds settling within $50 of the target: 377, wrong winner 20 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 109 (goal: 300)
- Simulated paper trades: 24 · no-trade (expired/unconfirmed): 85
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 11/24 = 46% vs break-even 49.1% (price paid + fee)
- Paper P&L after fees: -21.65 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 111
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 71 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 34/109 | 75 | 0 | +21.93 |
| 10s | 32/109 | 77 | 0 | -7.20 |
| 20s | 27/109 | 82 | 0 | +6.58 |
| 30s | 24/109 | 85 | 0 | -21.65 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 64 · loops: 105582 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
