---
polybot_auto: true
updated: 2026-11-27 19:10 UTC
tags: [results, experiment/5m]
---
# 📈 5-Minute Research Report (all detail)

# polybot report

Updated 2026-11-27 18:37 UTC | 3144 checkpoints logged | 2972 graded | 632 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 584 settled rounds observed · 89 alerts (87 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 13/571 valid rounds (2.3%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1623 vs market 0.1692 on 584 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/87 · 10s 20/87 · 20s 17/87 · 30s 15/87
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 55 runs, stalls over 5s 4/90732 loops, longest BTC price gap 10.8s · checks with no market quote 73/2872 (book fallback used 1212) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (579 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 579 | 64.9% | 64.5% | +0.005 | -0.034 to +0.043 | $+27.25 | NO EDGE |
| Lean (bet the side BTC is on now) | 579 | 65.3% | 67.2% | -0.019 | -0.058 to +0.019 | $-112.65 | NO EDGE |
| Edge (model beats the ask by 3c+) | 293 | 49.1% | 41.5% | +0.077 | +0.024 to +0.129 | $+224.67 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 130 | 64.6% | 52.4% | +0.122 | +0.038 to +0.206 | $+158.92 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2131 vs market 0.2218 -> **model is sharper**

## 3:30 left (591 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 591 | 65.7% | 62.8% | +0.029 | -0.007 to +0.065 | $+169.79 | NO EDGE |
| Lean (bet the side BTC is on now) | 591 | 70.6% | 71.2% | -0.006 | -0.043 to +0.030 | $-36.92 | NO EDGE |
| Edge (model beats the ask by 3c+) | 330 | 40.3% | 34.4% | +0.059 | +0.012 to +0.106 | $+193.98 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 68 | 58.8% | 52.3% | +0.065 | -0.047 to +0.177 | $+44.16 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1971 vs market 0.2025 -> **model is sharper**

## 3:00 left (598 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 597 | 64.5% | 61.4% | +0.031 | -0.002 to +0.065 | $+187.29 | NO EDGE |
| Lean (bet the side BTC is on now) | 597 | 75.4% | 74.4% | +0.010 | -0.024 to +0.044 | $+59.72 | NO EDGE |
| Edge (model beats the ask by 3c+) | 358 | 34.4% | 29.6% | +0.047 | +0.006 to +0.089 | $+169.54 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 31 | 87.1% | 71.3% | +0.158 | +0.033 to +0.282 | $+48.84 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1726 vs market 0.1783 -> **model is sharper**

## 2:00 left (605 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 569 | 63.3% | 59.7% | +0.036 | +0.006 to +0.066 | $+203.46 | PASSES |
| Lean (bet the side BTC is on now) | 558 | 82.6% | 79.8% | +0.028 | -0.002 to +0.058 | $+156.01 | NO EDGE |
| Edge (model beats the ask by 3c+) | 452 | 24.8% | 21.7% | +0.031 | +0.000 to +0.062 | $+140.54 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1293 vs market 0.1329 -> **model is sharper**

## 1:00 left (599 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 444 | 49.5% | 47.8% | +0.018 | -0.013 to +0.048 | $+79.00 | NO EDGE |
| Lean (bet the side BTC is on now) | 378 | 85.2% | 81.5% | +0.037 | +0.002 to +0.073 | $+140.82 | PASSES |
| Edge (model beats the ask by 3c+) | 528 | 17.2% | 12.5% | +0.047 | +0.024 to +0.070 | $+248.53 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0880 vs market 0.1011 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=632, bias $-0.06, sd $0.65 (set BASIS_SD near 1)
- spot at open: n=632, bias $-3.07, sd $23.85 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 720 | 375 | 55% | 58% |
| 60%-70% | 669 | 405 | 65% | 69% |
| 70%-80% | 575 | 378 | 75% | 79% |
| 80%-90% | 997 | 453 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 584 | 2792 | 0.1623 | 0.1692 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 632 (584 with decision logging, v16+)
- Markets with a signal: 219
- Alerts attempted: 89 · delivered: 87 · delivery failed: 2
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 72 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 95 markets, would have won 65, +54.78 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 49 markets, would have won 37, +112.99 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 83/87 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 604 · valid comparisons: 571
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.04, typical gap $4.04, worst $20.80
- Coinbase would have named the wrong winner: 13/571 (2.3%)
- Rounds settling within $10 of the target: 87, wrong winner 13 (15%)
- Rounds settling within $25 of the target: 180, wrong winner 13 (7%)
- Rounds settling within $50 of the target: 301, wrong winner 13 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 87 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 72
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 89
- Coinbase trade -> we received it: median 890 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 73 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/87 | 65 | 0 | +25.17 |
| 10s | 20/87 | 67 | 0 | -1.27 |
| 20s | 17/87 | 70 | 0 | -13.40 |
| 30s | 15/87 | 72 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 55 · loops: 90732 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
