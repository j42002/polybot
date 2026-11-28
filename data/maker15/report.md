# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T05:08:53Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 49/100 filled trades, 51 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 75 · **filled 49** (65% fill rate) · partial only 0 (not counted) · no signal 64 · no quote or data 16 · waiting 0
- Win rate **75.5%** vs break-even 73.7% (+1.8 points; needs +3)
- P&L after fees **+28.07** on 49 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +25.62
- Orders that never filled would have won 100% of 26. A big gap vs the filled win rate = fills come mostly when price runs against you.

