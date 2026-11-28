---
polybot_auto: true
updated: 2026-11-28 01:04 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **24 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 01:04 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 661 settled rounds observed · 107 alerts (105 delivered) · **24 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/648 valid rounds (3.1%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1633 vs market 0.1691 on 661 rounds -> model sharper
3. **Simulated profit after fees:** -21.65 on 24 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -5.46 to +3.65
4. **Quote available at simulated tap (size not verified):** 5s 34/105 · 10s 32/105 · 20s 27/105 · 30s 24/105
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 62 runs, stalls over 5s 4/102282 loops, longest BTC price gap 10.8s · checks with no market quote 92/3247 (book fallback used 1316) · bad close samples 14 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 24/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 24/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 64/105 delivered alerts (61%) vs average break-even 52% at the alert price.
- Same 24 tickets at every delay (right 11/24): 5s -24.40 · 10s -26.33 · 20s -21.24 · 30s -21.65. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 10, of which right 7/10. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
