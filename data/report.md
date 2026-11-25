# polybot report

Updated 2026-11-25 18:38 UTC | 434 checkpoints logged | 289 graded | 76 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 28 settled rounds observed · 0 alerts (0 delivered) · **0 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/33 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 0
2. **Model vs market accuracy (Brier, lower is better):** model 0.1484 vs market 0.1719 on 28 rounds -> model sharper
3. **Simulated profit after fees:** no simulated trades yet
4. **Quote available at simulated tap:** no delivered alerts watched yet
5. **Max drawdown:** n/a
6. **Loop health and missing data:** 3 runs, stalls over 5s 0/4949 loops, longest BTC price gap 5.4s · checks with no market quote 49/162 (book fallback used 20) · bad close samples 0 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 0/300.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (43 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 43 | 60.5% | 65.4% | -0.049 | -0.207 to +0.109 | $-21.23 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 43 | 53.5% | 69.9% | -0.164 | -0.316 to -0.012 | $-70.41 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 25 | 48.0% | 30.2% | +0.178 | -0.000 to +0.356 | $+44.49 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 9 | 77.8% | 46.1% | +0.317 | +0.035 to +0.600 | $+28.54 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2508 vs market 0.2747 -> **model is sharper**

## 3:30 left (50 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 50 | 78.0% | 64.6% | +0.134 | +0.010 to +0.258 | $+67.06 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 50 | 74.0% | 74.0% | -0.000 | -0.131 to +0.130 | $-0.18 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 20 | 40.0% | 24.2% | +0.158 | -0.044 to +0.360 | $+31.56 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 66.1% | +0.339 | -inf to +inf | $+3.39 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1997 vs market 0.2197 -> **model is sharper**

## 3:00 left (58 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 58 | 75.9% | 60.1% | +0.157 | +0.060 to +0.255 | $+91.30 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 58 | 72.4% | 75.6% | -0.032 | -0.141 to +0.076 | $-18.68 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 35 | 28.6% | 27.0% | +0.016 | -0.103 to +0.135 | $+5.60 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1761 vs market 0.1738 -> **market is sharper**

## 2:00 left (67 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 62 | 56.5% | 59.9% | -0.035 | -0.127 to +0.058 | $-21.42 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 59 | 84.7% | 80.6% | +0.041 | -0.055 to +0.138 | $+24.32 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 49 | 24.5% | 21.6% | +0.029 | -0.071 to +0.129 | $+14.29 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 2 | 100.0% | 71.9% | +0.281 | +0.149 to +0.413 | $+5.61 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1293 vs market 0.1375 -> **model is sharper**

## 1:00 left (71 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 50 | 50.0% | 44.8% | +0.052 | -0.047 to +0.150 | $+25.78 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 41 | 90.2% | 75.9% | +0.144 | +0.033 to +0.254 | $+58.91 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 55 | 21.8% | 15.3% | +0.065 | -0.015 to +0.145 | $+35.61 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0840 vs market 0.1108 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=76, bias $-0.49, sd $1.82 (set BASIS_SD near 2)
- spot at open: n=76, bias $-2.23, sd $36.42 (set BASIS_SD near 36)

## Is the win chance honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 60 | 35 | 55% | 60% |
| 60%-70% | 56 | 39 | 64% | 68% |
| 70%-80% | 60 | 39 | 74% | 77% |
| 80%-90% | 102 | 52 | 87% | 95% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 28 | 109 | 0.1484 | 0.1719 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 76 (28 with decision logging, v16+)
- Markets with a signal: 5
- Alerts attempted: 0 · delivered: 0 · delivery failed: 0
- Simulated fills (quote available, size not verified): 0
- Expired alerts: 0 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 2 markets, would have won 1, +1.45 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 3 markets, would have won 3, +15.59 at 10 shares. Negative = the filter saved money.
- Liquidity: the venue's quote has not reported ask size yet; fills stay 'simulated'.

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 33 · valid comparisons: 33
- Missing/untrusted: 0 sampling gaps (>6s hole or <20 samples), 0 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $+1.31, typical gap $3.04, worst $12.31
- Coinbase would have named the wrong winner: 0/33 (0.0%)
- Rounds settling within $10 of the target: 1, wrong winner 0 (0%)
- Rounds settling within $25 of the target: 4, wrong winner 0 (0%)
- Rounds settling within $50 of the target: 5, wrong winner 0 (0%)

## Honest scoreboard (tickets)

No settled tickets yet.

## Ticket speed

No v10 tickets yet.

## Loop health (are our timings trustworthy?)

- Runs: 3 · loops: 4949 · loops over 5s: 0 (0.00%)
- Worst single loop: 3.4s · longest gap between BTC prices: 5.4s
- No stalls recorded.
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
