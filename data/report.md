# polybot report

Updated 2026-11-27 16:46 UTC | 3040 checkpoints logged | 2869 graded | 610 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 562 settled rounds observed · 86 alerts (85 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/549 valid rounds (1.8%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1616 vs market 0.1677 on 562 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/85 · 10s 20/85 · 20s 17/85 · 30s 15/85
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 53 runs, stalls over 5s 3/87436 loops, longest BTC price gap 10.7s · checks with no market quote 73/2768 (book fallback used 1157) · bad close samples 13 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (557 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 557 | 64.6% | 64.6% | +0.001 | -0.038 to +0.040 | $+3.50 | NO EDGE |
| Lean (bet the side BTC is on now) | 557 | 65.2% | 67.4% | -0.022 | -0.061 to +0.017 | $-122.51 | NO EDGE |
| Edge (model beats the ask by 3c+) | 281 | 48.0% | 41.2% | +0.069 | +0.015 to +0.123 | $+193.55 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 122 | 63.1% | 52.3% | +0.108 | +0.021 to +0.196 | $+132.17 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2133 vs market 0.2219 -> **model is sharper**

## 3:30 left (570 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 570 | 65.4% | 62.7% | +0.027 | -0.010 to +0.064 | $+154.38 | NO EDGE |
| Lean (bet the side BTC is on now) | 570 | 70.5% | 71.1% | -0.006 | -0.043 to +0.031 | $-32.85 | NO EDGE |
| Edge (model beats the ask by 3c+) | 316 | 40.2% | 34.6% | +0.056 | +0.008 to +0.104 | $+176.64 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1967 vs market 0.2020 -> **model is sharper**

## 3:00 left (578 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 577 | 64.5% | 61.3% | +0.032 | -0.002 to +0.066 | $+184.91 | NO EDGE |
| Lean (bet the side BTC is on now) | 577 | 75.6% | 74.3% | +0.012 | -0.022 to +0.046 | $+71.21 | NO EDGE |
| Edge (model beats the ask by 3c+) | 345 | 33.0% | 29.3% | +0.038 | -0.005 to +0.080 | $+129.83 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1718 vs market 0.1764 -> **model is sharper**

## 2:00 left (585 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 549 | 63.6% | 60.0% | +0.036 | +0.005 to +0.066 | $+195.67 | PASSES |
| Lean (bet the side BTC is on now) | 539 | 83.1% | 80.1% | +0.030 | -0.001 to +0.061 | $+161.08 | NO EDGE |
| Edge (model beats the ask by 3c+) | 436 | 24.1% | 21.4% | +0.027 | -0.004 to +0.057 | $+116.00 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1283 vs market 0.1315 -> **model is sharper**

## 1:00 left (579 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 429 | 49.7% | 47.9% | +0.018 | -0.013 to +0.048 | $+75.94 | NO EDGE |
| Lean (bet the side BTC is on now) | 364 | 85.7% | 82.0% | +0.037 | +0.001 to +0.073 | $+133.82 | PASSES |
| Edge (model beats the ask by 3c+) | 511 | 16.6% | 12.4% | +0.042 | +0.019 to +0.065 | $+215.14 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0867 vs market 0.0977 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=610, bias $-0.06, sd $0.66 (set BASIS_SD near 1)
- spot at open: n=610, bias $-2.93, sd $23.51 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 696 | 362 | 55% | 58% |
| 60%-70% | 638 | 389 | 65% | 69% |
| 70%-80% | 553 | 366 | 75% | 79% |
| 80%-90% | 971 | 440 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 562 | 2689 | 0.1616 | 0.1677 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 610 (562 with decision logging, v16+)
- Markets with a signal: 207
- Alerts attempted: 86 · delivered: 85 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 70 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 89 markets, would have won 59, +36.89 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 45 markets, would have won 35, +115.62 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 81/85 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 582 · valid comparisons: 549
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.72, typical gap $3.72, worst $20.80
- Coinbase would have named the wrong winner: 10/549 (1.8%)
- Rounds settling within $10 of the target: 82, wrong winner 10 (12%)
- Rounds settling within $25 of the target: 173, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 289, wrong winner 10 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 84 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 69
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 86
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 73 ms (worst 168)
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

- Runs: 53 · loops: 87436 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
