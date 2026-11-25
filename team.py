"""The AI team, $0 edition: Gemini (free tier) automatically, ChatGPT by hand.

Budget rule: nothing here can cost money.
- The only AI the bot calls is Gemini through a free Google AI Studio key.
  A key from a project with NO billing account stays on the free tier: when a
  limit is hit Google answers 429 and the bot just stops asking until tomorrow.
- No OpenAI or Anthropic API calls exist in this code.
- ChatGPT joins by hand: share.py posts a scoreboard picture + a ready prompt to
  Discord; Jacob pastes them into the free ChatGPT app. ChatGPT's reply can be
  pasted into data/chatgpt_notes.md, and Gemini reads it on the next board round.

Two jobs for Gemini:
1. Ticket second opinion: AGREE or PASS + a short reason, in a background thread
   (never delays or blocks a ticket). Saved as ai_verdict / ai_why in tickets.csv,
   scored by grade.py.
2. Team board (data/team_board.md): once per run Gemini reads the scoreboard, the
   board, and ChatGPT's notes, then writes one note with ONE testable idea.

Free-tier guard: a daily cap (GEMINI_DAILY_CAP, default 150) counted in
data/gemini_usage.json, reset at midnight Pacific like Google's quota, and a hard
stop for the rest of the day after any 429. Only public market numbers are sent:
free-tier prompts may be read by Google to improve its products.
"""
import json
import os
import re
import sys
import threading
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests

KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_OVERRIDE = os.getenv("GEMINI_MODEL", "")
DAILY_CAP = int(os.getenv("GEMINI_DAILY_CAP", "150"))
API = "https://generativelanguage.googleapis.com/v1beta"
BOARD = os.path.join("data", "team_board.md")
REPORT = os.path.join("data", "report.md")
NOTES = os.path.join("data", "chatgpt_notes.md")
USAGE = os.path.join("data", "gemini_usage.json")
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")

RESULTS = []                 # finished second opinions, drained by agent.py's main loop
_LOCK = threading.Lock()
_MODEL = None

ROLE = ("You are on a small paper-trading research team for Polymarket US 'BTC Up or Down 5 minute' "
        "markets. Teammates: a Python scout bot, Gemini (you), ChatGPT (shared by hand), Claude (builds the "
        "code), and Jacob, who places trades by hand in the app. Goal: a strategy that wins most of the time "
        "after fees, proven on 300+ paper bets before real money. Be skeptical, specific and brief. Plain "
        "English. A high model probability is not a guaranteed win; a big gap with the market is often a warning.")


def enabled():
    return bool(KEY)


# ---------- free-tier guard ----------

def _today_pt():
    return datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d")


def _usage():
    try:
        with open(USAGE, encoding="utf-8") as f:
            u = json.load(f)
    except Exception:
        u = {}
    if u.get("day") != _today_pt():
        u = {"day": _today_pt(), "calls": 0, "stopped": False}
    return u


def _save_usage(u):
    os.makedirs("data", exist_ok=True)
    with open(USAGE, "w", encoding="utf-8") as f:
        json.dump(u, f)


def _take_slot():
    """True if we may make one more call today. Counts it."""
    with _LOCK:
        u = _usage()
        if u["stopped"] or u["calls"] >= DAILY_CAP:
            return False
        u["calls"] += 1
        _save_usage(u)
        return True


def _stop_for_today():
    with _LOCK:
        u = _usage()
        u["stopped"] = True
        _save_usage(u)


# ---------- Gemini ----------

def _version(name):
    m = re.search(r"gemini-(\d+(?:\.\d+)?)", name)
    return float(m.group(1)) if m else 0.0


def pick_model():
    """Newest stable Flash-Lite (largest free daily quota), else newest stable Flash. Listing is free."""
    global _MODEL
    if _MODEL:
        return _MODEL
    if MODEL_OVERRIDE:
        _MODEL = MODEL_OVERRIDE
        return _MODEL
    try:
        r = requests.get(f"{API}/models", params={"pageSize": 200}, headers={"x-goog-api-key": KEY}, timeout=15)
        names = [m["name"].split("/", 1)[-1] for m in r.json().get("models", [])
                 if "generateContent" in m.get("supportedGenerationMethods", [])]
    except Exception:
        names = []
    bad = ("preview", "exp", "tts", "image", "live", "audio", "embedding", "thinking", "latest")
    stable = [n for n in names if n.startswith("gemini-") and not any(b in n for b in bad)]
    for kind in ("flash-lite", "flash"):
        c = [n for n in stable if n.endswith(kind) or n.endswith(kind + "-001")]
        if kind == "flash":
            c = [n for n in c if "lite" not in n]
        if c:
            _MODEL = max(c, key=_version)
            return _MODEL
    _MODEL = "gemini-flash-lite-latest"     # Google's moving alias, last resort
    return _MODEL


