---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Oracle

> [!abstract] 🟢 implemented · self-test passed
> Stress tests and simulated screening outcomes

## Latest findings
Expected P&L per posted order at the live win rate (83%): +0.37
…at the historical AGREE win rate (78.1%): **-0.23**
…with the 0.0175 maker fee at the live rate: +0.34
Win probability needed to break even with this price mix and these fill rates: **80.0%**
If the true win rate were the historical 78.1%, the frozen 100-fill screen (+3 points) would still PASS in 69% of 2,000 simulations: the screen is a first look, not proof.
Assumes the observed fill rates (when right / when wrong) and price mix stay the same.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
