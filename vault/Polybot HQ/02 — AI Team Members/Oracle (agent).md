---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [agents, agents/implemented]
---
# 🟢 Oracle

> [!abstract] 🟢 implemented · self-test passed
> Stress tests and simulated screening outcomes

## Latest findings
Expected P&L per posted order at the live win rate (85%): +0.48
…at the historical AGREE win rate (78.1%): **-0.36**
…with the 0.0175 maker fee at the live rate: +0.45
Win probability needed to break even with this price mix and these fill rates: **81.1%**
If the true win rate were the historical 78.1%, the frozen 100-fill screen (+3 points) would still PASS in 55% of 2,000 simulations: the screen is a first look, not proof.
Assumes the observed fill rates (when right / when wrong) and price mix stay the same.

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
