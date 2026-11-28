# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T09:46:36Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 54/100 filled trades, 46 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 82 · **filled 54** (66% fill rate) · partial only 0 (not counted) · no signal 76 · no quote or data 16 · waiting 0
- Win rate **75.9%** vs break-even 74.6% (+1.3 points; needs +3)
- P&L after fees **+25.79** on 54 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +23.16
- Orders that never filled would have won 100% of 28. A big gap vs the filled win rate = fills come mostly when price runs against you.

