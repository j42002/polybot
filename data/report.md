# polybot report

Updated 2026-11-26 03:52 UTC | 949 checkpoints logged | 785 graded | 181 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 133 settled rounds observed · 17 alerts (16 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/132 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1380 vs market 0.1486 on 133 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/16 · 10s 4/16 · 20s 4/16 · 30s 3/16
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 13 runs, stalls over 5s 2/21442 loops, longest BTC price gap 10.7s · checks with no market quote 64/677 (book fallback used 252) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (140 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 140 | 68.6% | 65.4% | +0.032 | -0.046 to +0.110 | $+44.79 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 140 | 62.9% | 68.3% | -0.055 | -0.133 to +0.024 | $-76.87 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 77 | 50.6% | 37.4% | +0.133 | +0.032 to +0.234 | $+102.26 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 32 | 75.0% | 48.7% | +0.263 | +0.112 to +0.415 | $+84.30 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2095 vs market 0.2245 -> **model is sharper**

## 3:30 left (148 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 148 | 72.3% | 64.5% | +0.078 | +0.009 to +0.147 | $+115.35 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 148 | 75.0% | 72.2% | +0.028 | -0.042 to +0.099 | $+41.68 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 84 | 40.5% | 32.7% | +0.077 | -0.016 to +0.171 | $+64.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 15 | 60.0% | 51.1% | +0.089 | -0.173 to +0.350 | $+13.29 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1778 vs market 0.1930 -> **model is sharper**

## 3:00 left (156 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 156 | 69.2% | 62.5% | +0.067 | +0.005 to +0.129 | $+104.29 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 156 | 76.9% | 75.6% | +0.013 | -0.050 to +0.076 | $+20.54 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 91 | 31.9% | 28.2% | +0.037 | -0.040 to +0.114 | $+33.80 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 2 | 100.0% | 71.5% | +0.285 | +0.238 to +0.332 | $+5.70 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1605 vs market 0.1625 -> **model is sharper**

## 2:00 left (169 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 159 | 64.2% | 60.3% | +0.038 | -0.014 to +0.090 | $+60.46 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 156 | 87.2% | 81.0% | +0.062 | +0.009 to +0.114 | $+96.36 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 127 | 23.6% | 21.8% | +0.018 | -0.037 to +0.073 | $+23.15 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 8 | 100.0% | 73.9% | +0.261 | +0.212 to +0.311 | $+20.91 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1122 vs market 0.1154 -> **model is sharper**

## 1:00 left (172 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 127 | 50.4% | 49.2% | +0.012 | -0.040 to +0.064 | $+14.93 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 105 | 92.4% | 82.6% | +0.098 | +0.039 to +0.156 | $+102.85 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 142 | 16.2% | 12.2% | +0.040 | +0.000 to +0.080 | $+57.40 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0649 vs market 0.0836 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=181, bias $-0.21, sd $1.20 (set BASIS_SD near 1)
- spot at open: n=181, bias $-0.51, sd $29.02 (set BASIS_SD near 29)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 168 | 94 | 55% | 58% |
| 60%-70% | 166 | 107 | 65% | 70% |
| 70%-80% | 151 | 101 | 75% | 83% |
| 80%-90% | 289 | 141 | 87% | 98% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 133 | 605 | 0.138 | 0.1486 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 181 (133 with decision logging, v16+)
- Markets with a signal: 45
- Alerts attempted: 17 · delivered: 16 · delivery failed: 1
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 13 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 20 markets, would have won 14, +23.75 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 10 markets, would have won 9, +42.20 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 2 markets, would have won 2, +7.95 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 15/16 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 142 · valid comparisons: 132
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 6 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.94, typical gap $2.61, worst $12.31
- Coinbase would have named the wrong winner: 0/132 (0.0%)
- Rounds settling within $10 of the target: 10, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 22, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 46, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 16 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 13
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 17
- Coinbase trade -> we received it: median 908 ms (worst 1624)
- Coinbase request round trip: median 18 ms (worst 30)
- Polymarket quote round trip: median 34 ms (worst 75)
- Price read -> decision made: median 87 ms (worst 168)
- Decision -> Discord accepted: median 1538 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 4/16 | 12 | 0 | +1.17 |
| 10s | 4/16 | 12 | 0 | +1.17 |
| 20s | 4/16 | 12 | 0 | +1.17 |
| 30s | 3/16 | 13 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 13 · loops: 21442 · loops over 5s: 2 (0.01%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
