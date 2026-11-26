# polybot report

Updated 2026-11-26 00:10 UTC | 742 checkpoints logged | 581 graded | 138 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 90 settled rounds observed · 10 alerts (10 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/89 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1421 vs market 0.1498 on 90 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/10 · 10s 4/10 · 20s 4/10 · 30s 3/10
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 9 runs, stalls over 5s 1/14847 loops, longest BTC price gap 9.0s · checks with no market quote 64/470 (book fallback used 161) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (97 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 97 | 66.0% | 65.9% | +0.001 | -0.093 to +0.094 | $+0.66 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 97 | 60.8% | 68.7% | -0.079 | -0.172 to +0.014 | $-76.71 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 53 | 49.1% | 36.1% | +0.129 | +0.011 to +0.248 | $+68.58 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 22 | 72.7% | 47.4% | +0.253 | +0.071 to +0.435 | $+55.67 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2114 vs market 0.2201 -> **model is sharper**

## 3:30 left (107 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 107 | 72.0% | 65.8% | +0.061 | -0.022 to +0.144 | $+65.43 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 107 | 72.9% | 72.8% | +0.001 | -0.084 to +0.086 | $+1.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 57 | 40.4% | 32.3% | +0.080 | -0.037 to +0.198 | $+45.82 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 10 | 50.0% | 49.3% | +0.007 | -0.320 to +0.334 | $+0.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1844 vs market 0.1978 -> **model is sharper**

## 3:00 left (116 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 116 | 63.8% | 61.5% | +0.022 | -0.053 to +0.098 | $+26.10 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 116 | 73.3% | 76.3% | -0.030 | -0.107 to +0.046 | $-35.09 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 62 | 29.0% | 26.1% | +0.029 | -0.068 to +0.126 | $+17.99 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1755 vs market 0.1748 -> **market is sharper**

## 2:00 left (129 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 121 | 64.5% | 60.8% | +0.037 | -0.025 to +0.099 | $+44.74 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 118 | 86.4% | 81.5% | +0.050 | -0.013 to +0.113 | $+58.67 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 95 | 24.2% | 21.6% | +0.026 | -0.041 to +0.092 | $+24.42 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 6 | 100.0% | 73.1% | +0.269 | +0.204 to +0.335 | $+16.16 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1179 vs market 0.1230 -> **model is sharper**

## 1:00 left (132 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 93 | 49.5% | 46.8% | +0.027 | -0.036 to +0.090 | $+25.14 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 78 | 91.0% | 81.6% | +0.095 | +0.023 to +0.166 | $+73.85 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 105 | 15.2% | 11.6% | +0.036 | -0.011 to +0.084 | $+38.23 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0705 vs market 0.0867 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=138, bias $-0.27, sd $1.37 (set BASIS_SD near 1)
- spot at open: n=138, bias $-0.41, sd $31.02 (set BASIS_SD near 31)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 121 | 68 | 55% | 58% |
| 60%-70% | 115 | 77 | 65% | 65% |
| 70%-80% | 113 | 76 | 74% | 80% |
| 80%-90% | 221 | 105 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 90 | 401 | 0.1421 | 0.1498 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 138 (90 with decision logging, v16+)
- Markets with a signal: 29
- Alerts attempted: 10 · delivered: 10 · delivery failed: 0
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 7 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 13 markets, would have won 9, +19.98 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 7 markets, would have won 6, +26.06 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 9/10 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 98 · valid comparisons: 89
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.47, typical gap $2.74, worst $12.31
- Coinbase would have named the wrong winner: 0/89 (0.0%)
- Rounds settling within $10 of the target: 7, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 15, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 32, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 10 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 7
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 10
- Coinbase trade -> we received it: median 1146 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 30)
- Polymarket quote round trip: median 34 ms (worst 48)
- Price read -> decision made: median 88 ms (worst 105)
- Decision -> Discord accepted: median 1665 ms (worst 3027)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 4/10 | 6 | 0 | +1.17 |
| 10s | 4/10 | 6 | 0 | +1.17 |
| 20s | 4/10 | 6 | 0 | +1.17 |
| 30s | 3/10 | 7 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 9 · loops: 14847 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
