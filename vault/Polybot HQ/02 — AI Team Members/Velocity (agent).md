---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Velocity

> [!abstract] 🟢 implemented · self-test passed
> Latency, quote lifetime, 30s deadline consistency
> Folded in: Expiration Guard

## Latest findings
Delivered alerts watched: 103 · first price-crossing slot: 5s 69, 10s 2, 20s 5, 30s 3, 45s 3, 60s 4, none 17
Crossed only after the 30s deadline (45/60s): 7 · of those scored EXPIRED at 30s despite a 30s ask under the cap: **0** (must be 0)
30s check lateness: worst +0.90s (trusted up to +3s) · rows with no 30s check: 0
Discord delivery: median 661 ms, worst 2244 ms
Picks right 63/103 · same 24 tickets at every delay: 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65 · dropouts 5s→30s: 10 (right 7)
v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.
v21 (Nov 28): wording only: 'model estimate' instead of 'win chance', no buy-now language, paper window close time on the card.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
