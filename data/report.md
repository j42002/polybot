# polybot report

Updated 2026-11-26 17:42 UTC | 1733 checkpoints logged | 1568 graded | 342 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 294 settled rounds observed · 40 alerts (39 delivered) · **7 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/289 valid rounds (1.4%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1456 vs market 0.1543 on 294 rounds -> model sharper
3. **Simulated profit after fees:** -41.74 on 7 trades of $10 · win rate 29% vs break-even 45%, 95% range per trade -11.86 to -0.07
4. **Quote available at simulated tap (size not verified):** 5s 11/39 · 10s 11/39 · 20s 9/39 · 30s 7/39
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 28 runs, stalls over 5s 3/46187 loops, longest BTC price gap 10.7s · checks with no market quote 65/1461 (book fallback used 593) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 7/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (297 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 297 | 67.7% | 65.2% | +0.025 | -0.028 to +0.078 | $+73.68 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 297 | 66.7% | 68.1% | -0.014 | -0.067 to +0.039 | $-41.33 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 155 | 54.2% | 40.0% | +0.141 | +0.073 to +0.210 | $+219.25 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 62 | 72.6% | 50.8% | +0.218 | +0.110 to +0.326 | $+135.19 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2011 vs market 0.2174 -> **model is sharper**

## 3:30 left (306 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 306 | 70.3% | 64.6% | +0.057 | +0.008 to +0.105 | $+172.90 | PASSES |
| Lean (bet the side BTC is on now) | 306 | 74.8% | 72.1% | +0.027 | -0.022 to +0.076 | $+83.46 | NO EDGE |
| Edge (model beats the ask by 3c+) | 173 | 41.6% | 34.2% | +0.074 | +0.009 to +0.138 | $+127.50 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 33 | 60.6% | 51.6% | +0.090 | -0.070 to +0.251 | $+29.80 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1786 vs market 0.1923 -> **model is sharper**

## 3:00 left (315 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 315 | 65.4% | 61.6% | +0.038 | -0.006 to +0.081 | $+119.26 | NO EDGE |
| Lean (bet the side BTC is on now) | 315 | 77.5% | 75.3% | +0.021 | -0.023 to +0.065 | $+66.87 | NO EDGE |
| Edge (model beats the ask by 3c+) | 197 | 31.0% | 28.1% | +0.028 | -0.025 to +0.081 | $+55.80 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 12 | 91.7% | 71.2% | +0.205 | +0.037 to +0.374 | $+24.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1557 vs market 0.1588 -> **model is sharper**

## 2:00 left (325 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 302 | 61.6% | 59.0% | +0.026 | -0.013 to +0.065 | $+78.79 | NO EDGE |
| Lean (bet the side BTC is on now) | 297 | 85.5% | 80.8% | +0.047 | +0.008 to +0.086 | $+139.19 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 248 | 23.0% | 21.2% | +0.018 | -0.022 to +0.058 | $+44.25 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 14 | 100.0% | 75.1% | +0.249 | +0.218 to +0.280 | $+34.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1193 vs market 0.1191 -> **market is sharper**

## 1:00 left (325 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 243 | 48.1% | 46.2% | +0.020 | -0.018 to +0.058 | $+47.90 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 201 | 89.6% | 82.9% | +0.067 | +0.022 to +0.111 | $+133.89 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 281 | 15.7% | 11.7% | +0.040 | +0.011 to +0.069 | $+111.35 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0769 vs market 0.0890 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=342, bias $-0.11, sd $0.88 (set BASIS_SD near 1)
- spot at open: n=342, bias $-1.89, sd $24.41 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 359 | 190 | 55% | 57% |
| 60%-70% | 340 | 209 | 65% | 73% |
| 70%-80% | 288 | 195 | 75% | 83% |
| 80%-90% | 570 | 257 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 294 | 1388 | 0.1456 | 0.1543 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 342 (294 with decision logging, v16+)
- Markets with a signal: 103
- Alerts attempted: 40 · delivered: 39 · delivery failed: 1
- Simulated fills (quote available, size not verified): 7
- Expired alerts: 32 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 46 markets, would have won 33, +47.29 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 21 markets, would have won 18, +75.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 37/39 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 307 · valid comparisons: 289
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 11 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.60, typical gap $2.88, worst $12.31
- Coinbase would have named the wrong winner: 4/289 (1.4%)
- Rounds settling within $10 of the target: 36, wrong winner 4 (11%)
- Rounds settling within $25 of the target: 81, wrong winner 4 (5%)
- Rounds settling within $50 of the target: 137, wrong winner 4 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 39 (goal: 300)
- Simulated paper trades: 7 · no-trade (expired/unconfirmed): 32
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 2/7 = 29% vs break-even 45.2% (price paid + fee)
- Paper P&L after fees: -41.74 at $10 a trade · max drawdown: -48.03

## Ticket speed (measured, not assumed)

- Tickets: 40
- Coinbase trade -> we received it: median 1027 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 11/39 | 28 | 0 | +2.27 |
| 10s | 11/39 | 28 | 0 | +2.27 |
| 20s | 9/39 | 30 | 0 | -20.30 |
| 30s | 7/39 | 32 | 0 | -41.74 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 28 · loops: 46187 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
