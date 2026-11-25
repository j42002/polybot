# polybot report

Updated 2026-11-25 19:34 UTC | 488 checkpoints logged | 336 graded | 87 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 39 settled rounds observed · 1 alerts (1 delivered) · **0 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/42 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 2
2. **Model vs market accuracy (Brier, lower is better):** model 0.1465 vs market 0.1629 on 39 rounds -> model sharper
3. **Simulated profit after fees:** no simulated trades yet
4. **Quote available at simulated tap (size not verified):** 5s 0/1 · 10s 0/1 · 20s 0/1 · 30s 0/1
5. **Max drawdown:** n/a
6. **Loop health and missing data:** 4 runs, stalls over 5s 0/6598 loops, longest BTC price gap 6.0s · checks with no market quote 56/216 (book fallback used 42) · bad close samples 2 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 0/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (51 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 51 | 64.7% | 65.4% | -0.007 | -0.147 to +0.133 | $-3.58 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 51 | 56.9% | 69.7% | -0.128 | -0.265 to +0.009 | $-65.45 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 31 | 48.4% | 32.0% | +0.164 | +0.005 to +0.323 | $+50.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 13 | 76.9% | 46.2% | +0.307 | +0.072 to +0.542 | $+39.91 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2329 vs market 0.2564 -> **model is sharper**

## 3:30 left (59 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 59 | 79.7% | 66.3% | +0.134 | +0.023 to +0.245 | $+78.96 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 59 | 74.6% | 74.7% | -0.001 | -0.119 to +0.117 | $-0.78 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 26 | 34.6% | 23.2% | +0.114 | -0.058 to +0.286 | $+29.62 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 66.1% | +0.339 | -inf to +inf | $+3.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1948 vs market 0.2112 -> **model is sharper**

## 3:00 left (67 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 67 | 73.1% | 60.5% | +0.126 | +0.033 to +0.219 | $+84.51 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 67 | 73.1% | 76.0% | -0.029 | -0.129 to +0.072 | $-19.26 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 41 | 26.8% | 25.6% | +0.012 | -0.099 to +0.123 | $+4.92 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1747 vs market 0.1727 -> **market is sharper**

## 2:00 left (78 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 71 | 56.3% | 57.8% | -0.015 | -0.101 to +0.071 | $-10.66 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 68 | 85.3% | 79.9% | +0.054 | -0.034 to +0.142 | $+36.62 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 58 | 22.4% | 21.8% | +0.007 | -0.082 to +0.095 | $+3.78 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 3 | 100.0% | 69.4% | +0.306 | +0.215 to +0.398 | $+9.19 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1312 vs market 0.1354 -> **model is sharper**

## 1:00 left (81 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 58 | 50.0% | 46.0% | +0.040 | -0.050 to +0.129 | $+23.01 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 47 | 89.4% | 76.8% | +0.125 | +0.022 to +0.228 | $+58.86 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 63 | 22.2% | 16.0% | +0.062 | -0.009 to +0.132 | $+39.01 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0836 vs market 0.1086 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=87, bias $-0.43, sd $1.71 (set BASIS_SD near 2)
- spot at open: n=87, bias $-1.47, sd $35.57 (set BASIS_SD near 36)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 70 | 40 | 55% | 60% |
| 60%-70% | 66 | 44 | 64% | 67% |
| 70%-80% | 70 | 46 | 74% | 80% |
| 80%-90% | 119 | 61 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 39 | 156 | 0.1465 | 0.1629 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 87 (39 with decision logging, v16+)
- Markets with a signal: 9
- Alerts attempted: 1 · delivered: 1 · delivery failed: 0
- Simulated fills (quote available, size not verified): 0
- Expired alerts: 1 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 4 markets, would have won 3, +11.10 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 5 markets, would have won 5, +25.42 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 1/1 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 44 · valid comparisons: 42
- Missing/untrusted: 2 sampling gaps (>6s hole or <20 samples), 0 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.83, typical gap $3.04, worst $12.31
- Coinbase would have named the wrong winner: 0/42 (0.0%)
- Rounds settling within $10 of the target: 1, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 5, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 9, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 1 (goal: 300)
- Simulated paper trades: 0 · no-trade (expired/unconfirmed): 1
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 0/0
- Paper P&L after fees: +0.00 at $10 a trade · max drawdown: -0.00

## Ticket speed (measured, not assumed)

- Tickets: 1
- Coinbase trade -> we received it: median 1394 ms (worst 1394)
- Coinbase request round trip: median 14 ms (worst 14)
- Polymarket quote round trip: median 32 ms (worst 32)
- Price read -> decision made: median 81 ms (worst 81)
- Decision -> Discord accepted: median 1665 ms (worst 1665)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.3s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 0/1 | 1 | 0 | +0.00 |
| 10s | 0/1 | 1 | 0 | +0.00 |
| 20s | 0/1 | 1 | 0 | +0.00 |
| 30s | 0/1 | 1 | 0 | +0.00 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 4 · loops: 6598 · loops over 5s: 0 (0.00%)
- Worst single loop: 4.1s · longest gap between BTC prices: 6.0s
- No stalls recorded.
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
