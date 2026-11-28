# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T01:26:03Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 43/100 filled trades, 57 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 66 · **filled 43** (65% fill rate) · partial only 0 (not counted) · no signal 60 · no quote or data 14 · waiting 0
- Win rate **74.4%** vs break-even 73.0% (+1.4 points; needs +3)
- P&L after fees **+30.29** on 43 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +28.09
- Orders that never filled would have won 100% of 23. A big gap vs the filled win rate = fills come mostly when price runs against you.

