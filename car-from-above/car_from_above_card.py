"""Card image for 'A Car From Above, Taken Literally': left the first-grade drawing (a rectangle,
a circle at every corner, a cross in the middle), right the same car in 3D if you take the top view
literally: wheels lying flat like plates, and a roof made entirely of window, bulging up like a Beetle. Usage: python car_from_above_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SKY = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#9EC3DE'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)

# ---------- left: the drawing, with a slightly wobbly crayon line ----------
axl = fig.add_axes([0.03, 0.1, 0.42, 0.78]); axl.axis('off'); axl.set_aspect('equal')
axl.set_xlim(-3.2, 3.2); axl.set_ylim(-2.4, 2.4)
rng = np.random.default_rng(2)


def wobbly(x, y, **kw):
    t = np.linspace(0, 1, len(x))
    n = 0.02 * np.sin(2 * np.pi * (2 * t + rng.random())) + rng.normal(0, 0.003, len(x))
    axl.plot(np.asarray(x) + n, np.asarray(y) - n, solid_capstyle='round', **kw)


def seg(p, q, k=60):
    return np.linspace(p[0], q[0], k), np.linspace(p[1], q[1], k)


corners = [(-2, -1.1), (2, -1.1), (2, 1.1), (-2, 1.1)]
for p, q in zip(corners, corners[1:] + corners[:1]):
    wobbly(*seg(p, q), color=TERRA, lw=4)
R = 0.45  # wheels sit outside the corners, touching them only at the corner point
for cx, cy in corners:
    t = np.linspace(0, 2 * np.pi, 120)
    mx, my = cx + np.sign(cx) * R / np.sqrt(2), cy + np.sign(cy) * R / np.sqrt(2)
    wobbly(mx + R * np.cos(t), my + R * np.sin(t), color=DARK, lw=3.5)
wobbly(*seg((-2, 0), (2, 0)), color=SKY, lw=3.5)
wobbly(*seg((0, -1.1), (0, 1.1)), color=SKY, lw=3.5)
axl.text(0, -2.15, 'a car, seen from above', ha='center', fontsize=21, color=PLUM, family='serif', style='italic')

# ---------- right: taken literally in 3D ----------
ax = fig.add_axes([0.46, 0.0, 0.54, 1.0], projection='3d'); ax.set_axis_off()
ax.set_facecolor(IVORY)
ax.view_init(elev=38, azim=-58)
L, B, z0, z1 = 2.0, 1.1, 0.35, 1.25
polys, cols = [], []
# body without its top face (the dome covers it)
v = np.array([[-L, -B, z0], [L, -B, z0], [L, B, z0], [-L, B, z0], [-L, -B, z1], [L, -B, z1], [L, B, z1], [-L, B, z1]])
for f in [[0, 1, 2, 3], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]]:
    polys.append(v[f]); cols.append(CORAL)
# roof: a glass dome over the whole top, bulging up like a Beetle, the cross of the drawing as window bars across it
a, b, h, g = L, B, 0.95, 0.07
xs = np.unique(np.concatenate([np.linspace(-a, a, 27), [-g, g]]))
ys = np.unique(np.concatenate([np.linspace(-b, b, 19), [-g, g]]))


LIGHT = np.array([-0.45, -0.55, 0.7]) / np.linalg.norm([-0.45, -0.55, 0.7])


def shade(color, quad):
    # a little light from the front left, so the bulge reads as a bulge
    n = np.cross(quad[1] - quad[0], quad[3] - quad[0]); n = n / np.linalg.norm(n)
    k = 0.78 + 0.32 * max(0.0, float(n @ LIGHT))
    rgb = np.array(matplotlib.colors.to_rgb(color))
    return tuple(np.clip(rgb * k + (1 - k) * 0.25 * (k < 1), 0, 1))


def dome(x, y):
    return z1 + h * np.clip(1 - np.abs(x / a) ** 2.4, 0, 1) ** 0.42 * np.clip(1 - np.abs(y / b) ** 2.4, 0, 1) ** 0.42


for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        q = [(xs[i], ys[j]), (xs[i + 1], ys[j]), (xs[i + 1], ys[j + 1]), (xs[i], ys[j + 1])]
        polys.append(np.array([[x, y, dome(x, y)] for x, y in q]))
        xc, yc = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
        cols.append(shade(TERRA if abs(xc) < g or abs(yc) < g else SKY, polys[-1]))
# wheels: flat discs lying outside the corners, like plates glued to the car
t = np.linspace(0, 2 * np.pi, 60)
r = 0.6
for cx, cy in [(-L, -B), (L, -B), (L, B), (-L, B)]:
    mx, my = cx + np.sign(cx) * r / np.sqrt(2), cy + np.sign(cy) * r / np.sqrt(2)
    polys.append(np.column_stack([mx + r * np.cos(t), my + r * np.sin(t), np.full_like(t, 0.8)])); cols.append(DARK)
ax.add_collection3d(Poly3DCollection(polys, facecolors=cols, edgecolors=[TERRA if isinstance(c, str) and c == CORAL else c for c in cols], linewidths=[1.2 if isinstance(c, str) and c == CORAL else 0.4 for c in cols]))
ax.set_xlim(-3.0, 3.0); ax.set_ylim(-3.0, 3.0); ax.set_zlim(-1.0, 3.0)
ax.set_box_aspect((1, 1, 0.68))
fig.text(0.73, 0.1, '…taken literally', ha='center', fontsize=21, color=PLUM, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
