---
polybot_auto: true
updated: 2026-11-27 09:37 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **13 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-27 09:23 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 478 settled rounds observed · 77 alerts (76 delivered) · **13 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 6/469 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 25
2. **Model vs market accuracy (Brier, lower is better):** model 0.1534 vs market 0.1609 on 478 rounds -> model sharper
3. **Simulated profit after fees:** -13.94 on 13 trades of $10 · win rate 46% vs break-even 49%, 95% range per trade -7.43 to +5.28
4. **Quote available at simulated tap (size not verified):** 5s 19/76 · 10s 17/76 · 20s 15/76 · 30s 13/76
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 45 runs, stalls over 5s 3/74237 loops, longest BTC price gap 10.7s · checks with no market quote 73/2352 (book fallback used 970) · bad close samples 10 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 13/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
