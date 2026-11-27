# polybot report

Updated 2026-11-27 15:50 UTC | 2989 checkpoints logged | 2819 graded | 600 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 552 settled rounds observed · 85 alerts (84 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/539 valid rounds (1.9%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1618 vs market 0.1682 on 552 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/84 · 10s 20/84 · 20s 17/84 · 30s 15/84
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 52 runs, stalls over 5s 3/85786 loops, longest BTC price gap 10.7s · checks with no market quote 73/2717 (book fallback used 1129) · bad close samples 13 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (547 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 547 | 64.7% | 64.5% | +0.002 | -0.037 to +0.042 | $+12.02 | NO EDGE |
| Lean (bet the side BTC is on now) | 547 | 65.1% | 67.3% | -0.022 | -0.062 to +0.017 | $-121.89 | NO EDGE |
| Edge (model beats the ask by 3c+) | 275 | 47.6% | 40.9% | +0.068 | +0.013 to +0.122 | $+185.96 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 119 | 63.0% | 52.4% | +0.106 | +0.018 to +0.195 | $+126.64 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2135 vs market 0.2220 -> **model is sharper**

## 3:30 left (560 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 560 | 65.0% | 62.7% | +0.023 | -0.014 to +0.060 | $+127.40 | NO EDGE |
| Lean (bet the side BTC is on now) | 560 | 70.5% | 71.0% | -0.005 | -0.042 to +0.033 | $-26.05 | NO EDGE |
| Edge (model beats the ask by 3c+) | 310 | 40.3% | 34.6% | +0.057 | +0.008 to +0.106 | $+177.02 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1970 vs market 0.2024 -> **model is sharper**

## 3:00 left (568 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 567 | 65.1% | 61.8% | +0.033 | -0.001 to +0.067 | $+186.30 | NO EDGE |
| Lean (bet the side BTC is on now) | 567 | 75.7% | 74.5% | +0.012 | -0.023 to +0.046 | $+67.46 | NO EDGE |
| Edge (model beats the ask by 3c+) | 338 | 33.4% | 29.3% | +0.041 | -0.001 to +0.084 | $+139.32 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1714 vs market 0.1769 -> **model is sharper**

## 2:00 left (575 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 540 | 63.3% | 59.7% | +0.036 | +0.006 to +0.067 | $+197.01 | PASSES |
| Lean (bet the side BTC is on now) | 530 | 83.0% | 80.2% | +0.028 | -0.003 to +0.059 | $+149.62 | NO EDGE |
| Edge (model beats the ask by 3c+) | 428 | 23.8% | 21.3% | +0.025 | -0.006 to +0.056 | $+107.49 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1289 vs market 0.1318 -> **model is sharper**

## 1:00 left (569 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 422 | 49.5% | 47.8% | +0.018 | -0.013 to +0.048 | $+73.94 | NO EDGE |
| Lean (bet the side BTC is on now) | 357 | 85.4% | 82.0% | +0.035 | -0.002 to +0.071 | $+124.17 | NO EDGE |
| Edge (model beats the ask by 3c+) | 501 | 16.8% | 12.4% | +0.043 | +0.020 to +0.067 | $+217.29 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0873 vs market 0.0989 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=600, bias $-0.06, sd $0.66 (set BASIS_SD near 1)
- spot at open: n=600, bias $-2.71, sd $23.49 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 682 | 356 | 55% | 58% |
| 60%-70% | 625 | 382 | 65% | 69% |
| 70%-80% | 546 | 362 | 75% | 79% |
| 80%-90% | 955 | 433 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 552 | 2639 | 0.1618 | 0.1682 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 600 (552 with decision logging, v16+)
- Markets with a signal: 204
- Alerts attempted: 85 · delivered: 84 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 69 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 86 markets, would have won 57, +31.36 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 45 markets, would have won 35, +115.62 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 80/84 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 571 · valid comparisons: 539
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 19 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.51, typical gap $3.34, worst $13.97
- Coinbase would have named the wrong winner: 10/539 (1.9%)
- Rounds settling within $10 of the target: 82, wrong winner 10 (12%)
- Rounds settling within $25 of the target: 172, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 287, wrong winner 10 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 84 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 69
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 85
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/84 | 62 | 0 | +25.17 |
| 10s | 20/84 | 64 | 0 | -1.27 |
| 20s | 17/84 | 67 | 0 | -13.40 |
| 30s | 15/84 | 69 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 52 · loops: 85786 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
