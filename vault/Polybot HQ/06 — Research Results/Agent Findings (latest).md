---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [results, agents]
---
# 🧭 Agent Findings (latest)

# Polybot HQ specialist agents

Generated 2026-11-27 22:06 UTC. Deterministic Python checks, read-only, $0. Status 🟢 = self-test with planted failures passed AND the check ran on real data in this run. Nothing here changes a strategy or experiment.

| | Agent | Folded in | Job | Self-test | Flags |
|---|---|---|---|---|---|
| 🟢 | Velocity | Expiration Guard | Latency, quote lifetime, 30s deadline consistency | passed | 0 |
| 🟢 | Titan | Liquidity Intelligence | Size availability, fill volume, quote freshness | passed | 29 |
| 🟢 | Ghost | Market Stability Monitor (data) | Anomalies and missing data in public feeds | passed | 3 |
| 🟢 | Hawk | Market Stability Monitor (regimes) | Descriptive results by volatility / momentum | passed | 0 |
| 🟢 | Judge | Confidence Auditor, Profit Validator | Independent stats, calibration, simulated vs executable | passed | 0 |
| 🟢 | Nemesis | Loss Intelligence | Red-team challenges, every loss explained | passed | 5 |
| 🟢 | Oracle | - | Stress tests and simulated screening outcomes | passed | 0 |
| 🟢 | Chronos | - | Coverage timeline, gaps, versions, provenance | passed | 0 |
| 🔵 | Mirror | - | Venue fees and settlement definitions compared | passed | 0 |
| 🟢 | Overwatch | Mechanic | Workflow failures, data freshness, relay health | passed | 1 |
| 🟢 | Genesis | - | Pre-registration template and validator | passed | 1 |
| 🟢 | Evolution | - | Proposal-only hypotheses from measured patterns | passed | 0 |
| 🟢 | Cortex | Archive, Nexus | Shared registry for the vault and relay (this file's output) | passed | 0 |

Existing roles keep their duties: Data Auditor (team_checks.py), Quant Analyst (team_checks.py), Risk Sentinel (team_checks.py), Maker QC audit (audit_maker15.py), Relay (Nexus queue) (relay.py), Vault sync (Archive) (vault_sync.py)

## Velocity (+ Expiration Guard)

Delivered alerts watched: 95 · first price-crossing slot: 5s 66, 10s 2, 20s 4, 30s 3, 45s 2, 60s 3, none 15
Crossed only after the 30s deadline (45/60s): 5 · of those scored EXPIRED at 30s despite a 30s ask under the cap: **0** (must be 0)
30s check lateness: worst +0.90s (trusted up to +3s) · rows with no 30s check: 0
Discord delivery: median 684 ms, worst 2244 ms
Picks right 58/95 · same 20 tickets at every delay: 5s -44.85 · 10s -44.09 · 20s -43.39 · 30s -44.28 · dropouts 5s→30s: 9 (right 7)
v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.

## Titan (+ Liquidity Intelligence)

5m: 30s ask size logged on 95/95 alerts · size >= $10 at 30s: 90 yes / 5 no / 0 unknown. **Size units are not verified against the app, so 5m P&L is quote-availability only.**
Maker: through-volume / order size on fills: min 17x, median 15198x (volume never the constraint)
Maker quote freshness (from the read-only audit): recorded ask >5c from same-second prints on 22/55 orders; marketable at post 7/55

## Ghost (+ Market Stability Monitor (data))

5m checks with no market quote: 84/3031 (2.8%)
Up+Down asks outside 0.95-1.15 (broken or stale book): 0/2688
Coinbase proxy disagrees with the official settlement: 16/605 rounds (proxy only; official winner is used for scoring)
Runs whose longest BTC price gap exceeded 10s: 3/58
Maker: stale recorded quotes 22/55 (see Titan)

## Hawk (+ Market Stability Monitor (regimes))

| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 20 | 16 | 69% | -1.60 |
| maker | 1-min BTC move mid | 19 | 10 | 80% | +0.89 |
| maker | 1-min BTC move high | 19 | 13 | 92% | +2.68 |
| maker | distance to target low | 20 | 18 | 67% | +1.37 |
| maker | distance to target mid | 19 | 13 | 85% | -0.10 |
| maker | distance to target high | 19 | 8 | 100% | +0.54 |
| 5m | BTC volatility low | 32 alerts | 9 buyable at 30s | picks right 50% | -29.73 total |
| 5m | BTC volatility mid | 32 alerts | 6 buyable at 30s | picks right 62% | -14.15 total |
| 5m | BTC volatility high | 31 alerts | 5 buyable at 30s | picks right 71% | -0.40 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Judge (+ Confidence Auditor, Profit Validator)

**Maker (15m)**: 39 fills / 58 posted · screening 39/100 fills
P&L +35.91 · **per posted order +0.62** (95% by 4-hour blocks: -0.50 to +1.69, 9 blocks)
Win of fills 31/39 = 79.5% (95% 64%-89%) vs break-even 74.5% · contract-weighted 75.6% vs 69.0%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 20 simulated trades from 95 alerts · screening 20/100 · research 20/300
P&L -44.28 · per alert -0.466 · win 8/20 (22%-61%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 128/234 (48%-61%) · 60-70%: won 125/192 (58%-71%) · 70-80%: won 95/127 (67%-82%) · 80-90%: won 62/69 (81%-95%)
Brier: model 0.2104 vs market 0.2184 on 592 rounds (lower = sharper; sharper is not profit)

## Nemesis (+ Loss Intelligence)

**Challenges**
- Maker signal right on 86% of 58 posted orders, but the same AGREE signal won 78.1% (break-even 80.9%) on 2022 historical trades. Expect regression toward history.
- Adverse selection: fill rate 62% when right vs 100% when wrong. Unfilled 'wins' are not earnings.
- Price risk: 17 fills at 85c+ earn about +0.95 each when right; one loss costs up to -9.90. A high win rate on expensive contracts can still lose.
- Independence: 58 orders over 2 calendar day(s). Few independent periods: one regime can explain it all.
- 5m survivorship: picks right on 61% of all alerts but 40% of the ones still buyable at 30s.

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

## Oracle

Expected P&L per posted order at the live win rate (86%): +0.64
…at the historical AGREE win rate (78.1%): **-0.32**
…with the 0.0175 maker fee at the live rate: +0.61
Win probability needed to break even with this price mix and these fill rates: **80.8%**
If the true win rate were the historical 78.1%, the frozen 100-fill screen (+3 points) would still PASS in 54% of 2,000 simulations: the screen is a first look, not proof.
Assumes the observed fill rates (when right / when wrong) and price mix stay the same.

## Chronos

Maker windows logged 126 of ~126 in its span · coverage gaps over 22 min: 0
5m settled rounds recorded 679 · gaps over 7.5 min: 21 (longest 1.2 h)
5m ticket versions in the experiment: {'v19': 95}
Provenance: 5m prices = Polymarket US gateway (/bbo, /book fallback) · 5m winners = Polymarket US settlementPx · BTC = Coinbase · maker quotes = Kalshi /markets list · maker fills = Kalshi public trades · 15m history = Kalshi candles (Phase 1).

## Mirror

| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |
|---|---|---|
| Taker fee | round-up of 0.07 x C x P x (1-P) | 0.095 x P x (1-P) per share |
| Maker fee | only on listed series (0.0175); this series reads 'quadratic' (none) | not modelled (taker-only tests) |
| Settlement | BRTI 60s average | BRTI 60s average |
| Settlement agreement (Phase 1) | 696/696 windows identical | |
Matched events on two venues are the same event, not independent evidence.
Pending: a live price comparison needs a Polymarket US 15m quote at each maker post time (not collected).

## Overwatch (+ Mechanic)

**Flags:** team relay: 1 failed in 24h
Workflows active in the last 24h: 8 · runs 100 · failed 1
5m tickets data: last update 0.7 h ago (limit 6 h)
maker15 orders: last update 0.4 h ago (limit 3 h)
maker15 audit: last update 1.2 h ago (limit 6 h)
vault: last update 0.0 h ago (limit 6 h)
Relay: 12 requests tracked, 0 cards waiting for Discord

## Genesis

Template: lab/templates/PREREG_TEMPLATE.md
15m Phase 1 PREREG: missing: PASS/FAIL verdict rule (exploratory by design: it reports results but sets no PASS/FAIL)
maker15 PREREG: all required sections present

## Evolution

- 5m: correct calls are priced in within 5-30s. Hypothesis to pre-register later: alerts sent with more time left, or faster delivery, keep more correct calls buyable. Needs a Genesis PREREG and Jacob's approval.
- Maker: fills cluster in losing outcomes. Hypothesis: the edge, if any, is in the signal, not the resting price; compare with a taker baseline at real prices before any new maker variant.
- Maker: profit depends on the signal staying above its historical win rate. Track the live rate against history as fills grow; no change to the frozen test.
Proposal only. Nothing is tested, tuned or launched by Evolution. New strategy work is paused by Jacob (2026-11-26).

## Cortex (+ Archive, Nexus)

Writes lab/agents/status.json (read by vault_sync for agent profiles) and lab/agents/report.md; the relay request queue is Nexus's coordination list.

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
