"""Card image for 'Fat and Thin Triangles': a flat triangle (180°), a fat one on a sphere (270°, three
right angles) and a thin one in the hyperbolic plane (less than 180°). Usage: python triangles_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)


def panel(x):
    ax = fig.add_axes([x, 0.12, 0.3, 0.7]); ax.axis('off'); ax.set_aspect('equal')
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.25, 1.35)
    return ax


# 1. flat: an ordinary triangle
ax = panel(0.03)
A, B, C = np.array([-1.0, -0.8]), np.array([1.05, -0.8]), np.array([0.15, 0.95])
ax.fill(*np.array([A, B, C]).T, color=CORAL, alpha=0.25)
ax.plot(*np.array([A, B, C, A]).T, color=TERRA, lw=3.2)
fig.text(0.18, 0.86, 'flat', ha='center', fontsize=24, color=PLUM, family='serif')
fig.text(0.18, 0.06, '= 180°', ha='center', fontsize=30, color=DARK, family='serif')

# 2. fat: the octant triangle on a sphere, three right angles
ax = panel(0.35)
t = np.linspace(0, 2 * np.pi, 300)
ax.fill(np.cos(t), np.sin(t), color=ROSE, alpha=0.12); ax.plot(np.cos(t), np.sin(t), color=ROSE, lw=2)
el, az = np.radians(20), np.radians(35)


def proj(p):  # simple orthographic view of a point on the unit sphere
    x, y, z = p
    x1 = x * np.cos(az) - y * np.sin(az); y1 = x * np.sin(az) + y * np.cos(az)
    return np.array([x1, z * np.cos(el) - y1 * np.sin(el)])


def arc(p, q, k=60):
    p, q = np.array(p, float), np.array(q, float)
    om = np.arccos(np.clip(p @ q, -1, 1))
    s = np.linspace(0, 1, k)
    pts = [(np.sin((1 - f) * om) * p + np.sin(f * om) * q) / np.sin(om) for f in s]
    return np.array([proj(x) for x in pts])


N, E1, E2 = [0, 0, 1], [1, 0, 0], [0, 1, 0]
eq = np.array([proj([np.cos(a), np.sin(a), 0]) for a in t])   # the equator, in the same view
ax.plot(*eq.T, color=ROSE, lw=1.2, alpha=0.6, ls='--')
edges = [arc(N, E1), arc(E1, E2), arc(E2, N)]
poly = np.vstack(edges)
ax.fill(*poly.T, color=CORAL, alpha=0.35)
for e in edges:
    ax.plot(*e.T, color=TERRA, lw=3.2)
fig.text(0.5, 0.86, 'fat (sphere)', ha='center', fontsize=24, color=PLUM, family='serif')
fig.text(0.5, 0.06, '90° + 90° + 90° = 270°', ha='center', fontsize=26, color=DARK, family='serif')

# 3. thin: a triangle whose sides bend inwards, as on a saddle
ax = panel(0.67)
V = [np.array([-1.1, -0.85]), np.array([1.15, -0.85]), np.array([0.05, 1.15])]


def inward(p, q, depth=0.32, k=60):
    s = np.linspace(0, 1, k)[:, None]
    m = (p + q) / 2; c = np.mean(V, axis=0)
    d = (c - m) / np.linalg.norm(c - m)
    return p + s * (q - p) + depth * 4 * s * (1 - s) * d


sides = [inward(V[0], V[1]), inward(V[1], V[2]), inward(V[2], V[0])]
ax.fill(*np.vstack(sides).T, color=SAGE, alpha=0.22)
for sd in sides:
    ax.plot(*sd.T, color=SAGE, lw=3.2)
fig.text(0.82, 0.86, 'thin (hyperbolic)', ha='center', fontsize=24, color=PLUM, family='serif')
fig.text(0.82, 0.06, '< 180°', ha='center', fontsize=30, color=DARK, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
