---
polybot_auto: true
updated: 2026-11-26 01:33 UTC
tags: [strategy]
---
# Issue 5 — Halfway leader buy the side ahead at 730 of a BTC 15m window

> [!abstract] Status
> **stage:1-submitted, evidence:L0-claim** · [open on GitHub](https://github.com/j42002/polybot/issues/5) · 3 comments

## Submission
### Submitted by

Grok (strategy scout)

### Market

Kalshi KXBTC15M; Polymarket US BTC Up/Down 15m

### The claim, in the source's own terms

"The side ahead at halfway won 75% of the time; strong leaders (70c+) returned a small positive edge before fees." Author says +2.2% (Kalshi) / +1.6% (Polymarket) modeled return on stake for 70c+ leaders before fees, about +1.0% on Kalshi after its taker fee. Modeled, not live P&L.

### Original sources

Reddit r/PredictionMarkets: "I logged 6,532 15-minute bitcoin markets on Kalshi" https://www.reddit.com/r/PredictionMarkets/comments/1x2uuwr/i_logged_6532_15minute_bitcoin_markets_on_kalshi (posted ~10 Oct 2026, per Grok). Grok reports no course, bot, signal group or referral code. NOT YET VERIFIED by Perplexity: link, date and numbers come from Grok.

### Exact rules (as testable as possible)

Entry: 7:30 into the 15-minute window. Signal: the side priced above 50c (the leader); preferred variant: leader at 70c or more. Side: buy the leader. Price limit: UNSPECIFIED (author used mid/last price, not the ask). Exit: hold to settlement.

### Supporting evidence

Author logged every settled BTC 15m window on both venues 6 Sep - 10 Oct 2026 (6,532 windows). Leader at 7:30 won 2,440/3,242 on Kalshi (75.2%) and 2,449/3,260 on Polymarket (75.1%). 70c+ leaders won ~85.2-85.3% at average prices 83.4-83.9c. Data not published as far as Grok reports; numbers unverified.

### Weaknesses and red flags

Modeled on mid/last prices, not executable asks: paying the ask (+1c or more) and the fee could erase a 1-2c edge. Only ~5 weeks of data, no out-of-sample or live check. The author himself says the market looks roughly efficient overall (leaders priced near their win rate). No reaction delay modeled. Same family as the 12-minute rule (#1): favourites win often by construction; profit needs under-pricing.

### How could we paper-test it at $0?

Kalshi public 1-minute candles (yes ask/bid) for every settled KXBTC15M market, as in backtest15.py: leader = side with ask above 50c at 7:30, entry = ask about 60s later, Kalshi taker fee, hold to settlement. Compare win rate with break-even (ask + fee), overall and for 70c+ leaders, by week/volatility/session. Fail = no positive P&L after fees at the ask.

## Discussion
Full thread: [[Issue 5 — Halfway leader buy the side ahead at 730 of a BTC 15m window (thread)]]

## Related
- [[Strategy Library]] · [[Experiment Registry]] · [[Evidence Levels]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
