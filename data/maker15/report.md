# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T17:05:10Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 32/100 filled trades, 68 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 49 · **filled 32** (65% fill rate) · partial only 0 (not counted) · no signal 47 · no quote or data 11 · waiting 0
- Win rate **84.4%** vs break-even 72.8% (+11.6 points; needs +3)
- P&L after fees **+61.16** on 32 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +59.50
- Orders that never filled would have won 100% of 17. A big gap vs the filled win rate = fills come mostly when price runs against you.

