# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-26T23:29:31Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 8/100 filled trades, 92 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 14 · **filled 8** (57% fill rate) · partial only 0 (not counted) · no signal 19 · no quote or data 3 · waiting 1
- Win rate **87.5%** vs break-even 71.6% (+15.9 points; needs +3)
- P&L after fees **+22.49** on 8 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +22.06
- Orders that never filled would have won 100% of 6. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

