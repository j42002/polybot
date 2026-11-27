# polybot report

Updated 2026-11-27 07:32 UTC | 2517 checkpoints logged | 2346 graded | 503 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 455 settled rounds observed · 74 alerts (73 delivered) · **12 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/446 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1556 vs market 0.1628 on 455 rounds -> model sharper
3. **Simulated profit after fees:** -3.33 on 12 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -6.97 to +6.42
4. **Quote available at simulated tap (size not verified):** 5s 19/73 · 10s 17/73 · 20s 15/73 · 30s 13/73
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 43 runs, stalls over 5s 3/70937 loops, longest BTC price gap 10.7s · checks with no market quote 71/2245 (book fallback used 934) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 12/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (454 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 454 | 65.9% | 64.8% | +0.011 | -0.032 to +0.054 | $+50.30 | NO EDGE |
| Lean (bet the side BTC is on now) | 454 | 66.1% | 67.3% | -0.013 | -0.055 to +0.030 | $-56.75 | NO EDGE |
| Edge (model beats the ask by 3c+) | 230 | 49.6% | 40.9% | +0.086 | +0.027 to +0.145 | $+198.61 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 101 | 67.3% | 51.8% | +0.156 | +0.063 to +0.248 | $+157.09 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2080 vs market 0.2180 -> **model is sharper**

## 3:30 left (464 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 464 | 65.9% | 63.1% | +0.029 | -0.011 to +0.069 | $+132.90 | NO EDGE |
| Lean (bet the side BTC is on now) | 464 | 71.3% | 71.1% | +0.002 | -0.038 to +0.042 | $+9.85 | NO EDGE |
| Edge (model beats the ask by 3c+) | 256 | 40.2% | 34.6% | +0.056 | +0.003 to +0.109 | $+143.73 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 54 | 61.1% | 52.2% | +0.089 | -0.036 to +0.215 | $+48.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1888 vs market 0.1964 -> **model is sharper**

## 3:00 left (471 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 470 | 64.5% | 61.6% | +0.029 | -0.009 to +0.066 | $+134.23 | NO EDGE |
| Lean (bet the side BTC is on now) | 470 | 76.0% | 74.3% | +0.016 | -0.021 to +0.053 | $+76.04 | NO EDGE |
| Edge (model beats the ask by 3c+) | 285 | 33.7% | 29.8% | +0.039 | -0.006 to +0.084 | $+111.10 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 88.0% | 71.3% | +0.167 | +0.032 to +0.301 | $+41.72 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1655 vs market 0.1716 -> **model is sharper**

## 2:00 left (480 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 451 | 62.1% | 59.9% | +0.022 | -0.011 to +0.055 | $+100.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 444 | 84.2% | 80.1% | +0.041 | +0.008 to +0.074 | $+181.90 | PASSES |
| Edge (model beats the ask by 3c+) | 354 | 24.3% | 21.5% | +0.028 | -0.006 to +0.061 | $+97.48 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1252 vs market 0.1277 -> **model is sharper**

## 1:00 left (477 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 358 | 50.6% | 49.0% | +0.016 | -0.016 to +0.049 | $+57.52 | NO EDGE |
| Lean (bet the side BTC is on now) | 302 | 87.4% | 82.9% | +0.045 | +0.007 to +0.083 | $+136.40 | PASSES |
| Edge (model beats the ask by 3c+) | 419 | 16.5% | 12.4% | +0.040 | +0.016 to +0.065 | $+169.00 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0829 vs market 0.0944 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=503, bias $-0.07, sd $0.73 (set BASIS_SD near 1)
- spot at open: n=503, bias $-1.66, sd $22.72 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 557 | 295 | 55% | 56% |
| 60%-70% | 530 | 320 | 65% | 70% |
| 70%-80% | 445 | 300 | 75% | 82% |
| 80%-90% | 803 | 365 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 455 | 2166 | 0.1556 | 0.1628 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 503 (455 with decision logging, v16+)
- Markets with a signal: 171
- Alerts attempted: 74 · delivered: 73 · delivery failed: 1
- Simulated fills (quote available, size not verified): 13
- Expired alerts: 60 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 73 markets, would have won 50, +43.23 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 37 markets, would have won 30, +102.96 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 69/73 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 472 · valid comparisons: 446
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.89, typical gap $2.85, worst $12.31
- Coinbase would have named the wrong winner: 6/446 (1.3%)
- Rounds settling within $10 of the target: 67, wrong winner 6 (9%)
- Rounds settling within $25 of the target: 139, wrong winner 6 (4%)
- Rounds settling within $50 of the target: 235, wrong winner 6 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 72 (goal: 300)
- Simulated paper trades: 12 · no-trade (expired/unconfirmed): 60
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/12 = 50% vs break-even 49.7% (price paid + fee)
- Paper P&L after fees: -3.33 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 74
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 74 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 18/72 | 54 | 0 | +67.12 |
| 10s | 16/72 | 56 | 0 | +40.68 |
| 20s | 14/72 | 58 | 0 | +18.11 |
| 30s | 12/72 | 60 | 0 | -3.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 43 · loops: 70937 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
