---
polybot_auto: true
updated: 2026-11-28 00:49 UTC
tags: [agents, agents/implemented]
---
# 🟢 Nemesis

> [!abstract] 🟢 implemented · self-test passed
> Red-team challenges, every loss explained
> Folded in: Loss Intelligence

## Latest findings
**Challenges**
- Maker signal right on 83% of 65 posted orders, but the same AGREE signal won 78.1% (break-even 80.9%) on 2022 historical trades. Expect regression toward history.
- Adverse selection: fill rate 59% when right vs 100% when wrong. Unfilled 'wins' are not earnings.
- Price risk: 17 fills at 85c+ earn about +0.95 each when right; one loss costs up to -9.96. A high win rate on expensive contracts can still lose.
- Independence: 65 orders over 2 calendar day(s). Few independent periods: one regime can explain it all.
- 5m survivorship: picks right on 61% of all alerts but 46% of the ones still buyable at 30s.

**Every loss (Loss Intelligence)**
| Test | Market | Entry | P&L | Time | Context | Context | Fill |
|---|---|---|---|---|---|---|---|
| maker | M-26NOV261145-45 | Down at 0.52 x19 | -9.88 | 11h ET | move 45 | dist 7 | filled +1s |
| maker | M-26NOV261845-45 | Down at 0.45 x22 | -9.90 | 18h ET | move 10 | dist 8 | filled +84s |
| maker | M-26NOV262000-00 | Up at 0.51 x19 | -9.69 | 19h ET | move 12 | dist 3 | filled +14s |
| maker | M-26NOV262030-30 | Down at 0.82 x12 | -9.84 | 20h ET | move 6 | dist 58 | filled +1s |
| maker | M-26NOV270415-15 | Up at 0.58 x17 | -9.86 | 04h ET | move 9 | dist 27 | filled +27s |
| maker | M-26NOV271215-15 | Down at 0.61 x16 | -9.76 | 12h ET | move 22 | dist 31 | filled +1s |
| maker | M-26NOV271545-45 | Down at 0.95 x10 | -9.50 | 15h ET | move 9 | dist 68 | filled +45s |
| maker | M-26NOV271600-00 | Up at 0.56 x17 | -9.52 | 15h ET | move 7 | dist 4 | filled +1s |
| maker | M-26NOV271700-00 | Up at 0.66 x15 | -9.90 | 16h ET | move 17 | dist 2 | filled +4s |
| maker | M-26NOV271745-45 | Down at 0.83 x12 | -9.96 | 17h ET | move 6 | dist 55 | filled +1s |
| maker | M-26NOV271845-45 | Down at 0.55 x18 | -9.90 | 18h ET | move 1 | dist 10 | filled +1s |
| 5m | 1-25-2005z | Up at 0.3 | -10.66 | 15h ET | alert 0.42 cap 0.52 | 237.3s left | - |
| 5m | 1-25-2240z | Up at 0.33 | -10.64 | 17h ET | alert 0.37 cap 0.5 | 205.2s left | - |
| 5m | 1-26-0755z | Up at 0.39 | -10.58 | 02h ET | alert 0.37 cap 0.41 | 238.1s left | - |
| 5m | 1-26-1215z | Down at 0.38 | -10.59 | 07h ET | alert 0.41 cap 0.54 | 237.9s left | - |
| 5m | 1-26-1225z | Down at 0.36 | -10.61 | 07h ET | alert 0.39 cap 0.45 | 207.9s left | - |
| 5m | 1-26-1935z | Down at 0.74 | -10.25 | 14h ET | alert 0.69 cap 0.75 | 207.8s left | - |
| 5m | 1-27-0730z | Down at 0.36 | -10.61 | 02h ET | alert 0.35 cap 0.48 | 206.5s left | - |
| 5m | 1-27-0930z | Down at 0.37 | -10.60 | 04h ET | alert 0.36 cap 0.42 | 206.9s left | - |
| 5m | 1-27-1020z | Down at 0.62 | -10.36 | 05h ET | alert 0.69 cap 0.74 | 236.4s left | - |
| 5m | 1-27-1930z | Down at 0.41 | -10.56 | 14h ET | alert 0.53 cap 0.61 | 236.9s left | - |
| 5m | 1-27-1955z | Down at 0.49 | -10.48 | 14h ET | alert 0.5 cap 0.54 | 206.9s left | - |
| 5m | 1-27-2025z | Down at 0.43 | -10.54 | 15h ET | alert 0.44 cap 0.5 | 206.9s left | - |
| 5m | 1-27-2345z | Down at 0.46 | -10.51 | 18h ET | alert 0.56 cap 0.63 | 206.9s left | - |

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
