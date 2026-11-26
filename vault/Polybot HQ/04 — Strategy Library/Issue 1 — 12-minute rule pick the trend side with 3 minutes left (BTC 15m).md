---
polybot_auto: true
updated: 2026-11-26 01:33 UTC
tags: [strategy]
---
# Issue 1 — 12-minute rule pick the trend side with 3 minutes left (BTC 15m)

> [!abstract] Status
> **stage:5-testing, evidence:L0-claim** · [open on GitHub](https://github.com/j42002/polybot/issues/1) · 4 comments

## Submission
### Submitted by

Jacob (founder)

### Market

Kalshi KXBTC15M; Polymarket US BTC Up/Down 15m

### The claim, in the source's own terms

A TikTok creator watches a 15-minute BTC contract for 12 minutes, then picks UP or DOWN by the current trend with 3 minutes left, and says it wins.

### Original sources

TikTok video found by Jacob (link to add). Original not yet verified by Perplexity. Unknown whether the creator sells anything.

### Exact rules (as testable as possible)

Source: entry at 12:00 elapsed, side = 'trend' (UNSPECIFIED). Lab pre-registration (data/15m/PREREG.md): PRIMARY = AGREE, i.e. bet only when BTC is on the winning side of the target AND moved that way over the last 60s. Entry = ask ~60s later, Kalshi taker fee, held to settlement.

### Supporting evidence

None checkable yet. Legacy 5m data at the same 80%-elapsed point hinted at it (not evidence: known bugs, no delay).

### Weaknesses and red flags

Trend rule unspecified. The trend side is usually already the favourite at 75-90c, so it wins often by construction; profit needs the market to under-price continuation. Fees and delay not mentioned by the source.

### How could we paper-test it at $0?

Phase 1 (running): Kalshi historical backtest, backtest15.py -> data/15m/report.md (exploratory). Phase 2 (if justified): forward paper test on Polymarket US 15m, 300 trades.

_Seeded by the lab from existing work._

## Discussion
Full thread: [[Issue 1 — 12-minute rule pick the trend side with 3 minutes left (BTC 15m) (thread)]]

## Related
- [[Strategy Library]] · [[Experiment Registry]] · [[Evidence Levels]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
