# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-26T21:38:31Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 7/100 filled trades, 93 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 13 · **filled 7** (54% fill rate) · partial only 0 (not counted) · no signal 15 · no quote or data 1 · waiting 0
- Win rate **85.7%** vs break-even 68.9% (+16.9 points; needs +3)
- P&L after fees **+21.59** on 7 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +21.18
- Orders that never filled would have won 100% of 6. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

