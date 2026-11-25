# polybot report

Updated 2026-11-25 22:20 UTC | 642 checkpoints logged | 484 graded | 118 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 70 settled rounds observed · 7 alerts (7 delivered) · **2 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/70 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 6
2. **Model vs market accuracy (Brier, lower is better):** model 0.1539 vs market 0.1674 on 70 rounds -> model sharper
3. **Simulated profit after fees:** -5.61 on 2 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -18.20 to +12.59
4. **Quote available at simulated tap (size not verified):** 5s 2/7 · 10s 2/7 · 20s 2/7 · 30s 2/7
5. **Max drawdown:** -10.66
6. **Loop health and missing data:** 7 runs, stalls over 5s 1/11547 loops, longest BTC price gap 9.0s · checks with no market quote 61/370 (book fallback used 118) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 2/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (78 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 78 | 65.4% | 64.7% | +0.007 | -0.101 to +0.115 | $+5.66 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 78 | 59.0% | 68.2% | -0.092 | -0.199 to +0.015 | $-71.72 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 45 | 46.7% | 34.0% | +0.127 | -0.005 to +0.259 | $+57.16 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 18 | 72.2% | 47.9% | +0.244 | +0.042 to +0.446 | $+43.86 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2228 vs market 0.2355 -> **model is sharper**

## 3:30 left (88 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 88 | 72.7% | 65.4% | +0.073 | -0.022 to +0.168 | $+64.38 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 88 | 71.6% | 72.4% | -0.008 | -0.105 to +0.089 | $-6.95 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 46 | 43.5% | 31.6% | +0.118 | -0.017 to +0.254 | $+54.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 9 | 55.6% | 50.4% | +0.052 | -0.301 to +0.404 | $+4.64 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1959 vs market 0.2135 -> **model is sharper**

## 3:00 left (97 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 97 | 63.9% | 60.9% | +0.030 | -0.056 to +0.116 | $+29.19 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 97 | 70.1% | 75.2% | -0.051 | -0.137 to +0.036 | $-49.24 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 56 | 32.1% | 27.8% | +0.044 | -0.062 to +0.150 | $+24.58 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1872 vs market 0.1880 -> **model is sharper**

## 2:00 left (109 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 102 | 63.7% | 60.5% | +0.032 | -0.039 to +0.102 | $+32.42 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 99 | 84.8% | 80.0% | +0.049 | -0.024 to +0.121 | $+48.35 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 78 | 25.6% | 22.5% | +0.031 | -0.046 to +0.108 | $+24.36 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 5 | 100.0% | 71.9% | +0.281 | +0.205 to +0.356 | $+14.03 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1266 vs market 0.1354 -> **model is sharper**

## 1:00 left (112 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 80 | 51.2% | 47.9% | +0.034 | -0.039 to +0.107 | $+26.99 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 67 | 89.6% | 79.3% | +0.103 | +0.020 to +0.186 | $+68.93 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 87 | 18.4% | 13.3% | +0.051 | -0.006 to +0.108 | $+44.22 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0782 vs market 0.0997 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=118, bias $-0.32, sd $1.48 (set BASIS_SD near 1)
- spot at open: n=118, bias $-1.68, sd $33.16 (set BASIS_SD near 33)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 106 | 59 | 55% | 59% |
| 60%-70% | 103 | 67 | 64% | 62% |
| 70%-80% | 97 | 65 | 74% | 79% |
| 80%-90% | 167 | 85 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 70 | 304 | 0.1539 | 0.1674 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 118 (70 with decision logging, v16+)
- Markets with a signal: 23
- Alerts attempted: 7 · delivered: 7 · delivery failed: 0
- Simulated fills (quote available, size not verified): 2
- Expired alerts: 5 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 11 markets, would have won 7, +11.77 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 6 markets, would have won 6, +30.29 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 7/7 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 76 · valid comparisons: 70
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 2 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.36, typical gap $2.90, worst $12.31
- Coinbase would have named the wrong winner: 0/70 (0.0%)
- Rounds settling within $10 of the target: 6, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 13, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 24, wrong winner 0 (0%)

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

- Runs: 7 · loops: 11547 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
