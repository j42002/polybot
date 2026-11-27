---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/development]
---
# 🔵 Mirror

> [!abstract] 🔵 development · self-test passed · definitions done; live cross-venue prices not collected yet
> Venue fees and settlement definitions compared

## Latest findings
| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |
|---|---|---|
| Taker fee | round-up of 0.07 x C x P x (1-P) | 0.095 x P x (1-P) per share |
| Maker fee | only on listed series (0.0175); this series reads 'quadratic' (none) | not modelled (taker-only tests) |
| Settlement | BRTI 60s average | BRTI 60s average |
| Settlement agreement (Phase 1) | 696/696 windows identical | |
Matched events on two venues are the same event, not independent evidence.
Pending: a live price comparison needs a Polymarket US 15m quote at each maker post time (not collected).

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
