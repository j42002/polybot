# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T11:32:07Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 23/100 filled trades, 77 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 37 · **filled 23** (62% fill rate) · partial only 0 (not counted) · no signal 41 · no quote or data 7 · waiting 0
- Win rate **78.3%** vs break-even 71.4% (+6.8 points; needs +3)
- P&L after fees **+27.12** on 23 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +25.88
- Orders that never filled would have won 100% of 14. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

