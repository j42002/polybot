---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/implemented]
---
# 🟢 Hawk

> [!abstract] 🟢 implemented · self-test passed
> Descriptive results by volatility / momentum
> Folded in: Market Stability Monitor (regimes)

## Latest findings
| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 20 | 16 | 69% | -1.60 |
| maker | 1-min BTC move mid | 19 | 10 | 80% | +0.89 |
| maker | 1-min BTC move high | 19 | 13 | 92% | +2.68 |
| maker | distance to target low | 20 | 18 | 67% | +1.37 |
| maker | distance to target mid | 19 | 13 | 85% | -0.10 |
| maker | distance to target high | 19 | 8 | 100% | +0.54 |
| 5m | BTC volatility low | 32 alerts | 9 buyable at 30s | picks right 50% | -29.73 total |
| 5m | BTC volatility mid | 32 alerts | 6 buyable at 30s | picks right 62% | -14.15 total |
| 5m | BTC volatility high | 31 alerts | 5 buyable at 30s | picks right 71% | -0.40 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
