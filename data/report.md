# polybot report

Updated 2026-11-28 14:54 UTC | 4302 checkpoints logged | 4104 graded | 869 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 821 settled rounds observed · 139 alerts (136 delivered) · **33 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/803 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 43
2. **Model vs market accuracy (Brier, lower is better):** model 0.1594 vs market 0.1631 on 821 rounds -> model sharper
3. **Simulated profit after fees:** -9.33 on 33 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.16 to +3.59
4. **Quote available at simulated tap (size not verified):** 5s 47/136 · 10s 45/136 · 20s 38/136 · 30s 33/136
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 77 runs, stalls over 5s 13/127013 loops, longest BTC price gap 21.8s · checks with no market quote 101/4030 (book fallback used 1632) · bad close samples 19 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 33/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 33/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 84/136 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 33 tickets at every delay (right 16/33): 5s -15.59 · 10s -17.52 · 20s -12.43 · 30s -9.33. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (803 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 801 | 66.5% | 64.6% | +0.020 | -0.012 to +0.052 | $+159.42 | NO EDGE |
| Lean (bet the side BTC is on now) | 803 | 66.6% | 66.8% | -0.002 | -0.034 to +0.030 | $-17.63 | NO EDGE |
| Edge (model beats the ask by 3c+) | 410 | 50.5% | 43.0% | +0.075 | +0.031 to +0.119 | $+306.96 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 194 | 64.4% | 52.3% | +0.121 | +0.053 to +0.189 | $+234.54 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2087 vs market 0.2152 -> **model is sharper**

## 3:30 left (819 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 816 | 66.4% | 63.6% | +0.028 | -0.002 to +0.059 | $+231.13 | NO EDGE |
| Lean (bet the side BTC is on now) | 819 | 70.1% | 71.2% | -0.011 | -0.042 to +0.019 | $-91.75 | NO EDGE |
| Edge (model beats the ask by 3c+) | 463 | 38.7% | 35.3% | +0.033 | -0.006 to +0.073 | $+154.98 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 94 | 56.4% | 52.1% | +0.042 | -0.055 to +0.140 | $+39.81 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1949 vs market 0.1965 -> **model is sharper**

## 3:00 left (827 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 825 | 65.7% | 62.1% | +0.036 | +0.007 to +0.064 | $+293.91 | PASSES |
| Lean (bet the side BTC is on now) | 826 | 75.4% | 74.4% | +0.010 | -0.018 to +0.039 | $+85.87 | NO EDGE |
| Edge (model beats the ask by 3c+) | 504 | 36.1% | 31.1% | +0.050 | +0.016 to +0.085 | $+254.44 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 47 | 89.4% | 71.8% | +0.175 | +0.084 to +0.267 | $+82.36 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1691 vs market 0.1746 -> **model is sharper**

## 2:00 left (833 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 791 | 61.1% | 58.8% | +0.023 | -0.002 to +0.048 | $+180.68 | NO EDGE |
| Lean (bet the side BTC is on now) | 777 | 83.1% | 80.1% | +0.030 | +0.005 to +0.056 | $+236.92 | PASSES |
| Edge (model beats the ask by 3c+) | 618 | 23.8% | 21.4% | +0.024 | -0.002 to +0.050 | $+146.42 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1259 vs market 0.1259 -> **model is sharper**

## 1:00 left (822 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 612 | 49.7% | 48.0% | +0.017 | -0.008 to +0.042 | $+103.52 | NO EDGE |
| Lean (bet the side BTC is on now) | 519 | 85.5% | 81.8% | +0.037 | +0.008 to +0.067 | $+193.84 | PASSES |
| Edge (model beats the ask by 3c+) | 731 | 15.3% | 12.2% | +0.031 | +0.012 to +0.051 | $+228.09 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0876 vs market 0.0943 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=869, bias $-0.04, sd $0.55 (set BASIS_SD near 1)
- spot at open: n=869, bias $-4.02, sd $22.13 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 997 | 518 | 55% | 57% |
| 60%-70% | 929 | 561 | 65% | 70% |
| 70%-80% | 768 | 506 | 75% | 81% |
| 80%-90% | 1399 | 620 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 821 | 3924 | 0.1594 | 0.1631 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 869 (821 with decision logging, v16+)
- Markets with a signal: 318
- Alerts attempted: 139 · delivered: 136 · delivery failed: 3
- Simulated fills (quote available, size not verified): 33
- Expired alerts: 103 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 131 markets, would have won 89, +86.99 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 66 markets, would have won 48, +128.35 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 123/136 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 846 · valid comparisons: 803
- Missing/untrusted: 19 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-3.10, typical gap $4.25, worst $20.80
- Coinbase would have named the wrong winner: 25/803 (3.1%)
- Rounds settling within $10 of the target: 119, wrong winner 24 (20%)
- Rounds settling within $25 of the target: 292, wrong winner 25 (9%)
- Rounds settling within $50 of the target: 471, wrong winner 25 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 136 (goal: 300)
- Simulated paper trades: 33 · no-trade (expired/unconfirmed): 103
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 16/33 = 48% vs break-even 49.4% (price paid + fee)
- Paper P&L after fees: -9.33 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 139
- Coinbase trade -> we received it: median 966 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1538 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 47/136 | 89 | 0 | +76.05 |
| 10s | 45/136 | 91 | 0 | +46.92 |
| 20s | 38/136 | 98 | 0 | +39.33 |
| 30s | 33/136 | 103 | 0 | -9.33 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 77 · loops: 127013 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
