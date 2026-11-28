---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [agents, agents/implemented]
---
# 🟢 Ghost

> [!abstract] 🟢 implemented · self-test passed
> Anomalies and missing data in public feeds
> Folded in: Market Stability Monitor (data)

## Latest findings
5m checks with no market quote: 98/3654 (2.7%)
Up+Down asks outside 0.95-1.15 (broken or stale book): 0/3250
Coinbase proxy disagrees with the official settlement: 20/727 rounds (proxy only; official winner is used for scoring)
Runs whose longest BTC price gap exceeded 10s: 4/70
Maker: stale recorded quotes 28/70 (see Titan)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
