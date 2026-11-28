---
polybot_auto: true
updated: 2026-11-28 02:36 UTC
tags: [agents, agents/implemented]
---
# 🟢 Judge

> [!abstract] 🟢 implemented · self-test passed
> Independent stats, calibration, simulated vs executable
> Folded in: Confidence Auditor, Profit Validator

## Latest findings
**Maker (15m)**: 44 fills / 67 posted · screening 44/100 fills
P&L +30.59 · **per posted order +0.46** (95% by 4-hour blocks: -0.59 to +1.63, 10 blocks)
Win of fills 33/44 = 75.0% (95% 61%-85%) vs break-even 73.6% · contract-weighted 71.9% vs 67.1%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 24 simulated trades from 107 alerts · screening 24/100 · research 24/300
P&L -21.65 · per alert -0.202 · win 11/24 (28%-65%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 138/248 (49%-62%) · 60-70%: won 141/215 (59%-72%) · 70-80%: won 102/137 (67%-81%) · 80-90%: won 68/77 (79%-94%)
Brier: model 0.2106 vs market 0.2170 on 644 rounds (lower = sharper; sharper is not profit)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
