# polybot report

Updated 2026-11-28 15:50 UTC | 4352 checkpoints logged | 4154 graded | 879 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 831 settled rounds observed · 141 alerts (138 delivered) · **33 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/812 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 45
2. **Model vs market accuracy (Brier, lower is better):** model 0.1590 vs market 0.1625 on 831 rounds -> model sharper
3. **Simulated profit after fees:** -9.33 on 33 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.16 to +3.59
4. **Quote available at simulated tap (size not verified):** 5s 47/138 · 10s 45/138 · 20s 38/138 · 30s 33/138
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 78 runs, stalls over 5s 13/128663 loops, longest BTC price gap 21.8s · checks with no market quote 101/4080 (book fallback used 1644) · bad close samples 20 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 33/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 33/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 85/138 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 33 tickets at every delay (right 16/33): 5s -15.59 · 10s -17.52 · 20s -12.43 · 30s -9.33. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (813 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 811 | 66.5% | 64.6% | +0.019 | -0.013 to +0.051 | $+154.27 | NO EDGE |
| Lean (bet the side BTC is on now) | 813 | 66.7% | 66.9% | -0.002 | -0.034 to +0.030 | $-18.36 | NO EDGE |
| Edge (model beats the ask by 3c+) | 417 | 49.9% | 42.9% | +0.070 | +0.026 to +0.113 | $+290.10 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 196 | 64.3% | 52.4% | +0.119 | +0.052 to +0.187 | $+233.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2084 vs market 0.2142 -> **model is sharper**

## 3:30 left (829 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 825 | 66.5% | 63.7% | +0.028 | -0.002 to +0.058 | $+234.43 | NO EDGE |
| Lean (bet the side BTC is on now) | 829 | 70.3% | 71.2% | -0.009 | -0.039 to +0.021 | $-75.58 | NO EDGE |
| Edge (model beats the ask by 3c+) | 471 | 38.6% | 35.4% | +0.033 | -0.006 to +0.072 | $+154.92 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 96 | 57.3% | 52.2% | +0.051 | -0.046 to +0.147 | $+48.84 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1940 vs market 0.1955 -> **model is sharper**

## 3:00 left (837 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 835 | 65.9% | 62.2% | +0.036 | +0.008 to +0.064 | $+302.27 | PASSES |
| Lean (bet the side BTC is on now) | 836 | 75.5% | 74.5% | +0.010 | -0.018 to +0.038 | $+85.63 | NO EDGE |
| Edge (model beats the ask by 3c+) | 508 | 35.8% | 31.0% | +0.049 | +0.014 to +0.083 | $+247.49 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 47 | 89.4% | 71.8% | +0.175 | +0.084 to +0.267 | $+82.36 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1687 vs market 0.1739 -> **model is sharper**

## 2:00 left (843 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 800 | 61.0% | 58.6% | +0.024 | -0.001 to +0.048 | $+188.80 | NO EDGE |
| Lean (bet the side BTC is on now) | 786 | 83.1% | 80.1% | +0.030 | +0.005 to +0.055 | $+237.46 | PASSES |
| Edge (model beats the ask by 3c+) | 626 | 23.6% | 21.3% | +0.023 | -0.003 to +0.049 | $+144.44 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1260 vs market 0.1261 -> **model is sharper**

## 1:00 left (832 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 621 | 49.6% | 47.8% | +0.018 | -0.007 to +0.043 | $+113.03 | NO EDGE |
| Lean (bet the side BTC is on now) | 525 | 85.5% | 81.9% | +0.036 | +0.007 to +0.066 | $+190.80 | PASSES |
| Edge (model beats the ask by 3c+) | 740 | 15.3% | 12.2% | +0.031 | +0.012 to +0.050 | $+230.59 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0873 vs market 0.0938 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=879, bias $-0.04, sd $0.55 (set BASIS_SD near 1)
- spot at open: n=879, bias $-4.01, sd $22.02 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 1011 | 524 | 55% | 57% |
| 60%-70% | 933 | 564 | 65% | 69% |
| 70%-80% | 780 | 513 | 75% | 81% |
| 80%-90% | 1419 | 628 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 831 | 3974 | 0.159 | 0.1625 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 879 (831 with decision logging, v16+)
- Markets with a signal: 322
- Alerts attempted: 141 · delivered: 138 · delivery failed: 3
- Simulated fills (quote available, size not verified): 33
- Expired alerts: 105 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 133 markets, would have won 91, +95.44 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 66 markets, would have won 48, +128.35 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 125/138 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 857 · valid comparisons: 812
- Missing/untrusted: 20 sampling gaps (>6s hole or <20 samples), 25 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.11, typical gap $4.23, worst $20.80
- Coinbase would have named the wrong winner: 25/812 (3.1%)
- Rounds settling within $10 of the target: 120, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 295, wrong winner 25 (8%)
- Rounds settling within $50 of the target: 477, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 138 (goal: 300)
- Simulated paper trades: 33 · no-trade (expired/unconfirmed): 105
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 16/33 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -9.33 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 141
- Coinbase trade -> we received it: median 966 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 47/138 | 91 | 0 | +76.05 |
| 10s | 45/138 | 93 | 0 | +46.92 |
| 20s | 38/138 | 100 | 0 | +39.33 |
| 30s | 33/138 | 105 | 0 | -9.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 78 · loops: 128663 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
