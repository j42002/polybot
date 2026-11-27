# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T01:21:07Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 13/100 filled trades, 87 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 19 · **filled 13** (68% fill rate) · partial only 0 (not counted) · no signal 22 · no quote or data 3 · waiting 0
- Win rate **76.9%** vs break-even 68.4% (+8.5 points; needs +3)
- P&L after fees **+20.19** on 13 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +19.42
- Orders that never filled would have won 100% of 6. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

