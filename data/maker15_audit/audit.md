# maker15 QC audit (read-only)

Generated 2026-11-28 01:26 UTC from data/maker15/orders.csv. Does not change maker15.py, its rules or its data. Requested in ChatGPT's QC review (PR #9).

## Integrity audit

- Orders re-checked: 66 · fetch errors: 0 · incomplete pagination: 0
- Duplicate trade IDs: 0 · wrong-ticker prints: 0 · block trades seen (excluded by the rule): 0 · unordered pages: 0
- **Fill status recomputed on deduplicated, complete trade lists: 66/66 match the recorded status**
- Marketable at post (a print below our limit in the 2 min before posting, so we might have been a taker): **8** · recorded ask more than 5c from the last print: 27
- Age of the last print before posting (s): median 0, max 0
- Series fee fields now: `{'fee_multiplier': 1, 'fee_type': 'quadratic'}`

### Quote staleness (discovered issue: design faithfulness, not fill correctness)

- The ask maker15 records comes from the `/markets` list. On 27/66 orders it was more than 5c from trades printing in the same second, so the posted limit was often not really 'ask minus 2c'. Fill grading stays valid for the limit actually posted (53/53 recomputed), but the test is not cleanly testing its stated rule.
- Maker P&L on clean-quote orders: +14.44 (38 orders) · on flagged-quote orders: +15.85 (28)
- Marketable-at-post orders would really have executed at once as takers: a taker fee at the limit would cost 1.74 in total (and the price could only have been better). Not material to P&L.
- **Taker counterfactual at the last real print** (instead of the stale ask): +14.64 on 66 orders vs maker P&L in the headline below. The stale-ask taker line further down is kept for transparency but is not reliable.
- Proposed fix (needs Jacob's approval, would start a separately labelled cohort): read the ask from the order book at post time. Not applied: the running cohort stays frozen.

Per-order detail: data/maker15_audit/audit.csv.

## Headline numbers (unfilled orders count as $0, never as earned)

- Orders posted **66** · filled **43** · unfilled 23 · span 2026-11-26 14:27 to 2026-11-28 00:57 UTC (3 calendar days, 10 four-hour blocks)
- **P&L per posted order: +0.46** (total +30.29 over 66 posted). 95% range by day blocks: not shown (needs 5+ blocks) · by 4-hour blocks: -0.61 to +1.66
- P&L per fill: +0.70 · if a 0.0175 maker fee applied: total +28.09
- Equal-weight: win 74.4% vs break-even 73.0% (+1.4 pts)
- **Contract-weighted: win 71.5% vs break-even 66.6% (+4.9 pts)** over 621 contracts
- Worst single loss -9.96 · max drawdown -30.87

## Adverse selection (fill rate depends on the outcome)

- Signal right on 55/66 posted orders (83%).
- **Fill rate when our side WON: 32/55 (58%) · when it LOST: 11/11 (100%)**
- A resting buy fills when the price falls through it. Losers always fall, so they always fill; many winners never come back down.

## Same orders, as taker buys at the RECORDED ask (unreliable: that ask is often stale, see the audit above)

- Taker P&L on the same 66 posted signals: **+58.73** (+0.89 per order) vs maker +30.29
- Shows whether the cheaper price or the signal itself is doing the work. Exploratory, not part of the frozen rule.

## Splits (exploratory; small cells)

| Split | posted | filled | win of fills | P&L | P&L / posted |
|---|---|---|---|---|---|
| ask under 60c | 14 | 11 | 55% | +33.69 | +2.41 |
| ask 60-85c | 17 | 13 | 69% | -0.87 | -0.05 |
| ask 85c+ | 35 | 19 | 89% | -2.53 | -0.07 |
| 00-08 ET | 16 | 8 | 88% | +7.18 | +0.45 |
| 08-16 ET | 28 | 18 | 78% | +17.41 | +0.62 |
| 16-24 ET | 22 | 17 | 65% | +5.70 | +0.26 |
| day 2026-11-26 | 17 | 11 | 82% | +28.34 | +1.67 |
| day 2026-11-27 | 48 | 32 | 72% | +1.95 | +0.04 |
| day 2026-11-28 | 1 | 0 | - | +0.00 | +0.00 |

Small cells: these splits describe the sample, they are not findings. Nothing here changes the frozen rule.
