# polybot report

Updated 2026-11-27 02:55 UTC | 2259 checkpoints logged | 2094 graded | 450 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 402 settled rounds observed · 63 alerts (62 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/393 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 24
2. **Model vs market accuracy (Brier, lower is better):** model 0.1523 vs market 0.1591 on 402 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 14/62 · 10s 13/62 · 20s 11/62 · 30s 9/62
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 38 runs, stalls over 5s 3/62687 loops, longest BTC price gap 10.7s · checks with no market quote 68/1987 (book fallback used 828) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (402 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 402 | 65.9% | 64.8% | +0.011 | -0.034 to +0.056 | $+43.88 | NO EDGE |
| Lean (bet the side BTC is on now) | 402 | 66.7% | 67.5% | -0.008 | -0.053 to +0.037 | $-32.68 | NO EDGE |
| Edge (model beats the ask by 3c+) | 208 | 50.5% | 41.0% | +0.095 | +0.034 to +0.157 | $+198.21 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 92 | 68.5% | 51.5% | +0.169 | +0.075 to +0.264 | $+155.94 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2049 vs market 0.2152 -> **model is sharper**

## 3:30 left (413 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 413 | 66.6% | 64.0% | +0.026 | -0.016 to +0.068 | $+108.26 | NO EDGE |
| Lean (bet the side BTC is on now) | 413 | 72.4% | 71.2% | +0.012 | -0.031 to +0.054 | $+48.22 | NO EDGE |
| Edge (model beats the ask by 3c+) | 232 | 39.7% | 34.6% | +0.050 | -0.005 to +0.105 | $+116.28 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 46 | 58.7% | 51.5% | +0.072 | -0.066 to +0.210 | $+33.01 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1872 vs market 0.1938 -> **model is sharper**

## 3:00 left (422 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 422 | 64.5% | 62.0% | +0.025 | -0.014 to +0.064 | $+105.44 | NO EDGE |
| Lean (bet the side BTC is on now) | 422 | 77.0% | 74.5% | +0.025 | -0.013 to +0.064 | $+107.46 | NO EDGE |
| Edge (model beats the ask by 3c+) | 255 | 33.3% | 29.5% | +0.038 | -0.010 to +0.085 | $+96.51 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 21 | 85.7% | 71.6% | +0.142 | -0.017 to +0.300 | $+29.74 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1617 vs market 0.1688 -> **model is sharper**

## 2:00 left (430 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 403 | 62.0% | 59.8% | +0.022 | -0.012 to +0.057 | $+90.14 | NO EDGE |
| Lean (bet the side BTC is on now) | 397 | 84.6% | 80.5% | +0.042 | +0.007 to +0.076 | $+166.04 | PASSES |
| Edge (model beats the ask by 3c+) | 322 | 23.6% | 21.5% | +0.021 | -0.014 to +0.056 | $+67.23 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1227 vs market 0.1245 -> **model is sharper**

## 1:00 left (427 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 320 | 49.7% | 48.3% | +0.014 | -0.020 to +0.047 | $+43.58 | NO EDGE |
| Lean (bet the side BTC is on now) | 269 | 88.1% | 83.1% | +0.050 | +0.011 to +0.090 | $+134.72 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 373 | 15.3% | 11.9% | +0.033 | +0.008 to +0.059 | $+124.53 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0804 vs market 0.0901 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=450, bias $-0.08, sd $0.77 (set BASIS_SD near 1)
- spot at open: n=450, bias $-1.32, sd $23.18 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 491 | 259 | 55% | 57% |
| 60%-70% | 465 | 285 | 65% | 72% |
| 70%-80% | 401 | 270 | 75% | 83% |
| 80%-90% | 726 | 332 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 402 | 1914 | 0.1523 | 0.1591 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 450 (402 with decision logging, v16+)
- Markets with a signal: 152
- Alerts attempted: 63 · delivered: 62 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 53 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 68 markets, would have won 47, +43.44 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 30 markets, would have won 24, +86.41 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 58/62 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 417 · valid comparisons: 393
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 14 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.58, typical gap $2.77, worst $12.31
- Coinbase would have named the wrong winner: 5/393 (1.3%)
- Rounds settling within $10 of the target: 59, wrong winner 5 (8%)
- Rounds settling within $25 of the target: 121, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 204, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 62 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 53
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 63
- Coinbase trade -> we received it: median 992 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 78)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 75 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 14/62 | 48 | 0 | +26.60 |
| 10s | 13/62 | 49 | 0 | +15.83 |
| 20s | 11/62 | 51 | 0 | -6.74 |
| 30s | 9/62 | 53 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 38 · loops: 62687 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
