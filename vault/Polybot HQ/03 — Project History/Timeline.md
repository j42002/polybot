---
polybot_auto: true
updated: 2026-11-27 01:29 UTC
tags: [history]
---
# 🗓️ Project Timeline

Built from the git history (routine data commits left out). Newest first.

## 2026-11-27
- `84c8892` maker15 data 2026-11-27T00:25Z
- `71c55fe` maker15 data 2026-11-27T01:21Z

## 2026-11-26
- `9c67126` vault sync 2026-11-26T01:27Z
- `c569858` vault sync 2026-11-26T01:33Z
- `c7d463e` Founder decisions: 12-minute rule refuted (#1), new strategy development paused (#4); logged in vault
- `7562309` Vault: rebuild after polybot/relay/checks runs (GitHub schedules barely fire); rewrite a note only when its content changed
- `72c31d2` vault sync 2026-11-26T07:58Z
- `9e350be` maker15: paper-only limit-order (maker) test on Kalshi BTC 15m
- `366a19f` vault sync 2026-11-26T08:42Z
- `ebb2a5b` vault sync 2026-11-26T09:24Z
- `d8bd25d` vault sync 2026-11-26T12:10Z
- `974adbc` vault sync 2026-11-26T13:07Z
- `c3352fe` maker15: start on merge and requeue itself (GitHub cron rarely fires here)
- `11e41f9` maker15 data 2026-11-26T15:10Z
- `595a253` maker15 data 2026-11-26T16:05Z
- `2a0210a` maker15 data 2026-11-26T17:01Z
- `3b45a04` maker15 data 2026-11-26T17:56Z
- `b15558f` vault sync 2026-11-26T18:44Z
- `1c6f9f3` maker15 data 2026-11-26T18:52Z
- `66299ac` maker15 data 2026-11-26T19:47Z
- `032fe0c` maker15 data 2026-11-26T20:43Z
- `58e3513` vault sync 2026-11-26T21:24Z
- `eb3f797` maker15 data 2026-11-26T21:38Z
- `806340a` maker15 data 2026-11-26T22:34Z
- `558ebb9` maker15 data 2026-11-26T23:29Z
- `17907c1` vault sync 2026-11-26T23:59Z

## 2026-11-25
- `d29516c` polybot v1: paper-only BTC 5m scout + grader + hourly Actions schedule
- `deaf2a4` Show live log output in Actions (unbuffered python)
- `28b2684` v2: price bets from the live order book only
- `028b328` v3: JJ strategy + Discord tickets
- `6c3fc42` Add one-click Discord test ticket workflow
- `6248d50` v4: tickets link straight to the contract
- `0962591` Test ticket links to the live window
- `f7aa516` v5: trade the Polymarket US app, not polymarket.com
- `95b4d6b` Self-queue the next 55-min run so coverage never depends on cron timing
- `966eb5e` Start a run whenever the bot code changes; chain runs from push/schedule too
- `b660faf` v6: visual ticket card + pair-sum logging
- `a16be46` Ticket: edge always green
- `20a8062` v7: SAFE strategy + ticket card v2
- `92ebbc5` Ticket: plain-English stat boxes and record line
- `f15f037` Ticket: say exactly what to tap and by when
- `16a8537` Ticket speaks the app's language
- `a910fd5` v8: one strong ticket per round + WIN/LOSS results
- `3e54b25` v9: read-only Polymarket US account watcher
- `1d34005` v10: latency-aware tickets (from Jacob's 6:40 recording)
- `a974235` One-click read-only account check
- `9c801ec` account check: seen-list
- `2e6c980` v11: cautious, self-tuning model + spike guard
- `1767bde` Fix data loss: runs start from latest main and merge data on save
- `441e907` v12: ChatGPT joins the team (second opinions + team board with Claude)
- `fb4aac7` v13: $0 AI team - Gemini free tier automatic, ChatGPT by hand
- `d577e81` v14: honest paper fills + measured timestamps (ChatGPT review #1)
- `428aba2` v15: measurement integrity (ChatGPT review #2)
- `ffcb6a5` v16: delivery proof, research funnel, forward test, account watcher off (ChatGPT review #3)
- `3d58f61` team board: account keys revoked and secrets removed
- `b1d064e` v17: log Coinbase close per round, grade it against the real settlement price
- `bf8fedf` v18: experiment start - sampling-gap checks, version split, research report (ChatGPT review #4)
- `31edd1e` Freeze the model for the experiment: no auto-tuning can change it
- `3037970` v19 bug fix: fall back to the order book when the BBO 404s on a live market
- `2a16d33` team board: assessment of the 15m '12-minute rule' experiment (no code)
- `389daf7` 15m Phase 1: pre-registration (frozen before any 15m result)
- `1ddd1b7` 15m Phase 1: read-only Kalshi backtest of the 12-minute rule (exploratory)
- `22b2b13` Research lab: strategy database on GitHub Issues, AI team roles, free Gemini reviews
- `86efa7b` Team relay: ChatGPT <-> Claude through issue comments, Discord notifications, loop guards
- `48f00bf` Polybot HQ: team/research Discord channels, 3 free check roles, Phase 1 results queued
- `9ecaa7c` Polybot HQ acceptance tests: one card per channel
- `66595f7` Issue #6: Polybot HQ status + acceptance test evidence
- `c851c04` Scoreboard: calibration uses 1 pre-specified check per settled v18+ round (was all checkpoints), labels rounds vs checks, drops the copy-paste prompt (ChatGPT review on #2)
- `d624b90` Polybot HQ Obsidian vault: vault_sync.py builds vault/Polybot HQ/ (12 folders, dashboard, team profiles, strategies, threads, reports, decisions, lessons, templates, graph colors) from GitHub every 3h; human notes never overwritten; secrets redacted
- `a068146` Vault: add Discoveries and Wins note + dashboard link
- `d7a7e3f` Risk Sentinel: verify each Discord webhook's channel with a read-only lookup (tickets → new #polybot-moves, team → #ai-team-chat, reports → #research-reports)

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
