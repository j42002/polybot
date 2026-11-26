# polybot report

Updated 2026-11-26 06:38 UTC | 1109 checkpoints logged | 949 graded | 215 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 167 settled rounds observed · 24 alerts (23 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/166 valid rounds (0.6%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1339 vs market 0.1449 on 167 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 7/23 · 10s 7/23 · 20s 5/23 · 30s 3/23
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 16 runs, stalls over 5s 2/26392 loops, longest BTC price gap 10.7s · checks with no market quote 64/837 (book fallback used 316) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (174 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 174 | 69.5% | 66.2% | +0.034 | -0.035 to +0.102 | $+58.35 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 174 | 66.1% | 68.9% | -0.028 | -0.097 to +0.041 | $-48.71 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 98 | 54.1% | 39.8% | +0.143 | +0.056 to +0.230 | $+140.06 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 42 | 76.2% | 50.0% | +0.262 | +0.133 to +0.392 | $+110.20 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2001 vs market 0.2172 -> **model is sharper**

## 3:30 left (182 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 182 | 75.3% | 65.9% | +0.094 | +0.034 to +0.154 | $+170.87 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 182 | 77.5% | 73.3% | +0.042 | -0.020 to +0.103 | $+75.81 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 104 | 40.4% | 32.5% | +0.079 | -0.002 to +0.160 | $+82.43 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 17 | 64.7% | 51.6% | +0.131 | -0.107 to +0.368 | $+22.25 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1677 vs market 0.1818 -> **model is sharper**

## 3:00 left (190 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 190 | 72.1% | 64.1% | +0.080 | +0.026 to +0.134 | $+152.14 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 190 | 79.5% | 76.7% | +0.028 | -0.028 to +0.083 | $+52.62 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 116 | 32.8% | 28.3% | +0.045 | -0.022 to +0.111 | $+51.67 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 6 | 100.0% | 74.1% | +0.259 | +0.217 to +0.302 | $+15.57 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1483 vs market 0.1531 -> **model is sharper**

## 2:00 left (200 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 187 | 60.4% | 58.5% | +0.019 | -0.030 to +0.067 | $+35.27 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 183 | 87.4% | 81.2% | +0.063 | +0.014 to +0.111 | $+114.78 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 153 | 23.5% | 21.5% | +0.021 | -0.029 to +0.071 | $+31.77 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 10 | 100.0% | 73.8% | +0.262 | +0.222 to +0.303 | $+26.22 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1119 vs market 0.1155 -> **model is sharper**

## 1:00 left (203 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 150 | 46.7% | 45.8% | +0.009 | -0.038 to +0.056 | $+12.88 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 121 | 90.9% | 82.0% | +0.090 | +0.035 to +0.145 | $+108.32 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 171 | 15.2% | 11.8% | +0.034 | -0.002 to +0.071 | $+58.94 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0684 vs market 0.0838 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=215, bias $-0.17, sd $1.10 (set BASIS_SD near 1)
- spot at open: n=215, bias $-0.93, sd $27.27 (set BASIS_SD near 27)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 197 | 110 | 55% | 59% |
| 60%-70% | 193 | 124 | 65% | 73% |
| 70%-80% | 180 | 120 | 75% | 83% |
| 80%-90% | 368 | 168 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 167 | 769 | 0.1339 | 0.1449 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 215 (167 with decision logging, v16+)
- Markets with a signal: 59
- Alerts attempted: 24 · delivered: 23 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 20 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 29 markets, would have won 22, +43.44 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 12 markets, would have won 11, +50.93 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 22/23 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 175 · valid comparisons: 166
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 5 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.38, typical gap $2.88, worst $12.31
- Coinbase would have named the wrong winner: 1/166 (0.6%)
- Rounds settling within $10 of the target: 16, wrong winner 1 (6%)
- Rounds settling within $25 of the target: 35, wrong winner 1 (3%)
- Rounds settling within $50 of the target: 68, wrong winner 1 (1%)

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

- Runs: 16 · loops: 26392 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
