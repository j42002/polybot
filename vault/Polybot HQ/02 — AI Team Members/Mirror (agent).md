---
polybot_auto: true
updated: 2026-11-28 02:36 UTC
tags: [agents, agents/implemented]
---
# 🟢 Mirror

> [!abstract] 🟢 implemented · self-test passed
> Kalshi vs Polymarket US: fees, settlement and same-moment prices

## Latest findings
| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |
|---|---|---|
| Taker fee | round-up of 0.07 x C x P x (1-P) | feeCoefficient x P x (1-P) per share (5m bot assumes 0.095) |
| Maker fee | only on listed series (0.0175); this series reads 'quadratic' (none) | not modelled (taker-only tests) |
| Settlement | BRTI 60s average | BRTI 60s average |
| Settlement agreement (Phase 1) | 696/696 windows identical | |
Matched events on two venues are the same event, not independent evidence.
Live snapshots at the maker decision time: 4 · Polymarket US quote found: 4
Same moment: the two reads are at most 0.06s apart.
Maker's chosen side, ask on both venues: 1 pairs · Polymarket minus Kalshi: median +0.5c, mean +0.5c · Polymarket cheaper 0, same 0, Kalshi cheaper 1 · gaps of 5c or more: 0
Quoted prices before fees. Small sample: descriptive only, no PASS/FAIL rule.
Polymarket US feeCoefficient seen live: 15m [0.11] · 5m not read yet (the 5m bot scores with 0.095)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
