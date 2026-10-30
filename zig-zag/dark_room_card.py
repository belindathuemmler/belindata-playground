"""Card image: the dark room from the first interactive, explored by the string of lights (Zig-Zag).
Same room, same target density and the same small-time-step Zig-Zag as in dark_room.html; the light it leaves
behind is stronger than live so that a still image carries it. The image on the site: seed 8, T = 30.3, amt 6.
usage: python dark_room_card.py out.jpg seed T [lights] [amt]   (lights=1: room fully lit; amt: how bright, default 8)"""
import sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

out, seed, T = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
LIGHTS_ON = len(sys.argv) > 4 and sys.argv[4] == '1'
rng = np.random.default_rng(seed)

W, H = 10.75, 6.0                 # room in metres (the card is 1376 x 768, so a little wider than in the animation)
SS = 2                            # supersampling
PX = 128 * SS
IW, IH = int(W * PX), int(H * PX)
START = (5.3, 5.55)               # the door

# what is in the room: sofa corner with lamp and plant, the chair, the cat
MIX = [
    dict(w=0.22, mx=1.8, my=0.95, sx=0.75, sy=0.35),
    dict(w=0.08, mx=0.75, my=2.35, sx=0.3, sy=0.3),
    dict(w=0.08, mx=3.2, my=2.2, sx=0.3, sy=0.3),
    dict(w=0.25, mx=7.1, my=3.6, sx=0.4, sy=0.4),
    dict(w=0.09, mx=9.6, my=1.1, sx=0.32, sy=0.32),
    dict(w=0.30, mx=5.4, my=3.0, sx=3.4, sy=2.0),
]
CAT = (9.6, 1.1)

def gradU(x, y):
    p = gx = gy = 0.0
    for c in MIX:
        u, v = (x - c['mx']) / c['sx'], (y - c['my']) / c['sy']
        q = c['w'] / (c['sx'] * c['sy']) * math.exp(-0.5 * (u * u + v * v))
        p += q; gx += q * u / c['sx']; gy += q * v / c['sy']
    return gx / p, gy / p

# ---------- Zig-Zag, approximated in small time steps, as in the animation ----------
DT = 0.54 / 48
x, y = START
th = [rng.choice([-1, 1]), -1]
pts = [(x, y)]
t = 0.0
while t < T:
    g = gradU(x, y)
    for i in range(2):
        lam = max(0.0, th[i] * g[i])
        if rng.random() < 1 - math.exp(-lam * DT): th[i] = -th[i]
    x += th[0] * DT; y += th[1] * DT
    if x < 0.1 or x > W - 0.1: x = min(W - 0.1, max(0.1, x)); th[0] = -th[0]
    if y < 0.1 or y > H - 0.1: y = min(H - 0.1, max(0.1, y)); th[1] = -th[1]
    pts.append((x, y)); t += DT
pts = np.array(pts)
print(len(pts), 'points')

# ---------- the room, fully lit ----------
def P(v): return v * PX
scene = Image.new('RGB', (IW, IH), '#E9DCC8')
d = ImageDraw.Draw(scene)
for yy in np.arange(0.5, H, 0.5):                                           # floorboards
    d.line([(0, P(yy)), (IW, P(yy))], fill=(201, 184, 163), width=int(0.02 * PX))
