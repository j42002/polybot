# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T12:27:37Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 24/100 filled trades, 76 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 39 · **filled 24** (62% fill rate) · partial only 0 (not counted) · no signal 42 · no quote or data 7 · waiting 1
- Win rate **79.2%** vs break-even 70.9% (+8.3 points; needs +3)
- P&L after fees **+34.26** on 24 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +32.94
- Orders that never filled would have won 100% of 15. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

