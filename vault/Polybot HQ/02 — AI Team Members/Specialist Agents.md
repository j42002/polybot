---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [team, agents, index]
---
# 🧭 Specialist Agents

> [!info] 🟢 implemented + tested · 🔵 in development · 🟡 pending · 🔴 blocked
> 🟢 means the agent's self-test with planted failures passed AND it ran on real data in the latest run (2026-11-28 08:51 UTC). These are deterministic Python checks, not separate AI models.

| | Agent | Folded in | Job | Self-test |
|---|---|---|---|---|
| 🟢 | [[Velocity (agent)]] | Expiration Guard | Latency, quote lifetime, 30s deadline consistency | passed |
| 🟢 | [[Titan (agent)]] | Liquidity Intelligence | Size availability, fill volume, quote freshness | passed |
| 🟢 | [[Ghost (agent)]] | Market Stability Monitor (data) | Anomalies and missing data in public feeds | passed |
| 🟢 | [[Hawk (agent)]] | Market Stability Monitor (regimes) | Descriptive results by volatility / momentum | passed |
| 🟢 | [[Judge (agent)]] | Confidence Auditor, Profit Validator | Independent stats, calibration, simulated vs executable | passed |
| 🟢 | [[Nemesis (agent)]] | Loss Intelligence | Red-team challenges, every loss explained | passed |
| 🟢 | [[Oracle (agent)]] | - | Stress tests and simulated screening outcomes | passed |
| 🟢 | [[Chronos (agent)]] | - | Coverage timeline, gaps, versions, provenance | passed |
| 🟢 | [[Mirror (agent)]] | - | Kalshi vs Polymarket US: fees, settlement and same-moment prices | passed |
| 🟢 | [[Overwatch (agent)]] | Mechanic | Workflow failures, data freshness, relay health | passed |
| 🟢 | [[Genesis (agent)]] | - | Pre-registration template and validator | passed |
| 🟢 | [[Evolution (agent)]] | - | Proposal-only hypotheses from measured patterns | passed |
| 🟢 | [[Cortex (agent)]] | Archive, Nexus | Shared registry for the vault and relay (this file's output) | passed |

Existing roles: [[Data Auditor]], [[Quant Analyst]], [[Risk Sentinel]], Maker QC audit, Relay (Nexus queue), Vault sync (Archive)

Blueprint: [[System Blueprint]] · Findings: [[Agent Findings (latest)]] · Plan: issue #11

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
