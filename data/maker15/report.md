# Maker (limit-order) paper test, Kalshi BTC 15m

Generated 2026-11-26T17:01:09Z. Paper only, never trades. Rules frozen in data/maker15/PREREG.md.

**Verdict: PENDING. 4/100 filled trades, 96 to go.**

Rule: post a buy limit 2c below the ask on the 12-minute AGREE side; it fills only if later trades print strictly through the limit with enough volume to cover the whole order; unfilled orders cancel at the close.

## Live forward test (judged)

- Orders posted 6 · **filled 4** (67% fill rate) · partial only 0 (not counted) · no signal 5 · no quote or data 0 · waiting 0
- Win rate **75.0%** vs break-even 63.0% (+12.0 points; needs +3)
- P&L after fees **+9.89** on 4 fills of $10 (maker fee as published for this series: quadratic). If a 0.0175 maker fee applied: +9.62
- Orders that never filled would have won 100% of 2. A big gap vs the filled win rate = fills come mostly when price runs against you.
- Sample too small to mean anything yet.

