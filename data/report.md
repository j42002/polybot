# polybot report

Updated 2026-11-27 01:04 UTC | 2159 checkpoints logged | 1994 graded | 430 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 382 settled rounds observed · 60 alerts (59 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/374 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 21
2. **Model vs market accuracy (Brier, lower is better):** model 0.1530 vs market 0.1605 on 382 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 14/59 · 10s 13/59 · 20s 11/59 · 30s 9/59
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 36 runs, stalls over 5s 3/59387 loops, longest BTC price gap 10.7s · checks with no market quote 68/1887 (book fallback used 775) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (382 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 382 | 66.0% | 64.7% | +0.013 | -0.034 to +0.059 | $+48.71 | NO EDGE |
| Lean (bet the side BTC is on now) | 382 | 66.5% | 67.5% | -0.010 | -0.057 to +0.036 | $-38.96 | NO EDGE |
| Edge (model beats the ask by 3c+) | 197 | 50.3% | 40.7% | +0.095 | +0.032 to +0.158 | $+187.89 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 86 | 67.4% | 51.3% | +0.161 | +0.062 to +0.260 | $+138.71 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2063 vs market 0.2159 -> **model is sharper**

## 3:30 left (393 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 393 | 66.9% | 64.0% | +0.029 | -0.015 to +0.072 | $+113.65 | NO EDGE |
| Lean (bet the side BTC is on now) | 393 | 72.3% | 71.2% | +0.010 | -0.033 to +0.054 | $+39.99 | NO EDGE |
| Edge (model beats the ask by 3c+) | 218 | 40.8% | 34.6% | +0.063 | +0.006 to +0.120 | $+136.75 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 44 | 59.1% | 51.2% | +0.079 | -0.062 to +0.220 | $+34.77 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1868 vs market 0.1960 -> **model is sharper**

## 3:00 left (402 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 402 | 64.9% | 61.8% | +0.031 | -0.009 to +0.071 | $+124.39 | NO EDGE |
| Lean (bet the side BTC is on now) | 402 | 77.1% | 74.5% | +0.026 | -0.014 to +0.066 | $+104.79 | NO EDGE |
| Edge (model beats the ask by 3c+) | 243 | 33.7% | 29.3% | +0.045 | -0.004 to +0.093 | $+109.22 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 89.5% | 71.5% | +0.180 | +0.033 to +0.328 | $+34.24 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1612 vs market 0.1700 -> **model is sharper**

## 2:00 left (410 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 385 | 61.6% | 59.9% | +0.017 | -0.019 to +0.052 | $+63.98 | NO EDGE |
| Lean (bet the side BTC is on now) | 379 | 84.2% | 80.4% | +0.038 | +0.002 to +0.073 | $+142.84 | PASSES |
| Edge (model beats the ask by 3c+) | 306 | 23.2% | 21.4% | +0.018 | -0.018 to +0.054 | $+53.99 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 17 | 100.0% | 74.7% | +0.253 | +0.225 to +0.281 | $+42.97 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1248 vs market 0.1254 -> **model is sharper**

## 1:00 left (407 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 305 | 49.5% | 48.1% | +0.014 | -0.021 to +0.049 | $+43.70 | NO EDGE |
| Lean (bet the side BTC is on now) | 256 | 87.9% | 82.7% | +0.052 | +0.010 to +0.093 | $+131.99 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 356 | 15.7% | 12.2% | +0.035 | +0.008 to +0.062 | $+124.95 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0822 vs market 0.0927 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=430, bias $-0.09, sd $0.78 (set BASIS_SD near 1)
- spot at open: n=430, bias $-1.53, sd $22.87 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 472 | 250 | 55% | 58% |
| 60%-70% | 439 | 271 | 65% | 71% |
| 70%-80% | 382 | 256 | 75% | 82% |
| 80%-90% | 690 | 313 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 382 | 1814 | 0.153 | 0.1605 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 430 (382 with decision logging, v16+)
- Markets with a signal: 141
- Alerts attempted: 60 · delivered: 59 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 50 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 62 markets, would have won 43, +43.57 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 28 markets, would have won 22, +78.37 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 55/59 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 395 · valid comparisons: 374
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.47, typical gap $2.74, worst $12.31
- Coinbase would have named the wrong winner: 5/374 (1.3%)
- Rounds settling within $10 of the target: 57, wrong winner 5 (9%)
- Rounds settling within $25 of the target: 117, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 198, wrong winner 5 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 59 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 50
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 60
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 76 ms (worst 168)
- Decision -> Discord accepted: median 1538 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 14/59 | 45 | 0 | +26.60 |
| 10s | 13/59 | 46 | 0 | +15.83 |
| 20s | 11/59 | 48 | 0 | -6.74 |
| 30s | 9/59 | 50 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 36 · loops: 59387 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
