# polybot report

Updated 2026-11-25 21:24 UTC | 592 checkpoints logged | 434 graded | 108 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 60 settled rounds observed · 7 alerts (7 delivered) · **2 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/61 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 5
2. **Model vs market accuracy (Brier, lower is better):** model 0.1489 vs market 0.1611 on 60 rounds -> model sharper
3. **Simulated profit after fees:** -5.61 on 2 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -18.20 to +12.59
4. **Quote available at simulated tap (size not verified):** 5s 2/7 · 10s 2/7 · 20s 2/7 · 30s 2/7
5. **Max drawdown:** -10.66
6. **Loop health and missing data:** 6 runs, stalls over 5s 1/9897 loops, longest BTC price gap 9.0s · checks with no market quote 61/320 (book fallback used 90) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 2/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (68 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 68 | 64.7% | 64.7% | -0.000 | -0.118 to +0.118 | $-0.04 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 68 | 58.8% | 68.3% | -0.095 | -0.212 to +0.022 | $-64.51 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 42 | 50.0% | 34.4% | +0.156 | +0.019 to +0.293 | $+65.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 17 | 76.5% | 48.4% | +0.281 | +0.081 to +0.481 | $+47.79 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2281 vs market 0.2456 -> **model is sharper**

## 3:30 left (78 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 78 | 75.6% | 64.8% | +0.108 | +0.010 to +0.207 | $+84.50 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 78 | 74.4% | 72.7% | +0.017 | -0.086 to +0.119 | $+13.17 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 39 | 41.0% | 29.6% | +0.114 | -0.031 to +0.260 | $+44.61 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 7 | 57.1% | 49.8% | +0.073 | -0.338 to +0.485 | $+5.11 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1953 vs market 0.2125 -> **model is sharper**

## 3:00 left (87 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 87 | 67.8% | 60.1% | +0.077 | -0.010 to +0.164 | $+67.03 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 87 | 72.4% | 75.0% | -0.026 | -0.115 to +0.063 | $-22.61 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 54 | 31.5% | 27.2% | +0.043 | -0.062 to +0.147 | $+22.98 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1791 vs market 0.1785 -> **market is sharper**

## 2:00 left (99 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 92 | 63.0% | 61.5% | +0.015 | -0.057 to +0.087 | $+13.76 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 89 | 87.6% | 80.3% | +0.074 | +0.001 to +0.146 | $+65.57 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 74 | 24.3% | 22.9% | +0.015 | -0.062 to +0.092 | $+10.89 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 5 | 100.0% | 71.9% | +0.281 | +0.205 to +0.356 | $+14.03 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1207 vs market 0.1256 -> **model is sharper**

## 1:00 left (102 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 73 | 47.9% | 46.1% | +0.019 | -0.058 to +0.096 | $+13.71 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 60 | 88.3% | 79.5% | +0.089 | -0.001 to +0.178 | $+53.14 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 81 | 18.5% | 13.8% | +0.047 | -0.011 to +0.106 | $+38.21 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0812 vs market 0.1006 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=108, bias $-0.35, sd $1.54 (set BASIS_SD near 2)
- spot at open: n=108, bias $-0.55, sd $34.24 (set BASIS_SD near 34)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 94 | 54 | 55% | 62% |
| 60%-70% | 91 | 60 | 65% | 67% |
| 70%-80% | 87 | 58 | 74% | 79% |
| 80%-90% | 151 | 78 | 86% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 60 | 254 | 0.1489 | 0.1611 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 108 (60 with decision logging, v16+)
- Markets with a signal: 20
- Alerts attempted: 7 · delivered: 7 · delivery failed: 0
- Simulated fills (quote available, size not verified): 2
- Expired alerts: 5 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 8 markets, would have won 6, +16.17 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 6 markets, would have won 6, +30.29 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 7/7 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 66 · valid comparisons: 61
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 1 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.68, typical gap $2.79, worst $12.31
- Coinbase would have named the wrong winner: 0/61 (0.0%)
- Rounds settling within $10 of the target: 4, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 9, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 17, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 7 (goal: 300)
- Simulated paper trades: 2 · no-trade (expired/unconfirmed): 5
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/2 = 50% vs break-even 49.6% (price paid + fee)
- Paper P&L after fees: -5.61 at $10 a trade · max drawdown: -10.66

## Ticket speed (measured, not assumed)

- Tickets: 7
- Coinbase trade -> we received it: median 1146 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 28)
- Polymarket quote round trip: median 32 ms (worst 38)
- Price read -> decision made: median 87 ms (worst 93)
- Decision -> Discord accepted: median 1665 ms (worst 2386)
- Time left on the timer when sent: median 208s
- Price checks ran late by: median 0.4s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 2/7 | 5 | 0 | -5.48 |
| 10s | 2/7 | 5 | 0 | -5.48 |
| 20s | 2/7 | 5 | 0 | -5.48 |
| 30s | 2/7 | 5 | 0 | -5.61 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 6 · loops: 9897 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
