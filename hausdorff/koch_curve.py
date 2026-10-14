"""Card image: Koch curve (level 5) with its earlier construction steps faintly underneath."""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]

def koch(level):
    pts = np.array([[0.0, 0.0], [1.0, 0.0]])
    rot = np.array([[0.5, -np.sqrt(3) / 2], [np.sqrt(3) / 2, 0.5]])  # +60°
    for _ in range(level):
        new = [pts[0]]
        for a, b in zip(pts[:-1], pts[1:]):
            d = (b - a) / 3
            p1, p3 = a + d, a + 2 * d
            new += [p1, p1 + rot @ d, p3, b]
        pts = np.array(new)
    return pts

W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor('#FAF8F5')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor('#FAF8F5')
ax.set_aspect('equal'); ax.axis('off')
ax.set_xlim(-0.08, 1.08)
ax.set_ylim(0.15 - 0.5 * 1.16 * H / W, 0.15 + 0.5 * 1.16 * H / W)

for lvl, alpha in [(1, 0.55), (2, 0.65), (3, 0.8)]:
    p = koch(lvl)
    ax.plot(p[:, 0], p[:, 1] - 0.0, color='#C98FAA', lw=1.8, alpha=alpha)
p = koch(5)
ax.plot(p[:, 0], p[:, 1], color='#DF7654', lw=2.2, solid_joinstyle='round')
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor(), pil_kwargs={'quality': 92})
