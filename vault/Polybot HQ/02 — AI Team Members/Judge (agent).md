---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/implemented]
---
# 🟢 Judge

> [!abstract] 🟢 implemented · self-test passed
> Independent stats, calibration, simulated vs executable
> Folded in: Confidence Auditor, Profit Validator

## Latest findings
**Maker (15m)**: 39 fills / 58 posted · screening 39/100 fills
P&L +35.91 · **per posted order +0.62** (95% by 4-hour blocks: -0.50 to +1.69, 9 blocks)
Win of fills 31/39 = 79.5% (95% 64%-89%) vs break-even 74.5% · contract-weighted 75.6% vs 69.0%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 20 simulated trades from 95 alerts · screening 20/100 · research 20/300
P&L -44.28 · per alert -0.466 · win 8/20 (22%-61%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 128/234 (48%-61%) · 60-70%: won 125/192 (58%-71%) · 70-80%: won 95/127 (67%-82%) · 80-90%: won 62/69 (81%-95%)
Brier: model 0.2104 vs market 0.2184 on 592 rounds (lower = sharper; sharper is not profit)

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
