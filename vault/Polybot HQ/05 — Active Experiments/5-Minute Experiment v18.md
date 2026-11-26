---
polybot_auto: true
updated: 2026-11-26 08:42 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **4 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-26 08:28 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 189 settled rounds observed · 27 alerts (26 delivered) · **4 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 1/188 valid rounds (0.5%) where Coinbase points at the wrong winner · missing 9
2. **Model vs market accuracy (Brier, lower is better):** model 0.1340 vs market 0.1448 on 189 rounds -> model sharper
3. **Simulated profit after fees:** -26.83 on 4 trades of $10 · win rate 25% vs break-even 44%, 95% range per trade -14.39 to +0.97
4. **Quote available at simulated tap (size not verified):** 5s 8/26 · 10s 8/26 · 20s 6/26 · 30s 4/26
5. **Max drawdown:** -26.83
6. **Loop health and missing data:** 18 runs, stalls over 5s 2/29692 loops, longest BTC price gap 10.7s · checks with no market quote 64/945 (book fallback used 358) · bad close samples 4 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 4/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
