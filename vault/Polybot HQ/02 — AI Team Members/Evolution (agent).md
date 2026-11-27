---
polybot_auto: true
updated: 2026-11-27 22:06 UTC
tags: [agents, agents/implemented]
---
# 🟢 Evolution

> [!abstract] 🟢 implemented · self-test passed
> Proposal-only hypotheses from measured patterns

## Latest findings
- 5m: correct calls are priced in within 5-30s. Hypothesis to pre-register later: alerts sent with more time left, or faster delivery, keep more correct calls buyable. Needs a Genesis PREREG and Jacob's approval.
- Maker: fills cluster in losing outcomes. Hypothesis: the edge, if any, is in the signal, not the resting price; compare with a taker baseline at real prices before any new maker variant.
- Maker: profit depends on the signal staying above its historical win rate. Track the live rate against history as fills grow; no change to the frozen test.
Proposal only. Nothing is tested, tuned or launched by Evolution. New strategy work is paused by Jacob (2026-11-26).

## Links
- [[Specialist Agents]] · [[System Blueprint]] · [[Brain Overview]]

---
*Auto-generated from GitHub by `vault_sync.py`. Edits here are overwritten; write your own notes in a new file.*
