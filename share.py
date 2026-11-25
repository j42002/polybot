"""Scoreboard picture + ready-made prompt for sharing with ChatGPT by hand ($0: free ChatGPT app).

python share.py          -> build data/share/scoreboard.png + chatgpt_prompt.txt and post both to Discord
python share.py --daily  -> same, but only once per day (first run after 8 PM Eastern)

Jacob copies the prompt + picture into the ChatGPT app. ChatGPT's answer can be pasted
into data/chatgpt_notes.md (GitHub web editor), and Gemini reads it on its next board note.
"""
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

OUT = os.path.join("data", "share")
STATE = os.path.join("data", "share_state.json")
WEBHOOK = os.getenv("DISCORD_WEBHOOK", "")
ET = ZoneInfo("America/New_York")


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def med(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


EXP_MIN = 18                                   # experiment rows only (same rule as grade.py)


def _exp(rs):
    import re
    out = []
    for r in rs:
        m = re.search(r"v(\d+)", str(r.get("version") or ""))
        if m and int(m.group(1)) >= EXP_MIN:
            out.append(r)
    return out


def stats():
    t = _exp(rows(os.path.join("data", "tickets.csv")))
    done = [r for r in t if r.get("result") in ("WIN", "LOSS", "MISSED")]
    wl = [r for r in done if r["result"] in ("WIN", "LOSS")]
    wins = sum(r["result"] == "WIN" for r in wl)
    pnl = sum(float(r.get("pnl10") or 0) for r in done)
    fee = 0.095                                              # Polymarket US taker fee coefficient
    prices = [float(r["fill_price"]) * (1 + fee * (1 - float(r["fill_price"]))) for r in wl if r.get("fill_price")]
    lag = [float(r["t_sent"]) - float(r["t_spot"]) for r in t if r.get("t_sent") and r.get("t_spot")]
    watched = [r for r in t if r.get("status")]
    fill = sum(r["status"] == "FILLABLE" for r in watched)
    ai = {}
    for v in ("AGREE", "PASS"):
        g = [r for r in wl if r.get("ai_verdict") == v]
        if g:
            ai[v] = (len(g), sum(r["result"] == "WIN" for r in g), sum(float(r.get("pnl10") or 0) for r in g))
    # calibration: favored side's model chance vs how often it won (all graded checkpoints)
    res = {r["slug"]: r.get("winner", "") for r in rows(os.path.join("data", "results.csv"))}
    bk = defaultdict(list)
    for r in _exp(rows(os.path.join("data", "checkpoints.csv"))):
        w = res.get(r.get("slug"))
        if not w or not r.get("model_up"):
            continue
        p = float(r["model_up"])
        up_won = str(w).lower().startswith("up")
        conf = max(p, 1 - p)
        bk[min(int(conf * 10), 9)].append((conf, up_won == (p >= 0.5)))
    calib = [(f"{k * 10}-{k * 10 + 10}%", len(v), sum(c for c, _ in v) / len(v), sum(x for _, x in v) / len(v))
             for k, v in sorted(bk.items()) if k >= 5]
    rounds = len({s for s in res})
    return {"tickets": len(t), "graded": len(done), "wins": wins, "losses": len(wl) - wins,
            "missed": sum(r["result"] == "MISSED" for r in done), "pnl": pnl,
            "win_rate": wins / len(wl) if wl else None, "breakeven": sum(prices) / len(prices) if prices else None,
            "lag": med(lag), "fill": (fill, len(watched)), "ai": ai, "calib": calib, "rounds": rounds}


def card(s, path):
    from PIL import Image, ImageDraw, ImageFont
    A = "assets"
    S = 2
    W, H = 1080 * S, 1350 * S
    im = Image.new("RGB", (W, H), "#0f1117")
    d = ImageDraw.Draw(im)
    f = lambda n, b=False: ImageFont.truetype(os.path.join(A, "DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), n * S)
    G, R, Y, GR, WH, C = "#22c55e", "#ef4444", "#eab308", "#9ca3af", "#f3f4f6", "#1a1d27"
    now = datetime.now(ET).strftime("%b %d, %I:%M %p ET")
    d.text((60 * S, 50 * S), "polybot scoreboard", font=f(50, True), fill=WH)
    d.text((60 * S, 118 * S), f"Experiment v{EXP_MIN}+ · PAPER only · {now}", font=f(22), fill=GR)

    def tile(x, y, w, label, value, col):
        d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + 150) * S], radius=20 * S, fill=C)
        d.text(((x + 24) * S, (y + 20) * S), label, font=f(22), fill=GR)
        d.text(((x + 24) * S, (y + 62) * S), value, font=f(48, True), fill=col)

    wr = s["win_rate"]
    be = s["breakeven"]
    tile(60, 180, 300, "Tickets graded", f"{s['graded']}", WH)
    tile(390, 180, 300, "Won / Lost", f"{s['wins']} / {s['losses']}", WH)
    tile(720, 180, 300, "Missed (price ran)", f"{s['missed']}", Y)
    tile(60, 360, 300, "Win rate", f"{wr:.0%}" if wr is not None else "-", G if wr and be and wr > be else R if wr is not None else WH)
    tile(390, 360, 300, "Break-even (w/ fee)", f"{be:.0%}" if be else "-", WH)
    tile(720, 360, 300, "P&L ($10 a ticket)", f"{s['pnl']:+.2f}", G if s["pnl"] > 0 else R if s["pnl"] < 0 else WH)

    y = 550
    d.text((60 * S, y * S), "Is the win chance honest?", font=f(30, True), fill=WH)
    d.text((60 * S, (y + 44) * S), f"Model said  →  actually won   ({s['rounds']} rounds graded)", font=f(22), fill=GR)
    y += 90
    if not s["calib"]:
        d.text((60 * S, y * S), "Not enough graded rounds yet.", font=f(24), fill=GR)
        y += 40
    for label, n, said, won in s["calib"]:
        d.text((60 * S, y * S), label, font=f(24), fill=GR)
        x0, bw = 220, 640
        d.rounded_rectangle([x0 * S, (y + 4) * S, (x0 + bw) * S, (y + 30) * S], radius=8 * S, fill=C)
        d.rounded_rectangle([x0 * S, (y + 4) * S, (x0 + int(bw * won)) * S, (y + 30) * S], radius=8 * S,
                            fill=G if won >= said - 0.03 else R)
        sx = x0 + int(bw * said)
        d.line([sx * S, y * S, sx * S, (y + 34) * S], fill=WH, width=4 * S)
        d.text(((x0 + bw + 16) * S, y * S), f"{said:.0%}→{won:.0%}", font=f(22, True), fill=WH)
        y += 46
    d.text((60 * S, (y + 4) * S), "white line = what the bot said · bar = how often it really won · red = overconfident",
           font=f(19), fill=GR)

    y += 60
    d.text((60 * S, y * S), "Speed + second opinion", font=f(30, True), fill=WH)
    y += 52
    fill, watched = s["fill"]
    lines = [f"Price read → ticket in Discord: {s['lag']:.1f}s median" if s["lag"] is not None else "No timed tickets yet.",
             f"Quote available 30s later (simulated, size not verified): {fill}/{watched}" if watched else "Quote available 30s later: no data yet"]
    for v, (n, w, p) in s["ai"].items():
        lines.append(f"Gemini said {v}: {n} tickets, won {w} ({w / n:.0%}), {p:+.2f}")
    if not s["ai"]:
        lines.append("Gemini second opinions: none graded yet")
    for ln in lines:
        d.text((60 * S, y * S), "• " + ln, font=f(24), fill=WH)
        y += 40
    im = im.crop((0, 0, W, min(H, (y + 50) * S)))
    im.save(path, optimize=True)