def ask_gemini(prompt, want_json=False, timeout=40):
    if not enabled():
        raise RuntimeError("no GEMINI_API_KEY")
    if not _take_slot():
        raise RuntimeError("free daily cap reached")
    body = {"systemInstruction": {"parts": [{"text": ROLE}]},
            "contents": [{"role": "user", "parts": [{"text": prompt}]}]}
    if want_json:
        body["generationConfig"] = {"responseMimeType": "application/json"}
    r = requests.post(f"{API}/models/{pick_model()}:generateContent", timeout=timeout,
                      headers={"x-goog-api-key": KEY}, json=body)
    if r.status_code == 429:
        _stop_for_today()                   # free quota used up: wait for the Pacific midnight reset
        raise RuntimeError("Gemini free limit hit (429) - paused until tomorrow")
    if r.status_code != 200:
        raise RuntimeError(f"Gemini HTTP {r.status_code}")    # code only: never echo the key
    parts = r.json()["candidates"][0]["content"].get("parts", [])
    return "".join(p.get("text", "") for p in parts if not p.get("thought")).strip()


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
        out = ask_gemini("The scout bot just sent this paper ticket. Would you take it? Answer JSON only: "
                         '{"verdict": "AGREE" or "PASS", "why": "max 20 words, plain English"}\n'
                         + json.dumps(facts), want_json=True)
        d = json.loads(out)
        verdict = "AGREE" if str(d.get("verdict", "")).upper().startswith("A") else "PASS"
        why = str(d.get("why", ""))[:160]
    except Exception as e:
        verdict, why = "SKIP", str(e)[:80]
    with _LOCK:
        RESULTS.append({"t_start": t_start, "ai_verdict": verdict, "ai_why": why, "ai_model": _MODEL or ""})


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
    if r["ai_verdict"] == "SKIP":
        return None                                   # cap hit or error: stay quiet in Discord
    icon = {"AGREE": "👍", "PASS": "✋"}[r["ai_verdict"]]
    return f"{icon} **Gemini: {r['ai_verdict']}** - {r['ai_why']}  _(paper test, does not change the ticket)_"


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
            f.write("# Team board\nGemini, ChatGPT and Claude talk here about the bot. Newest at the bottom.\n")
        f.write(f"\n### {stamp} · {who}\n{text.strip()}\n")


def board_round():
    """Gemini writes one note per run. Costs 1 free request."""
    if not enabled():
        print("team board: no GEMINI_API_KEY - Gemini is off")
        return
    try:
        note = ask_gemini("Latest scoreboard:\n" + _read(REPORT, 6000) +
                          "\n\nLatest team board:\n" + _read(BOARD, 4000) +
                          "\n\nLatest notes from ChatGPT (pasted by Jacob):\n" + (_read(NOTES, 2000) or "(none)") +
                          "\n\nWrite your note to the team (max 120 words): answer any question asked of you, say "
                          "what in the numbers worries you or looks promising, and propose ONE concrete, testable "
                          "change. End with one question for ChatGPT or Claude.")
    except Exception as e:
        print(f"team board: Gemini skipped ({e})")
        return
    _append(f"Gemini ({_MODEL})", note)
    print(f"team board: Gemini wrote a note ({_MODEL}, {_usage()['calls']}/{DAILY_CAP} free calls today)")
    if WEBHOOK:
        try:
            requests.post(WEBHOOK, json={"content": f"🧠 **Team board** · Gemini\n{note}"[:1900]}, timeout=6)
        except Exception:
            pass


if __name__ == "__main__":
    if sys.argv[1:] == ["board"]:
        board_round()
    elif sys.argv[1:] == ["model"]:
        print(pick_model() if enabled() else "no GEMINI_API_KEY")
