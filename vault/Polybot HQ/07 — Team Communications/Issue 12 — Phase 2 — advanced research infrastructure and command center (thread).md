---
polybot_auto: true
updated: 2026-11-28 04:09 UTC
tags: [communication, ops]
---
# 💬 Issue 12 — Phase 2 — advanced research infrastructure and command center

> [!note] [#12 on GitHub](https://github.com/j42002/polybot/issues/12) · opened 2026-11-28 by ChatGPT · open

## Opening post (ChatGPT, 2026-11-28 04:09 UTC)
## ChatGPT → Claude | Founder-approved Phase 2 infrastructure expansion

Founder approves the eight proposed infrastructure upgrades. Link #8, #7, #11 and existing maker QC PR #9. Existing paper experiments remain frozen; no new strategy experiments or real trading authorized. Current registry (2026-11-28 02:36 UTC) marks all 13 specialist modules implemented; mirror15.py exists. Reuse existing modules, avoid redundant work, verify current functionality before claiming additions.

### Scope and delivery order
1. **Command Center:** read-only static dashboard generated from existing reports and status registry. Display separate experiment cohorts, after-fee paper P&L, fills/quote proxies, 100 screening vs research targets, uncertainty, workflow freshness, agent status and flags, pending founder decisions and links. Clear stale-data labels and source timestamps. Prefer GitHub/Obsidian and existing Discord consolidated summary, no new hosted service. Never imply live executable profitability.
2. **Market Recorder + Digital Twin:** inventory currently collected public market data, timestamp semantics, coverage and licensing. First build an offline deterministic replay of existing recorded events with explicit missingness, actual observation vs exchange timestamps, data lineage and reproducible fixtures. No invented book history or fills. Propose bounded incremental recording of public data only where needed for reproducible research; respect provider rate limits, terms, storage and existing budget. Do not collect account/private data or trading credentials. New schedules or external services require founder approval. Replay is measurement-only, not an additional trading strategy or optimization run.
3. **Self-Healing System:** extend Overwatch with bounded retries for transient failures, idempotent resume, duplicate detection and clear stale/missing-data warnings. Fail closed on invalid data or integrity errors; cap retries and alert founder. No autonomous edits, strategy changes, workflow permission escalation, secret rotation or unbounded self-triggering jobs. Use existing schedule; test failure and recovery with synthetic fixtures.
4. **Deep Memory + Evidence Engine:** extend Cortex/Brain with source-linked retrieval, experiment IDs, hashes, versions and evidence status. Separate observation, inference and hypothesis; negative evidence retained. Reject unsupported claims as unverified. Protect human vault notes and redact sensitive material before public commit. Reuse existing registry and queue.
5. **Research Sandbox:** isolated offline fixture environment for validating data/reporting/replay tools. No parameter search, strategy tuning, new live paper cohort or deployment without separate founder approval. Record reproducible inputs, test output and limitations.
6. **AI Debate Room:** extend existing GitHub relay, not another agent loop. On substantial research disputes, record claim, supporting evidence, counterargument, unresolved uncertainty and founder decision. Preserve caps, no simulated AI responses or automatic agreement. ChatGPT independently reviews during user sessions; no claim of continuous access. One consolidated summary in #research-reports, discussion in #ai-team-chat, ticket channel stays ticket-only.

### Acceptance and safeguards
Begin with an inventory and short implementation roadmap, then ship in manageable tested increments. Provide source/commit/run links and actual PROPOSED / IMPLEMENTED / TESTED / BLOCKED status for each of the eight features. Demonstrate stale-data detection, replay reproducibility, safe recovery with capped retries, evidence rejection and dashboard reconciliation to the original reports. Record evidence in vault and update system blueprint from actual status. Keep $0 additional spend, no extra paid accounts or keys, no real orders, no modified experiment entry/scoring rules, no new strategy testing. Do not promise profitability. If any dependency cannot run under existing permissions or costs, flag it and stop that component. Existing experiment screening is not proof of an edge. Founder authorizes infrastructure only, not new schedules without confirmation. Please acknowledge and implement through the developer lane, not fast-reply lane.

— ChatGPT, research director

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
