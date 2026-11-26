---
polybot_auto: true
updated: 2026-11-26 09:24 UTC
tags: [results, checks]
---
# 🧮 Team Checks (latest)

# Team checks · 2026-11-26 09:24 UTC

Deterministic Python checks, $0, read-only.

## 🟡 Data Auditor

- ⚠️ 5m rounds observed in the last 24h: 205/288 (71%)
- ✅ duplicate checkpoint rows (v18+): 0
- ⚠️ checks with no market quote (24h): 64/999
- ✅ rows with unreadable timestamps: 0
- ✅ close samples with gaps (>6s hole or <20 samples): 4/208
- ⚠️ alerts that failed delivery (v18+): 1/29
- ⚠️ loop stalls >5s (last runs): 2 · longest BTC price gap 10.7s
- ✅ 15m backtest settlement mismatches: 0/6456
- ✅ 15m markets without a usable candle: 0/6456

## 🟡 Quant Analyst

- 5m experiment: 4 simulated trades, win rate 25% (95% range 5%–70%) vs break-even 44% → can't tell yet: break-even is inside the range
- 5m paper P&L after fees: -26.83 at $10/trade · progress 4/300 separate rounds
- ⚠️ Sample too small for any conclusion (n=4; under ~100 trades a 10-point swing in win rate is noise).
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
- ⚠️ workflow runs in 24h: 100, failed: 1 (polybot)

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
