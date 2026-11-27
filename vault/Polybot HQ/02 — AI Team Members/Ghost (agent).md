---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/implemented]
---
# 🟢 Ghost

> [!abstract] 🟢 implemented · self-test passed
> Anomalies and missing data in public feeds
> Folded in: Market Stability Monitor (data)

## Latest findings
5m checks with no market quote: 84/3031 (2.8%)
Up+Down asks outside 0.95-1.15 (broken or stale book): 0/2688
Coinbase proxy disagrees with the official settlement: 16/605 rounds (proxy only; official winner is used for scoring)
Runs whose longest BTC price gap exceeded 10s: 3/58
Maker: stale recorded quotes 22/55 (see Titan)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
