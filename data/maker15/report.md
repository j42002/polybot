# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-28T18:06:11Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 64/100 filled trades, 36 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 97 · **filled 64** (66% fill rate) · partial only 0 (not counted) · no signal 92 · no quote or data 18 · waiting 0
- Win rate **75.0%** vs break-even 74.6% (+0.4 points; needs +3)
- P&L after fees **+13.91** on 64 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +10.83
- Orders that never filled would have won 100% of 33. A big gap vs the filled win rate = fills come mostly when price runs against you.

