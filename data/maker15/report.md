# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T19:51:31Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 35/100 filled trades, 65 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 53 · **filled 35** (66% fill rate) · partial only 0 (not counted) · no signal 51 · no quote or data 14 · waiting 0
- Win rate **82.9%** vs break-even 73.6% (+9.2 points; needs +3)
- P&L after fees **+52.70** on 35 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +50.94
- Orders that never filled would have won 100% of 18. A big gap vs the filled win rate = fills come mostly when price runs against you.

