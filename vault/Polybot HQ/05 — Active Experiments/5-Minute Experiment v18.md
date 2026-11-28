---
polybot_auto: true
updated: 2026-11-28 12:19 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **30 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 12:08 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 788 settled rounds observed · 132 alerts (129 delivered) · **30 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 24/772 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 41
2. **Model vs market accuracy (Brier, lower is better):** model 0.1609 vs market 0.1651 on 788 rounds -> model sharper
3. **Simulated profit after fees:** -6.29 on 30 trades of $10 · win rate 50% vs break-even 50%, 95% range per trade -4.19 to +3.77
4. **Quote available at simulated tap (size not verified):** 5s 44/129 · 10s 42/129 · 20s 35/129 · 30s 30/129
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 74 runs, stalls over 5s 13/122064 loops, longest BTC price gap 21.8s · checks with no market quote 98/3869 (book fallback used 1578) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 30/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 30/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 81/129 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 30 tickets at every delay (right 15/30): 5s -12.55 · 10s -14.48 · 20s -9.39 · 30s -6.29. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
