---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [agents, agents/implemented]
---
# 🟢 Hawk

> [!abstract] 🟢 implemented · self-test passed
> Descriptive results by volatility / momentum
> Folded in: Market Stability Monitor (regimes)

## Latest findings
| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 28 | 21 | 67% | -1.83 |
| maker | 1-min BTC move mid | 27 | 16 | 75% | +1.04 |
| maker | 1-min BTC move high | 26 | 16 | 94% | +2.26 |
| maker | distance to target low | 28 | 22 | 64% | +1.39 |
| maker | distance to target mid | 27 | 21 | 81% | -0.55 |
| maker | distance to target high | 26 | 10 | 100% | +0.46 |
| 5m | BTC volatility low | 41 alerts | 13 buyable at 30s | picks right 56% | -31.39 total |
| 5m | BTC volatility mid | 40 alerts | 6 buyable at 30s | picks right 62% | +30.41 total |
| 5m | BTC volatility high | 39 alerts | 8 buyable at 30s | picks right 69% | -10.37 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
