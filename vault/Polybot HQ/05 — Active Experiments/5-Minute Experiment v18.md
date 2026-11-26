---
polybot_auto: true
updated: 2026-11-26 01:33 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **3 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-26 01:06 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 100 settled rounds observed · 10 alerts (10 delivered) · **3 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 0/99 valid rounds (0.0%) where Coinbase points at the wrong winner · missing 10
2. **Model vs market accuracy (Brier, lower is better):** model 0.1377 vs market 0.1426 on 100 rounds -> model sharper
3. **Simulated profit after fees:** -16.25 on 3 trades of $10 · win rate 33% vs break-even 45%, 95% range per trade -15.67 to +4.84
4. **Quote available at simulated tap (size not verified):** 5s 4/10 · 10s 4/10 · 20s 4/10 · 30s 3/10
5. **Max drawdown:** -16.25
6. **Loop health and missing data:** 10 runs, stalls over 5s 1/16497 loops, longest BTC price gap 9.0s · checks with no market quote 64/521 (book fallback used 183) · bad close samples 4 · undelivered alerts 0 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 3/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
