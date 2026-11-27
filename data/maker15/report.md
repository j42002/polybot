# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-27T22:38:56Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 41/100 filled trades, 59 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 62 · **filled 41** (66% fill rate) · partial only 0 (not counted) · no signal 53 · no quote or data 14 · waiting 0
- Win rate **78.0%** vs break-even 73.2% (+4.8 points; needs +3)
- P&L after fees **+50.15** on 41 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +48.06
- Orders that never filled would have won 100% of 21. A big gap vs the filled win rate = fills come mostly when price runs against you.

