---
polybot_auto: true
updated: 2026-11-28 00:53 UTC
tags: [results, checks]
---
# 🧮 Team Checks (latest)

# Team checks · 2026-11-28 00:52 UTC

Deterministic Python checks, $0, read-only.

## 🟡 Data Auditor

- ✅ 5m rounds observed in the last 24h: 272/288 (94%)
- ✅ duplicate checkpoint rows (v18+): 0
- ✅ checks with no market quote (24h): 24/1318
- ✅ rows with unreadable timestamps: 0
- ✅ close samples with gaps (>6s hole or <20 samples): 13/670
- ⚠️ alerts that failed delivery (v18+): 2/105
- ⚠️ loop stalls >5s (last runs): 1 · longest BTC price gap 10.8s
- ✅ 15m backtest settlement mismatches: 0/6456
- ✅ 15m markets without a usable candle: 0/6456

## 🟡 Quant Analyst

- 5m experiment: 24 simulated trades, win rate 46% (95% range 28%–65%) vs break-even 49% → can't tell yet: break-even is inside the range
- 5m paper P&L after fees: -21.65 at $10/trade · progress 24/300 separate rounds
- ⚠️ Sample too small for any conclusion (n=24; under ~100 trades a 10-point swing in win rate is noise).
- 15m Phase 1 primary row (exploratory): | 2022 | 78.1% | 80.9% | -632.13 | -0.313 (-0.713 to +0.088) | -3.85 | -768.38 | 4 |
- Reminder: historical results are exploratory; only the forward test can confirm. Secondary rules carry multiple-testing risk.

## 🟡 Risk Sentinel

- ✅ no credentials committed to the repo
- ✅ no code that places real orders
- ✅ no paid AI API keys used by any workflow ($0)
- ✅ account access off (no Polymarket keys in workflows)
- ✅ 5m model still frozen (MODEL_FROZEN = True)
- ✅ team relay can't post into the #polybot ticket channel
- ✅ DISCORD_WEBHOOK → #polybot-moves (tickets only) (verified with Discord)
- ✅ DISCORD_TEAM_WEBHOOK → #ai-team-chat (verified with Discord)
- ✅ DISCORD_RESEARCH_WEBHOOK → #research-reports (verified with Discord)
- ⚠️ workflow runs in 24h: 100, failed: 1 (team relay)

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
