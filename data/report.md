# polybot report

Updated 2026-11-28 11:13 UTC | 4087 checkpoints logged | 3893 graded | 825 windows settled

PAPER ONLY. P&L is per $1 share after the taker fee; Total assumes 10 shares per bet. Breakeven = win rate needed after the fee (price + fee).

## Research report: experiment v18+ only

Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 777 settled rounds observed · 132 alerts (129 delivered) · **30 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 21/761 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1610 vs market 0.1659 on 777 rounds -> model sharper
3. **Simulated profit after fees:** -6.29 on 30 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -4.19 to +3.77
4. **Quote available at simulated tap (size not verified):** 5s 44/129 · 10s 42/129 · 20s 35/129 · 30s 30/129
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 73 runs, stalls over 5s 13/120414 loops, longest BTC price gap 21.8s · checks with no market quote 98/3815 (book fallback used 1559) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 30/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 30/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 81/128 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 30 tickets at every delay (right 15/30): 5s -12.55 · 10s -14.48 · 20s -9.39 · 30s -6.29. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

# Detail and history (ALL versions, mixed models; for context, not evidence)

## 4:00 left (763 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 761 | 66.0% | 64.5% | +0.014 | -0.019 to +0.047 | $+110.24 | NO EDGE |
| Lean (bet the side BTC is on now) | 763 | 66.3% | 67.0% | -0.007 | -0.040 to +0.027 | $-49.80 | NO EDGE |
| Edge (model beats the ask by 3c+) | 383 | 50.9% | 42.6% | +0.083 | +0.037 to +0.129 | $+317.48 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 181 | 65.7% | 52.3% | +0.135 | +0.064 to +0.205 | $+243.46 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.2093 vs market 0.2173 -> **model is sharper**

## 3:30 left (777 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 774 | 66.4% | 63.5% | +0.029 | -0.002 to +0.060 | $+224.68 | NO EDGE |
| Lean (bet the side BTC is on now) | 777 | 69.9% | 71.1% | -0.012 | -0.044 to +0.019 | $-95.63 | NO EDGE |
| Edge (model beats the ask by 3c+) | 438 | 38.8% | 35.3% | +0.035 | -0.006 to +0.076 | $+152.34 | NO EDGE |
| JJ (60-90s in, 35-70c ask, model +4c) | 90 | 56.7% | 52.6% | +0.041 | -0.059 to +0.140 | $+36.71 | INCONCLUSIVE (need 300+) |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.1965 vs market 0.1984 -> **model is sharper**

## 3:00 left (784 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 783 | 65.4% | 62.0% | +0.034 | +0.005 to +0.063 | $+267.73 | PASSES |
| Lean (bet the side BTC is on now) | 783 | 75.1% | 74.2% | +0.009 | -0.020 to +0.038 | $+69.87 | NO EDGE |
| Edge (model beats the ask by 3c+) | 480 | 36.5% | 31.3% | +0.052 | +0.016 to +0.088 | $+248.20 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 44 | 88.6% | 71.9% | +0.168 | +0.070 to +0.265 | $+73.76 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1712 vs market 0.1771 -> **model is sharper**

## 2:00 left (789 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 749 | 61.3% | 59.0% | +0.023 | -0.003 to +0.049 | $+173.56 | NO EDGE |
| Lean (bet the side BTC is on now) | 735 | 82.7% | 79.8% | +0.030 | +0.003 to +0.056 | $+217.28 | PASSES |
| Edge (model beats the ask by 3c+) | 588 | 24.7% | 21.9% | +0.028 | +0.001 to +0.055 | $+162.71 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 27 | 92.6% | 74.1% | +0.185 | +0.086 to +0.285 | $+50.04 | INCONCLUSIVE (need 300+) |

Brier (lower is better): model 0.1283 vs market 0.1294 -> **model is sharper**

## 1:00 left (780 windows)

| Strategy | Bets | Hit | Breakeven | Per bet | 95% CI | Total | Verdict |
|---|---|---|---|---|---|---|---|
| Momentum (bet the last-60s direction) | 581 | 50.4% | 48.6% | +0.019 | -0.008 to +0.045 | $+108.88 | NO EDGE |
| Lean (bet the side BTC is on now) | 496 | 85.5% | 81.9% | +0.036 | +0.005 to +0.067 | $+179.34 | PASSES |
| Edge (model beats the ask by 3c+) | 690 | 15.9% | 12.3% | +0.037 | +0.016 to +0.057 | $+253.72 | PASSES |
| JJ (60-90s in, 35-70c ask, model +4c) | 0 | - | - | - | - | - | no bets |
| SAFE (model 75%+, 55-85c ask, +4c, 3:00/2:00 left) | 0 | - | - | - | - | - | no bets |

Brier (lower is better): model 0.0880 vs market 0.0980 -> **model is sharper**

## Price-to-beat proxy (Coinbase vs real Chainlink)

