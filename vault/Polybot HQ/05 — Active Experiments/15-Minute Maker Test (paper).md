---
polybot_auto: true
updated: 2026-11-28 10:42 UTC
tags: [experiment, experiment/maker15, status/running]
---
# 🪤 15-Minute Maker (limit-order) Test

> [!warning] Running · paper only · rules frozen (data/maker15/PREREG.md)
> PENDING. 54/100 filled trades, 46 to go. The 100-fill verdict is a **screening** rule, not proof.

## What it tests
A resting buy limit 2c below the ask on the 12-minute AGREE side (Kalshi BTC 15m). Fills only when later public trades print strictly through the limit for the full size.

## Known caveats (QC review, PR #9)
- **Adverse selection:** losing orders always fill; many winners never do. Unfilled hypothetical wins are not earned P&L.
- Same signal as the refuted 12-minute rule (2,022 historical trades, negative). Compare live results with the taker counterfactual in the audit.
- Few independent days so far.

## Latest report
# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T10:42:02Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 54/100 filled trades, 46 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 83 · **filled 54** (65% fill rate) · partial only 0 (not counted) · no signal 78 · no quote or data 16 · waiting 0
- Win rate **75.9%** vs break-even 74.6% (+1.3 points; needs +3)
- P&L after fees **+25.79** on 54 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +23.16
- Orders that never filled would have won 100% of 29. A big gap vs the filled win rate = fills come mostly when price runs against you.



Audit: [[Maker Test QC Audit]] · Merged via PR #9 (2026-11-26).

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
