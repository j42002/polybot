# polybot report

Updated 2026-11-25 16:48 UTC | 326 checkpoints logged | 213 graded | 57 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 9 settled rounds observed · 0 alerts (0 delivered) · **0 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/11 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 0
2. **Model vs market accuracy (Brier, lower is better):** model 0.1808 vs market 0.2062 on 9 rounds -> model sharper
3. **Simulated profit after fees:** no simulated trades yet
4. **Quote available at simulated tap:** no delivered alerts watched yet
5. **Max drawdown:** n/a
6. **Loop health and missing data:** 1 runs, stalls over 5s 0/1650 loops, longest BTC price gap 2.0s · bad close samples 0 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 0/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (30 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 30 | 56.7% | 66.2% | -0.095 | -0.287 to +0.096 | $-28.60 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 30 | 50.0% | 70.4% | -0.204 | -0.385 to -0.022 | $-61.08 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 16 | 50.0% | 28.4% | +0.216 | -0.014 to +0.447 | $+34.59 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 5 | 80.0% | 44.6% | +0.354 | -0.023 to +0.730 | $+17.68 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2680 vs market 0.2827 -> **model is sharper**

## 3:30 left (36 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 36 | 77.8% | 62.2% | +0.156 | +0.009 to +0.303 | $+56.24 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 36 | 72.2% | 72.7% | -0.005 | -0.163 to +0.153 | $-1.81 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 15 | 40.0% | 27.4% | +0.126 | -0.101 to +0.353 | $+18.91 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 66.1% | +0.339 | -inf to +inf | $+3.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2109 vs market 0.2291 -> **model is sharper**

## 3:00 left (43 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 43 | 74.4% | 59.0% | +0.154 | +0.029 to +0.279 | $+66.27 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 43 | 67.4% | 73.0% | -0.056 | -0.191 to +0.080 | $-23.95 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 23 | 43.5% | 31.4% | +0.120 | -0.043 to +0.283 | $+27.69 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1921 vs market 0.2022 -> **model is sharper**

## 2:00 left (50 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 48 | 52.1% | 60.0% | -0.079 | -0.187 to +0.029 | $-37.92 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 46 | 82.6% | 80.2% | +0.024 | -0.089 to +0.137 | $+11.19 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 35 | 25.7% | 25.2% | +0.005 | -0.120 to +0.130 | $+1.81 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 2 | 100.0% | 71.9% | +0.281 | +0.149 to +0.413 | $+5.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1437 vs market 0.1458 -> **model is sharper**

## 1:00 left (54 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 38 | 55.3% | 46.9% | +0.084 | -0.024 to +0.191 | $+31.78 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 32 | 90.6% | 76.9% | +0.138 | +0.018 to +0.258 | $+44.05 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 41 | 22.0% | 16.7% | +0.053 | -0.039 to +0.144 | $+21.57 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0847 vs market 0.1017 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=57, bias $-0.66, sd $2.08 (set BASIS_SD near 2)
- spot at open: n=57, bias $-3.57, sd $34.64 (set BASIS_SD near 35)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 45 | 28 | 55% | 60% |
| 60%-70% | 46 | 33 | 65% | 65% |
| 70%-80% | 39 | 26 | 74% | 74% |
| 80%-90% | 72 | 40 | 87% | 93% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- Development data, split by market, oldest first: train 33 markets (131 checks), test 15 markets (49 checks).
- 9 rounds predicted live by the current model are a forward test: never used to fit or choose anything (see 'Forward test').
- Not fitted yet: needs 60 train + 30 test markets. Default volatility x1.4 stays.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 9 | 33 | 0.1808 | 0.2062 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 57 (9 with decision logging, v16+)
- Markets with a signal: 1
- Alerts attempted: 0 · delivered: 0 · delivery failed: 0
- Simulated fills (quote available, size not verified): 0
- Expired alerts: 0 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 1 markets, would have won 1, +6.18 at 10 shares. Negative = the filter saved money.
- Liquidity: the venue's quote has not reported ask size yet; fills stay 'simulated'.

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 11 · valid comparisons: 11
- Missing/untrusted: 0 sampling gaps (>6s hole or <20 samples), 0 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+0.07, typical gap $2.46, worst $4.84
- Coinbase would have named the wrong winner: 0/11 (0.0%)
- Rounds settling within $10 of the target: 0, wrong winner 0
- Rounds settling within $25 of the target: 0, wrong winner 0
- Rounds settling within $50 of the target: 1, wrong winner 0 (0%)

## Honest scoreboard (tickets)

No settled tickets yet.

## Ticket speed

No v10 tickets yet.

## Loop health (are our timings trustworthy?)

- Runs: 1 · loops: 1650 · loops over 5s: 0 (0.00%)
- Worst single loop: 0.1s · longest gap between BTC prices: 2.0s
- No stalls recorded.
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
