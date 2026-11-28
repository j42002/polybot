---
polybot_auto: true
updated: 2026-11-28 02:24 UTC
tags: [experiment, experiment/maker15, status/running]
---
# 🪤 15-Minute Maker (limit-order) Test

> [!warning] Running · paper only · rules frozen (data/maker15/PREREG.md)
> PENDING. 44/100 filled trades, 56 to go. The 100-fill verdict is a **screening** rule, not proof.

## What it tests
A resting buy limit 2c below the ask on the 12-minute AGREE side (Kalshi BTC 15m). Fills only when later public trades print strictly through the limit for the full size.

## Known caveats (QC review, PR #9)
- **Adverse selection:** losing orders always fill; many winners never do. Unfilled hypothetical wins are not earned P&L.
- Same signal as the refuted 12-minute rule (2,022 historical trades, negative). Compare live results with the taker counterfactual in the audit.
- Few independent days so far.

## Latest report
# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T02:21:34Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 44/100 filled trades, 56 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 67 · **filled 44** (66% fill rate) · partial only 0 (not counted) · no signal 62 · no quote or data 15 · waiting 0
- Win rate **75.0%** vs break-even 73.6% (+1.4 points; needs +3)
- P&L after fees **+30.59** on 44 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +28.38
- Orders that never filled would have won 100% of 23. A big gap vs the filled win rate = fills come mostly when price runs against you.



Audit: [[Maker Test QC Audit]] · Merged via PR #9 (2026-11-26).

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
