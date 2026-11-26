---
polybot_auto: true
updated: 2026-11-26 18:44 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **7 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-26 18:37 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 305 settled rounds observed · 40 alerts (39 delivered) · **7 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 4/300 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 18
2. **Model vs market accuracy (Brier, lower is better):** model 0.1465 vs market 0.1547 on 305 rounds -> model sharper
3. **Simulated profit after fees:** -41.74 on 7 trades of $10 · win rate 29% vs break-even 45%, 95% range per trade -11.86 to -0.07
4. **Quote available at simulated tap (size not verified):** 5s 11/39 · 10s 11/39 · 20s 9/39 · 30s 7/39
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 29 runs, stalls over 5s 3/47837 loops, longest BTC price gap 10.7s · checks with no market quote 65/1514 (book fallback used 611) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 7/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
