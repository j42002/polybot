# polybot report

Updated 2026-11-27 02:00 UTC | 2209 checkpoints logged | 2044 graded | 440 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 392 settled rounds observed · 61 alerts (60 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/383 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 23
2. **Model vs market accuracy (Brier, lower is better):** model 0.1529 vs market 0.1602 on 392 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 14/60 · 10s 13/60 · 20s 11/60 · 30s 9/60
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 37 runs, stalls over 5s 3/61037 loops, longest BTC price gap 10.7s · checks with no market quote 68/1937 (book fallback used 804) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (392 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 392 | 66.1% | 64.8% | +0.013 | -0.033 to +0.059 | $+51.05 | NO EDGE |
| Lean (bet the side BTC is on now) | 392 | 66.6% | 67.5% | -0.009 | -0.055 to +0.037 | $-36.61 | NO EDGE |
| Edge (model beats the ask by 3c+) | 202 | 50.0% | 40.9% | +0.091 | +0.029 to +0.153 | $+184.10 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 88 | 68.2% | 51.6% | +0.166 | +0.069 to +0.263 | $+146.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2054 vs market 0.2147 -> **model is sharper**

## 3:30 left (403 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 403 | 66.3% | 63.9% | +0.024 | -0.019 to +0.067 | $+95.09 | NO EDGE |
| Lean (bet the side BTC is on now) | 403 | 72.0% | 71.2% | +0.008 | -0.035 to +0.051 | $+31.84 | NO EDGE |
| Edge (model beats the ask by 3c+) | 227 | 40.1% | 34.9% | +0.052 | -0.004 to +0.108 | $+117.00 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 46 | 58.7% | 51.5% | +0.072 | -0.066 to +0.210 | $+33.01 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1878 vs market 0.1952 -> **model is sharper**

## 3:00 left (412 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 412 | 64.3% | 62.0% | +0.023 | -0.016 to +0.063 | $+95.64 | NO EDGE |
| Lean (bet the side BTC is on now) | 412 | 76.9% | 74.6% | +0.024 | -0.016 to +0.063 | $+97.25 | NO EDGE |
| Edge (model beats the ask by 3c+) | 248 | 33.9% | 29.4% | +0.045 | -0.004 to +0.093 | $+111.08 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 20 | 85.0% | 71.5% | +0.135 | -0.031 to +0.301 | $+26.94 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1624 vs market 0.1710 -> **model is sharper**

## 2:00 left (420 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 394 | 62.4% | 60.2% | +0.023 | -0.012 to +0.058 | $+89.39 | NO EDGE |
| Lean (bet the side BTC is on now) | 388 | 84.3% | 80.4% | +0.039 | +0.004 to +0.074 | $+150.56 | PASSES |
| Edge (model beats the ask by 3c+) | 314 | 23.9% | 21.7% | +0.022 | -0.014 to +0.058 | $+68.66 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1237 vs market 0.1258 -> **model is sharper**

## 1:00 left (417 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 314 | 49.4% | 47.8% | +0.015 | -0.019 to +0.049 | $+47.96 | NO EDGE |
| Lean (bet the side BTC is on now) | 263 | 88.2% | 83.0% | +0.052 | +0.012 to +0.092 | $+137.80 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 365 | 15.6% | 12.1% | +0.035 | +0.009 to +0.061 | $+127.15 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0810 vs market 0.0911 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=440, bias $-0.09, sd $0.78 (set BASIS_SD near 1)
- spot at open: n=440, bias $-1.49, sd $22.66 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 477 | 253 | 55% | 57% |
| 60%-70% | 454 | 279 | 65% | 71% |
| 70%-80% | 392 | 264 | 75% | 82% |
| 80%-90% | 710 | 323 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 392 | 1864 | 0.1529 | 0.1602 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 440 (392 with decision logging, v16+)
- Markets with a signal: 147
- Alerts attempted: 61 · delivered: 60 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 51 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 66 markets, would have won 46, +45.78 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 29 markets, would have won 23, +82.74 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 56/60 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 406 · valid comparisons: 383
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 13 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.55, typical gap $2.77, worst $12.31
- Coinbase would have named the wrong winner: 5/383 (1.3%)
- Rounds settling within $10 of the target: 58, wrong winner 5 (9%)
- Rounds settling within $25 of the target: 120, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 203, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 60 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 51
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 61
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 78)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 75 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 14/60 | 46 | 0 | +26.60 |
| 10s | 13/60 | 47 | 0 | +15.83 |
| 20s | 11/60 | 49 | 0 | -6.74 |
| 30s | 9/60 | 51 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 37 · loops: 61037 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
