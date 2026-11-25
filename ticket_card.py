"""polybot ticket card v2 - one crisp PNG per signal for Discord.

Rendered at 2x (2160x2160) so text stays sharp on phone screens.
Read top to bottom in ~2 seconds:
  header : BTC 5M badge, window time, countdown pill
  hero   : BUY UP / BUY DOWN + tier, with a WIN CHANCE ring
  stats  : it costs -> it's really worth -> so it's cheap by (plain English)
  chart  : BTC's last ~3 min vs the price to beat (green zone = Up wins, red = Down wins)
  plain  : the bet in plain English (pay X, get $1 if right, lose X if wrong, wins ~N in 10)
  money  : what $10 wins or loses after the fee
  footer : paper record + "tap the title to open in the app"
"""
import io
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = os.path.join(HERE, "assets", "DejaVuSans-Bold.ttf")
FONT_REG = os.path.join(HERE, "assets", "DejaVuSans.ttf")

K = 2                      # render scale: 1080 layout units -> 2160 px
W = H = 1080
BG_TOP, BG_BOT = (18, 22, 32), (8, 9, 13)
PANEL = (26, 30, 41)
TEXT = (240, 242, 246)
MUTED = (138, 145, 162)
INK = (10, 12, 16)
GREEN, GREEN_D = (34, 197, 94), (21, 128, 61)
RED, RED_D = (239, 68, 68), (153, 27, 27)
GOLD = (247, 147, 26)
BLUE = (96, 150, 255)


def f(size, bold=True):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, int(size * K))
    except OSError:
        return ImageFont.load_default(size=int(size * K))


def s(*v):
    return tuple(int(round(x * K)) for x in v)


def tw(d, text, fnt):
    l, _, r, _ = d.textbbox((0, 0), text, font=fnt)
    return (r - l) / K


def vgradient(size, top, bot):
    w, h = size
    g = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(h - 1, 1)
        g.putpixel((0, y), tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return g.resize((w, h))


def panel(img, box, r=22, fill=PANEL, outline=None):
    ImageDraw.Draw(img).rounded_rectangle(s(*box), radius=r * K, fill=fill,
                                          outline=outline, width=2 * K if outline else 0)


def glow_box(img, box, r, color, top, bot):
    """Gradient-filled rounded box with a soft colored glow behind it."""
    x0, y0, x1, y1 = s(*box)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 10 * K, x1, y1 + 10 * K), radius=r * K, fill=color + (110,))
    sh = sh.filter(ImageFilter.GaussianBlur(26 * K))
    img.paste(sh, (0, 0), sh)
    grad = vgradient((x1 - x0, y1 - y0), top, bot)
    mask = Image.new("L", grad.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, grad.size[0] - 1, grad.size[1] - 1), radius=r * K, fill=255)
    img.paste(grad, (x0, y0), mask)


def money_line(price, fee_rate, stake=10.0):
    shares = stake / price
    fee = fee_rate * price * (1 - price) * shares
    return shares, shares * (1 - price) - fee, stake + fee


def plain_english(price, fair, side="Up", secs_left=240, max_price=None):
    """In the app's own words. Tells you the highest % that is still a good buy."""
    pay = round(price * 100)
    top = round((max_price or price) * 100)
    in10 = max(1, min(9, round(fair * 10)))
    btn = "Up" if side == "Up" else "Down"
    return (f"DO THIS: tap {btn} now, up to {top}%. Ticket expires in 30 sec.",
            f"{btn} wins if BTC ends {'above' if side == 'Up' else 'below'} the Target. We think it wins about {in10} in 10.")


