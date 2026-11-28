# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T11:37:34Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 55/100 filled trades, 45 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 84 · **filled 55** (65% fill rate) · partial only 0 (not counted) · no signal 81 · no quote or data 16 · waiting 0
- Win rate **74.5%** vs break-even 74.7% (-0.1 points; needs +3)
- P&L after fees **+16.55** on 55 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +13.88
- Orders that never filled would have won 100% of 29. A big gap vs the filled win rate = fills come mostly when price runs against you.

