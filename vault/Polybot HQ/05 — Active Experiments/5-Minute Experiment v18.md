---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **27 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 08:27 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 743 settled rounds observed · 124 alerts (121 delivered) · **27 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/727 valid rounds (2.8%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1606 vs market 0.1650 on 743 rounds -> model sharper
3. **Simulated profit after fees:** -11.35 on 27 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.69 to +3.84
4. **Quote available at simulated tap (size not verified):** 5s 40/121 · 10s 38/121 · 20s 33/121 · 30s 28/121
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 70 runs, stalls over 5s 13/115464 loops, longest BTC price gap 21.8s · checks with no market quote 98/3654 (book fallback used 1486) · bad close samples 17 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 27/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 27/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 75/120 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 27 tickets at every delay (right 13/27): 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 12, of which right 9/12. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
