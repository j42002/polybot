# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T02:21:34Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 44/100 filled trades, 56 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 67 · **filled 44** (66% fill rate) · partial only 0 (not counted) · no signal 62 · no quote or data 15 · waiting 0
- Win rate **75.0%** vs break-even 73.6% (+1.4 points; needs +3)
- P&L after fees **+30.59** on 44 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +28.38
- Orders that never filled would have won 100% of 23. A big gap vs the filled win rate = fills come mostly when price runs against you.

