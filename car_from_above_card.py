"""Card image for 'A Car From Above, Taken Literally': left the first-grade drawing (a rectangle,
a circle at every corner, a cross in the middle), right the same car in 3D if you take the top view
literally: wheels lying flat like plates, and a roof made entirely of window. Usage: python car_from_above_card.py out.jpg"""
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
for cx, cy in corners:
    t = np.linspace(0, 2 * np.pi, 120)
    wobbly(cx + 0.45 * np.cos(t), cy + 0.45 * np.sin(t), color=DARK, lw=3.5)
wobbly(*seg((-2, 0), (2, 0)), color=SKY, lw=3.5)
wobbly(*seg((0, -1.1), (0, 1.1)), color=SKY, lw=3.5)
axl.text(0, -2.15, 'a car, seen from above', ha='center', fontsize=21, color=PLUM, family='serif', style='italic')

# ---------- right: taken literally in 3D ----------
ax = fig.add_axes([0.46, 0.0, 0.54, 1.0], projection='3d'); ax.set_axis_off()
ax.set_facecolor(IVORY)
ax.view_init(elev=38, azim=-58)
L, B, z0, z1 = 2.0, 1.1, 0.35, 1.25
polys, cols = [], []
# body without its top face (the top is all window)
v = np.array([[-L, -B, z0], [L, -B, z0], [L, B, z0], [-L, B, z0], [-L, -B, z1], [L, -B, z1], [L, B, z1], [-L, B, z1]])
for f in [[0, 1, 2, 3], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]]:
    polys.append(v[f]); cols.append(CORAL)
# roof: four big window panes and the cross between them, as non-overlapping pieces
g = 0.09


def rect(xa, xb, ya, yb, z=z1):
    return np.array([[xa, ya, z], [xb, ya, z], [xb, yb, z], [xa, yb, z]])


for xs in [(-L, -g), (g, L)]:
    for ys in [(-B, -g), (g, B)]:
        polys.append(rect(*xs, *ys)); cols.append(SKY)
polys.append(rect(-L, L, -g, g)); cols.append(TERRA)
polys.append(rect(-g, g, -B, -g)); cols.append(TERRA)
polys.append(rect(-g, g, g, B)); cols.append(TERRA)
# wheels: flat discs lying at the corners, like plates glued to the car
t = np.linspace(0, 2 * np.pi, 60)
for cx, cy in [(-L, -B), (L, -B), (L, B), (-L, B)]:
    polys.append(np.column_stack([cx + 0.6 * np.cos(t), cy + 0.6 * np.sin(t), np.full_like(t, 0.8)])); cols.append(DARK)
ax.add_collection3d(Poly3DCollection(polys, facecolors=cols, edgecolors=[TERRA if c in (SKY, CORAL) else c for c in cols], linewidths=1.2))
ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.8, 2.8); ax.set_zlim(-1.2, 2.6)
ax.set_box_aspect((1, 1, 0.68))
fig.text(0.73, 0.1, '…taken literally', ha='center', fontsize=21, color=PLUM, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
