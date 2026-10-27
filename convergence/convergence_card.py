"""Card image for 'Convergence: Yay, We Will Get There! But When?': the view from the back seat of a car,
arms thrown up, the child asking "are we there yet?", and a dead-straight road to a destination an unguessable distance away. Usage: python convergence_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, Circle, Rectangle

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, APRI, DARK, SAGE, SKY = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#F4C98F', '#1F1A1C', '#C0D1B9', '#9FC5D6'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 13.76); ax.set_ylim(0, 7.68)

VX, VY = 6.88, 5.0
ax.add_patch(Rectangle((0, VY), 13.76, 7.68 - VY, fc=SKY, alpha=0.35, ec='none'))
ax.add_patch(Rectangle((0, 0), 13.76, VY, fc=SAGE, alpha=0.55, ec='none'))
ax.add_patch(Polygon([[1.2, 0], [12.56, 0], [VX + 0.05, VY], [VX - 0.05, VY]], closed=True, fc='#8E8A8C', ec='none'))
for k in range(1, 26):
    t0, t1 = (k - 0.2) / 26, (k + 0.3) / 26
    s0, s1 = (1 - t0) ** 2.4, (1 - t1) ** 2.4
    y0, y1 = VY * (1 - s0), VY * (1 - s1)
    w0, w1 = 0.12 * s0, 0.12 * s1
    if y1 < VY - 0.02:
        ax.add_patch(Polygon([[VX - w0, y0], [VX + w0, y0], [VX + w1, y1], [VX - w1, y1]], closed=True, fc=APRI, ec='none'))
hx = np.linspace(0, 13.76, 400)
ax.fill_between(hx, VY, VY + 0.25 * np.exp(-((hx - 3) / 2.2) ** 2) + 0.35 * np.exp(-((hx - 11) / 2.6) ** 2), color=ROSE, alpha=0.35, lw=0)
ax.plot([VX, VX], [VY, VY + 0.42], color=DARK, lw=1.2)
ax.add_patch(Polygon([[VX, VY + 0.42], [VX + 0.3, VY + 0.33], [VX, VY + 0.24]], closed=True, fc=TERRA, ec='none'))

# car interior: roof, slanted A-pillars (the windscreen is narrower at the top), sun visors, mirror, dashboard
ax.add_patch(Rectangle((0, 6.9), 13.76, 0.9, fc=DARK, ec='none'))
ax.add_patch(Polygon([[0, 0], [0, 7.68], [2.3, 7.68], [2.3, 6.9], [1.0, 1.9], [1.0, 0]], closed=True, fc=DARK, ec='none'))
ax.add_patch(Polygon([[13.76, 0], [13.76, 7.68], [11.46, 7.68], [11.46, 6.9], [12.76, 1.9], [12.76, 0]], closed=True, fc=DARK, ec='none'))
ax.add_patch(Polygon([[2.3, 6.9], [5.0, 6.9], [4.8, 6.45], [2.45, 6.45]], closed=True, fc='#2B2225', ec='none'))      # sun visors
ax.add_patch(Polygon([[11.46, 6.9], [8.76, 6.9], [8.96, 6.45], [11.31, 6.45]], closed=True, fc='#2B2225', ec='none'))
ax.plot([6.88, 6.88], [6.9, 6.72], color=DARK, lw=5)                                                                    # rear-view mirror
ax.add_patch(FancyBboxPatch((5.98, 6.3), 1.8, 0.44, boxstyle='round,pad=0,rounding_size=0.12', fc=DARK, ec='none'))
ax.add_patch(Rectangle((6.06, 6.36), 1.64, 0.32, fc='#8E8A8C', ec='none'))
ax.add_patch(Rectangle((6.06, 6.36), 1.64, 0.14, fc=SAGE, alpha=0.6, ec='none'))
ax.text(VX + 2.0, VY - 0.85, '? km', fontsize=28, color=DARK, family='monospace', ha='center', va='top', zorder=1.5,
        bbox=dict(boxstyle='round,pad=0.3', fc=IVORY, ec=DARK, lw=2))
dx = np.linspace(0, 13.76, 300)                                                                                         # curved dashboard top
dy = 1.75 + 0.35 * np.exp(-((dx - 6.88) / 4.5) ** 2) + 0.25 * np.exp(-((dx - 2.6) / 1.6) ** 2)
ax.fill_between(dx, 0, dy, color='#2B2225', lw=0)
ax.plot(dx, dy, color='#3C3034', lw=5, zorder=0.9)
for cx in (2.9, 10.6):
    ax.add_patch(FancyBboxPatch((cx - 1.35, 0), 2.7, 2.2, boxstyle='round,pad=0,rounding_size=0.35', fc=PLUM, ec='none'))
    ax.add_patch(FancyBboxPatch((cx - 0.55, 2.1), 1.1, 0.75, boxstyle='round,pad=0,rounding_size=0.3', fc=PLUM, ec='none'))
    ax.plot([cx - 0.2, cx - 0.2], [2.05, 2.15], color=DARK, lw=3); ax.plot([cx + 0.2, cx + 0.2], [2.05, 2.15], color=DARK, lw=3)

# arms up and the child's head
SKIN = '#F3C9A8'


def arm(x0, y0, x1, y1, w=0.8):
    d = np.array([x1 - x0, y1 - y0]); n = np.array([-d[1], d[0]]) / np.linalg.norm(d) * w / 2
    ax.add_patch(Polygon([[x0, y0] + n, [x1, y1] + n, [x1, y1] - n, [x0, y0] - n], closed=True, fc=CORAL, ec='none'))
    e = np.array([x0, y0]) + 0.62 * d
    ax.add_patch(Polygon([e + n * 0.85, [x1, y1] + n * 0.85, [x1, y1] - n * 0.85, e - n * 0.85], closed=True, fc=SKIN, ec='none'))


def hand(cx, cy, ang):
    ax.add_patch(Circle((cx, cy), 0.6, fc=SKIN, ec='none'))
    for a in np.deg2rad(ang + np.array([-55, -28, 0, 28, 55])):
        ax.plot([cx, cx + 0.95 * np.cos(a)], [cy, cy + 0.95 * np.sin(a)], color=SKIN, lw=14, solid_capstyle='round')


arm(5.1, 0.6, 3.9, 3.6); hand(3.85, 3.8, 100)
arm(8.66, 0.6, 9.86, 3.6); hand(9.91, 3.8, 80)
ax.add_patch(Circle((6.88, 0.55), 1.55, fc='#5A3A2E', ec='none'))                      # the back of the child's head
ax.add_patch(Rectangle((5.9, -0.2), 1.96, 0.9, fc='#5A3A2E', ec='none'))

# the question, as a speech bubble from the child in the back
ax.add_patch(FancyBboxPatch((2.6, 4.85), 8.56, 1.35, boxstyle='round,pad=0,rounding_size=0.6', fc=IVORY, ec=DARK, lw=2.5, zorder=5))
ax.add_patch(Polygon([[6.3, 4.87], [7.1, 4.87], [6.75, 2.45]], closed=True, fc=IVORY, ec='none', zorder=5))
ax.plot([6.3, 6.75], [4.87, 2.45], color=DARK, lw=2.5, zorder=5); ax.plot([7.1, 6.75], [4.87, 2.45], color=DARK, lw=2.5, zorder=5)
ax.text(6.88, 5.52, 'Are we there yet?', fontsize=52, color=DARK, family='serif', style='italic', ha='center', va='center', zorder=6)
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
