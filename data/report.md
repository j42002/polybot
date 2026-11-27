# polybot report

Updated 2026-11-27 13:04 UTC | 2839 checkpoints logged | 2669 graded | 570 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 522 settled rounds observed · 84 alerts (83 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 10/511 valid rounds (2.0%) where Coinbase points at the wrong winner · missing 27
2. **Model vs market accuracy (Brier, lower is better):** model 0.1597 vs market 0.1661 on 522 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/83 · 10s 20/83 · 20s 17/83 · 30s 15/83
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 49 runs, stalls over 5s 3/80837 loops, longest BTC price gap 10.7s · checks with no market quote 73/2567 (book fallback used 1069) · bad close samples 12 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (517 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 517 | 65.0% | 64.4% | +0.006 | -0.034 to +0.047 | $+32.16 | NO EDGE |
| Lean (bet the side BTC is on now) | 517 | 65.0% | 67.2% | -0.022 | -0.062 to +0.019 | $-112.76 | NO EDGE |
| Edge (model beats the ask by 3c+) | 263 | 48.3% | 41.0% | +0.073 | +0.017 to +0.128 | $+191.48 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 116 | 63.8% | 52.2% | +0.116 | +0.027 to +0.205 | $+134.68 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2116 vs market 0.2202 -> **model is sharper**

## 3:30 left (530 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 530 | 64.7% | 62.7% | +0.020 | -0.018 to +0.058 | $+104.27 | NO EDGE |
| Lean (bet the side BTC is on now) | 530 | 70.8% | 70.9% | -0.002 | -0.040 to +0.036 | $-8.92 | NO EDGE |
| Edge (model beats the ask by 3c+) | 296 | 40.9% | 35.1% | +0.057 | +0.008 to +0.107 | $+169.82 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1945 vs market 0.2006 -> **model is sharper**

## 3:00 left (538 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 537 | 65.0% | 61.8% | +0.032 | -0.003 to +0.067 | $+173.86 | NO EDGE |
| Lean (bet the side BTC is on now) | 537 | 75.4% | 74.4% | +0.011 | -0.025 to +0.046 | $+56.67 | NO EDGE |
| Edge (model beats the ask by 3c+) | 319 | 33.2% | 29.5% | +0.037 | -0.007 to +0.081 | $+117.60 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 85.2% | 71.0% | +0.142 | -0.000 to +0.284 | $+38.30 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1699 vs market 0.1750 -> **model is sharper**

## 2:00 left (545 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 511 | 63.2% | 60.0% | +0.033 | +0.001 to +0.064 | $+166.15 | PASSES |
| Lean (bet the side BTC is on now) | 502 | 83.5% | 80.1% | +0.034 | +0.002 to +0.066 | $+170.58 | PASSES |
| Edge (model beats the ask by 3c+) | 402 | 23.9% | 21.3% | +0.026 | -0.006 to +0.057 | $+103.20 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 21 | 95.2% | 75.0% | +0.202 | +0.102 to +0.302 | $+42.45 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1276 vs market 0.1303 -> **model is sharper**

## 1:00 left (539 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 401 | 49.9% | 48.2% | +0.016 | -0.015 to +0.048 | $+65.38 | NO EDGE |
| Lean (bet the side BTC is on now) | 340 | 86.8% | 82.3% | +0.045 | +0.008 to +0.081 | $+152.02 | PASSES |
| Edge (model beats the ask by 3c+) | 473 | 16.5% | 12.5% | +0.040 | +0.016 to +0.064 | $+188.78 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0842 vs market 0.0960 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=570, bias $-0.07, sd $0.68 (set BASIS_SD near 1)
- spot at open: n=570, bias $-2.34, sd $22.16 (set BASIS_SD near 22)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 642 | 338 | 55% | 57% |
| 60%-70% | 589 | 359 | 65% | 69% |
| 70%-80% | 518 | 343 | 75% | 80% |
| 80%-90% | 909 | 412 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 522 | 2489 | 0.1597 | 0.1661 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 570 (522 with decision logging, v16+)
- Markets with a signal: 200
- Alerts attempted: 84 · delivered: 83 · delivery failed: 1
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 68 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 84 markets, would have won 56, +36.13 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 44 markets, would have won 34, +109.84 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 79/83 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 538 · valid comparisons: 511
- Missing/untrusted: 12 sampling gaps (>6s hole or <20 samples), 15 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.34, typical gap $3.15, worst $12.47
- Coinbase would have named the wrong winner: 10/511 (2.0%)
- Rounds settling within $10 of the target: 80, wrong winner 10 (12%)
- Rounds settling within $25 of the target: 165, wrong winner 10 (6%)
- Rounds settling within $50 of the target: 275, wrong winner 10 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 83 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 68
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 84
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 73 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/83 | 61 | 0 | +25.17 |
| 10s | 20/83 | 63 | 0 | -1.27 |
| 20s | 17/83 | 66 | 0 | -13.40 |
| 30s | 15/83 | 68 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 49 · loops: 80837 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
