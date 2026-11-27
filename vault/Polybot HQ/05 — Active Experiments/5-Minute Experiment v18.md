---
polybot_auto: true
updated: 2026-11-27 20:30 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **18 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-27 20:27 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 605 settled rounds observed · 95 alerts (93 delivered) · **18 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 15/593 valid rounds (2.5%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1611 vs market 0.1675 on 605 rounds -> model sharper
3. **Simulated profit after fees:** -50.17 on 18 trades of $10 · win rate 39% vs break-even 50%, 95% range per trade -7.78 to +2.21
4. **Quote available at simulated tap (size not verified):** 5s 27/93 · 10s 25/93 · 20s 22/93 · 30s 19/93
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 57 runs, stalls over 5s 4/94032 loops, longest BTC price gap 10.8s · checks with no market quote 80/2978 (book fallback used 1241) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 18/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
