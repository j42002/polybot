# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T15:19:37Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 61/100 filled trades, 39 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 92 · **filled 61** (66% fill rate) · partial only 0 (not counted) · no signal 87 · no quote or data 17 · waiting 0
- Win rate **75.4%** vs break-even 75.3% (+0.1 points; needs +3)
- P&L after fees **+14.19** on 61 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +11.31
- Orders that never filled would have won 100% of 31. A big gap vs the filled win rate = fills come mostly when price runs against you.

