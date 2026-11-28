# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T13:28:38Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 59/100 filled trades, 41 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 90 · **filled 59** (66% fill rate) · partial only 0 (not counted) · no signal 82 · no quote or data 17 · waiting 0
- Win rate **74.6%** vs break-even 75.1% (-0.5 points; needs +3)
- P&L after fees **+9.75** on 59 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +6.94
- Orders that never filled would have won 100% of 31. A big gap vs the filled win rate = fills come mostly when price runs against you.

