# polybot report

Updated 2026-11-26 07:33 UTC | 1163 checkpoints logged | 1003 graded | 226 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 178 settled rounds observed · 24 alerts (23 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/177 valid rounds (0.6%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1358 vs market 0.1470 on 178 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 7/23 · 10s 7/23 · 20s 5/23 · 30s 3/23
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 17 runs, stalls over 5s 2/28042 loops, longest BTC price gap 10.7s · checks with no market quote 64/891 (book fallback used 333) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (185 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 185 | 68.6% | 65.7% | +0.029 | -0.037 to +0.096 | $+53.93 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 185 | 66.5% | 68.7% | -0.023 | -0.089 to +0.044 | $-41.71 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 103 | 52.4% | 39.3% | +0.131 | +0.045 to +0.217 | $+135.13 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 44 | 72.7% | 49.5% | +0.233 | +0.102 to +0.363 | $+102.36 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2000 vs market 0.2151 -> **model is sharper**

## 3:30 left (193 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 193 | 73.6% | 65.7% | +0.079 | +0.020 to +0.138 | $+152.87 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 193 | 76.2% | 72.9% | +0.033 | -0.027 to +0.093 | $+63.72 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 110 | 40.9% | 32.9% | +0.080 | +0.001 to +0.160 | $+88.18 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 19 | 63.2% | 51.8% | +0.114 | -0.106 to +0.334 | $+21.61 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1726 vs market 0.1848 -> **model is sharper**

## 3:00 left (201 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 201 | 71.1% | 63.8% | +0.073 | +0.020 to +0.127 | $+147.25 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 201 | 79.6% | 75.9% | +0.037 | -0.017 to +0.091 | $+74.63 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 123 | 35.0% | 28.8% | +0.061 | -0.005 to +0.127 | $+75.31 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 7 | 100.0% | 71.7% | +0.283 | +0.224 to +0.342 | $+19.83 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1488 vs market 0.1574 -> **model is sharper**

## 2:00 left (211 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 198 | 60.1% | 58.2% | +0.019 | -0.028 to +0.067 | $+38.15 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 194 | 88.1% | 80.6% | +0.076 | +0.029 to +0.122 | $+146.61 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 159 | 23.9% | 21.8% | +0.021 | -0.028 to +0.071 | $+33.73 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 10 | 100.0% | 73.8% | +0.262 | +0.222 to +0.303 | $+26.22 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1111 vs market 0.1159 -> **model is sharper**

## 1:00 left (213 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 157 | 46.5% | 46.2% | +0.003 | -0.043 to +0.049 | $+4.82 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 128 | 91.4% | 81.9% | +0.095 | +0.042 to +0.148 | $+121.68 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 180 | 16.1% | 12.3% | +0.038 | +0.002 to +0.073 | $+67.91 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0688 vs market 0.0835 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=226, bias $-0.17, sd $1.08 (set BASIS_SD near 1)
- spot at open: n=226, bias $-1.19, sd $27.10 (set BASIS_SD near 27)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 214 | 119 | 55% | 60% |
| 60%-70% | 208 | 131 | 65% | 74% |
| 70%-80% | 193 | 130 | 75% | 83% |
| 80%-90% | 377 | 175 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 178 | 823 | 0.1358 | 0.147 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 226 (178 with decision logging, v16+)
- Markets with a signal: 63
- Alerts attempted: 24 · delivered: 23 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 20 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 32 markets, would have won 23, +38.87 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 14 markets, would have won 12, +51.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 22/23 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 186 · valid comparisons: 177
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.17, typical gap $2.93, worst $12.31
- Coinbase would have named the wrong winner: 1/177 (0.6%)
- Rounds settling within $10 of the target: 19, wrong winner 1 (5%)
- Rounds settling within $25 of the target: 40, wrong winner 1 (2%)
- Rounds settling within $50 of the target: 74, wrong winner 1 (1%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 23 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 20
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 24
- Coinbase trade -> we received it: median 1083 ms (worst 1913)
- Coinbase request round trip: median 18 ms (worst 34)
- Polymarket quote round trip: median 34 ms (worst 75)
- Price read -> decision made: median 88 ms (worst 168)
- Decision -> Discord accepted: median 1445 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 7/23 | 16 | 0 | +27.55 |
| 10s | 7/23 | 16 | 0 | +27.55 |
| 20s | 5/23 | 18 | 0 | +4.98 |
| 30s | 3/23 | 20 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 17 · loops: 28042 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
