"""polybot ticket card - renders one PNG per JJ signal for Discord.

Built to be read in 2 seconds on a phone:
  top    : market, window, time left
  hero   : BUY UP / BUY DOWN, big, green or red
  row    : what you pay / what it's worth to us / edge
  bar    : market price vs our fair value on a 0-100 scale
  chart  : BTC over the last ~3 minutes vs the price to beat (dashed)
  money  : what $10 wins or loses, after the fee
  footer : paper record + "tap the title to open in the app"
"""
import io
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = os.path.join(HERE, "assets", "DejaVuSans-Bold.ttf")
FONT_REG = os.path.join(HERE, "assets", "DejaVuSans.ttf")

W, H = 1080, 1080
BG = (13, 15, 20)
PANEL = (24, 27, 35)
LINE = (44, 48, 60)
TEXT = (236, 238, 242)
MUTED = (140, 146, 160)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
GOLD = (247, 147, 26)          # bitcoin orange
BLUE = (88, 140, 255)


def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except OSError:
        return ImageFont.load_default(size=size)


def text_w(d, s, f):
    l, t, r, b = d.textbbox((0, 0), s, font=f)
    return r - l


def rounded(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def money_line(price, fee_rate, stake=10.0):
    shares = stake / price
    fee = fee_rate * price * (1 - price) * shares
    win = shares * (1 - price) - fee
    lose = stake + fee
    return shares, win, lose


def render(t):
    """t = dict(side, price, fair, ev, secs_left, window_label, dist, ptb, spot,
                prices=[(ts, px)...], fee_rate, record, venue)"""
    up = t["side"] == "Up"
    accent = GREEN if up else RED
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # top strip
    rounded(d, (40, 36, 300, 96), 18, PANEL)
    d.ellipse((58, 48, 94, 84), fill=GOLD)
    d.text((76, 66), "B", font=font(24, True), fill=BG, anchor="mm")
    d.text((108, 66), "BTC 5M", font=font(28, True), fill=TEXT, anchor="lm")
    d.text((320, 66), t["window_label"], font=font(26), fill=MUTED, anchor="lm")
    left = t["secs_left"]
    clock = f"{left // 60}:{left % 60:02d} LEFT"
    cw = text_w(d, clock, font(28, True)) + 48
    rounded(d, (W - 40 - cw, 36, W - 40, 96), 30, BG, outline=GOLD, width=3)
    d.text((W - 40 - cw / 2, 66), clock, font=font(28, True), fill=TEXT, anchor="mm")

    # hero
    rounded(d, (40, 124, W - 40, 324), 28, accent)
    arrow = "▲" if up else "▼"
    d.text((W / 2, 205), f"{arrow}  BUY {'UP' if up else 'DOWN'}", font=font(104, True), fill=BG, anchor="mm")
    d.text((W / 2, 290), f"at {t['price'] * 100:.0f}¢ or better", font=font(32, True), fill=BG, anchor="mm")

    # three stat boxes
    stats = [("YOU PAY", f"{t['price'] * 100:.0f}¢", TEXT),
             ("FAIR VALUE", f"{t['fair'] * 100:.0f}¢", BLUE),
             ("EDGE", f"{t['ev'] * 100:+.1f}¢", GREEN)]
    bw = (W - 80 - 2 * 24) / 3
    for i, (label, val, col) in enumerate(stats):
        x0 = 40 + i * (bw + 24)
        rounded(d, (x0, 352, x0 + bw, 492), 22, PANEL)
        d.text((x0 + bw / 2, 392), label, font=font(24, True), fill=MUTED, anchor="mm")
        d.text((x0 + bw / 2, 450), val, font=font(60, True), fill=col, anchor="mm")

    # price vs fair bar
    y = 548
    d.text((40, y - 26), "MARKET PRICE vs OUR FAIR VALUE", font=font(22, True), fill=MUTED, anchor="lm")
    x0, x1 = 40, W - 40
    rounded(d, (x0, y, x1, y + 22), 11, PANEL)
    px = x0 + (x1 - x0) * t["price"]
    fx = x0 + (x1 - x0) * t["fair"]
    lo, hi = sorted((px, fx))
    d.rectangle((lo, y, hi, y + 22), fill=accent)
    for xx, col, lab in ((px, TEXT, f"pay {t['price'] * 100:.0f}"), (fx, BLUE, f"fair {t['fair'] * 100:.0f}")):
        d.ellipse((xx - 14, y - 3, xx + 14, y + 25), fill=col, outline=BG, width=3)
    d.text((px, y + 50), f"pay {t['price'] * 100:.0f}¢", font=font(22, True), fill=TEXT, anchor="mm")
    fy = y + 50 if abs(fx - px) > 140 else y + 80
    d.text((fx, fy), f"fair {t['fair'] * 100:.0f}¢", font=font(22, True), fill=BLUE, anchor="mm")

    # BTC chart vs price to beat
    cy0, cy1 = 680, 880
    rounded(d, (40, cy0 - 20, W - 40, cy1 + 20), 22, PANEL)
    pts = [p for _, p in t.get("prices") or []]
    ptb = t["ptb"]
    where = "above" if t["dist"] >= 0 else "below"
    label = f"BTC ${t['spot']:,.0f}  \u00b7  ${abs(t['dist']):,.0f} {where} price to beat ${ptb:,.0f}"
    d.text((64, cy0 + 8), label, font=font(24, True), fill=TEXT, anchor="lm")
    gx0, gx1, gy0, gy1 = 64, W - 64, cy0 + 40, cy1 - 4
    if len(pts) >= 2:
        lo_p, hi_p = min(pts + [ptb]), max(pts + [ptb])
        pad = max((hi_p - lo_p) * 0.15, 5)
        lo_p, hi_p = lo_p - pad, hi_p + pad
        sy = lambda v: gy1 - (v - lo_p) / (hi_p - lo_p) * (gy1 - gy0)
        sx = lambda i: gx0 + i / (len(pts) - 1) * (gx1 - gx0)
        yb = sy(ptb)
        for xx in range(int(gx0), int(gx1), 22):          # dashed price-to-beat line
            d.line((xx, yb, min(xx + 12, gx1), yb), fill=MUTED, width=3)
        d.text((gx1, yb - 16), "PRICE TO BEAT", font=font(18, True), fill=MUTED, anchor="rm")
        line = [(sx(i), sy(v)) for i, v in enumerate(pts)]
        d.line(line, fill=GOLD, width=5, joint="curve")
        ex, ey = line[-1]
        d.ellipse((ex - 9, ey - 9, ex + 9, ey + 9), fill=GOLD)
    else:
        d.text((W / 2, (gy0 + gy1) / 2), "chart warming up", font=font(24), fill=MUTED, anchor="mm")

    # money line
    shares, win, lose = money_line(t["price"], t["fee_rate"])
    my = 930
    d.text((40, my), "$10 →", font=font(34, True), fill=TEXT, anchor="lm")
    d.text((160, my), f"{shares:.1f} shares", font=font(30), fill=MUTED, anchor="lm")
    d.text((470, my), f"WIN +${win:.2f}", font=font(34, True), fill=GREEN, anchor="lm")
    d.text((770, my), f"LOSE -${lose:.2f}", font=font(34, True), fill=RED, anchor="lm")

    # footer
    d.line((40, 972, W - 40, 972), fill=LINE, width=2)
    d.text((40, 1004), t.get("record") or "Paper record: no settled bets yet", font=font(22), fill=MUTED, anchor="lm")
    d.text((40, 1040), "PAPER SIGNAL · NOT ADVICE · tap the title above to open it in the app",
           font=font(22, True), fill=GOLD, anchor="lm")

    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue()


if __name__ == "__main__":
    import math, random
    random.seed(4)
    p, prices = 58910.0, []
    for i in range(90):
        p += random.gauss(0.4, 4)
        prices.append((i * 2, p))
    sample = dict(side="Up", price=0.52, fair=0.594, ev=0.061, secs_left=240,
                  window_label="Nov 25 · 5:40–5:45 AM ET", dist=prices[-1][1] - 58928.09,
                  ptb=58928.09, spot=prices[-1][1], prices=prices, fee_rate=0.095,
                  record="JJ paper record: 14 bets · hit 64% vs 52% breakeven · +$1.85/share")
    open("ticket_sample.png", "wb").write(render(sample))
    print("wrote ticket_sample.png")
