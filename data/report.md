# polybot report

Updated 2026-11-27 05:41 UTC | 2412 checkpoints logged | 2245 graded | 481 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 433 settled rounds observed · 70 alerts (69 delivered) · **12 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/424 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1531 vs market 0.1607 on 433 rounds -> model sharper
3. **Simulated profit after fees:** -3.33 on 12 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -6.97 to +6.42
4. **Quote available at simulated tap (size not verified):** 5s 17/69 · 10s 16/69 · 20s 14/69 · 30s 12/69
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 41 runs, stalls over 5s 3/67637 loops, longest BTC price gap 10.7s · checks with no market quote 68/2140 (book fallback used 896) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 12/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (433 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 433 | 66.5% | 64.9% | +0.017 | -0.027 to +0.060 | $+71.73 | NO EDGE |
| Lean (bet the side BTC is on now) | 433 | 66.7% | 67.5% | -0.008 | -0.051 to +0.036 | $-32.53 | NO EDGE |
| Edge (model beats the ask by 3c+) | 222 | 50.0% | 41.1% | +0.089 | +0.029 to +0.149 | $+197.20 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 98 | 67.3% | 51.9% | +0.154 | +0.061 to +0.248 | $+151.18 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2048 vs market 0.2149 -> **model is sharper**

## 3:30 left (443 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 443 | 66.1% | 63.3% | +0.028 | -0.013 to +0.069 | $+123.61 | NO EDGE |
| Lean (bet the side BTC is on now) | 443 | 71.8% | 71.3% | +0.005 | -0.037 to +0.046 | $+20.44 | NO EDGE |
| Edge (model beats the ask by 3c+) | 252 | 39.7% | 34.5% | +0.052 | -0.001 to +0.105 | $+130.83 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 53 | 60.4% | 52.0% | +0.084 | -0.043 to +0.211 | $+44.59 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1881 vs market 0.1956 -> **model is sharper**

## 3:00 left (452 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 451 | 63.9% | 61.5% | +0.024 | -0.014 to +0.062 | $+106.34 | NO EDGE |
| Lean (bet the side BTC is on now) | 451 | 76.3% | 74.4% | +0.019 | -0.019 to +0.057 | $+86.13 | NO EDGE |
| Edge (model beats the ask by 3c+) | 275 | 33.8% | 29.8% | +0.040 | -0.006 to +0.086 | $+110.17 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 24 | 87.5% | 71.4% | +0.161 | +0.021 to +0.300 | $+38.53 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1638 vs market 0.1709 -> **model is sharper**

## 2:00 left (460 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 433 | 62.6% | 59.8% | +0.028 | -0.005 to +0.061 | $+121.61 | NO EDGE |
| Lean (bet the side BTC is on now) | 426 | 84.5% | 80.5% | +0.040 | +0.007 to +0.074 | $+172.37 | PASSES |
| Edge (model beats the ask by 3c+) | 343 | 23.9% | 21.4% | +0.025 | -0.009 to +0.059 | $+85.37 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1232 vs market 0.1258 -> **model is sharper**

## 1:00 left (457 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 341 | 50.4% | 48.4% | +0.020 | -0.013 to +0.053 | $+68.72 | NO EDGE |
| Lean (bet the side BTC is on now) | 287 | 88.2% | 83.1% | +0.051 | +0.012 to +0.089 | $+145.86 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 402 | 16.2% | 12.3% | +0.038 | +0.013 to +0.063 | $+153.67 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0793 vs market 0.0912 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=481, bias $-0.08, sd $0.74 (set BASIS_SD near 1)
- spot at open: n=481, bias $-1.60, sd $23.08 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 522 | 278 | 55% | 57% |
| 60%-70% | 502 | 306 | 65% | 71% |
| 70%-80% | 425 | 285 | 75% | 82% |
| 80%-90% | 785 | 356 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 433 | 2065 | 0.1531 | 0.1607 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 481 (433 with decision logging, v16+)
- Markets with a signal: 167
- Alerts attempted: 70 · delivered: 69 · delivery failed: 1
- Simulated fills (quote available, size not verified): 12
- Expired alerts: 57 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 71 markets, would have won 49, +45.58 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 36 markets, would have won 29, +97.60 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 65/69 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 450 · valid comparisons: 424
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.79, typical gap $2.85, worst $12.31
- Coinbase would have named the wrong winner: 5/424 (1.2%)
- Rounds settling within $10 of the target: 62, wrong winner 5 (8%)
- Rounds settling within $25 of the target: 130, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 218, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 69 (goal: 300)
- Simulated paper trades: 12 · no-trade (expired/unconfirmed): 57
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/12 = 50% vs break-even 49.7% (price paid + fee)
- Paper P&L after fees: -3.33 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 70
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 75 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 17/69 | 52 | 0 | +50.69 |
| 10s | 16/69 | 53 | 0 | +40.68 |
| 20s | 14/69 | 55 | 0 | +18.11 |
| 30s | 12/69 | 57 | 0 | -3.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 41 · loops: 67637 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
