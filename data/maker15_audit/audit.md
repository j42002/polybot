# maker15 QC audit (read-only)

Generated 2026-11-27 20:12 UTC from data/maker15/orders.csv. Does not change maker15.py, its rules or its data. Requested in ChatGPT's QC review (PR #9).

## Integrity audit

- Orders re-checked: 53 · fetch errors: 0 · incomplete pagination: 0
- Duplicate trade IDs: 0 · wrong-ticker prints: 0 · block trades seen (excluded by the rule): 0 · unordered pages: 0
- **Fill status recomputed on deduplicated, complete trade lists: 53/53 match the recorded status**
- Marketable at post (a print below our limit in the 2 min before posting, so we might have been a taker): **7** · recorded ask more than 5c from the last print: 22
- Age of the last print before posting (s): median 0, max 0
- Series fee fields now: `{'fee_multiplier': 1, 'fee_type': 'quadratic'}`

Per-order detail: data/maker15_audit/audit.csv.

## Headline numbers (unfilled orders count as $0, never as earned)

- Orders posted **53** · filled **35** · unfilled 18 · span 2026-11-26 14:27 to 2026-11-27 18:27 UTC (2 calendar days, 8 four-hour blocks)
- **P&L per posted order: +0.99** (total +52.70 over 53 posted). 95% range by day blocks: not shown (needs 5+ blocks) · by 4-hour blocks: +0.09 to +2.01
- P&L per fill: +1.51 · if a 0.0175 maker fee applied: total +50.94
- Equal-weight: win 82.9% vs break-even 73.6% (+9.2 pts)
- **Contract-weighted: win 78.7% vs break-even 68.1% (+10.7 pts)** over 494 contracts
- Worst single loss -9.90 · max drawdown -27.39

## Adverse selection (fill rate depends on the outcome)

- Signal right on 47/53 posted orders (89%).
- **Fill rate when our side WON: 29/47 (62%) · when it LOST: 6/6 (100%)**
- A resting buy fills when the price falls through it. Losers always fall, so they always fill; many winners never come back down.

## Same orders, as taker buys at the ask (counterfactual, 0.07 quadratic taker fee)

- Taker P&L on the same 53 posted signals: **+74.82** (+1.41 per order) vs maker +52.70
- Shows whether the cheaper price or the signal itself is doing the work. Exploratory, not part of the frozen rule.

## Splits (exploratory; small cells)

| Split | posted | filled | win of fills | P&L | P&L / posted |
|---|---|---|---|---|---|
| ask under 60c | 10 | 8 | 62% | +28.97 | +2.90 |
| ask 60-85c | 15 | 12 | 75% | +9.03 | +0.60 |
| ask 85c+ | 28 | 15 | 100% | +14.70 | +0.53 |
| 00-08 ET | 16 | 8 | 88% | +7.18 | +0.45 |
| 08-16 ET | 25 | 16 | 88% | +36.43 | +1.46 |
| 16-24 ET | 12 | 11 | 73% | +9.09 | +0.76 |
| day 2026-11-26 | 17 | 11 | 82% | +28.34 | +1.67 |
| day 2026-11-27 | 36 | 24 | 83% | +24.36 | +0.68 |

Small cells: these splits describe the sample, they are not findings. Nothing here changes the frozen rule.
