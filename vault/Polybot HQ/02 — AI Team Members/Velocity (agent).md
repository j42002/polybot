---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [agents, agents/implemented]
---
# 🟢 Velocity

> [!abstract] 🟢 implemented · self-test passed
> Latency, quote lifetime, 30s deadline consistency
> Folded in: Expiration Guard

## Latest findings
Delivered alerts watched: 121 · first price-crossing slot: 5s 81, 10s 2, 20s 5, 30s 5, 45s 4, 60s 4, none 20
Crossed only after the 30s deadline (45/60s): 8 · of those scored EXPIRED at 30s despite a 30s ask under the cap: **0** (must be 0)
30s check lateness: worst +0.90s (trusted up to +3s) · rows with no 30s check: 0
Discord delivery: median 648 ms, worst 2244 ms
Picks right 75/120 · same 27 tickets at every delay: 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35 · dropouts 5s→30s: 12 (right 9)
v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.
v21 (Nov 28): wording only: 'model estimate' instead of 'win chance', no buy-now language, paper window close time on the card.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
