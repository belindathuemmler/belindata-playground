"""Card image for 'Turning Pieces and Cubes', redrawn in the style of a fourth-grade worksheet
(our own pieces, not a copy): a coloured target rectangle and four grid pieces A-D; two of them make it.
Usage: python two_pieces_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

out = sys.argv[1]
IVORY, PLUM, CORAL, TERRA, DARK, GREY = '#FAF8F5', '#874C62', '#EE9779', '#DF7654', '#1F1A1C', '#6E6266'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off'); ax.set_aspect('equal')
ax.set_xlim(-0.8, 30.8); ax.set_ylim(-0.8, 16.85)


def inside(poly, x, y):
    c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[i - 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def piece(poly, dx, dy, fill=None, lw=2.2):
    P = np.array(poly, dtype=float)
    ax.add_patch(Polygon(P + [dx, dy], closed=True, fc=fill or 'none', ec=DARK, lw=lw, joinstyle='round', zorder=3))
    xs, ys = P[:, 0], P[:, 1]
    for i in range(int(xs.max())):          # grid lines inside the piece, cell by cell
        for j in range(int(ys.max())):
            if inside(poly, i + 0.5, j + 0.5):
                ax.add_patch(Polygon([(dx + i, dy + j), (dx + i + 1, dy + j), (dx + i + 1, dy + j + 1), (dx + i, dy + j + 1)],
                                     closed=True, fc='none', ec=GREY, lw=0.9, alpha=0.7, zorder=2))


def turn(poly):                              # a quarter turn, then back to the origin
    P = [(-y, x) for x, y in poly]
    mx, my = min(p[0] for p in P), min(p[1] for p in P)
    return [(x - mx, y - my) for x, y in P]


def mirror(poly):
    mx = max(x for x, _ in poly)
    return [(mx - x, y) for x, y in poly]


# the target, 8 x 6, and the cut into two pieces
bottom = [(0, 0), (8, 0), (8, 4), (5, 4), (5, 2), (0, 2)]          # area 22
top = [(0, 2), (5, 2), (5, 4), (8, 4), (8, 6), (0, 6)]             # area 26
top = [(x, y - 2) for x, y in top]
other = [(0, 0), (8, 0), (8, 3), (5, 3), (5, 2), (0, 2)]           # from another cut

# left: the coloured target
piece([(0, 0), (8, 0), (8, 6), (0, 6)], 0, 5.0, fill='#EE9779')
for i in range(1, 8):
    ax.plot([i, i], [5.0, 11.0], color=DARK, lw=0.9, alpha=0.45, zorder=4)
for j in range(1, 6):
    ax.plot([0, 8], [5.0 + j, 5.0 + j], color=DARK, lw=0.9, alpha=0.45, zorder=4)
ax.text(4, 12.0, 'Which two pieces', ha='center', fontsize=26, color=DARK, family='serif')
ax.text(4, 3.4, 'make the rectangle?', ha='center', fontsize=26, color=DARK, family='serif')

# right: four pieces A-D, two of them the answer (one turned), one a mirror image, one from another cut
pieces = [('A', top, 11.0, 10.6), ('B', mirror(bottom), 21.6, 10.6), ('C', other, 11.0, 2.0), ('D', turn(bottom), 23.8, 0.6)]
for name, poly, dx, dy in pieces:
    piece(poly, dx, dy)
    ax.text(dx - 0.7, dy + max(y for _, y in poly) - 0.3, name, fontsize=22, color=PLUM, family='serif', weight='bold')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
