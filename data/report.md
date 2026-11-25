# polybot report

Updated 2026-11-25 23:15 UTC | 692 checkpoints logged | 534 graded | 128 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 80 settled rounds observed · 8 alerts (8 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/79 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 8
2. **Model vs market accuracy (Brier, lower is better):** model 0.1487 vs market 0.1585 on 80 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 3/8 · 10s 3/8 · 20s 3/8 · 30s 3/8
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 8 runs, stalls over 5s 1/13197 loops, longest BTC price gap 9.0s · checks with no market quote 61/420 (book fallback used 141) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (88 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 88 | 65.9% | 65.4% | +0.005 | -0.094 to +0.105 | $+4.63 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 88 | 60.2% | 68.5% | -0.083 | -0.182 to +0.016 | $-72.74 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 48 | 47.9% | 35.9% | +0.120 | -0.005 to +0.245 | $+57.64 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 18 | 72.2% | 47.9% | +0.244 | +0.042 to +0.446 | $+43.86 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2154 vs market 0.2256 -> **model is sharper**

## 3:30 left (98 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 98 | 71.4% | 65.8% | +0.057 | -0.032 to +0.145 | $+55.44 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 98 | 71.4% | 72.6% | -0.012 | -0.102 to +0.078 | $-11.39 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 52 | 42.3% | 33.8% | +0.085 | -0.041 to +0.211 | $+44.40 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 10 | 50.0% | 49.3% | +0.007 | -0.320 to +0.334 | $+0.72 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1914 vs market 0.2046 -> **model is sharper**

## 3:00 left (107 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 107 | 63.6% | 61.3% | +0.023 | -0.059 to +0.104 | $+24.09 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 107 | 72.0% | 75.8% | -0.038 | -0.120 to +0.043 | $-41.11 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 59 | 30.5% | 27.0% | +0.035 | -0.067 to +0.136 | $+20.59 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1835 vs market 0.1835 -> **model is sharper**

## 2:00 left (119 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 112 | 63.4% | 59.5% | +0.039 | -0.027 to +0.105 | $+43.47 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 109 | 85.3% | 80.7% | +0.046 | -0.022 to +0.114 | $+50.47 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 87 | 26.4% | 22.8% | +0.037 | -0.035 to +0.109 | $+31.98 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 6 | 100.0% | 73.1% | +0.269 | +0.204 to +0.335 | $+16.16 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1243 vs market 0.1315 -> **model is sharper**

## 1:00 left (122 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 86 | 51.2% | 48.0% | +0.032 | -0.036 to +0.100 | $+27.22 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 72 | 90.3% | 80.3% | +0.099 | +0.022 to +0.176 | $+71.48 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 95 | 16.8% | 12.4% | +0.044 | -0.008 to +0.097 | $+42.25 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0730 vs market 0.0918 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=128, bias $-0.29, sd $1.42 (set BASIS_SD near 1)
- spot at open: n=128, bias $-0.74, sd $32.05 (set BASIS_SD near 32)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 114 | 64 | 55% | 59% |
| 60%-70% | 110 | 73 | 65% | 64% |
| 70%-80% | 104 | 70 | 74% | 79% |
| 80%-90% | 195 | 95 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 80 | 354 | 0.1487 | 0.1585 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 128 (80 with decision logging, v16+)
- Markets with a signal: 25
- Alerts attempted: 8 · delivered: 8 · delivery failed: 0
- Simulated fills (quote available, size not verified): 3
- Expired alerts: 5 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 12 markets, would have won 8, +13.91 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 6 markets, would have won 6, +30.29 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 8/8 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 87 · valid comparisons: 79
- Missing/untrusted: 4 sampling gaps (>6s hole or <20 samples), 4 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.44, typical gap $2.84, worst $12.31
- Coinbase would have named the wrong winner: 0/79 (0.0%)
- Rounds settling within $10 of the target: 6, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 13, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 28, wrong winner 0 (0%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 8 (goal: 300)
- Simulated paper trades: 3 · no-trade (expired/unconfirmed): 5
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 1/3 = 33% vs break-even 44.8% (price paid + fee)
- Paper P&L after fees: -16.25 at $10 a trade · max drawdown: -16.25

## Ticket speed (measured, not assumed)

- Tickets: 8
- Coinbase trade -> we received it: median 1146 ms (worst 1624)
- Coinbase request round trip: median 20 ms (worst 30)
- Polymarket quote round trip: median 34 ms (worst 38)
- Price read -> decision made: median 88 ms (worst 93)
- Decision -> Discord accepted: median 1777 ms (worst 3027)
- Time left on the timer when sent: median 208s
- Price checks ran late by: median 0.3s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 3/8 | 5 | 0 | -16.00 |
| 10s | 3/8 | 5 | 0 | -16.00 |
| 20s | 3/8 | 5 | 0 | -16.00 |
| 30s | 3/8 | 5 | 0 | -16.25 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 8 · loops: 13197 · loops over 5s: 1 (0.01%)
- Worst single loop: 5.0s · longest gap between BTC prices: 9.0s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
