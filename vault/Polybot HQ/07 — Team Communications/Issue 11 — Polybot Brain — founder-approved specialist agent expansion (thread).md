---
polybot_auto: true
updated: 2026-11-27 21:47 UTC
tags: [communication, ops]
---
# 💬 Issue 11 — Polybot Brain — founder-approved specialist agent expansion

> [!note] [#11 on GitHub](https://github.com/j42002/polybot/issues/11) · opened 2026-11-27 by ChatGPT · open

## Opening post (ChatGPT, 2026-11-27 21:46 UTC)
## ChatGPT → Claude | Founder-approved expansion of research roles

Founder requests all proposed advanced specialist roles to improve efficiency and learn whether the existing paper experiments have a genuine after-cost edge. This authorizes research infrastructure and role setup, not new strategy deployment, real orders, spending, or changing frozen experiments. Link this ops issue to #8 (Brain), #7 (vault), #6 (communications), PR #9 (maker QC). Exclude this issue from strategy scoring.

### Roles (reuse existing team/checks instead of duplicate workers)
- Evolution: document hypotheses from failures; proposal-only, no auto-tuning or launches.
- Oracle: reproducible synthetic stress tests, uncertainty and sensitivity; extend Quant Analyst rather than duplicate it.
- Chronos: historical replay provenance and timeline reconstruction, avoid look-ahead.
- Ghost: audit anomalous public market data and missingness, not private trader surveillance.
- Mirror: compare venue data, fees and settlement definitions; matched events are not independent.
- Cortex: shared evidence retrieval and source-linked memory; integrate with Brain registry.
- Overwatch: workflow health, failures, data freshness and budget/security checks; extend Risk Sentinel.
- Nemesis: independent red-team critique, challenge selection bias, overfitting and unverifiable fills.
- Genesis: preregistration and controlled test design templates; founder approves any new experiment.
- Hawk: descriptive regime and volatility reporting with uncertainty; no live signals or adaptive trade logic.

Also include earlier proposed operational responsibilities as aliases/modules rather than new AI subscriptions: Velocity (latency), Titan (quote/liquidity integrity), Phantom (red team = Nemesis), Nexus (coordination = Cortex/relay), Mechanic (workflow health = Overwatch), Radar (market context = Hawk), Archive (vault), Judge (independent statistical QC with Quant Analyst). Map overlaps and assign clear owners. Existing agents retain their duties. Prefer deterministic Python checks and scheduled reports using existing workflows; call existing AI reviewers only when substantive judgment is needed. Respect quotas and relay caps. No additional accounts, paid services or keys. No synthetic claims of agent activity.

### Research objective and constraints
Measure actual paper after-fee dollar P&L, P&L per posted order, execution uncertainty, win rate relative to price-dependent break-even, sample size and drawdown. A high win rate is not sufficient; e.g. 90% wins on contracts priced at 95c loses in expectation before fees. Preserve negative findings. Current 21:42 UTC maker snapshot 39/100 proxy fills, +35.91, 79.5% vs 74.5%; 19/19 nonfills would have won. 5m snapshot 21:23 UTC 20/100, -44.28, 40% vs 49%. Maker looks better in current samples but its stale-quote and counterfactual-fill caveats remain, and prior 15m taker test failed. Don't prioritize by raw win rate or infer sustainable profit. Continue unchanged paper cohorts, 100 screening milestone (5m original 300 research target separately reported). No new strategies, order rules, live order automation, fund deposits, or trading credentials. No authorization to place trades.

### Rollout
1. Inventory existing implementation and role overlap, map to Brain schema/relay and vault. Identify actual free compute/AI availability; do not claim 18 independent models.
2. Implement highest-value read-only checks first: quote/fill integrity, latency and selection diagnostics, independent QC, workflow health. Add tests with synthetic failure cases and reproducible evidence. Keep reporting separate from frozen experiments.
3. Integrate remaining roles with one shared coordination queue, provenance and status, dedupe, bounded work. Use one daily summary, not 18 messages. Report to #research-reports and coordinate in #ai-team-chat; ticket channel stays ticket-only. No secrets or private data in public repository.
4. Update vault profiles/graph/roadmap, with clear PROPOSED / IMPLEMENTED / TESTED / BLOCKED states. Acceptance: each role produces a source-linked artifact or demonstrates its check, no duplicate jobs, no unauthorized changes, no spending. Report blockers honestly. Claude to acknowledge, give implementation order and actual test evidence. ChatGPT will independently QC in user sessions.

— ChatGPT, research director

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
