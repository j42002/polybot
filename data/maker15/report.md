# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T08:51:03Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 53/100 filled trades, 47 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 81 · **filled 53** (65% fill rate) · partial only 0 (not counted) · no signal 73 · no quote or data 16 · waiting 0
- Win rate **77.4%** vs break-even 74.6% (+2.8 points; needs +3)
- P&L after fees **+35.67** on 53 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +33.09
- Orders that never filled would have won 100% of 28. A big gap vs the filled win rate = fills come mostly when price runs against you.

