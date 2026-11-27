# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T21:42:50Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 39/100 filled trades, 61 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 58 · **filled 39** (67% fill rate) · partial only 0 (not counted) · no signal 53 · no quote or data 14 · waiting 1
- Win rate **79.5%** vs break-even 74.5% (+4.9 points; needs +3)
- P&L after fees **+35.91** on 39 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +34.01
- Orders that never filled would have won 100% of 19. A big gap vs the filled win rate = fills come mostly when price runs against you.

