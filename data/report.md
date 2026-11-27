# polybot report

Updated 2026-11-27 17:41 UTC | 3092 checkpoints logged | 2920 graded | 621 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 573 settled rounds observed · 87 alerts (85 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 12/560 valid rounds (2.1%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1621 vs market 0.1684 on 573 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/85 · 10s 20/85 · 20s 17/85 · 30s 15/85
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 54 runs, stalls over 5s 4/89082 loops, longest BTC price gap 10.8s · checks with no market quote 73/2820 (book fallback used 1181) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (568 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 568 | 64.8% | 64.5% | +0.003 | -0.036 to +0.042 | $+16.67 | NO EDGE |
| Lean (bet the side BTC is on now) | 568 | 65.1% | 67.3% | -0.022 | -0.060 to +0.017 | $-123.24 | NO EDGE |
| Edge (model beats the ask by 3c+) | 288 | 48.6% | 41.4% | +0.072 | +0.019 to +0.125 | $+207.60 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 126 | 63.5% | 52.5% | +0.110 | +0.025 to +0.196 | $+138.95 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2135 vs market 0.2216 -> **model is sharper**

## 3:30 left (580 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 580 | 65.3% | 62.8% | +0.025 | -0.011 to +0.062 | $+147.11 | NO EDGE |
| Lean (bet the side BTC is on now) | 580 | 70.5% | 71.2% | -0.007 | -0.043 to +0.030 | $-39.81 | NO EDGE |
| Edge (model beats the ask by 3c+) | 323 | 40.2% | 34.3% | +0.059 | +0.012 to +0.107 | $+191.10 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 66 | 59.1% | 52.1% | +0.070 | -0.044 to +0.183 | $+46.03 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1972 vs market 0.2027 -> **model is sharper**

## 3:00 left (588 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 587 | 64.4% | 61.3% | +0.031 | -0.003 to +0.065 | $+183.67 | NO EDGE |
| Lean (bet the side BTC is on now) | 587 | 75.5% | 74.3% | +0.011 | -0.023 to +0.045 | $+65.79 | NO EDGE |
| Edge (model beats the ask by 3c+) | 351 | 33.6% | 29.3% | +0.043 | +0.001 to +0.085 | $+150.07 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 28 | 85.7% | 71.4% | +0.143 | +0.007 to +0.280 | $+40.14 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1722 vs market 0.1775 -> **model is sharper**

## 2:00 left (595 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 559 | 63.5% | 59.9% | +0.036 | +0.006 to +0.066 | $+203.57 | PASSES |
| Lean (bet the side BTC is on now) | 548 | 82.8% | 80.0% | +0.029 | -0.002 to +0.059 | $+157.69 | NO EDGE |
| Edge (model beats the ask by 3c+) | 444 | 24.5% | 21.5% | +0.030 | -0.001 to +0.061 | $+134.14 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 22 | 95.5% | 75.2% | +0.203 | +0.108 to +0.298 | $+44.58 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1291 vs market 0.1322 -> **model is sharper**

## 1:00 left (589 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 436 | 49.8% | 47.7% | +0.021 | -0.010 to +0.051 | $+91.19 | NO EDGE |
| Lean (bet the side BTC is on now) | 370 | 85.4% | 81.8% | +0.036 | +0.001 to +0.072 | $+134.70 | PASSES |
| Edge (model beats the ask by 3c+) | 520 | 16.7% | 12.4% | +0.043 | +0.020 to +0.066 | $+225.38 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0874 vs market 0.0986 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=621, bias $-0.06, sd $0.65 (set BASIS_SD near 1)
- spot at open: n=621, bias $-3.19, sd $23.57 (set BASIS_SD near 24)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 710 | 369 | 55% | 58% |
| 60%-70% | 653 | 397 | 65% | 69% |
| 70%-80% | 557 | 369 | 75% | 78% |
| 80%-90% | 989 | 448 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 573 | 2740 | 0.1621 | 0.1684 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 621 (573 with decision logging, v16+)
- Markets with a signal: 212
- Alerts attempted: 87 · delivered: 85 · delivery failed: 2
- Simulated fills (quote available, size not verified): 15
- Expired alerts: 70 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 91 markets, would have won 61, +42.41 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 47 markets, would have won 36, +113.76 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 81/85 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 593 · valid comparisons: 560
- Missing/untrusted: 13 sampling gaps (>6s hole or <20 samples), 20 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-1.92, typical gap $3.97, worst $20.80
- Coinbase would have named the wrong winner: 12/560 (2.1%)
- Rounds settling within $10 of the target: 85, wrong winner 12 (14%)
- Rounds settling within $25 of the target: 176, wrong winner 12 (7%)
- Rounds settling within $50 of the target: 294, wrong winner 12 (4%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 85 (goal: 300)
- Simulated paper trades: 15 · no-trade (expired/unconfirmed): 70
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 6/15 = 40% vs break-even 49.2% (price paid + fee)
- Paper P&L after fees: -34.90 at $10 a trade · max drawdown: -51.99

## Ticket speed (measured, not assumed)

- Tickets: 87
- Coinbase trade -> we received it: median 908 ms (worst 6396)
- Coinbase request round trip: median 16 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 75)
- Price read -> decision made: median 72 ms (worst 168)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.6s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 22/85 | 63 | 0 | +25.17 |
| 10s | 20/85 | 65 | 0 | -1.27 |
| 20s | 17/85 | 68 | 0 | -13.40 |
| 30s | 15/85 | 70 | 0 | -34.90 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 54 · loops: 89082 · loops over 5s: 4 (0.00%)
- Worst single loop: 10.8s · longest gap between BTC prices: 10.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
