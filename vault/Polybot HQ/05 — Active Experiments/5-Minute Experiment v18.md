---
polybot_auto: true
updated: 2026-11-27 23:13 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **23 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-27 23:13 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 639 settled rounds observed · 102 alerts (100 delivered) · **23 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 20/627 valid rounds (3.2%) where Coinbase points at the wrong winner · missing 32
2. **Model vs market accuracy (Brier, lower is better):** model 0.1634 vs market 0.1696 on 639 rounds -> model sharper
3. **Simulated profit after fees:** -11.14 on 23 trades of $10 · win rate 48% vs break-even 49%, 95% range per trade -5.17 to +4.20
4. **Quote available at simulated tap (size not verified):** 5s 32/100 · 10s 30/100 · 20s 26/100 · 30s 23/100
5. **Max drawdown:** -60.71
6. **Loop health and missing data:** 60 runs, stalls over 5s 4/98982 loops, longest BTC price gap 10.8s · checks with no market quote 92/3139 (book fallback used 1286) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

**Thresholds (reported separately, never merged):** screening milestone 23/100 (set by Jacob 2026-11-26: a first look, not proof) · research target 23/300 (pre-registered: nothing is judged before 300 separate settled rounds with simulated trades).

**Speed vs picks (reporting only, quote availability not verified fills):**

- Picks: the side was right on 63/100 delivered alerts (63%) vs average break-even 52% at the alert price.
- Same 23 tickets at every delay (right 11/23): 5s -13.98 · 10s -15.91 · 20s -10.82 · 30s -11.14. Within the same tickets, waiting barely changes the result.
- Buyable at 5s but gone by 30s: 9, of which right 7/9. Correct calls get priced in fastest, so slower taps keep a larger share of wrong calls.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
