# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T02:16:40Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 14/100 filled trades, 86 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 20 · **filled 14** (70% fill rate) · partial only 0 (not counted) · no signal 24 · no quote or data 4 · waiting 0
- Win rate **71.4%** vs break-even 69.4% (+2.1 points; needs +3)
- P&L after fees **+10.35** on 14 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +9.54
- Orders that never filled would have won 100% of 6. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

