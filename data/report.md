# polybot report

Updated 2026-11-26 22:18 UTC | 2001 checkpoints logged | 1837 graded | 398 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 350 settled rounds observed · 55 alerts (54 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/345 valid rounds (1.4%) where Coinbase points at the wrong winner · missing 17
2. **Model vs market accuracy (Brier, lower is better):** model 0.1510 vs market 0.1592 on 350 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 13/54 · 10s 13/54 · 20s 11/54 · 30s 9/54
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 33 runs, stalls over 5s 3/54437 loops, longest BTC price gap 10.7s · checks with no market quote 68/1729 (book fallback used 708) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (352 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 352 | 65.6% | 64.5% | +0.011 | -0.038 to +0.060 | $+39.02 | NO EDGE |
| Lean (bet the side BTC is on now) | 352 | 65.3% | 67.5% | -0.022 | -0.071 to +0.027 | $-76.34 | NO EDGE |
| Edge (model beats the ask by 3c+) | 184 | 52.2% | 41.0% | +0.112 | +0.047 to +0.177 | $+205.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 81 | 67.9% | 51.5% | +0.164 | +0.062 to +0.266 | $+132.97 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2076 vs market 0.2184 -> **model is sharper**

## 3:30 left (361 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 361 | 68.1% | 64.1% | +0.041 | -0.005 to +0.086 | $+147.36 | NO EDGE |
| Lean (bet the side BTC is on now) | 361 | 72.6% | 71.2% | +0.014 | -0.032 to +0.060 | $+50.57 | NO EDGE |
| Edge (model beats the ask by 3c+) | 204 | 41.7% | 35.0% | +0.067 | +0.007 to +0.127 | $+136.32 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 42 | 59.5% | 51.4% | +0.081 | -0.064 to +0.226 | $+34.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1860 vs market 0.1965 -> **model is sharper**

## 3:00 left (370 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 370 | 65.1% | 61.5% | +0.037 | -0.005 to +0.078 | $+135.76 | NO EDGE |
| Lean (bet the side BTC is on now) | 370 | 76.8% | 74.5% | +0.022 | -0.019 to +0.064 | $+82.63 | NO EDGE |
| Edge (model beats the ask by 3c+) | 225 | 34.2% | 29.7% | +0.046 | -0.005 to +0.096 | $+102.87 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 18 | 88.9% | 71.2% | +0.177 | +0.022 to +0.333 | $+31.92 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1605 vs market 0.1689 -> **model is sharper**

## 2:00 left (378 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 354 | 62.1% | 59.8% | +0.023 | -0.013 to +0.060 | $+82.74 | NO EDGE |
| Lean (bet the side BTC is on now) | 349 | 85.1% | 80.4% | +0.047 | +0.011 to +0.084 | $+165.22 | PASSES |
| Edge (model beats the ask by 3c+) | 282 | 23.4% | 21.3% | +0.021 | -0.016 to +0.058 | $+59.28 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 16 | 100.0% | 75.2% | +0.248 | +0.220 to +0.276 | $+39.68 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1203 vs market 0.1211 -> **model is sharper**

## 1:00 left (376 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 281 | 49.1% | 47.6% | +0.015 | -0.021 to +0.051 | $+41.65 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 235 | 89.4% | 82.8% | +0.065 | +0.023 to +0.107 | $+153.07 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 327 | 15.3% | 11.8% | +0.035 | +0.008 to +0.062 | $+114.70 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0781 vs market 0.0897 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=398, bias $-0.09, sd $0.81 (set BASIS_SD near 1)
- spot at open: n=398, bias $-1.79, sd $22.97 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 430 | 227 | 55% | 57% |
| 60%-70% | 408 | 250 | 65% | 72% |
| 70%-80% | 344 | 232 | 75% | 82% |
| 80%-90% | 644 | 294 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 350 | 1657 | 0.151 | 0.1592 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 398 (350 with decision logging, v16+)
- Markets with a signal: 133
- Alerts attempted: 55 · delivered: 54 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 45 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 60 markets, would have won 41, +37.97 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 26 markets, would have won 21, +77.44 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 50/54 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 362 · valid comparisons: 345
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.50, typical gap $2.82, worst $12.31
- Coinbase would have named the wrong winner: 5/345 (1.4%)
- Rounds settling within $10 of the target: 47, wrong winner 5 (11%)
- Rounds settling within $25 of the target: 102, wrong winner 5 (5%)
- Rounds settling within $50 of the target: 178, wrong winner 5 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 54 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 45
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 55
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 30 ms (worst 75)
- Price read -> decision made: median 79 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 13/54 | 41 | 0 | +15.83 |
| 10s | 13/54 | 41 | 0 | +15.83 |
| 20s | 11/54 | 43 | 0 | -6.74 |
| 30s | 9/54 | 45 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 33 · loops: 54437 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