- 60s average: n=825, bias $-0.05, sd $0.57 (set BASIS_SD near 1)
- spot at open: n=825, bias $-3.96, sd $22.47 (set BASIS_SD near 22)

## Is the model estimate honest? (calibration)

| Bot said | Checks | Separate markets | Said (avg) | Actually won |
|---|---|---|---|---|
| 50%-60% | 947 | 492 | 55% | 57% |
| 60%-70% | 890 | 537 | 65% | 69% |
| 70%-80% | 729 | 481 | 75% | 80% |
| 80%-90% | 1316 | 584 | 87% | 96% |
| 90%-100% | 11 | 9 | 96% | 91% |

These are the live predictions as logged before each round settled, so they are out of sample.
Checks in one market move together: trust 'Separate markets', not 'Checks'.
If 'Actually won' sits well below 'Said', the model is overconfident.

## Model tuning

- **Model frozen for the experiment:** rw-m1.4-c0.88-b15. Automatic tuning is off; data/model_tune.json is neither written nor read.

## Forward test (untouched data)

| Model | Separate markets | Checks | Model Brier | Market Brier | Sharper |
|---|---|---|---|---|---|
| rw-m1.4-c0.88-b15 | 777 | 3713 | 0.161 | 0.1659 | model |
- Read only after 100+ separate markets per model. Brier: lower is better.

## Research dashboard (funnel)

- Markets observed and settled: 825 (777 with decision logging, v16+)
- Markets with a signal: 299
- Alerts attempted: 132 · delivered: 129 · delivery failed: 3
- Simulated fills (quote available, size not verified): 30
- Expired alerts: 99 · unconfirmed price checks: 0
- Missed opportunities (blocked by a filter; P&L at the signal price is hypothetical):
  - BELOW_BAR: 124 markets, would have won 84, +76.35 at 10 shares. Negative = the filter saved money.
  - EDGE_CAP: 62 markets, would have won 46, +127.57 at 10 shares. Negative = the filter saved money.
  - SKIP_SPIKE: 7 markets, would have won 5, +8.52 at 10 shares. Negative = the filter saved money.
- Liquidity (units UNVERIFIED, not used): 117/129 simulated taps showed ask size >= $10 worth

## Settlement check (Coinbase vs the real settlement price, v18+)

- Rounds with a logged close: 802 · valid comparisons: 761
- Missing/untrusted: 17 sampling gaps (>6s hole or <20 samples), 24 not settled yet, 0 without a published settlement price
- Coinbase minus settlement: bias $-2.97, typical gap $4.29, worst $20.80
- Coinbase would have named the wrong winner: 21/761 (2.8%)
- Rounds settling within $10 of the target: 113, wrong winner 20 (18%)
- Rounds settling within $25 of the target: 277, wrong winner 21 (8%)
- Rounds settling within $50 of the target: 444, wrong winner 21 (5%)

## Honest scoreboard (tickets)

- Independent settled markets with a ticket: 128 (goal: 300)
- Simulated paper trades: 30 · no-trade (expired/unconfirmed): 98
- 'Trade' = the best ask was within the limit at the simulated tap. Liquidity (size) is not verified,
  so this is simulated quote availability, not a proven fill.
- Win rate 15/30 = 50% vs break-even 49.8% (price paid + fee)
- Paper P&L after fees: -6.29 at $10 a trade · max drawdown: -60.71

## Ticket speed (measured, not assumed)

- Tickets: 132
- Coinbase trade -> we received it: median 896 ms (worst 6396)
- Coinbase request round trip: median 15 ms (worst 106)
- Polymarket quote round trip: median 27 ms (worst 142)
- Price read -> decision made: median 71 ms (worst 240)
- Decision -> Discord accepted: median 1547 ms (worst 10697)
- Time left on the timer when sent: median 237s
- Price checks ran late by: median 0.5s (over 3s = not trusted for a fill)

| Simulated tap after | Quote available | Expired | Unconfirmed | Paper P&L ($10 each) |
|---|---|---|---|---|
| 5s | 44/128 | 84 | 0 | +79.09 |
| 10s | 42/128 | 86 | 0 | +49.96 |
| 20s | 35/128 | 93 | 0 | +42.37 |
| 30s | 30/128 | 98 | 0 | -6.29 |
- Simulated quote availability, not verified fills: size at the ask is not known yet.
- Expired or unconfirmed = no trade.

## Loop health (are our timings trustworthy?)

- Runs: 73 · loops: 120414 · loops over 5s: 13 (0.01%)
- Worst single loop: 10.8s · longest gap between BTC prices: 21.8s
- Most common stall cause: spot
- A tick or price check during a stall is late; price checks over 3s late never count as a fill.

## Gemini second opinion

No graded tickets with a Gemini opinion yet.

## Legacy tickets (before v18: known measurement bugs, not evidence)

- 2 alerts, 1 counted as trades at the time, -10.54. Excluded from every number above.

_polybot grader v7_
