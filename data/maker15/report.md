# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T15:14:03Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 29/100 filled trades, 71 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 45 · **filled 29** (64% fill rate) · partial only 0 (not counted) · no signal 45 · no quote or data 9 · waiting 1
- Win rate **82.8%** vs break-even 73.0% (+9.8 points; needs +3)
- P&L after fees **+45.61** on 29 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +44.12
- Orders that never filled would have won 100% of 16. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

