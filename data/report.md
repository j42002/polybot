# polybot report

Updated 2026-11-26 02:01 UTC | 844 checkpoints logged | 682 graded | 159 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 111 settled rounds observed · 12 alerts (12 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/110 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1408 vs market 0.1470 on 111 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/12 · 10s 4/12 · 20s 4/12 · 30s 3/12
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 11 runs, stalls over 5s 1/18146 loops, longest BTC price gap 9.0s · checks with no market quote 64/572 (book fallback used 208) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (118 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 118 | 66.1% | 65.5% | +0.006 | -0.079 to +0.091 | $+7.34 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 118 | 61.9% | 68.2% | -0.064 | -0.149 to +0.021 | $-75.23 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 64 | 48.4% | 37.0% | +0.115 | +0.007 to +0.223 | $+73.45 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 26 | 73.1% | 48.1% | +0.250 | +0.082 to +0.418 | $+64.96 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2141 vs market 0.2223 -> **model is sharper**

## 3:30 left (127 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 127 | 71.7% | 65.6% | +0.060 | -0.015 to +0.136 | $+76.48 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 127 | 73.2% | 72.5% | +0.007 | -0.070 to +0.084 | $+8.88 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 66 | 37.9% | 31.3% | +0.066 | -0.042 to +0.173 | $+43.25 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 10 | 50.0% | 49.3% | +0.007 | -0.320 to +0.334 | $+0.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1824 vs market 0.1933 -> **model is sharper**

## 3:00 left (136 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 136 | 66.9% | 62.5% | +0.044 | -0.023 to +0.112 | $+60.34 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 136 | 75.7% | 76.1% | -0.003 | -0.072 to +0.066 | $-4.34 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 78 | 29.5% | 27.0% | +0.025 | -0.058 to +0.109 | $+19.74 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 1 | 100.0% | 73.9% | +0.261 | -inf to +inf | $+2.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1668 vs market 0.1667 -> **market is sharper**

## 2:00 left (149 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 141 | 62.4% | 59.8% | +0.026 | -0.030 to +0.081 | $+36.43 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 138 | 87.0% | 81.4% | +0.055 | -0.001 to +0.111 | $+76.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 111 | 22.5% | 21.6% | +0.009 | -0.050 to +0.068 | $+10.16 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 7 | 100.0% | 73.2% | +0.268 | +0.213 to +0.324 | $+18.77 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1150 vs market 0.1155 -> **model is sharper**

## 1:00 left (152 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 109 | 51.4% | 48.8% | +0.026 | -0.031 to +0.082 | $+28.18 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 91 | 92.3% | 82.1% | +0.103 | +0.039 to +0.166 | $+93.33 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 123 | 15.4% | 11.5% | +0.040 | -0.003 to +0.083 | $+49.12 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0660 vs market 0.0842 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=159, bias $-0.24, sd $1.28 (set BASIS_SD near 1)
- spot at open: n=159, bias $-0.14, sd $29.85 (set BASIS_SD near 30)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 145 | 82 | 55% | 58% |
| 60%-70% | 144 | 95 | 65% | 69% |
| 70%-80% | 131 | 89 | 74% | 82% |
| 80%-90% | 251 | 123 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 111 | 502 | 0.1408 | 0.147 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 159 (111 with decision logging, v16+)
- Markets with a signal: 34
- Alerts attempted: 12 · delivered: 12 · delivery failed: 0
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 9 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 16 markets, would have won 12, +31.18 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 7 markets, would have won 6, +26.06 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 1 markets, would have won 1, +3.09 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 11/12 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 120 · valid comparisons: 110
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.75, typical gap $2.70, worst $12.31
- Coinbase would have named the wrong winner: 0/110 (0.0%)
- Rounds settling within $10 of the target: 8, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 16, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 35, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 12 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 9
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 12
- Coinbase trade -> we received it: median 908 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 30)
- Polymarket quote round trip: median 34 ms (worst 48)
- Price read -> decision made: median 87 ms (worst 105)
- Decision -> Discord accepted: median 1665 ms (worst 3027)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 4/12 | 8 | 0 | +1.17 |
| 10s | 4/12 | 8 | 0 | +1.17 |
| 20s | 4/12 | 8 | 0 | +1.17 |
| 30s | 3/12 | 9 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 11 · loops: 18146 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
