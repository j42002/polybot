---
polybot_auto: true
updated: 2026-11-28 02:36 UTC
tags: [agents, agents/implemented]
---
# 🟢 Hawk

> [!abstract] 🟢 implemented · self-test passed
> Descriptive results by volatility / momentum
> Folded in: Market Stability Monitor (regimes)

## Latest findings
| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 23 | 17 | 65% | -1.91 |
| maker | 1-min BTC move mid | 22 | 13 | 69% | +1.03 |
| maker | 1-min BTC move high | 22 | 14 | 93% | +2.35 |
| maker | distance to target low | 23 | 19 | 63% | +1.69 |
| maker | distance to target mid | 22 | 17 | 76% | -0.85 |
| maker | distance to target high | 22 | 8 | 100% | +0.47 |
| 5m | BTC volatility low | 36 alerts | 11 buyable at 30s | picks right 53% | -32.16 total |
| 5m | BTC volatility mid | 36 alerts | 7 buyable at 30s | picks right 61% | -0.32 total |
| 5m | BTC volatility high | 35 alerts | 6 buyable at 30s | picks right 71% | +10.83 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
