---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Hawk

> [!abstract] 🟢 implemented · self-test passed
> Descriptive results by volatility / momentum
> Folded in: Market Stability Monitor (regimes)

## Latest findings
| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 22 | 17 | 59% | -2.46 |
| maker | 1-min BTC move mid | 22 | 12 | 75% | +1.48 |
| maker | 1-min BTC move high | 21 | 14 | 93% | +2.47 |
| maker | distance to target low | 22 | 18 | 61% | +1.69 |
| maker | distance to target mid | 22 | 17 | 76% | -0.79 |
| maker | distance to target high | 21 | 8 | 100% | +0.49 |
| 5m | BTC volatility low | 35 alerts | 11 buyable at 30s | picks right 49% | -32.16 total |
| 5m | BTC volatility mid | 34 alerts | 7 buyable at 30s | picks right 65% | -0.32 total |
| 5m | BTC volatility high | 34 alerts | 6 buyable at 30s | picks right 71% | +10.83 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
