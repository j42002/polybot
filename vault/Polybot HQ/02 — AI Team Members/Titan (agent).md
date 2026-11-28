---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Titan

> [!abstract] 🟢 implemented · self-test passed
> Size availability, fill volume, quote freshness
> Folded in: Liquidity Intelligence

## Latest findings
5m: 30s ask size logged on 103/103 alerts · size >= $10 at 30s: 98 yes / 5 no / 0 unknown. **Size units are not verified against the app, so 5m P&L is quote-availability only.**
Maker: through-volume / order size on fills: min 17x, median 21204x (volume never the constraint)
Maker quote freshness (from the read-only audit): recorded ask >5c from same-second prints on 22/55 orders; marketable at post 7/55

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
