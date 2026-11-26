---
polybot_auto: true
updated: 2026-11-26 01:27 UTC
tags: [communication, strategy]
---
# 💬 Issue 4 — Two-sided market making buy Up and Down for under $1 combined

> [!note] [#4 on GitHub](https://github.com/j42002/polybot/issues/4) · opened 2026-11-26 by github-actions[bot] · open

## Opening post (github-actions[bot], 2026-11-26 00:07 UTC)
### Submitted by

Claude (developer)

### Market

Polymarket BTC Up/Down 5m/15m

### The claim, in the source's own terms

Top 5-minute wallets rest orders on both sides and lock in the spread when Up + Down costs less than $1.

### Original sources

Public wallet histories on the Polymarket leaderboard (researched 2026-11-25).

### Exact rules (as testable as possible)

Post limit orders on both sides so the combined cost is under $1; profit = $1 minus the cost, if both fill.

### Supporting evidence

Observed in public top-wallet trade histories (L1).

### Weaknesses and red flags

Needs resting orders that actually fill (queue position, adverse selection: you get filled when the market moves against you). Speed and capital game.

### How could we paper-test it at $0?

Not honestly with top-of-book snapshots: a paper test can't know whether a resting order would have filled. Untestable at $0 for now.

_Seeded by the lab from existing work._

Strategy note: [[Issue 4 — Two-sided market making buy Up and Down for under $1 combined]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
