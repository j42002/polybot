---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/implemented]
---
# 🟢 Velocity

> [!abstract] 🟢 implemented · self-test passed
> Latency, quote lifetime, 30s deadline consistency
> Folded in: Expiration Guard

## Latest findings
Delivered alerts watched: 95 · first price-crossing slot: 5s 66, 10s 2, 20s 4, 30s 3, 45s 2, 60s 3, none 15
Crossed only after the 30s deadline (45/60s): 5 · of those scored EXPIRED at 30s despite a 30s ask under the cap: **0** (must be 0)
30s check lateness: worst +0.90s (trusted up to +3s) · rows with no 30s check: 0
Discord delivery: median 684 ms, worst 2244 ms
Picks right 58/95 · same 20 tickets at every delay: 5s -44.85 · 10s -44.09 · 20s -43.39 · 30s -44.28 · dropouts 5s→30s: 9 (right 7)
v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
