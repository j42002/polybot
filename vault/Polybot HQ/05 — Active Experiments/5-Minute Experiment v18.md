---
polybot_auto: true
updated: 2026-11-28 13:59 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **33 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-28 13:59 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 810 settled rounds observed · 137 alerts (134 delivered) · **33 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 25/793 valid rounds (3.2%) where Coinbase points at the wrong winner · missing 42
2. **Model vs market accuracy (Brier, lower is better):** model 0.1600 vs market 0.1641 on 810 rounds -> model sharper
3. **Simulated profit after fees:** -9.33 on 33 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -4.16 to +3.59
4. **Quote available at simulated tap (size not verified):** 5s 47/134 · 10s 45/134 · 20s 38/134 · 30s 33/134
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 76 runs, stalls over 5s 13/125363 loops, longest BTC price gap 21.8s · checks with no market quote 98/3977 (book fallback used 1612) · bad close samples 18 · undelivered alerts 3 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 33/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 33/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 83/134 delivered alerts (62%) vs average break-even 52% at the alert price.
- Same 33 tickets at every delay (right 16/33): 5s -15.59 · 10s -17.52 · 20s -12.43 · 30s -9.33. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 14, of which right 11/14. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
