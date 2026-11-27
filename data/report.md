# polybot report

Updated 2026-11-27 03:50 UTC | 2309 checkpoints logged | 2144 graded | 460 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 412 settled rounds observed · 65 alerts (64 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/403 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1539 vs market 0.1613 on 412 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 14/64 · 10s 13/64 · 20s 11/64 · 30s 9/64
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 39 runs, stalls over 5s 3/64337 loops, longest BTC price gap 10.7s · checks with no market quote 68/2037 (book fallback used 852) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (412 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 412 | 65.5% | 64.8% | +0.008 | -0.037 to +0.053 | $+32.12 | NO EDGE |
| Lean (bet the side BTC is on now) | 412 | 66.5% | 67.4% | -0.009 | -0.054 to +0.036 | $-36.44 | NO EDGE |
| Edge (model beats the ask by 3c+) | 212 | 50.5% | 41.0% | +0.095 | +0.034 to +0.156 | $+200.94 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 94 | 68.1% | 51.6% | +0.165 | +0.071 to +0.259 | $+155.17 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2059 vs market 0.2166 -> **model is sharper**

## 3:30 left (423 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 423 | 66.2% | 63.8% | +0.024 | -0.018 to +0.066 | $+100.80 | NO EDGE |
| Lean (bet the side BTC is on now) | 423 | 71.9% | 71.2% | +0.006 | -0.036 to +0.048 | $+26.88 | NO EDGE |
| Edge (model beats the ask by 3c+) | 238 | 39.5% | 34.6% | +0.049 | -0.005 to +0.104 | $+117.04 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 48 | 58.3% | 51.7% | +0.066 | -0.070 to +0.202 | $+31.73 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1891 vs market 0.1961 -> **model is sharper**

## 3:00 left (432 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 432 | 64.4% | 61.7% | +0.026 | -0.012 to +0.065 | $+113.52 | NO EDGE |
| Lean (bet the side BTC is on now) | 432 | 76.6% | 74.4% | +0.022 | -0.017 to +0.061 | $+95.86 | NO EDGE |
| Edge (model beats the ask by 3c+) | 262 | 34.4% | 29.8% | +0.046 | -0.002 to +0.093 | $+119.28 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 23 | 87.0% | 71.6% | +0.153 | +0.008 to +0.298 | $+35.25 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1631 vs market 0.1711 -> **model is sharper**

## 2:00 left (440 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 413 | 62.0% | 59.8% | +0.022 | -0.012 to +0.056 | $+91.06 | NO EDGE |
| Lean (bet the side BTC is on now) | 407 | 84.0% | 80.4% | +0.036 | +0.002 to +0.071 | $+147.18 | PASSES |
| Edge (model beats the ask by 3c+) | 327 | 23.5% | 21.4% | +0.021 | -0.014 to +0.056 | $+68.89 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1247 vs market 0.1263 -> **model is sharper**

## 1:00 left (437 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 329 | 49.8% | 48.2% | +0.017 | -0.017 to +0.051 | $+55.44 | NO EDGE |
| Lean (bet the side BTC is on now) | 277 | 87.7% | 83.0% | +0.047 | +0.007 to +0.086 | $+129.93 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 383 | 16.4% | 12.5% | +0.039 | +0.014 to +0.065 | $+150.18 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0810 vs market 0.0925 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=460, bias $-0.08, sd $0.76 (set BASIS_SD near 1)
- spot at open: n=460, bias $-1.48, sd $23.23 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 503 | 267 | 55% | 57% |
| 60%-70% | 481 | 294 | 65% | 71% |
| 70%-80% | 408 | 274 | 75% | 82% |
| 80%-90% | 741 | 339 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 412 | 1964 | 0.1539 | 0.1613 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 460 (412 with decision logging, v16+)
- Markets with a signal: 157
- Alerts attempted: 65 · delivered: 64 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 55 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 70 markets, would have won 48, +40.41 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 32 markets, would have won 26, +93.48 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 60/64 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 428 · valid comparisons: 403
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.63, typical gap $2.79, worst $12.31
- Coinbase would have named the wrong winner: 5/403 (1.2%)
- Rounds settling within $10 of the target: 60, wrong winner 5 (8%)
- Rounds settling within $25 of the target: 124, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 209, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 64 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 55
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 65
- Coinbase trade -> we received it: median 992 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 79)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 75 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 14/64 | 50 | 0 | +26.60 |
| 10s | 13/64 | 51 | 0 | +15.83 |
| 20s | 11/64 | 53 | 0 | -6.74 |
| 30s | 9/64 | 55 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 39 · loops: 64337 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
