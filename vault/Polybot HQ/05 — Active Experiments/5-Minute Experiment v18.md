---
polybot_auto: true
updated: 2026-11-28 04:09 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **26 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 03:50 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 692 settled rounds observed · 114 alerts (112 delivered) · **26 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/676 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 38
2. **Model vs market accuracy (Brier, lower is better):** model 0.1621 vs market 0.1669 on 692 rounds -> model sharper
3. **Simulated profit after fees:** -20.88 on 26 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.17 to +3.56
4. **Quote available at simulated tap (size not verified):** 5s 37/112 · 10s 35/112 · 20s 30/112 · 30s 26/112
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 65 runs, stalls over 5s 4/107232 loops, longest BTC price gap 10.8s · checks with no market quote 92/3400 (book fallback used 1389) · bad close samples 16 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 26/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 26/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 69/112 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 26 tickets at every delay (right 12/26): 5s -23.63 · 10s -25.56 · 20s -20.47 · 30s -20.88. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 11, of which right 8/11. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
