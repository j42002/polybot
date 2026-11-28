# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T17:10:37Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 62/100 filled trades, 38 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 94 · **filled 62** (66% fill rate) · partial only 0 (not counted) · no signal 91 · no quote or data 18 · waiting 0
- Win rate **75.8%** vs break-even 75.0% (+0.8 points; needs +3)
- P&L after fees **+20.75** on 62 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +17.80
- Orders that never filled would have won 100% of 32. A big gap vs the filled win rate = fills come mostly when price runs against you.

