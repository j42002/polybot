"""The AI team: ChatGPT and Claude talk to each other about the bot.

Two channels:
1. Ticket second opinion: after each ticket goes out, ChatGPT reads the same facts
   and answers AGREE or PASS with a short reason. Posted under the ticket in Discord
   and saved to tickets.csv (gpt_verdict, gpt_why) so grade.py can score ChatGPT.
   It runs in a background thread, so it never slows a ticket down, and it never
   blocks one. Paper experiment: we learn whether its PASSes would have saved money.
2. Team board (data/team_board.md): after each run, ChatGPT reads the scoreboard
   plus the latest board notes and writes a note to Claude. If ANTHROPIC_API_KEY is
   set, Claude answers on the board right away. Claude in chat or the Claude
   Project reads and writes the same file, so the conversation carries over.

Each AI turns on only when its key is in the repo secrets:
  OPENAI_API_KEY (ChatGPT)    ANTHROPIC_API_KEY (Claude replies on the board)
Optional: OPENAI_MODEL (default gpt-5-mini), ANTHROPIC_MODEL (default claude-haiku-5-5).
Nothing private goes to either AI: market numbers and the public scoreboard only.
"""
import json
import os
import sys
import threading
from datetime import datetime, timezone

import requests

OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-5-5")
BOARD = os.path.join("data", "team_board.md")
REPORT = os.path.join("data", "report.md")
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")

RESULTS = []                 # finished second opinions, drained by agent.py's main loop
_LOCK = threading.Lock()

ROLE = ("You are on a small paper-trading research team for Polymarket US 'BTC Up or Down 5 minute' "
        "markets. Teammates: a Python scout bot, Claude (Anthropic), ChatGPT (OpenAI), and Jacob, the human "
        "who places trades by hand on the app. Goal: a strategy that wins most of the time after fees, "
        "proven on 300+ paper bets before real money. Be skeptical, specific and brief. Plain English. "
        "A high model probability is not a guaranteed win; a big gap with the market is often a warning.")


def enabled():
    return bool(OPENAI_KEY)


def ask_chatgpt(messages, want_json=False, timeout=40):
    body = {"model": OPENAI_MODEL, "messages": messages}
    if want_json:
        body["response_format"] = {"type": "json_object"}
    r = requests.post("https://api.openai.com/v1/chat/completions", timeout=timeout,
                      headers={"Authorization": f"Bearer {OPENAI_KEY}"}, json=body)
    if r.status_code != 200:
        raise RuntimeError(f"OpenAI HTTP {r.status_code}")      # code only: never echo headers or keys
    return r.json()["choices"][0]["message"]["content"].strip()


def ask_claude(system, user, timeout=40):
    r = requests.post("https://api.anthropic.com/v1/messages", timeout=timeout,
                      headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"},
                      json={"model": ANTHROPIC_MODEL, "max_tokens": 500, "system": system,
                            "messages": [{"role": "user", "content": user}]})
    if r.status_code != 200:
        raise RuntimeError(f"Anthropic HTTP {r.status_code}")
    return "".join(b.get("text", "") for b in r.json().get("content", [])).strip()


# ---------- 1. ticket second opinion ----------

def ticket_facts(row, secs_left, recent):
    side = row["jj_side"]
    p_up = float(row["model_up"])
    path = [round(p) for _, p in recent[::15]][-12:]          # ~30s steps over the last few minutes
    return {
        "bet": f"Buy {side} at {float(row['jj_price']):.0%}",
        "timer_left": f"{secs_left // 60}:{secs_left % 60:02d}",
        "target_price": row.get("ptb_proxy"),
        "btc_now": row.get("spot"),
        "btc_minus_target": row.get("dist"),
        "btc_change_last_60s": row.get("mom60"),
        "bot_win_chance": f"{(p_up if side == 'Up' else 1 - p_up):.0%}",
        "market_price": f"{float(row['jj_price']):.0%}",
        "bot_edge_after_fee": f"{float(row['jj_ev']):+.1%}",
        "btc_path_30s_steps": path,
        "settles_on": "60-second average of BTC in the last minute vs the target",
    }