d.rectangle([P(4.7), P(H - 0.08), P(5.9), IH], fill='#C9B8A3')              # door
d.ellipse([P(2.0 - 1.9), P(1.75 - 0.85), P(2.0 + 1.9), P(1.75 + 0.85)], fill=(241, 199, 180))   # rug
d.rectangle([P(0.5), P(0.3), P(3.1), P(1.45)], fill='#874C62')              # sofa
d.rectangle([P(0.5), P(0.3), P(3.1), P(0.65)], fill='#6E3B4E')
d.rectangle([P(0.75), P(0.75), P(1.75), P(1.3)], fill='#B77A8A')
d.rectangle([P(1.85), P(0.75), P(2.85), P(1.3)], fill='#B77A8A')
d.ellipse([P(0.75 - 0.28), P(2.35 - 0.28), P(0.75 + 0.28), P(2.35 + 0.28)], fill='#F4C98F')     # lamp
d.ellipse([P(0.75 - 0.08), P(2.35 - 0.08), P(0.75 + 0.08), P(2.35 + 0.08)], fill='#DF7654')
for k in range(7):                                                          # plant
    a = k * 2 * math.pi / 7
    cx, cy = 3.2 + 0.17 * math.cos(a), 2.2 + 0.17 * math.sin(a)
    leaf = Image.new('RGBA', (int(0.4 * PX), int(0.4 * PX)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(leaf)
    ld.ellipse([P(0.2 - 0.16), P(0.2 - 0.08), P(0.2 + 0.16), P(0.2 + 0.08)], fill='#7FA375')
    leaf = leaf.rotate(-math.degrees(a), resample=Image.BICUBIC)
    scene.paste(leaf, (int(P(cx - 0.2)), int(P(cy - 0.2))), leaf)
d.ellipse([P(3.2 - 0.09), P(2.2 - 0.09), P(3.2 + 0.09), P(2.2 + 0.09)], fill='#C0D1B9')
d.rectangle([P(6.75), P(3.3), P(7.45), P(3.95)], fill='#DF7654')            # chair
d.rectangle([P(6.75), P(3.18), P(7.45), P(3.32)], fill='#A9533A')
cx, cy = CAT
def draw_cat(target):                                                       # the cat, on the scene and again on top of the light
    dd = ImageDraw.Draw(target)
    body = Image.new('RGBA', (int(0.8 * PX), int(0.6 * PX)), (0, 0, 0, 0))
    bd = ImageDraw.Draw(body)
    bd.ellipse([P(0.4 - 0.3), P(0.3 - 0.2), P(0.4 + 0.3), P(0.3 + 0.2)], fill='#4A4044')
    body = body.rotate(-11, resample=Image.BICUBIC)
    target.paste(body, (int(P(cx + 0.05 - 0.4)), int(P(cy + 0.05 - 0.3))), body)
    hx, hy = cx - 0.33, cy - 0.17
    dd.ellipse([P(hx - 0.14), P(hy - 0.14), P(hx + 0.14), P(hy + 0.14)], fill='#4A4044')
    dd.polygon([(P(hx - 0.10), P(hy - 0.08)), (P(hx - 0.09), P(hy - 0.22)), (P(hx - 0.02), P(hy - 0.12))], fill='#4A4044')
    dd.polygon([(P(hx + 0.02), P(hy - 0.13)), (P(hx + 0.10), P(hy - 0.22)), (P(hx + 0.10), P(hy - 0.08))], fill='#4A4044')
    dd.line([(P(cx + 0.32), P(cy + 0.1)), (P(cx + 0.5), P(cy + 0.18)), (P(cx + 0.55), P(cy + 0.32)), (P(cx + 0.48), P(cy + 0.45))],
            fill='#4A4044', width=int(0.06 * PX), joint='curve')
    for ex in (hx - 0.045, hx + 0.045):
        dd.ellipse([P(ex - 0.028), P(hy - 0.02 - 0.028), P(ex + 0.028), P(hy - 0.02 + 0.028)], fill='#C0D1B9')
draw_cat(scene)
d.rectangle([P(0.04), P(0.04), P(W - 0.04), P(H - 0.04)], outline='#8A7A6A', width=int(0.08 * PX))

# ---------- the light the string of lights has left ----------
GX, GY = 215, 120
CELL = W / GX
light = np.zeros((GY, GX))
KS, KR = 5, 14                   # 0.25 m, as in the animation (its grid is coarser)
AMT = 0.1 * 2 / 48 * float(sys.argv[5]) if len(sys.argv) > 5 else 0.1 * 2 / 48 * 8   # brighter than live: the whole run adds up
jj, ii = np.mgrid[0:GY, 0:GX]
for (px, py) in pts:
    cxg, cyg = px / CELL, py / CELL
    i0, i1 = max(0, int(cxg - KR)), min(GX, int(cxg + KR) + 2)
    j0, j1 = max(0, int(cyg - KR)), min(GY, int(cyg + KR) + 2)
    dx = ii[j0:j1, i0:i1] + 0.5 - cxg; dy = jj[j0:j1, i0:i1] + 0.5 - cyg
    light[j0:j1, i0:i1] += AMT * np.exp(-(dx * dx + dy * dy) / (2 * KS * KS))
bright = 1 - np.exp(-light)

img = scene.copy()
if not LIGHTS_ON:
    alpha = (250 * (1 - bright)).clip(0, 255).astype(np.uint8)
    shade = Image.fromarray(alpha).resize((IW, IH), Image.BILINEAR)
    dark = Image.new('RGB', (IW, IH), (12, 8, 10))
    img.paste(dark, (0, 0), shade)

# ---------- the string of lights: the path, the bulbs, the glow at the end ----------
ov = Image.new('RGBA', (IW, IH), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
TR = pts[-420:]
line = [(P(a), P(b)) for a, b in TR[::3]]
od.line(line, fill=(255, 220, 150, 110 if not LIGHTS_ON else 170), width=int(0.045 * PX), joint='curve')
BULBS = [(238, 151, 121), (244, 201, 143), (216, 169, 191), (192, 209, 185), (159, 197, 214)]
sub = TR[::-12][::-1]
n = len(sub)
for k, (bx, by) in enumerate(sub):
    col = BULBS[k % len(BULBS)]
    r = 0.075
    a = int(255 * (0.35 + 0.65 * (k + 1) / n))
    od.ellipse([P(bx - r), P(by - r), P(bx + r), P(by + r)], fill=col + (a,))
img.paste(ov, (0, 0), ov)
# soft halo around the bulbs
halo = Image.new('RGBA', (IW, IH), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
for k, (bx, by) in enumerate(sub):
    r = 0.16
    hd.ellipse([P(bx - r), P(by - r), P(bx + r), P(by + r)], fill=BULBS[k % len(BULBS)] + (int(90 * (k + 1) / n),))
halo = halo.filter(ImageFilter.GaussianBlur(0.08 * PX))
img.paste(halo, (0, 0), halo)
# the glow at the current position
ex, ey = pts[-1]
glow = Image.new('RGBA', (IW, IH), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([P(ex - 0.4), P(ey - 0.4), P(ex + 0.4), P(ey + 0.4)], fill=(255, 236, 170, 160))
glow = glow.filter(ImageFilter.GaussianBlur(0.18 * PX))
img.paste(glow, (0, 0), glow)

catlayer = Image.new('RGBA', (IW, IH), (0, 0, 0, 0))
draw_cat(catlayer)
bj, bi = min(GY - 1, int(cy / CELL)), min(GX - 1, int(cx / CELL))
catalpha = catlayer.split()[3].point(lambda v: int(v * min(1.0, 0.1 + bright[bj, bi])))
img.paste(catlayer, (0, 0), catalpha)
img = img.resize((IW // SS, IH // SS), Image.LANCZOS)
img.save(out, quality=90)
print('saved', out, img.size, 'end', pts[-1].round(2))
