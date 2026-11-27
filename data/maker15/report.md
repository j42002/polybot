# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T20:47:07Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 36/100 filled trades, 64 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 55 · **filled 36** (65% fill rate) · partial only 0 (not counted) · no signal 53 · no quote or data 14 · waiting 0
- Win rate **80.6%** vs break-even 74.2% (+6.3 points; needs +3)
- P&L after fees **+43.20** on 36 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +41.43
- Orders that never filled would have won 100% of 19. A big gap vs the filled win rate = fills come mostly when price runs against you.

