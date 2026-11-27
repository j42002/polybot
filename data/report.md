# polybot report

Updated 2026-11-27 06:37 UTC | 2464 checkpoints logged | 2294 graded | 492 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 444 settled rounds observed · 70 alerts (69 delivered) · **12 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 5/435 valid rounds (1.1%) where Coinbase points at the wrong winner · missing 26
2. **Model vs market accuracy (Brier, lower is better):** model 0.1541 vs market 0.1615 on 444 rounds -> model sharper
3. **Simulated profit after fees:** -3.33 on 12 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -6.97 to +6.42
4. **Quote available at simulated tap (size not verified):** 5s 17/69 · 10s 16/69 · 20s 14/69 · 30s 12/69
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 42 runs, stalls over 5s 3/69287 loops, longest BTC price gap 10.7s · checks with no market quote 71/2192 (book fallback used 920) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 12/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (443 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 443 | 65.9% | 64.9% | +0.010 | -0.033 to +0.053 | $+43.34 | NO EDGE |
| Lean (bet the side BTC is on now) | 443 | 66.4% | 67.6% | -0.012 | -0.055 to +0.031 | $-52.61 | NO EDGE |
| Edge (model beats the ask by 3c+) | 226 | 50.0% | 40.9% | +0.091 | +0.032 to +0.150 | $+206.11 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 99 | 67.7% | 51.9% | +0.158 | +0.065 to +0.251 | $+156.54 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2060 vs market 0.2163 -> **model is sharper**

## 3:30 left (453 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 453 | 65.6% | 63.1% | +0.024 | -0.016 to +0.065 | $+110.55 | NO EDGE |
| Lean (bet the side BTC is on now) | 453 | 71.5% | 71.2% | +0.003 | -0.038 to +0.044 | $+14.09 | NO EDGE |
| Edge (model beats the ask by 3c+) | 254 | 40.2% | 34.5% | +0.056 | +0.003 to +0.109 | $+142.84 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 53 | 60.4% | 52.0% | +0.084 | -0.043 to +0.211 | $+44.59 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1886 vs market 0.1965 -> **model is sharper**

## 3:00 left (461 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 460 | 64.1% | 61.4% | +0.028 | -0.010 to +0.065 | $+126.85 | NO EDGE |
| Lean (bet the side BTC is on now) | 460 | 76.3% | 74.4% | +0.019 | -0.018 to +0.057 | $+89.06 | NO EDGE |
| Edge (model beats the ask by 3c+) | 281 | 33.8% | 29.8% | +0.040 | -0.006 to +0.085 | $+111.70 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 25 | 88.0% | 71.3% | +0.167 | +0.032 to +0.301 | $+41.72 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1639 vs market 0.1706 -> **model is sharper**

## 2:00 left (470 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 441 | 62.4% | 59.9% | +0.024 | -0.009 to +0.057 | $+106.50 | NO EDGE |
| Lean (bet the side BTC is on now) | 434 | 84.3% | 80.4% | +0.039 | +0.006 to +0.073 | $+171.27 | PASSES |
| Edge (model beats the ask by 3c+) | 348 | 23.6% | 21.2% | +0.023 | -0.010 to +0.057 | $+80.66 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 19 | 100.0% | 75.1% | +0.249 | +0.223 to +0.275 | $+47.33 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1243 vs market 0.1264 -> **model is sharper**

## 1:00 left (467 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 350 | 50.0% | 48.3% | +0.017 | -0.016 to +0.049 | $+57.98 | NO EDGE |
| Lean (bet the side BTC is on now) | 294 | 88.1% | 83.1% | +0.050 | +0.012 to +0.088 | $+147.76 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 411 | 16.3% | 12.4% | +0.039 | +0.015 to +0.064 | $+162.22 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0811 vs market 0.0928 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=492, bias $-0.08, sd $0.73 (set BASIS_SD near 1)
- spot at open: n=492, bias $-1.65, sd $22.89 (set BASIS_SD near 23)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 537 | 285 | 55% | 57% |
| 60%-70% | 515 | 313 | 65% | 70% |
| 70%-80% | 435 | 291 | 75% | 82% |
| 80%-90% | 796 | 361 | 87% | 97% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 444 | 2114 | 0.1541 | 0.1615 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 492 (444 with decision logging, v16+)
- Markets with a signal: 168
- Alerts attempted: 70 · delivered: 69 · delivery failed: 1
- Simulated fills (quote available, size not verified): 12
- Expired alerts: 57 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 72 markets, would have won 50, +48.76 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 37 markets, would have won 30, +102.96 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 6 markets, would have won 5, +15.14 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 65/69 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 461 · valid comparisons: 435
- Missing/untrusted: 10 sampling gaps (>6s hole or <20 samples), 16 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-0.86, typical gap $2.86, worst $12.31
- Coinbase would have named the wrong winner: 5/435 (1.1%)
- Rounds settling within $10 of the target: 64, wrong winner 5 (8%)
- Rounds settling within $25 of the target: 136, wrong winner 5 (4%)
- Rounds settling within $50 of the target: 226, wrong winner 5 (2%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 69 (goal: 300)
- Simulated paper trades: 12 · no-trade (expired/unconfirmed): 57
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/12 = 50% vs break-even 49.7% (price paid + fee)
- Paper P&L after fees: -3.33 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 70
- Coinbase trade -> we received it: median 990 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 29 ms (worst 75)
- Price read -> decision made: median 75 ms (worst 168)
- Decision -> Discord accepted: median 1523 ms (worst 10661)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 17/69 | 52 | 0 | +50.69 |
| 10s | 16/69 | 53 | 0 | +40.68 |
| 20s | 14/69 | 55 | 0 | +18.11 |
| 30s | 12/69 | 57 | 0 | -3.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 42 · loops: 69287 · loops over 5s: 3 (0.00%)
- Worst single loop: 10.7s · longest gap between BTC prices: 10.7s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
