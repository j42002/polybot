# Polybot Research Lab

A shared lab where the AI team submits trading ideas, checks the evidence and paper-tests the survivors.
**No strategy is trusted because a trader claims it works.** Budget $0. Paper trading only.
The live experiments (5m v18 in `agent.py`, 15m Phase 1 in `backtest15.py`) are not touched by the lab.

## The team

| Member | Role | How it takes part at $0 |
|---|---|---|
| Jacob | Founder: approves every stage change and every experiment | GitHub app on his phone |
| Claude | Lead developer: builds approved paper experiments | Writes code + this repo directly |
| ChatGPT | Research director: sets priorities, approves designs | Posts directly as issue comments through Jacob's GitHub connection (headed "ChatGPT → Claude") |
| Grok | Strategy scout: finds what public traders claim on X/TikTok/YouTube | Free app; output pasted as a new strategy issue |
| Perplexity | Fact-checker: finds original sources, checks claims, finds counter-evidence | Free app; output pasted as an issue comment |
| Gemini | Independent reviewer: automatic first review of every new strategy | Free API key; runs inside GitHub Actions |

ChatGPT posts its reviews straight to the issues (when Jacob opens a ChatGPT session). Claude and Gemini write on their own.
Grok and Perplexity have free chat apps but no free API, so their output is carried in (by Jacob, or by Claude in Jacob's
browser when he asks). Each has a paste-ready prompt in `lab/prompts/`.

## Team relay (no copy-paste)

- ChatGPT posts on GitHub (comments, or new issues). Within seconds the *team relay* workflow puts ONE status card per
  request in Discord **#ai-team-chat** and adds 👀 to the request on GitHub. The card is edited in place as it moves:
  📨 Received (delivered, not yet reviewed) → 🧠 Under review → ✅ Reviewed (links Claude's reply, shows response time)
  or ⚠️ Blocked (reason + next step). Ages use Discord timestamps, so "received 2 hours ago" stays current.
- Claude reviews **hourly** (scheduled task; the platform minimum is 1 hour), or **within minutes** in fast mode
  (`claude-fast.yml`, runs on Jacob's Claude subscription once he adds `CLAUDE_CODE_OAUTH_TOKEN`). Fast mode can only
  commit reply/status files that pass `relay.py validate`; it can't touch code, data, rules or workflows.
- Channels: **#polybot** = tickets only · **#ai-team-chat** = team conversation + status cards ·
  **#research-reports** = scoreboard, daily summary (8:30 PM ET), Data Auditor / Quant Analyst / Risk Sentinel.
  A missing team/report webhook means the message waits; it never falls back to #polybot.
- Guards: one card and at most one reply per request; max 12 Claude replies a day; after 3 exchanges on one issue in
  24h Claude waits for Jacob; bot comments can't trigger workflows, so there are no reply loops.
- ChatGPT's comments show as j42002 (Jacob's account), so no experiment, rule or stage changes from a comment alone:
  Jacob confirms those with Claude directly.
- The Obsidian vault `vault/Polybot HQ/` is rebuilt from GitHub every 3 hours (`vault_sync.py`, one-way, human notes kept).

## The database

Every strategy is one **GitHub Issue** made with the *Strategy submission* form. The issue is the record: claim, original
sources, exact rules, evidence, weaknesses, test plan, and every review as a comment. Labels track where it stands.
`lab/DATABASE.md` and `lab/strategies.csv` are rebuilt from the issues automatically.

## Pipeline (stage labels)

1. `stage:1-submitted`: a claim exists. Usually from Grok.
2. `stage:2-evidence`: Perplexity has looked for the original source, exact rules and counter-evidence.
3. `stage:3-review`: Gemini (automatically) and ChatGPT have challenged it. Claude has said whether it can be tested at $0.
4. `stage:4-preregistered`: rules frozen in writing before any result. ChatGPT + Jacob approved.
5. `stage:5-testing`: paper experiment running (historical = exploratory, forward = confirmatory).
6. `stage:6-verdict`: one of `verdict:supported`, `verdict:refuted`, `verdict:inconclusive`, `verdict:untestable`.

## Evidence levels

- `evidence:L0-claim`: someone says it works. Screenshots of wins count here.
- `evidence:L1-sourced`: original source found, rules written down exactly, conflicts of interest noted.
- `evidence:L2-historical`: survived an exploratory historical test after fees and realistic delay.
- `evidence:L3-forward`: survived a pre-registered forward paper test (300+ independent trades).

Only L3 counts as evidence that a strategy works. L2 only earns a forward test.

## Red flags (check every submission)

Sells a course, bot, signal group or referral code · shows wins but no losses · no exact rules · ignores fees ·
ignores reaction delay · tiny or cherry-picked sample · "works most of the time" (favourites win often and can still lose money).

## How a round works

1. Jacob asks Grok with `lab/prompts/grok.md` and pastes the result as a new issue (Strategy submission form).
2. Gemini reviews it automatically within minutes (once `GEMINI_API_KEY` is set).
3. Jacob asks Perplexity with `lab/prompts/perplexity.md` + the issue link and pastes the answer as a comment.
4. Jacob shares the issue with ChatGPT using `lab/prompts/chatgpt.md`, then pastes its decision as a comment.
5. If it is approved, Claude pre-registers and builds the paper test. Results go back on the issue.
