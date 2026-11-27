# polybot report

Updated 2026-11-27 00:09 UTC | 2109 checkpoints logged | 1944 graded | 420 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 372 settled rounds observed · 59 alerts (58 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/365 valid rounds (1.4%) where Coinbase points at the wrong winner · missing 19
2. **Model vs market accuracy (Brier, lower is better):** model 0.1521 vs market 0.1597 on 372 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 13/58 · 10s 13/58 · 20s 11/58 · 30s 9/58
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 35 runs, stalls over 5s 3/57737 loops, longest BTC price gap 10.7s · checks with no market quote 68/1837 (book fallback used 753) · bad close samples 9 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (372 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 372 | 66.1% | 64.6% | +0.016 | -0.032 to +0.063 | $+57.93 | NO EDGE |
| Lean (bet the side BTC is on now) | 372 | 66.4% | 67.4% | -0.010 | -0.058 to +0.037 | $-38.43 | NO EDGE |
| Edge (model beats the ask by 3c+) | 195 | 50.8% | 40.8% | +0.100 | +0.036 to +0.163 | $+194.26 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 86 | 67.4% | 51.3% | +0.161 | +0.062 to +0.260 | $+138.71 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2063 vs market 0.2164 -> **model is sharper**

## 3:30 left (383 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 383 | 67.4% | 64.3% | +0.030 | -0.014 to +0.074 | $+116.61 | NO EDGE |
| Lean (bet the side BTC is on now) | 383 | 72.3% | 71.3% | +0.010 | -0.034 to +0.054 | $+37.53 | NO EDGE |
| Edge (model beats the ask by 3c+) | 214 | 40.7% | 34.7% | +0.060 | +0.002 to +0.118 | $+128.13 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 43 | 58.1% | 51.2% | +0.069 | -0.074 to +0.212 | $+29.70 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1867 vs market 0.1956 -> **model is sharper**

## 3:00 left (392 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 392 | 65.1% | 61.7% | +0.034 | -0.006 to +0.074 | $+132.72 | NO EDGE |
| Lean (bet the side BTC is on now) | 392 | 77.0% | 74.5% | +0.025 | -0.015 to +0.066 | $+99.01 | NO EDGE |
| Edge (model beats the ask by 3c+) | 239 | 33.9% | 29.4% | +0.045 | -0.005 to +0.094 | $+106.37 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 89.5% | 71.5% | +0.180 | +0.033 to +0.328 | $+34.24 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1606 vs market 0.1693 -> **model is sharper**

## 2:00 left (400 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 376 | 62.0% | 59.7% | +0.022 | -0.013 to +0.058 | $+84.23 | NO EDGE |
| Lean (bet the side BTC is on now) | 370 | 84.3% | 80.4% | +0.040 | +0.004 to +0.075 | $+146.98 | PASSES |
| Edge (model beats the ask by 3c+) | 298 | 23.5% | 21.6% | +0.019 | -0.017 to +0.056 | $+57.47 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 17 | 100.0% | 74.7% | +0.253 | +0.225 to +0.281 | $+42.97 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1227 vs market 0.1234 -> **model is sharper**

## 1:00 left (397 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 298 | 49.3% | 47.8% | +0.015 | -0.020 to +0.051 | $+46.11 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 250 | 88.4% | 82.7% | +0.057 | +0.016 to +0.098 | $+142.18 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 347 | 15.9% | 12.2% | +0.036 | +0.009 to +0.063 | $+125.35 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0810 vs market 0.0920 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=420, bias $-0.09, sd $0.79 (set BASIS_SD near 1)
- spot at open: n=420, bias $-1.77, sd $22.97 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 456 | 242 | 55% | 57% |
| 60%-70% | 431 | 264 | 65% | 71% |
| 70%-80% | 372 | 249 | 75% | 82% |
| 80%-90% | 674 | 306 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 372 | 1764 | 0.1521 | 0.1597 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 420 (372 with decision logging, v16+)
- Markets with a signal: 140
- Alerts attempted: 59 · delivered: 58 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 49 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 62 markets, would have won 43, +43.57 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 28 markets, would have won 22, +78.37 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 54/58 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 384 · valid comparisons: 365
- Missing/untrusted: 9 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.48, typical gap $2.76, worst $12.31
- Coinbase would have named the wrong winner: 5/365 (1.4%)
- Rounds settling within $10 of the target: 54, wrong winner 5 (9%)
- Rounds settling within $25 of the target: 112, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 191, wrong winner 5 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 58 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 49
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 59
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 76 ms (worst 168)
- Decision -> Discord accepted: median 1538 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 13/58 | 45 | 0 | +15.83 |
| 10s | 13/58 | 45 | 0 | +15.83 |
| 20s | 11/58 | 47 | 0 | -6.74 |
| 30s | 9/58 | 49 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 35 · loops: 57737 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
