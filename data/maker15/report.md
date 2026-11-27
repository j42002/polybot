# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T07:50:03Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 18/100 filled trades, 82 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 28 · **filled 18** (64% fill rate) · partial only 0 (not counted) · no signal 35 · no quote or data 7 · waiting 0
- Win rate **77.8%** vs break-even 68.9% (+8.8 points; needs +3)
- P&L after fees **+30.68** on 18 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +29.63
- Orders that never filled would have won 100% of 10. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