def _second_opinion(t_start, facts):
    try:
        out = ask_chatgpt([
            {"role": "system", "content": ROLE},
            {"role": "user", "content":
                "The scout bot just sent this paper ticket. Would you take it? Answer JSON only: "
                '{"verdict": "AGREE" or "PASS", "why": "max 20 words, plain English"}\n'
                + json.dumps(facts)}], want_json=True)
        d = json.loads(out)
        verdict = "AGREE" if str(d.get("verdict", "")).upper().startswith("A") else "PASS"
        why = str(d.get("why", ""))[:160]
    except Exception as e:
        verdict, why = "ERROR", str(e)[:80]
    with _LOCK:
        RESULTS.append({"t_start": t_start, "gpt_verdict": verdict, "gpt_why": why})


def second_opinion(t_start, row, secs_left, recent):
    """Fire and forget: the ticket is already out, this never delays or blocks it."""
    if not enabled():
        return
    threading.Thread(target=_second_opinion, daemon=True,
                     args=(t_start, ticket_facts(row, secs_left, recent))).start()


def drain():
    with _LOCK:
        out, RESULTS[:] = list(RESULTS), []
    return out


def opinion_text(r):
    icon = {"AGREE": "👍", "PASS": "✋"}.get(r["gpt_verdict"], "⚠️")
    return f"{icon} **ChatGPT: {r['gpt_verdict']}** - {r['gpt_why']}  _(paper test, does not change the ticket)_"


# ---------- 2. team board ----------

def _read(path, tail_chars=None):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        s = f.read()
    return s[-tail_chars:] if tail_chars else s


def _append(who, text):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    new = not os.path.exists(BOARD)
    with open(BOARD, "a", encoding="utf-8") as f:
        if new:
            f.write("# Team board\nChatGPT and Claude talk here about the bot. Newest at the bottom.\n")
        f.write(f"\n### {stamp} · {who}\n{text.strip()}\n")


def _discord(text):
    if WEBHOOK:
        try:
            requests.post(WEBHOOK, json={"content": text[:1900]}, timeout=6)
        except Exception:
            pass


def board_round():
    """ChatGPT writes to Claude; Claude (if keyed) writes back. Called once per run."""
    if not enabled():
        print("team board: no OPENAI_API_KEY - ChatGPT is off")
        return
    report, board = _read(REPORT, 6000), _read(BOARD, 5000)
    try:
        gpt = ask_chatgpt([
            {"role": "system", "content": ROLE},
            {"role": "user", "content":
                "Latest scoreboard:\n" + report + "\n\nLatest team board:\n" + board +
                "\n\nWrite your note to Claude (max 120 words): answer anything Claude asked you, "
                "say what in the numbers worries you or looks promising, and propose ONE concrete, "
                "testable change. End with one question for Claude."}])
    except Exception as e:
        print(f"team board: ChatGPT failed ({e})")
        return
    _append("ChatGPT → Claude", gpt)
    print("team board: ChatGPT wrote a note")
    msg = f"🧠 **Team board** · ChatGPT → Claude\n{gpt}"
    if ANTHROPIC_KEY:
        try:
            claude = ask_claude(ROLE, "Latest scoreboard:\n" + report + "\n\nTeam board:\n" + _read(BOARD, 5000) +
                                "\n\nReply to ChatGPT's latest note (max 120 words). Agree or push back with "
                                "reasons from the numbers, and say whether its proposed change should be tested.")
            _append("Claude → ChatGPT", claude)
            msg += f"\n\n🧠 Claude → ChatGPT\n{claude}"
            print("team board: Claude replied")
        except Exception as e:
            print(f"team board: Claude failed ({e})")
    _discord(msg)


if __name__ == "__main__":
    if sys.argv[1:] == ["board"]:
        board_round()
