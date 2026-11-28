---
polybot_auto: true
updated: 2026-11-28 08:51 UTC
tags: [results, agents]
---
# 🧭 Agent Findings (latest)

# Polybot HQ specialist agents

Generated 2026-11-28 08:51 UTC. Deterministic Python checks, read-only, $0. Status 🟢 = self-test with planted failures passed AND the check ran on real data in this run. Nothing here changes a strategy or experiment.

| | Agent | Folded in | Job | Self-test | Flags |
|---|---|---|---|---|---|
| 🟢 | Velocity | Expiration Guard | Latency, quote lifetime, 30s deadline consistency | passed | 0 |
| 🟢 | Titan | Liquidity Intelligence | Size availability, fill volume, quote freshness | passed | 37 |
| 🟢 | Ghost | Market Stability Monitor (data) | Anomalies and missing data in public feeds | passed | 4 |
| 🟢 | Hawk | Market Stability Monitor (regimes) | Descriptive results by volatility / momentum | passed | 0 |
| 🟢 | Judge | Confidence Auditor, Profit Validator | Independent stats, calibration, simulated vs executable | passed | 0 |
| 🟢 | Nemesis | Loss Intelligence | Red-team challenges, every loss explained | passed | 5 |
| 🟢 | Oracle | - | Stress tests and simulated screening outcomes | passed | 0 |
| 🟢 | Chronos | - | Coverage timeline, gaps, versions, provenance | passed | 0 |
| 🟢 | Mirror | - | Kalshi vs Polymarket US: fees, settlement and same-moment prices | passed | 0 |
| 🟢 | Overwatch | Mechanic | Workflow failures, data freshness, relay health | passed | 0 |
| 🟢 | Genesis | - | Pre-registration template and validator | passed | 1 |
| 🟢 | Evolution | - | Proposal-only hypotheses from measured patterns | passed | 0 |
| 🟢 | Cortex | Archive, Nexus | Shared registry for the vault and relay (this file's output) | passed | 0 |

Existing roles keep their duties: Data Auditor (team_checks.py), Quant Analyst (team_checks.py), Risk Sentinel (team_checks.py), Maker QC audit (audit_maker15.py), Relay (Nexus queue) (relay.py), Vault sync (Archive) (vault_sync.py)

## Velocity (+ Expiration Guard)

Delivered alerts watched: 121 · first price-crossing slot: 5s 81, 10s 2, 20s 5, 30s 5, 45s 4, 60s 4, none 20
Crossed only after the 30s deadline (45/60s): 8 · of those scored EXPIRED at 30s despite a 30s ask under the cap: **0** (must be 0)
30s check lateness: worst +0.90s (trusted up to +3s) · rows with no 30s check: 0
Discord delivery: median 648 ms, worst 2244 ms
Picks right 75/120 · same 27 tickets at every delay: 5s -17.61 · 10s -19.54 · 20s -14.45 · 30s -11.35 · dropouts 5s→30s: 12 (right 9)
v20 (Nov 27): the card now says CLOSED at 30s; later checks are kept as diagnostics and no longer edit the card.
v21 (Nov 28): wording only: 'model estimate' instead of 'win chance', no buy-now language, paper window close time on the card.

## Titan (+ Liquidity Intelligence)

5m: 30s ask size logged on 121/121 alerts · size >= $10 at 30s: 110 yes / 11 no / 0 unknown. **Size units are not verified against the app, so 5m P&L is quote-availability only.**
Maker: through-volume / order size on fills: min 17x, median 21204x (volume never the constraint)
Maker quote freshness (from the read-only audit): recorded ask >5c from same-second prints on 28/70 orders; marketable at post 9/70

## Ghost (+ Market Stability Monitor (data))

5m checks with no market quote: 98/3654 (2.7%)
Up+Down asks outside 0.95-1.15 (broken or stale book): 0/3250
Coinbase proxy disagrees with the official settlement: 20/727 rounds (proxy only; official winner is used for scoring)
Runs whose longest BTC price gap exceeded 10s: 4/70
Maker: stale recorded quotes 28/70 (see Titan)

## Hawk (+ Market Stability Monitor (regimes))

| Test | Regime | posted | filled | win of fills | P&L per posted |
|---|---|---|---|---|---|
| maker | 1-min BTC move low | 28 | 21 | 67% | -1.83 |
| maker | 1-min BTC move mid | 27 | 16 | 75% | +1.04 |
| maker | 1-min BTC move high | 26 | 16 | 94% | +2.26 |
| maker | distance to target low | 28 | 22 | 64% | +1.39 |
| maker | distance to target mid | 27 | 21 | 81% | -0.55 |
| maker | distance to target high | 26 | 10 | 100% | +0.46 |
| 5m | BTC volatility low | 41 alerts | 13 buyable at 30s | picks right 56% | -31.39 total |
| 5m | BTC volatility mid | 40 alerts | 6 buyable at 30s | picks right 62% | +30.41 total |
| 5m | BTC volatility high | 39 alerts | 8 buyable at 30s | picks right 69% | -10.37 total |
Cells are small and regimes were cut after the fact: description, not findings.

## Judge (+ Confidence Auditor, Profit Validator)

**Maker (15m)**: 53 fills / 81 posted · screening 53/100 fills
P&L +35.67 · **per posted order +0.44** (95% by 4-hour blocks: -0.44 to +1.41, 12 blocks)
Win of fills 41/53 = 77.4% (95% 64%-87%) vs break-even 74.6% · contract-weighted 72.6% vs 67.8%
Profit Validator: SIMULATED. Fills are a trade-through proxy (conservative on volume) but posted limits used stale quotes on some orders; queue position unknown. Not executable-verified.
**5-minute**: 27 simulated trades from 120 alerts · screening 27/100 · research 27/300
P&L -11.35 · per alert -0.095 · win 13/27 (31%-66%) vs break-even 49%
Profit Validator: SIMULATED quote availability at 30s; ask size units unverified. Not executable-verified.
Confidence Auditor (model estimate vs outcome, 1 check per round): 50-60%: won 158/280 (51%-62%) · 60-70%: won 157/238 (60%-72%) · 70-80%: won 110/145 (68%-82%) · 80-90%: won 77/86 (81%-94%)
Brier: model 0.2078 vs market 0.2152 on 714 rounds (lower = sharper; sharper is not profit)

## Nemesis (+ Loss Intelligence)

**Challenges**
- Maker signal right on 85% of 81 posted orders, but the same AGREE signal won 78.1% (break-even 80.9%) on 2022 historical trades. Expect regression toward history.
- Adverse selection: fill rate 59% when right vs 100% when wrong. Unfilled 'wins' are not earnings.
- Price risk: 24 fills at 85c+ earn about +0.90 each when right; one loss costs up to -9.96. A high win rate on expensive contracts can still lose.
- Independence: 81 orders over 3 calendar day(s). Few independent periods: one regime can explain it all.
- 5m survivorship: picks right on 62% of all alerts but 48% of the ones still buyable at 30s.

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
| maker | M-26NOV272315-15 | Down at 0.34 x29 | -9.86 | 23h ET | move 3 | dist 6 | filled +40s |
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
| 5m | 1-28-0340z | Down at 0.52 | -10.46 | 22h ET | alert 0.52 cap 0.57 | 236.4s left | - |

## Oracle

Expected P&L per posted order at the live win rate (85%): +0.48
…at the historical AGREE win rate (78.1%): **-0.36**
…with the 0.0175 maker fee at the live rate: +0.45
Win probability needed to break even with this price mix and these fill rates: **81.1%**
If the true win rate were the historical 78.1%, the frozen 100-fill screen (+3 points) would still PASS in 55% of 2,000 simulations: the screen is a first look, not proof.
Assumes the observed fill rates (when right / when wrong) and price mix stay the same.

## Chronos

Maker windows logged 170 of ~170 in its span · coverage gaps over 22 min: 0
5m settled rounds recorded 806 · gaps over 7.5 min: 26 (longest 1.2 h)
5m ticket versions in the experiment: {'v19': 99, 'v20': 6, 'v21': 16}
Provenance: 5m prices = Polymarket US gateway (/bbo, /book fallback) · 5m winners = Polymarket US settlementPx · BTC = Coinbase · maker quotes = Kalshi /markets list · maker fills = Kalshi public trades · 15m history = Kalshi candles (Phase 1).

## Mirror

| | Kalshi KXBTC15M | Polymarket US BTC 15m / 5m |
|---|---|---|
| Taker fee | round-up of 0.07 x C x P x (1-P) | feeCoefficient x P x (1-P) per share (5m bot assumes 0.095) |
| Maker fee | only on listed series (0.0175); this series reads 'quadratic' (none) | not modelled (taker-only tests) |
| Settlement | BRTI 60s average | BRTI 60s average |
| Settlement agreement (Phase 1) | 696/696 windows identical | |
Matched events on two venues are the same event, not independent evidence.
Live snapshots at the maker decision time: 30 · Polymarket US quote found: 21 · missing {'event_none': 9}
Same moment: the two reads are at most 0.06s apart.
Maker's chosen side, ask on both venues: 10 pairs · Polymarket minus Kalshi: median -0.4c, mean -1.6c · Polymarket cheaper 5, same 2, Kalshi cheaper 3 · gaps of 5c or more: 3
Quoted prices before fees. Small sample: descriptive only, no PASS/FAIL rule.
Polymarket US feeCoefficient seen live: 15m [0.11] · 5m [0.11] (the 5m bot scores with 0.095)

## Overwatch (+ Mechanic)

No health flags.
Workflows active in the last 24h: 8 · runs 100 · failed 0
5m tickets data: last update 0.4 h ago (limit 6 h)
maker15 orders: last update 0.0 h ago (limit 3 h)
maker15 audit: last update 5.4 h ago (limit 6 h)
vault: last update 4.1 h ago (limit 6 h)
Relay: 14 requests tracked, 0 cards waiting for Discord

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
