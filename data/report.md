# polybot report

Updated 2026-11-26 20:28 UTC | 1893 checkpoints logged | 1732 graded | 376 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 328 settled rounds observed · 49 alerts (48 delivered) · **8 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/323 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 17
2. **Model vs market accuracy (Brier, lower is better):** model 0.1503 vs market 0.1582 on 328 rounds -> model sharper
3. **Simulated profit after fees:** -51.99 on 8 trades of $10 · win rate 25% vs break-even 49%, 95% range per trade -11.71 to -1.29
4. **Quote available at simulated tap (size not verified):** 5s 12/48 · 10s 12/48 · 20s 10/48 · 30s 8/48
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 31 runs, stalls over 5s 3/51137 loops, longest BTC price gap 10.7s · checks with no market quote 65/1621 (book fallback used 660) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 8/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (331 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 331 | 66.2% | 64.5% | +0.016 | -0.034 to +0.067 | $+53.93 | NO EDGE |
| Lean (bet the side BTC is on now) | 331 | 65.9% | 67.6% | -0.018 | -0.068 to +0.033 | $-58.83 | NO EDGE |
| Edge (model beats the ask by 3c+) | 173 | 52.0% | 40.7% | +0.113 | +0.047 to +0.180 | $+196.34 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 73 | 68.5% | 51.3% | +0.172 | +0.065 to +0.278 | $+125.27 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2080 vs market 0.2190 -> **model is sharper**

## 3:30 left (340 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 340 | 68.8% | 64.1% | +0.047 | +0.001 to +0.094 | $+160.39 | PASSES |
| Lean (bet the side BTC is on now) | 340 | 72.6% | 71.3% | +0.013 | -0.034 to +0.060 | $+44.48 | NO EDGE |
| Edge (model beats the ask by 3c+) | 190 | 41.6% | 34.9% | +0.067 | +0.005 to +0.129 | $+126.75 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 39 | 56.4% | 51.3% | +0.051 | -0.100 to +0.203 | $+20.04 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1857 vs market 0.1963 -> **model is sharper**

## 3:00 left (349 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 349 | 66.2% | 61.5% | +0.046 | +0.004 to +0.089 | $+162.09 | PASSES |
| Lean (bet the side BTC is on now) | 349 | 77.1% | 74.4% | +0.026 | -0.016 to +0.069 | $+92.42 | NO EDGE |
| Edge (model beats the ask by 3c+) | 217 | 34.1% | 29.2% | +0.049 | -0.003 to +0.100 | $+105.74 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 15 | 93.3% | 71.2% | +0.221 | +0.086 to +0.357 | $+33.22 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1584 vs market 0.1669 -> **model is sharper**

## 2:00 left (356 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 332 | 61.1% | 59.2% | +0.019 | -0.018 to +0.057 | $+63.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 327 | 85.3% | 80.4% | +0.050 | +0.012 to +0.087 | $+162.18 | PASSES |
| Edge (model beats the ask by 3c+) | 267 | 23.6% | 21.9% | +0.017 | -0.021 to +0.055 | $+46.18 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 16 | 100.0% | 75.2% | +0.248 | +0.220 to +0.276 | $+39.68 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1212 vs market 0.1205 -> **market is sharper**

## 1:00 left (356 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 267 | 49.4% | 47.3% | +0.022 | -0.015 to +0.058 | $+58.39 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 224 | 90.2% | 82.8% | +0.073 | +0.031 to +0.115 | $+164.35 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 309 | 15.2% | 11.8% | +0.034 | +0.007 to +0.062 | $+106.49 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0766 vs market 0.0883 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=376, bias $-0.10, sd $0.84 (set BASIS_SD near 1)
- spot at open: n=376, bias $-1.93, sd $23.54 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 407 | 216 | 55% | 57% |
| 60%-70% | 385 | 235 | 65% | 72% |
| 70%-80% | 316 | 216 | 75% | 82% |
| 80%-90% | 613 | 279 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 328 | 1552 | 0.1503 | 0.1582 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 376 (328 with decision logging, v16+)
- Markets with a signal: 122
- Alerts attempted: 49 · delivered: 48 · delivery failed: 1
- Simulated fills (quote available, size not verified): 8
- Expired alerts: 40 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 56 markets, would have won 38, +35.21 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 25 markets, would have won 20, +73.17 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 5 markets, would have won 4, +10.38 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 45/48 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 340 · valid comparisons: 323
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.63, typical gap $2.83, worst $12.31
- Coinbase would have named the wrong winner: 4/323 (1.2%)
- Rounds settling within $10 of the target: 43, wrong winner 4 (9%)
- Rounds settling within $25 of the target: 94, wrong winner 4 (4%)
- Rounds settling within $50 of the target: 164, wrong winner 4 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 47 (goal: 300)
- Simulated paper trades: 8 · no-trade (expired/unconfirmed): 39
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 2/8 = 25% vs break-even 49.0% (price paid + fee)
- Paper P&L after fees: -51.99 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 49
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 30 ms (worst 75)
- Price read -> decision made: median 77 ms (worst 168)
- Decision -> Discord accepted: median 1517 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 12/47 | 35 | 0 | -7.98 |
| 10s | 12/47 | 35 | 0 | -7.98 |
| 20s | 10/47 | 37 | 0 | -30.55 |
| 30s | 8/47 | 39 | 0 | -51.99 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 31 · loops: 51137 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
