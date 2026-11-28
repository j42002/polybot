---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Judge

> [!abstract] 🟢 implemented · self-test passed
> Independent stats, calibration, simulated vs executable
> Folded in: Confidence Auditor, Profit Validator

## Latest findings
**Maker (15m)**: 43 fills / 65 posted · screening 43/100 fills
P&L +30.29 · **per posted order +0.47** (95% by 4-hour blocks: -0.58 to +1.68, 9 blocks)
Win of fills 32/43 = 74.4% (95% 60%-85%) vs break-even 73.0% · contract-weighted 71.5% vs 66.6%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 24 simulated trades from 103 alerts · screening 24/100 · research 24/300
P&L -21.65 · per alert -0.210 · win 11/24 (28%-65%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 134/244 (49%-61%) · 60-70%: won 131/204 (57%-70%) · 70-80%: won 99/133 (66%-81%) · 80-90%: won 66/74 (80%-94%)
Brier: model 0.2118 vs market 0.2182 on 622 rounds (lower = sharper; sharper is not profit)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