def render(t):
    """t = dict(side, price, fair, ev, secs_left, window_label, dist, ptb, spot,
                prices=[(ts, px)...], fee_rate, record, tier)"""
    up = t["side"] == "Up"
    acc, acc_d = (GREEN, GREEN_D) if up else (RED, RED_D)
    tier = t.get("tier", "JJ")
    img = vgradient(s(W, H), BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img)

    # ---- header
    panel(img, (40, 34, 268, 96), 31)
    d.ellipse(s(52, 43, 96, 87), fill=GOLD)
    d.text(s(74, 65), "B", font=f(26), fill=INK, anchor="mm")
    d.text(s(110, 65), "BTC 5M", font=f(30), fill=TEXT, anchor="lm")
    d.text(s(290, 65), t["window_label"], font=f(26, False), fill=MUTED, anchor="lm")
    left = t["secs_left"]
    clock = f"TIMER {left // 60:02d}:{left % 60:02d}"
    cw = tw(d, clock, f(28)) + 52
    panel(img, (W - 40 - cw, 34, W - 40, 96), 31, (40, 30, 14), outline=GOLD)
    d.text(s(W - 40 - cw / 2, 65), clock, font=f(28), fill=GOLD, anchor="mm")

    # ---- hero + win-chance ring
    glow_box(img, (40, 120, W - 40, 330), 30, acc, acc, acc_d)
    d = ImageDraw.Draw(img)
    arrow = "▲" if up else "▼"
    d.text(s(78, 190), f"{arrow} BUY {'UP' if up else 'DOWN'}", font=f(94), fill=INK, anchor="lm")
    pill = f"{tier} SIGNAL"
    pw = tw(d, pill, f(24)) + 36
    d.rounded_rectangle(s(80, 254, 80 + pw, 298), radius=22 * K, fill=INK)
    d.text(s(80 + pw / 2, 276), pill, font=f(24), fill=acc, anchor="mm")
    left_s = t["secs_left"]
    d.text(s(100 + pw, 276), f"Tap {'Up' if up else 'Down'} now \u00b7 good up to {round((t.get('max_price') or t['price']) * 100)}%",
           font=f(30), fill=INK, anchor="lm")
    cx, cy, rad = W - 148, 225, 76
    d.ellipse(s(cx - rad - 8, cy - rad - 8, cx + rad + 8, cy + rad + 8), fill=INK)
    box = s(cx - rad, cy - rad, cx + rad, cy + rad)
    d.arc(box, 0, 360, fill=(48, 52, 64), width=14 * K)
    d.arc(box, -90, -90 + 360 * t["fair"], fill=acc, width=14 * K)
    d.text(s(cx, cy - 8), f"{t['fair'] * 100:.0f}%", font=f(40), fill=TEXT, anchor="mm")
    d.text(s(cx, cy + 28), "WIN CHANCE", font=f(14), fill=MUTED, anchor="mm")

    # ---- stats, in plain English: reads left to right as one sentence
    cents = lambda v: f"{v * 100:.0f}\u00a2" if v * 100 >= 1 else f"{v * 100:.1f}\u00a2"
    btn = "UP" if up else "DOWN"
    stats = [(f"APP SAYS {btn}", f"{t['price'] * 100:.0f}%", TEXT, "the button price now"),
             (f"WE SAY {btn}", f"{t['fair'] * 100:.0f}%", BLUE, "our real win chance"),
             ("YOUR EDGE", f"+{max(t['ev'] * 100, 0.1):.0f}%", GREEN, "after fees")]
    bw = (W - 80 - 2 * 20) / 3
    for i, (label, val, col, note) in enumerate(stats):
        x0 = 40 + i * (bw + 20)
        panel(img, (x0, 350, x0 + bw, 492), 24)
        d.text(s(x0 + bw / 2, 378), label, font=f(21), fill=MUTED, anchor="mm")
        d.text(s(x0 + bw / 2, 428), val, font=f(54), fill=col, anchor="mm")
        d.text(s(x0 + bw / 2, 470), note, font=f(17, False), fill=MUTED, anchor="mm")
        if i < 2:
            d.text(s(x0 + bw + 10, 421), "\u2192", font=f(22), fill=MUTED, anchor="mm")

    # ---- chart vs price to beat
    cy0, cy1 = 512, 772
    panel(img, (40, cy0, W - 40, cy1), 24)
    ptb, dist = t["ptb"], t["dist"]
    d.text(s(66, cy0 + 34), f"CURRENT ${t['spot']:,.2f}", font=f(28), fill=TEXT, anchor="lm")
    tag_col = GREEN if dist >= 0 else RED
    tag = f"${abs(dist):,.0f} {'ABOVE' if dist >= 0 else 'BELOW'} TARGET"
    tgw = tw(d, tag, f(21)) + 32
    d.rounded_rectangle(s(W - 66 - tgw, cy0 + 14, W - 66, cy0 + 54), radius=20 * K,
                        fill=tuple(int(c * 0.22) for c in tag_col))
    d.text(s(W - 66 - tgw / 2, cy0 + 34), tag, font=f(21), fill=tag_col, anchor="mm")
    gx0, gx1, gy0, gy1 = 66, W - 66, cy0 + 72, cy1 - 20
    pts = [p for _, p in (t.get("prices") or [])]
    if len(pts) >= 2:
        lo, hi = min(pts + [ptb]), max(pts + [ptb])
        pad = max((hi - lo) * 0.18, 6)
        lo, hi = lo - pad, hi + pad
        sy = lambda v: gy1 - (v - lo) / (hi - lo) * (gy1 - gy0)
        sx = lambda i: gx0 + i / (len(pts) - 1) * (gx1 - gx0)
        yb = sy(ptb)
        zone = Image.new("RGBA", img.size, (0, 0, 0, 0))
        zd = ImageDraw.Draw(zone)
        zd.rectangle(s(gx0, gy0, gx1, yb), fill=GREEN + (24,))
        zd.rectangle(s(gx0, yb, gx1, gy1), fill=RED + (24,))
        line = [(sx(i), sy(v)) for i, v in enumerate(pts)]
        zd.polygon([s(x, y) for x, y in [(gx0, gy1)] + line + [(gx1, gy1)]], fill=GOLD + (30,))
        img.paste(zone, (0, 0), zone)
        d = ImageDraw.Draw(img)
        d.text(s(gx0 + 8, gy0 + 14), "UP WINS ZONE", font=f(15), fill=GREEN, anchor="lm")
        d.text(s(gx0 + 8, gy1 - 12), "DOWN WINS ZONE", font=f(15), fill=RED, anchor="lm")
        x = gx0
        while x < gx1:
            d.line(s(x, yb, min(x + 14, gx1), yb), fill=(200, 204, 214), width=3 * K)
            x += 24
        d.text(s(gx1 - 4, yb - 16), f"TARGET ${ptb:,.2f}", font=f(15), fill=(200, 204, 214), anchor="rm")
        d.line([s(x, y) for x, y in line], fill=GOLD, width=5 * K, joint="curve")
        ex, ey = line[-1]
        gl = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(gl).ellipse(s(ex - 22, ey - 22, ex + 22, ey + 22), fill=GOLD + (120,))
        gl = gl.filter(ImageFilter.GaussianBlur(10 * K))
        img.paste(gl, (0, 0), gl)
        d = ImageDraw.Draw(img)
        d.ellipse(s(ex - 10, ey - 10, ex + 10, ey + 10), fill=GOLD, outline=(255, 255, 255), width=3 * K)
    else:
        d.text(s(W / 2, (gy0 + gy1) / 2), "chart warming up", font=f(24, False), fill=MUTED, anchor="mm")

    # ---- plain English
    l1, l2 = plain_english(t["price"], t["fair"], t["side"], t["secs_left"], t.get("max_price"))
    panel(img, (40, 792, W - 40, 884), 24, (30, 27, 18), outline=(92, 70, 30))
    d.text(s(64, 822), l1, font=f(23), fill=GOLD, anchor="lm")
    d.text(s(64, 858), l2, font=f(22, False), fill=TEXT, anchor="lm")

    # ---- money
    shares, win, lose = money_line(t["price"], t["fee_rate"])
    my0, my1 = 904, 976
    panel(img, (40, my0, 360, my1), 24)
    d.text(s(62, (my0 + my1) / 2), "$10 BET", font=f(30), fill=TEXT, anchor="lm")
    d.text(s(340, (my0 + my1) / 2), f"{shares:.1f} sh", font=f(22, False), fill=MUTED, anchor="rm")
    panel(img, (376, my0, 710, my1), 24, (16, 52, 32))
    d.text(s(543, (my0 + my1) / 2), f"WIN  +${win:.2f}", font=f(33), fill=GREEN, anchor="mm")
    panel(img, (726, my0, W - 40, my1), 24, (60, 20, 20))
    d.text(s((726 + W - 40) / 2, (my0 + my1) / 2), f"LOSE  -${lose:.2f}", font=f(33), fill=RED, anchor="mm")

    # ---- footer
    d.text(s(40, 1010), t.get("record") or f"{tier} paper record: no settled bets yet",
           font=f(21, False), fill=MUTED, anchor="lm")
    d.text(s(40, 1046), "PAPER SIGNAL · NOT ADVICE", font=f(21), fill=GOLD, anchor="lm")
    d.text(s(W - 40, 1046), "tap the title to open in the app", font=f(21), fill=TEXT, anchor="rm")

    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue()


if __name__ == "__main__":
    pr = [(i * 2, 58928.09 + 18 * i / 89 + 6 * math.sin(i / 7)) for i in range(90)]
    open("ticket_sample.png", "wb").write(render(dict(
        side="Up", price=0.52, fair=0.594, ev=0.061, secs_left=240, tier="JJ",
        window_label="Nov 25 · 5:40–5:45 AM ET", dist=18, ptb=58928.09, spot=58946.09,
        prices=pr, fee_rate=0.095, record="JJ paper record: 14 bets · hit 64% vs 52% breakeven · +1.85/share")))
    print("wrote ticket_sample.png")
