---
polybot_auto: true
updated: 2026-11-27 21:47 UTC
tags: [results, experiment/maker15, audit]
---
# 🔍 Maker Test QC Audit

# maker15 QC audit (read-only)

Generated 2026-11-27 20:47 UTC from data/maker15/orders.csv. Does not change maker15.py, its rules or its data. Requested in ChatGPT's QC review (PR #9).

## Integrity audit

- Orders re-checked: 55 · fetch errors: 0 · incomplete pagination: 0
- Duplicate trade IDs: 0 · wrong-ticker prints: 0 · block trades seen (excluded by the rule): 0 · unordered pages: 0
- **Fill status recomputed on deduplicated, complete trade lists: 55/55 match the recorded status**
- Marketable at post (a print below our limit in the 2 min before posting, so we might have been a taker): **7** · recorded ask more than 5c from the last print: 22
- Age of the last print before posting (s): median 0, max 0
- Series fee fields now: `{'fee_multiplier': 1, 'fee_type': 'quadratic'}`

### Quote staleness (discovered issue: design faithfulness, not fill correctness)

- The ask maker15 records comes from the `/markets` list. On 22/55 orders it was more than 5c from trades printing in the same second, so the posted limit was often not really 'ask minus 2c'. Fill grading stays valid for the limit actually posted (53/53 recomputed), but the test is not cleanly testing its stated rule.
- Maker P&L on clean-quote orders: +32.07 (32 orders) · on flagged-quote orders: +11.13 (23)
- Marketable-at-post orders would really have executed at once as takers: a taker fee at the limit would cost 1.44 in total (and the price could only have been better). Not material to P&L.
- **Taker counterfactual at the last real print** (instead of the stale ask): +35.73 on 55 orders vs maker P&L in the headline below. The stale-ask taker line further down is kept for transparency but is not reliable.
- Proposed fix (needs Jacob's approval, would start a separately labelled cohort): read the ask from the order book at post time. Not applied: the running cohort stays frozen.

Per-order detail: data/maker15_audit/audit.csv.

## Headline numbers (unfilled orders count as $0, never as earned)

- Orders posted **55** · filled **36** · unfilled 19 · span 2026-11-26 14:27 to 2026-11-27 20:42 UTC (2 calendar days, 9 four-hour blocks)
- **P&L per posted order: +0.79** (total +43.20 over 55 posted). 95% range by day blocks: not shown (needs 5+ blocks) · by 4-hour blocks: -0.21 to +1.78
- P&L per fill: +1.20 · if a 0.0175 maker fee applied: total +41.43
- Equal-weight: win 80.6% vs break-even 74.2% (+6.3 pts)
- **Contract-weighted: win 77.2% vs break-even 68.6% (+8.6 pts)** over 504 contracts
- Worst single loss -9.90 · max drawdown -27.39

## Adverse selection (fill rate depends on the outcome)

- Signal right on 48/55 posted orders (87%).
- **Fill rate when our side WON: 29/48 (60%) · when it LOST: 7/7 (100%)**
- A resting buy fills when the price falls through it. Losers always fall, so they always fill; many winners never come back down.

## Same orders, as taker buys at the RECORDED ask (unreliable: that ask is often stale, see the audit above)

- Taker P&L on the same 55 posted signals: **+65.19** (+1.19 per order) vs maker +43.20
- Shows whether the cheaper price or the signal itself is doing the work. Exploratory, not part of the frozen rule.

## Splits (exploratory; small cells)

| Split | posted | filled | win of fills | P&L | P&L / posted |
|---|---|---|---|---|---|
| ask under 60c | 10 | 8 | 62% | +28.97 | +2.90 |
| ask 60-85c | 15 | 12 | 75% | +9.03 | +0.60 |
| ask 85c+ | 30 | 16 | 94% | +5.20 | +0.17 |
| 00-08 ET | 16 | 8 | 88% | +7.18 | +0.45 |
| 08-16 ET | 27 | 17 | 82% | +26.93 | +1.00 |
| 16-24 ET | 12 | 11 | 73% | +9.09 | +0.76 |
| day 2026-11-26 | 17 | 11 | 82% | +28.34 | +1.67 |
| day 2026-11-27 | 38 | 25 | 80% | +14.86 | +0.39 |

Small cells: these splits describe the sample, they are not findings. Nothing here changes the frozen rule.

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
