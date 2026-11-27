---
polybot_auto: true
updated: 2026-11-27 19:10 UTC
tags: [experiment, experiment/5m, status/running]
---
# ⏱️ 5-Minute Experiment (v18, frozen)

> [!success] Running · paper only · model frozen
> Progress **15 / 300** separate settled simulated trades. Nothing is judged before 300.

## What it tests
Polymarket US *BTC Up or Down 5 min*: does the frozen model's win chance beat the ask (6-15% edge after fees)?

## Frozen settings
- Model `rw-m1.4-c0.88-b15` (sigma x1.4, cap 0.88, basis sd 15). `MODEL_FROZEN = True`.
- Experiment rows start at agent v18. Older versions had measurement bugs and are excluded.
- Only FILLABLE quotes count as trades. Break-even includes the 0.095 taker fee.

## Latest numbers (2026-11-27 18:37 UTC)
Strategy and model are frozen during this experiment. Older versions had known measurement bugs and are excluded.

**Data:** 584 settled rounds observed · 89 alerts (87 delivered) · **15 simulated trades**. Rounds observed are not trades.

1. **Settlement disagreement:** 13/571 valid rounds (2.3%) where Coinbase points at the wrong winner · missing 33
2. **Model vs market accuracy (Brier, lower is better):** model 0.1623 vs market 0.1692 on 584 rounds -> model sharper
3. **Simulated profit after fees:** -34.90 on 15 trades of $10 · win rate 40% vs break-even 49%, 95% range per trade -8.05 to +3.40
4. **Quote available at simulated tap (size not verified):** 5s 22/87 · 10s 20/87 · 20s 17/87 · 30s 15/87
5. **Max drawdown:** -51.99
6. **Loop health and missing data:** 55 runs, stalls over 5s 4/90732 loops, longest BTC price gap 10.8s · checks with no market quote 73/2872 (book fallback used 1212) · bad close samples 13 · undelivered alerts 2 · unconfirmed price checks 0
7. **Gemini:** not enabled or no opinions yet

Verdict rule: nothing is judged before 300 separate settled rounds with simulated trades. Progress: 15/300.

---

Full report: [[5-Minute Research Report]] · Calibration and checks: [[Team Checks (latest)]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