def prompt(s):
    wr = f"{s['win_rate']:.0%}" if s["win_rate"] is not None else "n/a"
    be = f"{s['breakeven']:.0%}" if s["breakeven"] else "n/a"
    cal = "; ".join(f"said {sd:.0%} won {w:.0%} (n={n})" for _, n, sd, w in s["calib"]) or "not enough data"
    ai = "; ".join(f"{v}: {n} tickets, won {w}" for v, (n, w, _) in s["ai"].items()) or "none graded yet"
    return (
        "You're the outside reviewer for my paper-trading bot on Polymarket US 'BTC Up or Down 5 min'. "
        "The bot sends at most 1 ticket per round (4:00 or 3:30 left, 6-15% edge after fees). "
        f"Numbers are from experiment v{EXP_MIN}+ only (strategy frozen). Full report: data/report.md in github.com/j42002/polybot. "
        "Paper only until 300+ graded bets. Scoreboard (picture attached):\n"
        f"- Tickets graded {s['graded']}: won {s['wins']}, lost {s['losses']}, missed {s['missed']}\n"
        f"- Win rate {wr}, break-even incl. fee {be}, P&L after fees {s['pnl']:+.2f} at $10/ticket\n"
        f"- Calibration: {cal}\n"
        f"- Ticket speed: {round(s['lag'], 1) if s['lag'] is not None else 'n/a'}s; quote available 30s later (simulated) {s['fill'][0]}/{s['fill'][1]}\n"
        f"- Gemini second opinion: {ai}\n"
        "Be skeptical. In under 120 words: 1) what looks wrong or too good to be true, "
        "2) ONE change we can test, 3) is the sample big enough to trust anything yet?"
    )


def main(daily=False):
    now = datetime.now(ET)
    try:
        with open(STATE, encoding="utf-8") as f:
            st = json.load(f)
    except Exception:
        st = {}
    if daily and (now.hour < 20 or st.get("posted") == now.strftime("%Y-%m-%d")):
        return
    os.makedirs(OUT, exist_ok=True)
    s = stats()
    png = os.path.join(OUT, "scoreboard.png")
    card(s, png)
    text = prompt(s)
    with open(os.path.join(OUT, "chatgpt_prompt.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)
    if WEBHOOK:
        msg = ("📊 **Scoreboard for ChatGPT** - save the picture, then copy the text below into the free ChatGPT app."
               "\n```\n" + text + "\n```")
        with open(png, "rb") as f:
            r = requests.post(WEBHOOK, data={"payload_json": json.dumps({"content": msg[:1990]})},
                              files={"files[0]": ("scoreboard.png", f, "image/png")}, timeout=15)
        print(f"posted to Discord ({r.status_code})")
    st["posted"] = now.strftime("%Y-%m-%d")
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(st, f)


if __name__ == "__main__":
    main(daily="--daily" in sys.argv)
