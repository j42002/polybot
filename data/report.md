# polybot report

Updated 2026-11-26 05:42 UTC | 1055 checkpoints logged | 891 graded | 203 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 155 settled rounds observed · 21 alerts (20 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/154 valid rounds (0.6%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1363 vs market 0.1455 on 155 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 6/20 · 10s 6/20 · 20s 5/20 · 30s 3/20
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 15 runs, stalls over 5s 2/24742 loops, longest BTC price gap 10.7s · checks with no market quote 64/783 (book fallback used 302) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (162 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 162 | 68.5% | 65.8% | +0.027 | -0.045 to +0.099 | $+43.69 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 162 | 64.8% | 68.7% | -0.039 | -0.112 to +0.033 | $-63.36 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 91 | 52.7% | 38.9% | +0.139 | +0.046 to +0.231 | $+126.20 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 39 | 74.4% | 49.6% | +0.248 | +0.109 to +0.387 | $+96.70 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2050 vs market 0.2216 -> **model is sharper**

## 3:30 left (170 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 170 | 74.1% | 65.5% | +0.086 | +0.023 to +0.149 | $+146.40 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 170 | 76.5% | 73.1% | +0.034 | -0.030 to +0.098 | $+57.74 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 95 | 38.9% | 32.1% | +0.068 | -0.018 to +0.155 | $+65.07 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 16 | 62.5% | 52.3% | +0.102 | -0.143 to +0.348 | $+16.38 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1732 vs market 0.1858 -> **model is sharper**

## 3:00 left (178 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 178 | 71.3% | 63.3% | +0.081 | +0.025 to +0.137 | $+143.64 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 178 | 78.7% | 76.6% | +0.021 | -0.037 to +0.079 | $+37.02 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 108 | 31.5% | 27.7% | +0.037 | -0.032 to +0.107 | $+40.47 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 5 | 100.0% | 73.7% | +0.263 | +0.212 to +0.314 | $+13.15 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1518 vs market 0.1557 -> **model is sharper**

## 2:00 left (189 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 178 | 62.4% | 59.3% | +0.030 | -0.019 to +0.079 | $+53.74 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 174 | 87.9% | 81.3% | +0.066 | +0.017 to +0.115 | $+114.82 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 143 | 23.1% | 21.3% | +0.017 | -0.034 to +0.069 | $+24.73 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 9 | 100.0% | 73.4% | +0.266 | +0.221 to +0.310 | $+23.90 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1109 vs market 0.1137 -> **model is sharper**

## 1:00 left (192 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 142 | 46.5% | 45.9% | +0.006 | -0.041 to +0.053 | $+8.32 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 116 | 91.4% | 82.5% | +0.089 | +0.035 to +0.143 | $+103.43 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 162 | 14.2% | 11.7% | +0.025 | -0.011 to +0.062 | $+41.03 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0683 vs market 0.0800 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=203, bias $-0.18, sd $1.14 (set BASIS_SD near 1)
- spot at open: n=203, bias $-0.70, sd $27.66 (set BASIS_SD near 28)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 187 | 105 | 55% | 59% |
| 60%-70% | 181 | 118 | 65% | 72% |
| 70%-80% | 176 | 116 | 75% | 83% |
| 80%-90% | 336 | 158 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 155 | 711 | 0.1363 | 0.1455 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 203 (155 with decision logging, v16+)
- Markets with a signal: 54
- Alerts attempted: 21 · delivered: 20 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 17 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 26 markets, would have won 19, +34.53 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 12 markets, would have won 11, +50.93 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 19/20 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 164 · valid comparisons: 154
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.65, typical gap $2.76, worst $12.31
- Coinbase would have named the wrong winner: 1/154 (0.6%)
- Rounds settling within $10 of the target: 15, wrong winner 1 (7%)
- Rounds settling within $25 of the target: 31, wrong winner 1 (3%)
- Rounds settling within $50 of the target: 64, wrong winner 1 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 20 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 17
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 21
- Coinbase trade -> we received it: median 908 ms (worst 1624)
- Coinbase request round trip: median 18 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 6/20 | 14 | 0 | +20.71 |
| 10s | 6/20 | 14 | 0 | +20.71 |
| 20s | 5/20 | 15 | 0 | +4.98 |
| 30s | 3/20 | 17 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 15 · loops: 24742 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
