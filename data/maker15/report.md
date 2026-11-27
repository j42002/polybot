# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T18:00:38Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 33/100 filled trades, 67 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 50 · **filled 33** (66% fill rate) · partial only 0 (not counted) · no signal 48 · no quote or data 12 · waiting 1
- Win rate **81.8%** vs break-even 72.4% (+9.4 points; needs +3)
- P&L after fees **+51.40** on 33 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +49.67
- Orders that never filled would have won 100% of 17. A big gap vs the filled win rate = fills come mostly when price runs against you.

