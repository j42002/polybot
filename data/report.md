# polybot report

Updated 2026-11-26 04:47 UTC | 1002 checkpoints logged | 838 graded | 192 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 144 settled rounds observed · 20 alerts (19 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/143 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1350 vs market 0.1455 on 144 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 6/19 · 10s 6/19 · 20s 5/19 · 30s 3/19
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 14 runs, stalls over 5s 2/23092 loops, longest BTC price gap 10.7s · checks with no market quote 64/730 (book fallback used 277) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (151 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 151 | 68.9% | 65.6% | +0.032 | -0.043 to +0.108 | $+48.88 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 151 | 63.6% | 68.4% | -0.048 | -0.124 to +0.028 | $-72.78 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 85 | 54.1% | 38.2% | +0.159 | +0.064 to +0.254 | $+135.12 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 36 | 77.8% | 49.3% | +0.285 | +0.149 to +0.422 | $+102.69 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2052 vs market 0.2252 -> **model is sharper**

## 3:30 left (159 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 159 | 73.0% | 64.8% | +0.082 | +0.016 to +0.147 | $+129.59 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 159 | 76.1% | 72.3% | +0.038 | -0.029 to +0.104 | $+59.82 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 88 | 40.9% | 33.5% | +0.074 | -0.016 to +0.164 | $+65.20 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 16 | 62.5% | 52.3% | +0.102 | -0.143 to +0.348 | $+16.38 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1739 vs market 0.1868 -> **model is sharper**

## 3:00 left (167 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 167 | 70.7% | 63.4% | +0.072 | +0.014 to +0.130 | $+120.61 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 167 | 78.4% | 75.9% | +0.025 | -0.034 to +0.085 | $+41.97 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 98 | 31.6% | 28.5% | +0.031 | -0.041 to +0.103 | $+30.22 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 4 | 100.0% | 74.8% | +0.252 | +0.192 to +0.311 | $+10.06 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1540 vs market 0.1559 -> **model is sharper**

## 2:00 left (179 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 168 | 63.1% | 60.0% | +0.031 | -0.020 to +0.081 | $+51.31 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 164 | 87.8% | 81.1% | +0.067 | +0.017 to +0.117 | $+109.65 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 135 | 23.0% | 21.5% | +0.015 | -0.038 to +0.068 | $+20.30 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 8 | 100.0% | 73.9% | +0.261 | +0.212 to +0.311 | $+20.91 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1100 vs market 0.1127 -> **model is sharper**

## 1:00 left (182 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 134 | 48.5% | 47.7% | +0.008 | -0.041 to +0.057 | $+10.81 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 110 | 92.7% | 83.1% | +0.096 | +0.040 to +0.152 | $+105.98 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 152 | 15.1% | 11.7% | +0.035 | -0.003 to +0.072 | $+52.64 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0651 vs market 0.0811 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=192, bias $-0.19, sd $1.17 (set BASIS_SD near 1)
- spot at open: n=192, bias $-0.48, sd $28.30 (set BASIS_SD near 28)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 179 | 99 | 55% | 59% |
| 60%-70% | 174 | 113 | 65% | 71% |
| 70%-80% | 161 | 108 | 75% | 84% |
| 80%-90% | 313 | 149 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 144 | 658 | 0.135 | 0.1455 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 192 (144 with decision logging, v16+)
- Markets with a signal: 50
- Alerts attempted: 20 · delivered: 19 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 16 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 22 markets, would have won 16, +28.11 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 12 markets, would have won 11, +50.93 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 18/19 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 153 · valid comparisons: 143
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.95, typical gap $2.58, worst $12.31
- Coinbase would have named the wrong winner: 0/143 (0.0%)
- Rounds settling within $10 of the target: 12, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 25, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 54, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 19 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 16
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 20
- Coinbase trade -> we received it: median 1083 ms (worst 1624)
- Coinbase request round trip: median 18 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 6/19 | 13 | 0 | +20.71 |
| 10s | 6/19 | 13 | 0 | +20.71 |
| 20s | 5/19 | 14 | 0 | +4.98 |
| 30s | 3/19 | 16 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 14 · loops: 23092 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
