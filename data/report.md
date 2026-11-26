# polybot report

Updated 2026-11-26 02:57 UTC | 896 checkpoints logged | 733 graded | 170 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 122 settled rounds observed · 14 alerts (13 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/121 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1353 vs market 0.1428 on 122 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/13 · 10s 4/13 · 20s 4/13 · 30s 3/13
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 12 runs, stalls over 5s 2/19792 loops, longest BTC price gap 10.7s · checks with no market quote 64/624 (book fallback used 235) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (129 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 129 | 68.2% | 65.4% | +0.028 | -0.053 to +0.109 | $+36.38 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 129 | 62.8% | 68.3% | -0.055 | -0.136 to +0.026 | $-70.78 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 71 | 49.3% | 37.3% | +0.120 | +0.016 to +0.223 | $+84.91 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 30 | 73.3% | 49.1% | +0.243 | +0.083 to +0.402 | $+72.76 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2085 vs market 0.2205 -> **model is sharper**

## 3:30 left (137 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 137 | 73.0% | 65.4% | +0.076 | +0.004 to +0.147 | $+103.51 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 137 | 75.2% | 72.3% | +0.029 | -0.044 to +0.101 | $+39.12 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 75 | 38.7% | 31.7% | +0.070 | -0.029 to +0.169 | $+52.31 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 12 | 58.3% | 49.7% | +0.086 | -0.203 to +0.376 | $+10.34 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1772 vs market 0.1893 -> **model is sharper**

## 3:00 left (146 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 146 | 68.5% | 63.0% | +0.055 | -0.009 to +0.118 | $+79.69 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 146 | 77.4% | 76.2% | +0.012 | -0.053 to +0.077 | $+17.63 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 85 | 31.8% | 28.2% | +0.035 | -0.043 to +0.113 | $+29.91 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 2 | 100.0% | 71.5% | +0.285 | +0.238 to +0.332 | $+5.70 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1589 vs market 0.1605 -> **model is sharper**

## 2:00 left (159 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 150 | 63.3% | 60.6% | +0.027 | -0.025 to +0.079 | $+40.42 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 147 | 87.8% | 82.0% | +0.058 | +0.005 to +0.111 | $+85.31 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 119 | 21.8% | 21.4% | +0.004 | -0.051 to +0.060 | $+5.27 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 8 | 100.0% | 73.9% | +0.261 | +0.212 to +0.311 | $+20.91 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1108 vs market 0.1097 -> **market is sharper**

## 1:00 left (162 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 118 | 50.8% | 48.5% | +0.023 | -0.030 to +0.076 | $+27.54 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 97 | 92.8% | 82.5% | +0.103 | +0.043 to +0.163 | $+100.03 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 133 | 15.8% | 11.8% | +0.040 | -0.000 to +0.080 | $+52.95 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0635 vs market 0.0811 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=170, bias $-0.22, sd $1.24 (set BASIS_SD near 1)
- spot at open: n=170, bias $+0.27, sd $29.37 (set BASIS_SD near 29)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 151 | 87 | 55% | 58% |
| 60%-70% | 153 | 100 | 65% | 70% |
| 70%-80% | 144 | 97 | 75% | 84% |
| 80%-90% | 274 | 134 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 122 | 553 | 0.1353 | 0.1428 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 170 (122 with decision logging, v16+)
- Markets with a signal: 40
- Alerts attempted: 14 · delivered: 13 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 10 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 19 markets, would have won 14, +30.07 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 9 markets, would have won 8, +36.02 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 12/13 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 131 · valid comparisons: 121
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.85, typical gap $2.66, worst $12.31
- Coinbase would have named the wrong winner: 0/121 (0.0%)
- Rounds settling within $10 of the target: 9, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 18, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 39, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 13 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 10
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 14
- Coinbase trade -> we received it: median 1083 ms (worst 1624)
- Coinbase request round trip: median 18 ms (worst 30)
- Polymarket quote round trip: median 32 ms (worst 48)
- Price read -> decision made: median 81 ms (worst 105)
- Decision -> Discord accepted: median 1665 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 4/13 | 9 | 0 | +1.17 |
| 10s | 4/13 | 9 | 0 | +1.17 |
| 20s | 4/13 | 9 | 0 | +1.17 |
| 30s | 3/13 | 10 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 12 · loops: 19792 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
