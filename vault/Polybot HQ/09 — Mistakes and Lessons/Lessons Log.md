---
tags: [lessons]
---
# 🧩 Mistakes and Lessons

What went wrong, what we learned, what changed. Add new ones with [[Lesson Template]]. Failures stay on the record.

| Date | What happened | Lesson | Fix |
|---|---|---|---|
| 2026-11-25 | An HTTP 500 Discord error was counted as a filled, winning ticket (+13.26) | A ticket that wasn't delivered can't be a trade | v16: only delivered (2xx + message id) and FILLABLE tickets count |
| 2026-11-25 | Two runs saved data at once and one overwrote the other (lost rows, erased team board entry) | Parallel jobs need merge-safe saving | sync_data.py merges against a snapshot; boards merge by entry |
| 2026-11-25 | Model tuned on 155 correlated checkpoints from the same markets (in-sample) | Checkpoints in one market aren't independent; tuning on them overfits | split by market, then froze the model |
| 2026-11-25 | Break-even ignored the fee | Fees decide whether a "winning" rule makes money | break-even = price + fee·p·(1-p) everywhere |
| 2026-11-25 | Polymarket /bbo returned 404 on ~31% of live checks | Don't trust one endpoint | v19: /book fallback, source recorded |
| 2026-11-25 | 12-minute rule: won 78% but needed 81% to break even | A rule that wins "most of the time" can still lose money: the price already includes the trend | judged by fee-inclusive break-even, pre-registered |
| 2026-11-26 | A scoreboard landed in #polybot after rerouting | A run started on old code keeps old settings until it ends | audit in-flight runs after routing changes |
| 2026-11-26 | Scoreboard counted every checkpoint and every market ever, mixing old and new | Count separate rounds, not checks; same snapshot as the report | 1 pre-specified check per v18+ round |
| 2026-11-27 | 5m: the bot was right on 63% of alerts, yet the tap table loses more at 30s than 5s | Correct calls get priced in within seconds; slower taps keep mostly wrong calls. On the same tickets, delay changed nothing | report speed vs picks on the same tickets, not across cohorts |
| 2026-11-27 | Maker test: losers filled 6/6, winners 29/47 | Resting orders fill when price moves against you; unfilled wins are not earnings | report P&L per posted order and outcome-conditional fill rates |
| 2026-11-27 | Fast mode's reply on PR #9 never posted (HTTP 403) and blocked the queue | PR comments need `pull-requests: write`; one bad item shouldn't stop the rest | permission added; failures now skip and retry |
