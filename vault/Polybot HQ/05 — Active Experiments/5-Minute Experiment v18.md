---
polybot_auto: true
updated: 2026-11-26 13:07 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **6 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-26 13:05 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 242 settled rounds observed · 33 alerts (32 delivered) · **6 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 3/237 valid rounds (1.3%) where Coinbase points at the wrong winner · missing 15
2. **Model vs market accuracy (Brier, lower is better):** model 0.1381 vs market 0.1477 on 242 rounds -> model sharper
3. **Simulated profit after fees:** -48.03 on 6 trades of $10 · win rate 17% vs break-even 42%, 95% range per trade -13.12 to -2.89
4. **Quote available at simulated tap (size not verified):** 5s 10/32 · 10s 10/32 · 20s 8/32 · 30s 6/32
5. **Max drawdown:** -48.03
6. **Loop health and missing data:** 23 runs, stalls over 5s 2/37939 loops, longest BTC price gap 10.7s · checks with no market quote 65/1206 (book fallback used 459) · bad close samples 7 · undelivered alerts 1 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 6/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
