---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [agents, agents/implemented]
---
# 🟢 Judge

> [!abstract] 🟢 implemented · self-test passed
> Independent stats, calibration, simulated vs executable
> Folded in: Confidence Auditor, Profit Validator

## Latest findings
**Maker (15m)**: 53 fills / 81 posted · screening 53/100 fills
P&L +35.67 · **per posted order +0.44** (95% by 4-hour blocks: -0.44 to +1.41, 12 blocks)
Win of fills 41/53 = 77.4% (95% 64%-87%) vs break-even 74.6% · contract-weighted 72.6% vs 67.8%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 27 simulated trades from 120 alerts · screening 27/100 · research 27/300
P&L -11.35 · per alert -0.095 · win 13/27 (31%-66%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 158/280 (51%-62%) · 60-70%: won 157/238 (60%-72%) · 70-80%: won 110/145 (68%-82%) · 80-90%: won 77/86 (81%-94%)
Brier: model 0.2078 vs market 0.2152 on 714 rounds (lower = sharper; sharper is not profit)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
