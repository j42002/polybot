---
polybot_auto: true
updated: 2026-11-26 01:27 UTC
tags: [strategy]
---
# Issue 2 — Polybot model edge buy when our win chance beats the price by 6-15% (BTC 5m)

> [!abstract] Status
> **stage:5-testing, evidence:L0-claim** · [open on GitHub](https://github.com/j42002/polybot/issues/2) · 1 comments

## Submission
### Submitted by

Claude (developer)

### Market

Polymarket US BTC Up/Down 5m

### The claim, in the source's own terms

Our random-walk model (volatility x1.4, capped at 88%) finds rounds where the market misprices the outcome by 6-15% after fees at 4:00 or 3:30 left.

### Original sources

Internal: agent.py v18+ (frozen model rw-m1.4-c0.88-b15), team board history.

### Exact rules (as testable as possible)

One ticket per round max; 6% <= edge <= 15% after fee; no ticket after a spike or in chop; re-priced right before sending; simulated fill = ask at +30s if within the limit.

### Supporting evidence

None yet: the v18 forward experiment started 2026-11-25. Out-of-sample calibration on legacy data was honest up to ~70% and overconfident above.

### Weaknesses and red flags

A big gap with the market is often a warning, not an edge. Coinbase is not the settlement index (BRTI). Few tickets per day, so 300 will take a while.

### How could we paper-test it at $0?

Running: forward paper test, report.md 'Research report: experiment v18+ only'.

_Seeded by the lab from existing work._

## Discussion
Full thread: [[Issue 2 — Polybot model edge buy when our win chance beats the price by 6-15% (BTC 5m) (thread)]]

## Related
- [[Strategy Library]] · [[Experiment Registry]] · [[Evidence Levels]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
