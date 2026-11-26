---
polybot_auto: true
updated: 2026-11-26 23:59 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-26 23:14 UTC | 2055 checkpoints logged | 1890 graded | 409 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 361 settled rounds observed · 57 alerts (56 delivered) · **9 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/355 valid rounds (1.4%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1510 vs market 0.1587 on 361 rounds -> model sharper
3. **Simulated profit after fees:** -28.18 on 9 trades of $10 · win rate 33% vs break-even 47%, 95% range per trade -11.17 to +4.91
4. **Quote available at simulated tap (size not verified):** 5s 13/56 · 10s 13/56 · 20s 11/56 · 30s 9/56
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 34 runs, stalls over 5s 3/56087 loops, longest BTC price gap 10.7s · checks with no market quote 68/1783 (book fallback used 746) · bad close samples 8 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 9/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (362 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 362 | 66.0% | 64.6% | +0.014 | -0.034 to +0.062 | $+51.45 | NO EDGE |
| Lean (bet the side BTC is on now) | 362 | 66.0% | 67.6% | -0.015 | -0.063 to +0.033 | $-55.62 | NO EDGE |
| Edge (model beats the ask by 3c+) | 190 | 51.6% | 40.7% | +0.109 | +0.045 to +0.172 | $+206.47 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 84 | 67.9% | 51.4% | +0.165 | +0.065 to +0.265 | $+138.48 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2057 vs market 0.2164 -> **model is sharper**

## 3:30 left (372 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 372 | 67.7% | 64.2% | +0.035 | -0.009 to +0.080 | $+131.72 | NO EDGE |
| Lean (bet the side BTC is on now) | 372 | 72.6% | 71.2% | +0.013 | -0.031 to +0.058 | $+49.53 | NO EDGE |
| Edge (model beats the ask by 3c+) | 209 | 41.1% | 34.9% | +0.062 | +0.004 to +0.121 | $+130.36 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 43 | 58.1% | 51.2% | +0.069 | -0.074 to +0.212 | $+29.70 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1857 vs market 0.1949 -> **model is sharper**

## 3:00 left (381 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 381 | 64.8% | 61.3% | +0.035 | -0.006 to +0.076 | $+133.17 | NO EDGE |
| Lean (bet the side BTC is on now) | 381 | 76.9% | 74.5% | +0.024 | -0.017 to +0.065 | $+93.16 | NO EDGE |
| Edge (model beats the ask by 3c+) | 233 | 34.3% | 29.7% | +0.046 | -0.004 to +0.096 | $+107.33 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 89.5% | 71.5% | +0.180 | +0.033 to +0.328 | $+34.24 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1597 vs market 0.1687 -> **model is sharper**

## 2:00 left (389 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 365 | 61.9% | 59.7% | +0.022 | -0.014 to +0.058 | $+81.43 | NO EDGE |
| Lean (bet the side BTC is on now) | 359 | 84.4% | 80.4% | +0.040 | +0.004 to +0.076 | $+143.85 | PASSES |
| Edge (model beats the ask by 3c+) | 290 | 23.1% | 21.3% | +0.018 | -0.019 to +0.055 | $+51.67 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 16 | 100.0% | 75.2% | +0.248 | +0.220 to +0.276 | $+39.68 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1217 vs market 0.1226 -> **model is sharper**

## 1:00 left (386 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 289 | 49.1% | 47.7% | +0.014 | -0.021 to +0.050 | $+41.39 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 242 | 88.8% | 82.9% | +0.059 | +0.018 to +0.100 | $+142.74 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 337 | 15.1% | 11.9% | +0.032 | +0.005 to +0.059 | $+108.88 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0796 vs market 0.0898 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=409, bias $-0.09, sd $0.80 (set BASIS_SD near 1)
- spot at open: n=409, bias $-1.88, sd $23.24 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 442 | 233 | 55% | 57% |
| 60%-70% | 416 | 256 | 65% | 71% |
| 70%-80% | 359 | 241 | 75% | 82% |
| 80%-90% | 662 | 300 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 361 | 1710 | 0.151 | 0.1587 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 409 (361 with decision logging, v16+)
- Markets with a signal: 137
- Alerts attempted: 57 · delivered: 56 · delivery failed: 1
- Simulated fills (quote available, size not verified): 9
- Expired alerts: 47 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 61 markets, would have won 42, +40.29 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 28 markets, would have won 22, +78.37 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 52/56 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 373 · valid comparisons: 355
- Missing/untrusted: 8 sampling gaps (>6s hole or <20 samples), 10 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.50, typical gap $2.79, worst $12.31
- Coinbase would have named the wrong winner: 5/355 (1.4%)
- Rounds settling within $10 of the target: 51, wrong winner 5 (10%)
- Rounds settling within $25 of the target: 107, wrong winner 5 (5%)
- Rounds settling within $50 of the target: 184, wrong winner 5 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 56 (goal: 300)
- Simulated paper trades: 9 · no-trade (expired/unconfirmed): 47
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 3/9 = 33% vs break-even 47.0% (price paid + fee)
- Paper P&L after fees: -28.18 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 57
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 78)
- Polymarket quote round trip: median 30 ms (worst 75)
- Price read -> decision made: median 77 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 13/56 | 43 | 0 | +15.83 |
| 10s | 13/56 | 43 | 0 | +15.83 |
| 20s | 11/56 | 45 | 0 | -6.74 |
| 30s | 9/56 | 47 | 0 | -28.18 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 34 · loops: 56087 · loops over 5s: 3 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
