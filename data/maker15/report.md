# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T23:34:48Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 42/100 filled trades, 58 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 64 · **filled 42** (66% fill rate) · partial only 0 (not counted) · no signal 55 · no quote or data 14 · waiting 0
- Win rate **76.2%** vs break-even 73.5% (+2.7 points; needs +3)
- P&L after fees **+40.19** on 42 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +38.07
- Orders that never filled would have won 100% of 22. A big gap vs the filled win rate = fills come mostly when price runs against you.

