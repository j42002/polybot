# polybot report

Updated 2026-11-27 12:09 UTC | 2786 checkpoints logged | 2616 graded | 559 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 511 settled rounds observed · 83 alerts (82 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/501 valid rounds (2.0%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1588 vs market 0.1655 on 511 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/82 · 10s 20/82 · 20s 17/82 · 30s 15/82
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 48 runs, stalls over 5s 3/79187 loops, longest BTC price gap 10.7s · checks with no market quote 73/2514 (book fallback used 1035) · bad close samples 11 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (507 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 507 | 65.1% | 64.3% | +0.008 | -0.033 to +0.049 | $+41.31 | NO EDGE |
| Lean (bet the side BTC is on now) | 507 | 64.9% | 67.0% | -0.022 | -0.062 to +0.019 | $-109.12 | NO EDGE |
| Edge (model beats the ask by 3c+) | 256 | 49.2% | 41.0% | +0.082 | +0.025 to +0.138 | $+209.12 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 115 | 64.3% | 52.1% | +0.123 | +0.034 to +0.211 | $+141.21 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2112 vs market 0.2206 -> **model is sharper**

## 3:30 left (520 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 520 | 64.6% | 62.8% | +0.018 | -0.021 to +0.056 | $+92.27 | NO EDGE |
| Lean (bet the side BTC is on now) | 520 | 70.6% | 70.8% | -0.003 | -0.041 to +0.036 | $-14.03 | NO EDGE |
| Edge (model beats the ask by 3c+) | 290 | 40.7% | 35.3% | +0.054 | +0.004 to +0.104 | $+156.15 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 65 | 58.5% | 52.0% | +0.065 | -0.050 to +0.180 | $+42.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1940 vs market 0.2001 -> **model is sharper**

## 3:00 left (527 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 526 | 65.0% | 62.0% | +0.031 | -0.005 to +0.066 | $+161.15 | NO EDGE |
| Lean (bet the side BTC is on now) | 526 | 75.7% | 74.4% | +0.012 | -0.023 to +0.048 | $+64.73 | NO EDGE |
| Edge (model beats the ask by 3c+) | 313 | 33.2% | 29.5% | +0.037 | -0.007 to +0.081 | $+115.82 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1686 vs market 0.1739 -> **model is sharper**

## 2:00 left (534 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 501 | 62.9% | 60.0% | +0.029 | -0.003 to +0.060 | $+143.49 | NO EDGE |
| Lean (bet the side BTC is on now) | 492 | 83.7% | 80.3% | +0.034 | +0.003 to +0.066 | $+169.49 | PASSES |
| Edge (model beats the ask by 3c+) | 396 | 23.7% | 21.1% | +0.026 | -0.005 to +0.058 | $+104.94 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 21 | 95.2% | 75.0% | +0.202 | +0.102 to +0.302 | $+42.45 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1260 vs market 0.1294 -> **model is sharper**

## 1:00 left (528 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 392 | 49.5% | 48.0% | +0.015 | -0.016 to +0.047 | $+59.50 | NO EDGE |
| Lean (bet the side BTC is on now) | 331 | 86.7% | 82.7% | +0.040 | +0.003 to +0.076 | $+131.34 | PASSES |
| Edge (model beats the ask by 3c+) | 464 | 16.2% | 12.3% | +0.039 | +0.015 to +0.063 | $+181.14 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0838 vs market 0.0948 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=559, bias $-0.07, sd $0.69 (set BASIS_SD near 1)
- spot at open: n=559, bias $-2.33, sd $22.29 (set BASIS_SD near 22)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 630 | 330 | 55% | 57% |
| 60%-70% | 575 | 351 | 65% | 69% |
| 70%-80% | 504 | 336 | 75% | 81% |
| 80%-90% | 896 | 405 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 511 | 2436 | 0.1588 | 0.1655 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 559 (511 with decision logging, v16+)
- Markets with a signal: 198
- Alerts attempted: 83 · delivered: 82 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 67 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 83 markets, would have won 55, +32.36 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 44 markets, would have won 34, +109.84 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 78/82 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 527 · valid comparisons: 501
- Missing/untrusted: 11 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.36, typical gap $3.16, worst $12.47
- Coinbase would have named the wrong winner: 10/501 (2.0%)
- Rounds settling within $10 of the target: 78, wrong winner 10 (13%)
- Rounds settling within $25 of the target: 161, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 267, wrong winner 10 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 82 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 67
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 83
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/82 | 60 | 0 | +25.17 |
| 10s | 20/82 | 62 | 0 | -1.27 |
| 20s | 17/82 | 65 | 0 | -13.40 |
| 30s | 15/82 | 67 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 48 · loops: 79187 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
