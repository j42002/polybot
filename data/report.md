# polybot report

Updated 2026-11-25 11:09 UTC | 60 checkpoints logged | 48 graded | 11 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven hit rate = avg price paid.

## 4:00 left (8 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 8 | 62.5% | 60.4% | +0.010 | -0.378 to +0.398 | $+0.81 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 8 | 37.5% | 61.9% | -0.255 | -0.602 to +0.092 | $-20.39 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 1 | 100.0% | 56.0% | +0.428 | -inf to +inf | $+4.28 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 56.0% | +0.428 | -inf to +inf | $+4.28 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.2793 vs market 0.2759 -> **market is sharper**

## 3:30 left (9 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 9 | 77.8% | 54.8% | +0.219 | -0.064 to +0.503 | $+19.73 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 9 | 77.8% | 66.9% | +0.098 | -0.223 to +0.419 | $+8.84 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 2 | 100.0% | 58.0% | +0.408 | +0.272 to +0.544 | $+8.16 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 1 | 100.0% | 65.0% | +0.339 | -inf to +inf | $+3.39 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.2192 vs market 0.2236 -> **model is sharper**

## 3:00 left (11 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 11 | 72.7% | 67.3% | +0.046 | -0.203 to +0.295 | $+5.03 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 11 | 72.7% | 75.1% | -0.032 | -0.285 to +0.220 | $-3.57 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 2 | 50.0% | 49.5% | -0.003 | -0.385 to +0.379 | $-0.06 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1707 vs market 0.1664 -> **market is sharper**

## 2:00 left (11 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 11 | 36.4% | 66.4% | -0.307 | -0.503 to -0.112 | $-33.80 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 11 | 81.8% | 78.8% | +0.023 | -0.241 to +0.287 | $+2.51 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 3 | 33.3% | 62.7% | -0.303 | -1.053 to +0.447 | $-9.09 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1904 vs market 0.1847 -> **market is sharper**

## 1:00 left (9 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 6 | 100.0% | 72.3% | +0.270 | +0.051 to +0.488 | $+16.19 | INCONCLUSIVE (need 300+) |
| Lean (bet the side BTC is on now) | 6 | 66.7% | 79.3% | -0.133 | -0.449 to +0.183 | $-8.01 | INCONCLUSIVE (need 300+) |
| Edge (model beats the ask by 3c+) | 3 | 33.3% | 26.7% | +0.059 | -0.633 to +0.750 | $+1.76 | INCONCLUSIVE (need 300+) |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1161 vs market 0.1078 -> **market is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=11, bias $-3.20, sd $3.72 (set BASIS_SD near 4)
- spot at open: n=11, bias $-5.13, sd $26.86 (set BASIS_SD near 27)

_polybot grader v3_
