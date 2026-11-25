# polybot report

Updated 2026-11-25 20:29 UTC | 542 checkpoints logged | 384 graded | 98 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 50 settled rounds observed · 5 alerts (5 delivered) · **1 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/52 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 3
2. **Model vs market accuracy (Brier, lower is better):** model 0.1487 vs market 0.1594 on 50 rounds -> model sharper
3. **Simulated profit after fees:** -10.66 on 1 trades of $10 · win rate 0% vs break-even 32%
4. **Quote available at simulated tap (size not verified):** 5s 1/5 · 10s 1/5 · 20s 1/5 · 30s 1/5
5. **Max drawdown:** -10.66
6. **Loop health and missing data:** 5 runs, stalls over 5s 1/8247 loops, longest BTC price gap 9.0s · checks with no market quote 61/270 (book fallback used 71) · bad close samples 3 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 1/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (58 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 58 | 62.1% | 64.3% | -0.023 | -0.152 to +0.106 | $-13.20 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 58 | 56.9% | 68.2% | -0.113 | -0.240 to +0.014 | $-65.38 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 35 | 42.9% | 32.5% | +0.104 | -0.048 to +0.255 | $+36.28 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 14 | 71.4% | 46.1% | +0.253 | +0.012 to +0.495 | $+35.48 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2346 vs market 0.2481 -> **model is sharper**

## 3:30 left (68 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 68 | 76.5% | 64.3% | +0.121 | +0.017 to +0.226 | $+82.55 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 68 | 75.0% | 72.5% | +0.025 | -0.085 to +0.134 | $+16.81 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 32 | 40.6% | 27.2% | +0.134 | -0.021 to +0.290 | $+42.98 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 5 | 80.0% | 48.3% | +0.317 | -0.072 to +0.707 | $+15.87 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1932 vs market 0.2127 -> **model is sharper**

## 3:00 left (77 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 77 | 71.4% | 60.9% | +0.106 | +0.017 to +0.194 | $+81.31 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 77 | 72.7% | 74.7% | -0.020 | -0.114 to +0.073 | $-15.56 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 48 | 27.1% | 26.8% | +0.003 | -0.102 to +0.107 | $+1.22 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1793 vs market 0.1730 -> **market is sharper**

## 2:00 left (89 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 82 | 59.8% | 59.7% | +0.000 | -0.079 to +0.080 | $+0.24 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 79 | 86.1% | 79.8% | +0.063 | -0.018 to +0.143 | $+49.43 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 68 | 25.0% | 22.8% | +0.022 | -0.060 to +0.104 | $+14.99 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 4 | 100.0% | 72.9% | +0.271 | +0.177 to +0.365 | $+10.85 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1274 vs market 0.1345 -> **model is sharper**

## 1:00 left (92 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 67 | 50.7% | 47.4% | +0.033 | -0.047 to +0.114 | $+22.35 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 56 | 89.3% | 78.7% | +0.106 | +0.015 to +0.197 | $+59.54 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 72 | 19.4% | 14.9% | +0.045 | -0.018 to +0.108 | $+32.52 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0818 vs market 0.1011 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=98, bias $-0.38, sd $1.61 (set BASIS_SD near 2)
- spot at open: n=98, bias $-0.77, sd $34.82 (set BASIS_SD near 35)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 86 | 49 | 55% | 62% |
| 60%-70% | 79 | 52 | 64% | 67% |
| 70%-80% | 75 | 51 | 74% | 80% |
| 80%-90% | 133 | 69 | 86% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 50 | 204 | 0.1487 | 0.1594 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 98 (50 with decision logging, v16+)
- Markets with a signal: 15
- Alerts attempted: 5 · delivered: 5 · delivery failed: 0
- Simulated fills (quote available, size not verified): 1
- Expired alerts: 4 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 5 markets, would have won 4, +12.76 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 6 markets, would have won 6, +30.29 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 5/5 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 55 · valid comparisons: 52
- Missing/untrusted: 3 sampling gaps (>6s hole or <20 samples), 0 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.78, typical gap $2.91, worst $12.31
- Coinbase would have named the wrong winner: 0/52 (0.0%)
- Rounds settling within $10 of the target: 3, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 8, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 14, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 5 (goal: 300)
- Simulated paper trades: 1 · no-trade (expired/unconfirmed): 4
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 0/1 = 0% vs break-even 32.0% (price paid + fee)
- Paper P&L after fees: -10.66 at $10 a trade · max drawdown: -10.66

## Ticket speed (measured, not assumed)

- Tickets: 5
- Coinbase trade -> we received it: median 1346 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 28)
- Polymarket quote round trip: median 34 ms (worst 38)
- Price read -> decision made: median 88 ms (worst 93)
- Decision -> Discord accepted: median 1665 ms (worst 2386)
- Time left on the timer when sent: median 208s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 1/5 | 4 | 0 | -10.53 |
| 10s | 1/5 | 4 | 0 | -10.53 |
| 20s | 1/5 | 4 | 0 | -10.53 |
| 30s | 1/5 | 4 | 0 | -10.66 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 5 · loops: 8247 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
