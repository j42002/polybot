# polybot

Paper-trading scout for **Polymarket US** (the app) **BTC Up or Down 5m** markets. Set `VENUE=intl` to scan polymarket.com instead.

Polymarket US is a separate exchange: own order book, settles on CF Benchmarks BRTI (not Chainlink), fee coefficient 0.095. polybot reads its public gateway (no key): the real price to beat, live Up/Down prices, and settled results. Log-only: it never places orders and needs no keys.

## What it does
- `agent.py`: watches BTC (Coinbase, every 2s) and the live Polymarket odds. At 3:00, 2:00 and 1:00 left in every window it paper-bets 3 strategies:
  - **mom**: bets the direction of the last 60 seconds
  - **lean**: bets the side BTC is on right now (follows the crowd favorite)
  - **edge**: bets only when the model's probability beats the ask by 3c+ after fees (the same idea the profitable latency bots use, run slower)
- `grade.py`: pulls the real result plus the real Chainlink price to beat, then scores every bet after the taker fee (`0.05 * p * (1-p)` per share).
- `data/report.md`: the scoreboard. Open it on GitHub from your phone.

## Rules fixed in advance
- Under 300 bets: INCONCLUSIVE
- 95% CI above 0 after fees: PASSES
- 95% CI below 0: LOSES
- Otherwise: NO EDGE
- Beating 50% means nothing. A bet bought at 73c has to win more than 73% of the time just to break even.

## Runs itself
GitHub Actions starts it every 20 minutes and each run lasts 55 minutes, so it runs around the clock. The repo is public because Actions minutes are free and unlimited on public repos. A private repo gets 2,000 minutes a month, which this would use up in about 2 days.
