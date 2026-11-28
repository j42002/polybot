# maker15 QC audit (read-only)

Generated 2026-11-28 19:01 UTC from data/maker15/orders.csv. Does not change maker15.py, its rules or its data. Requested in ChatGPT's QC review (PR #9).

## Integrity audit

- Orders re-checked: 98 · fetch errors: 0 · incomplete pagination: 0
- Duplicate trade IDs: 0 · wrong-ticker prints: 0 · block trades seen (excluded by the rule): 0 · unordered pages: 0
- **Fill status recomputed on deduplicated, complete trade lists: 98/98 match the recorded status**
- Marketable at post (a print below our limit in the 2 min before posting, so we might have been a taker): **14** · recorded ask more than 5c from the last print: 36
- Age of the last print before posting (s): median 0, max 0
- Series fee fields now: `{'fee_multiplier': 1, 'fee_type': 'quadratic'}`

### Quote staleness (discovered issue: design faithfulness, not fill correctness)

- The ask maker15 records comes from the `/markets` list. On 36/98 orders it was more than 5c from trades printing in the same second, so the posted limit was often not really 'ask minus 2c'. Fill grading stays valid for the limit actually posted (53/53 recomputed), but the test is not cleanly testing its stated rule.
- Maker P&L on clean-quote orders: +22.80 (60 orders) · on flagged-quote orders: -2.65 (38)
- Marketable-at-post orders would really have executed at once as takers: a taker fee at the limit would cost 2.50 in total (and the price could only have been better). Not material to P&L.
- **Taker counterfactual at the last real print** (instead of the stale ask): -1.09 on 98 orders vs maker P&L in the headline below. The stale-ask taker line further down is kept for transparency but is not reliable.
- Proposed fix (needs Jacob's approval, would start a separately labelled cohort): read the ask from the order book at post time. Not applied: the running cohort stays frozen.

Per-order detail: data/maker15_audit/audit.csv.

## Headline numbers (unfilled orders count as $0, never as earned)

- Orders posted **98** · filled **65** · unfilled 33 · span 2026-11-26 14:27 to 2026-11-28 18:27 UTC (3 calendar days, 14 four-hour blocks)
- **P&L per posted order: +0.21** (total +20.15 over 98 posted). 95% range by day blocks: not shown (needs 5+ blocks) · by 4-hour blocks: -0.62 to +1.10
- P&L per fill: +0.31 · if a 0.0175 maker fee applied: total +17.00
- Equal-weight: win 75.4% vs break-even 74.4% (+1.0 pts)
- **Contract-weighted: win 70.4% vs break-even 68.2% (+2.2 pts)** over 915 contracts
- Worst single loss -9.96 · max drawdown -54.21

## Adverse selection (fill rate depends on the outcome)

- Signal right on 82/98 posted orders (84%).
- **Fill rate when our side WON: 49/82 (60%) · when it LOST: 16/16 (100%)**
- A resting buy fills when the price falls through it. Losers always fall, so they always fill; many winners never come back down.

## Same orders, as taker buys at the RECORDED ask (unreliable: that ask is often stale, see the audit above)

- Taker P&L on the same 98 posted signals: **+47.23** (+0.48 per order) vs maker +20.15
- Shows whether the cheaper price or the signal itself is doing the work. Exploratory, not part of the frozen rule.

## Splits (exploratory; small cells)

| Split | posted | filled | win of fills | P&L | P&L / posted |
|---|---|---|---|---|---|
| ask under 60c | 17 | 14 | 43% | +4.63 | +0.27 |
| ask 60-85c | 25 | 21 | 71% | +8.95 | +0.36 |
| ask 85c+ | 56 | 30 | 93% | +6.57 | +0.12 |
| 00-08 ET | 30 | 17 | 76% | -12.24 | -0.41 |
| 08-16 ET | 37 | 25 | 80% | +28.91 | +0.78 |
| 16-24 ET | 31 | 23 | 70% | +3.48 | +0.11 |
| day 2026-11-26 | 17 | 11 | 82% | +28.34 | +1.67 |
| day 2026-11-27 | 48 | 32 | 72% | +1.95 | +0.04 |
| day 2026-11-28 | 33 | 22 | 77% | -10.14 | -0.31 |

Small cells: these splits describe the sample, they are not findings. Nothing here changes the frozen rule.
