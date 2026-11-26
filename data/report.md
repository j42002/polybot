# polybot report

Updated 2026-11-26 12:09 UTC | 1428 checkpoints logged | 1266 graded | 280 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 232 settled rounds observed · 31 alerts (30 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/228 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 13
2. **Model vs market accuracy (Brier, lower is better):** model 0.1370 vs market 0.1465 on 232 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/30 · 10s 8/30 · 20s 6/30 · 30s 4/30
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 22 runs, stalls over 5s 2/36290 loops, longest BTC price gap 10.7s · checks with no market quote 65/1156 (book fallback used 444) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (235 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 235 | 70.2% | 66.1% | +0.041 | -0.017 to +0.100 | $+97.25 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 235 | 68.1% | 68.6% | -0.006 | -0.065 to +0.054 | $-13.09 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 128 | 53.9% | 39.7% | +0.142 | +0.066 to +0.218 | $+181.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 52 | 73.1% | 50.7% | +0.224 | +0.107 to +0.340 | $+116.25 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1947 vs market 0.2148 -> **model is sharper**

## 3:30 left (246 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 246 | 72.0% | 65.1% | +0.069 | +0.016 to +0.121 | $+169.29 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 246 | 76.0% | 73.1% | +0.029 | -0.024 to +0.083 | $+72.32 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 140 | 40.0% | 33.6% | +0.064 | -0.007 to +0.134 | $+88.94 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 24 | 62.5% | 52.0% | +0.105 | -0.085 to +0.296 | $+25.26 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1742 vs market 0.1841 -> **model is sharper**

## 3:00 left (255 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 255 | 66.3% | 60.9% | +0.054 | +0.006 to +0.102 | $+136.61 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 255 | 79.2% | 75.4% | +0.038 | -0.010 to +0.086 | $+96.84 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 156 | 33.3% | 28.1% | +0.053 | -0.006 to +0.111 | $+81.92 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 9 | 100.0% | 71.2% | +0.288 | +0.241 to +0.335 | $+25.92 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1499 vs market 0.1580 -> **model is sharper**

## 2:00 left (265 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 247 | 62.8% | 59.8% | +0.029 | -0.012 to +0.070 | $+72.09 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 242 | 88.0% | 80.6% | +0.074 | +0.033 to +0.115 | $+178.73 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 197 | 22.3% | 20.9% | +0.015 | -0.028 to +0.058 | $+28.97 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 13 | 100.0% | 75.1% | +0.249 | +0.216 to +0.283 | $+32.43 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1105 vs market 0.1103 -> **market is sharper**

## 1:00 left (265 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 196 | 46.9% | 44.9% | +0.020 | -0.020 to +0.060 | $+39.30 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 160 | 91.2% | 82.9% | +0.083 | +0.037 to +0.130 | $+133.41 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 228 | 14.9% | 11.8% | +0.031 | +0.001 to +0.062 | $+71.46 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0696 vs market 0.0797 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=280, bias $-0.13, sd $0.97 (set BASIS_SD near 1)
- spot at open: n=280, bias $-1.74, sd $24.81 (set BASIS_SD near 25)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 273 | 146 | 55% | 60% |
| 60%-70% | 271 | 167 | 65% | 73% |
| 70%-80% | 241 | 162 | 75% | 84% |
| 80%-90% | 470 | 215 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 232 | 1086 | 0.137 | 0.1465 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 280 (232 with decision logging, v16+)
- Markets with a signal: 81
- Alerts attempted: 31 · delivered: 30 · delivery failed: 1
- Simulated fills (quote available, size not verified): 4
- Expired alerts: 26 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 39 markets, would have won 29, +51.01 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 17 markets, would have won 15, +64.28 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 3 markets, would have won 3, +11.53 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 29/30 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 241 · valid comparisons: 228
- Missing/untrusted: 7 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.26, typical gap $2.99, worst $12.31
- Coinbase would have named the wrong winner: 3/228 (1.3%)
- Rounds settling within $10 of the target: 30, wrong winner 3 (10%)
- Rounds settling within $25 of the target: 61, wrong winner 3 (5%)
- Rounds settling within $50 of the target: 105, wrong winner 3 (3%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 30 (goal: 300)
- Simulated paper trades: 4 · no-trade (expired/unconfirmed): 26
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/4 = 25% vs break-even 43.9% (price paid + fee)
- Paper P&L after fees: -26.83 at $10 a trade · max drawdown: -26.83

## Ticket speed (measured, not assumed)

- Tickets: 31
- Coinbase trade -> we received it: median 933 ms (worst 6396)
- Coinbase request round trip: median 17 ms (worst 34)
- Polymarket quote round trip: median 32 ms (worst 75)
- Price read -> decision made: median 81 ms (worst 168)
- Decision -> Discord accepted: median 1381 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 8/30 | 22 | 0 | +16.97 |
| 10s | 8/30 | 22 | 0 | +16.97 |
| 20s | 6/30 | 24 | 0 | -5.60 |
| 30s | 4/30 | 26 | 0 | -26.83 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 22 · loops: 36290 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
