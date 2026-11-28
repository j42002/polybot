"""Polybot HQ system blueprint, drawn from lab/agents/status.json so it can't drift from the real statuses.

python blueprint.py  ->  lab/agents/blueprint.png   (free: Pillow + the repo's DejaVu fonts)
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

A = "assets"
S = 2
W, H = 1600, 1180
BG, CARD, CARD2, LINE = "#0f1117", "#1a1d27", "#232736", "#3a4058"
WH, GR = "#f3f4f6", "#9ca3af"
COL = {"implemented": "#22c55e", "development": "#60a5fa", "pending": "#eab308", "blocked": "#ef4444"}
LABEL = {"implemented": "Implemented + tested", "development": "In development", "pending": "Pending", "blocked": "Blocked"}


def font(n, b=False):
    return ImageFont.truetype(os.path.join(A, "DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), n * S)


def fit(s, n):
    if len(s) <= n:
        return s
    cut = s[:n - 1].rsplit(" ", 1)[0].rstrip(",;/")
    return cut + "…"


def main(path=os.path.join("lab", "agents", "status.json"), out=os.path.join("lab", "agents", "blueprint.png")):
    st = json.load(open(path, encoding="utf-8"))
    ag = {a["key"]: a for a in st["agents"]}
    im = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(im)

    def box(x, y, w, h, fill=CARD, outline=None, r=14):
        d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], radius=r * S, fill=fill,
                            outline=outline, width=(2 * S if outline else 0))

    def text(x, y, s, n=16, b=False, c=WH):
        d.text((x * S, y * S), s, font=font(n, b), fill=c)

    def line(x1, y1, x2, y2, c=LINE):
        d.line([x1 * S, y1 * S, x2 * S, y2 * S], fill=c, width=2 * S)

    def dot(x, y, c, r=7):
        d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=c)

    text(40, 30, "Polybot HQ · system blueprint", 34, True)
    text(40, 78, f"Generated from lab/agents/status.json · {st['generated']} · paper only · $0 · no real orders", 16, c=GR)

    # center: Polybot Brain
    bx, by, bw, bh = 600, 430, 400, 210
    box(bx, by, bw, bh, fill="#1e1b3a", outline="#7c3aed")
    text(bx + 24, by + 18, "POLYBOT BRAIN", 24, True)
    for i, s in enumerate(["GitHub = source of truth (issues, data, reports)", "Obsidian vault = linked memory (auto-rebuilt)",
                           "Cortex registry = agent status + findings", "Relay = one request queue, status cards",
                           "Decisions stay with Jacob"]):
        text(bx + 24, by + 62 + i * 27, "• " + s, 14, c=WH)

    # left column: experiments (data in)
    exps = [("5-minute bot (Polymarket US)", "frozen · paper · v21 wording fix", "#22c55e"),
            ("15-min maker test (Kalshi)", "frozen · paper · audit running", "#22c55e"),
            ("12-minute rule (Phase 1)", "refuted · kept on record", "#ef4444")]
    text(40, 130, "EXPERIMENTS (data in)", 16, True, GR)
    for i, (a, b, c) in enumerate(exps):
        y = 160 + i * 92
        box(40, y, 400, 76)
        dot(62, y + 26, c)
        text(80, y + 14, a, 16, True)
        text(80, y + 44, b, 13, c=GR)
        line(440, y + 38, bx, by + 40 + i * 50)

    # right column: outputs
    outs = [("Discord #ai-team-chat", "team talk + request cards"), ("Discord #research-reports", "stats, daily summary, agent card"),
            ("Discord #polybot-moves", "tickets only"), ("Obsidian vault (Dell)", "hourly auto-update"),
            ("ChatGPT (research director)", "independent QC on GitHub")]
    text(1160, 130, "OUTPUTS", 16, True, GR)
    for i, (a, b) in enumerate(outs):
        y = 160 + i * 78
        box(1160, y, 400, 64)
        text(1180, y + 10, a, 15, True)
        text(1180, y + 36, b, 13, c=GR)
        line(bx + bw, by + 30 + i * 36, 1160, y + 32)

    # bottom: specialist agents grid
    keys = [a["key"] for a in st["agents"]]
    cols = 5
    cw, ch = 296, 92
    for i, k in enumerate(keys):                      # connectors first, so cards sit on top
        x = 40 + (i % cols) * (cw + 12)
        y = 720 + (i // cols) * (ch + 12)
        if i < cols:
            line(x + cw / 2, y, bx + bw / 2, by + bh, c="#2b3047")
    d.rectangle([36 * S, 676 * S, 760 * S, 704 * S], fill=BG)
    text(40, 682, "SPECIALIST AGENTS (deterministic checks in the existing team-checks run)", 16, True, GR)
    for i, k in enumerate(keys):
        a = ag[k]
        x = 40 + (i % cols) * (cw + 12)
        y = 720 + (i // cols) * (ch + 12)
        box(x, y, cw, ch, fill=CARD2)
        dot(x + 20, y + 24, COL[a["status"]])
        text(x + 36, y + 12, a["name"], 17, True)
        if a.get("folded_in"):
            text(x + 36, y + 38, fit("+ " + a["folded_in"], 33), 12, c=GR)
        text(x + 36, y + 62, fit(a["job"], 34), 12, c=WH)
    # existing roles strip
    ex = " · ".join(e["name"] for e in st.get("existing", []))
    text(40, 1045, "Existing roles (unchanged): " + ex, 13, c=GR)
    # legend
    lx = 40
    for k in ("implemented", "development", "pending", "blocked"):
        n = sum(a["status"] == k for a in st["agents"])
        dot(lx + 8, 1100, COL[k])
        text(lx + 22, 1089, f"{LABEL[k]} ({n})", 15)
        lx += 330
    text(40, 1130, "Green = self-test with planted failures passed AND ran on real data in the latest run. Nothing changes a strategy.", 13, c=GR)
    im = im.resize((W, H), Image.LANCZOS)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out)
    print(f"blueprint: {out}")


if __name__ == "__main__":
    main()
