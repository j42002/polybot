# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-26T16:05:37Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 2/100 filled trades, 98 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 4 · **filled 2** (50% fill rate) · partial only 0 (not counted) · no signal 3 · no quote or data 0 · waiting 0
- Win rate **100.0%** vs break-even 61.5% (+38.5 points; needs +3)
- P&L after fees **+17.01** on 2 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +16.87
- Orders that never filled would have won 100% of 2. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

