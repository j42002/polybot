---
polybot_auto: true
updated: 2026-11-28 00:53 UTC
tags: [agents, agents/development]
---
# 🔵 Mirror

> [!abstract] 🔵 development · self-test passed · definitions done; waiting for the first live same-moment price pairs
> Kalshi vs Polymarket US: fees, settlement and same-moment prices

## Latest findings
| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |
|---|---|---|
| Taker fee | round-up of 0.07 x C x P x (1-P) | 0.095 x P x (1-P) per share |
| Maker fee | only on listed series (0.0175); this series reads 'quadratic' (none) | not modelled (taker-only tests) |
| Settlement | BRTI 60s average | BRTI 60s average |
| Settlement agreement (Phase 1) | 696/696 windows identical | |
Matched events on two venues are the same event, not independent evidence.
Live comparison: no snapshots yet (collector runs alongside each maker15 run).

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
