# polybot report

Updated 2026-11-25 17:43 UTC | 380 checkpoints logged | 238 graded | 65 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 17 settled rounds observed · 0 alerts (0 delivered) · **0 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/22 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 0
2. **Model vs market accuracy (Brier, lower is better):** model 0.1475 vs market 0.1694 on 17 rounds -> model sharper
3. **Simulated profit after fees:** no simulated trades yet
4. **Quote available at simulated tap:** no delivered alerts watched yet
5. **Max drawdown:** n/a
6. **Loop health and missing data:** 2 runs, stalls over 5s 0/3300 loops, longest BTC price gap 2.1s · bad close samples 0 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 0/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (33 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 33 | 57.6% | 67.6% | -0.101 | -0.280 to +0.079 | $-33.23 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 33 | 51.5% | 71.4% | -0.199 | -0.370 to -0.029 | $-65.72 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 19 | 47.4% | 27.4% | +0.200 | -0.009 to +0.408 | $+37.93 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 5 | 80.0% | 44.6% | +0.354 | -0.023 to +0.730 | $+17.68 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2602 vs market 0.2746 -> **model is sharper**

## 3:30 left (40 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 40 | 77.5% | 64.7% | +0.128 | -0.013 to +0.269 | $+51.02 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 40 | 72.5% | 74.3% | -0.018 | -0.166 to +0.131 | $-7.04 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 19 | 36.8% | 24.8% | +0.120 | -0.078 to +0.319 | $+22.86 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 66.1% | +0.339 | -inf to +inf | $+3.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2063 vs market 0.2248 -> **model is sharper**

## 3:00 left (48 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 48 | 75.0% | 60.2% | +0.148 | +0.036 to +0.260 | $+70.98 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 48 | 70.8% | 74.6% | -0.038 | -0.160 to +0.085 | $-18.13 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 27 | 37.0% | 28.9% | +0.081 | -0.063 to +0.225 | $+22.00 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1800 vs market 0.1839 -> **model is sharper**

## 2:00 left (56 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 53 | 54.7% | 62.2% | -0.074 | -0.173 to +0.024 | $-39.47 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 51 | 84.3% | 81.3% | +0.030 | -0.072 to +0.132 | $+15.35 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 39 | 23.1% | 22.9% | +0.002 | -0.110 to +0.114 | $+0.72 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 2 | 100.0% | 71.9% | +0.281 | +0.149 to +0.413 | $+5.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1330 vs market 0.1339 -> **model is sharper**

## 1:00 left (61 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 42 | 52.4% | 45.4% | +0.070 | -0.038 to +0.177 | $+29.31 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 35 | 91.4% | 74.5% | +0.169 | +0.053 to +0.284 | $+59.09 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 47 | 23.4% | 16.5% | +0.069 | -0.017 to +0.155 | $+32.30 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0851 vs market 0.1117 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=65, bias $-0.58, sd $1.96 (set BASIS_SD near 2)
- spot at open: n=65, bias $-5.66, sd $36.47 (set BASIS_SD near 36)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 47 | 30 | 55% | 62% |
| 60%-70% | 48 | 35 | 65% | 65% |
| 70%-80% | 47 | 31 | 74% | 77% |
| 80%-90% | 85 | 45 | 86% | 94% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 17 | 58 | 0.1475 | 0.1694 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 65 (17 with decision logging, v16+)
- Markets with a signal: 1
- Alerts attempted: 0 · delivered: 0 · delivery failed: 0
- Simulated fills (quote available, size not verified): 0
- Expired alerts: 0 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 1 markets, would have won 1, +6.18 at 10 shares. Negative = the filter saved money.
- Liquidity: the venue's quote has not reported ask size yet; fills stay 'simulated'.

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 22 · valid comparisons: 22
- Missing/untrusted: 0 sampling gaps (>6s hole or <20 samples), 0 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.88, typical gap $2.15, worst $4.84
- Coinbase would have named the wrong winner: 0/22 (0.0%)
- Rounds settling within $10 of the target: 0, wrong winner 0
- Rounds settling within $25 of the target: 1, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 2, wrong winner 0 (0%)

## Honest scoreboard (tickets)

No settled tickets yet.

## Ticket speed

No v10 tickets yet.

## Loop health (are our timings trustworthy?)

- Runs: 2 · loops: 3300 · loops over 5s: 0 (0.00%)
- Worst single loop: 0.2s · longest gap between BTC prices: 2.1s
- No stalls recorded.
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
