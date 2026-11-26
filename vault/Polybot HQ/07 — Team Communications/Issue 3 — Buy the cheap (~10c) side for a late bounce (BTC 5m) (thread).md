---
polybot_auto: true
updated: 2026-11-26 01:27 UTC
tags: [communication, strategy]
---
# 💬 Issue 3 — Buy the cheap (~10c) side for a late bounce (BTC 5m)

> [!note] [#3 on GitHub](https://github.com/j42002/polybot/issues/3) · opened 2026-11-26 by github-actions[bot] · open

## Opening post (github-actions[bot], 2026-11-26 00:07 UTC)
### Submitted by

Claude (developer)

### Market

Polymarket BTC Up/Down 5m

### The claim, in the source's own terms

Cheap longshot contracts pay 9-10x, so buying the ~10c side near the end catches enough reversals to profit.

### Original sources

Common claim in prediction-market social posts; no single original source verified.

### Exact rules (as testable as possible)

Buy the side priced ~10c in the final minutes; hold to settlement.

### Supporting evidence

Lab backtest (exploratory, early polybot data) found no edge: longshots won about as often as priced or less, before fees.

### Weaknesses and red flags

Longshot bias usually runs the other way (cheap contracts are over-priced). Exploratory result on early data only.

### How could we paper-test it at $0?

Could be re-run on Kalshi 15m history with the same machinery as backtest15.py if the team wants a cleaner test.

_Seeded by the lab from existing work._

Strategy note: [[Issue 3 — Buy the cheap (~10c) side for a late bounce (BTC 5m)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
