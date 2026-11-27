# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T00:25:27Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 12/100 filled trades, 88 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 18 · **filled 12** (67% fill rate) · partial only 0 (not counted) · no signal 19 · no quote or data 3 · waiting 0
- Win rate **83.3%** vs break-even 69.8% (+13.5 points; needs +3)
- P&L after fees **+29.88** on 12 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +29.20
- Orders that never filled would have won 100% of 6. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

