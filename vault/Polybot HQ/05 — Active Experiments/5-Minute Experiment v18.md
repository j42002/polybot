---
polybot_auto: true
updated: 2026-11-28 18:37 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **34 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 18:36 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 861 settled rounds observed · 145 alerts (142 delivered) · **34 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/841 valid rounds (3.0%) where Coinbase points at the wrong winner · missing 49
2. **Model vs market accuracy (Brier, lower is better):** model 0.1591 vs market 0.1624 on 861 rounds -> model sharper
3. **Simulated profit after fees:** +5.73 on 34 trades of $10 · win rate 50% vs break-even 49%, 95% range per trade -3.69 to +4.03
4. **Quote available at simulated tap (size not verified):** 5s 48/142 · 10s 46/142 · 20s 39/142 · 30s 34/142
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 81 runs, stalls over 5s 13/133613 loops, longest BTC price gap 21.8s · checks with no market quote 104/4230 (book fallback used 1720) · bad close samples 20 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 34/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 34/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 87/141 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 34 tickets at every delay (right 17/34): 5s -0.53 · 10s -2.46 · 20s +2.63 · 30s +5.73. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
