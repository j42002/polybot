---
polybot_auto: true
updated: 2026-11-27 10:39 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **14 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-27 10:18 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 489 settled rounds observed · 81 alerts (80 delivered) · **14 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/480 valid rounds (1.2%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1534 vs market 0.1607 on 489 rounds -> model sharper
3. **Simulated profit after fees:** -24.54 on 14 trades of $10 · win rate 43% vs break-even 48%, 95% range per trade -7.78 to +4.28
4. **Quote available at simulated tap (size not verified):** 5s 21/80 · 10s 19/80 · 20s 16/80 · 30s 14/80
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 46 runs, stalls over 5s 3/75887 loops, longest BTC price gap 10.7s · checks with no market quote 73/2406 (book fallback used 987) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 14/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
