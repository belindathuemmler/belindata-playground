"""Card image for the π card: a circle of diameter 1, and its circumference is π. Usage: python pi_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

W, H = 1376, 768
IVORY, TERRA, GREY = '#FAF8F5', '#DF7654', '#6E6266'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect('equal')

cx, cy, R = W * 0.5, H * 0.42, 230
ax.add_patch(Circle((cx, cy), R, facecolor=(0.93, 0.59, 0.47, 0.15), edgecolor=TERRA, lw=6))
ax.plot([cx - R, cx + R], [cy, cy], color=GREY, lw=2.4, ls=(0, (4, 4)))
ax.plot([cx - R, cx + R], [cy, cy], 'o', color=GREY, ms=9)
ax.text(cx, cy + 18, r'$d = 1$', ha='center', va='bottom', fontsize=44, color=GREY)
# the circumference, pointed out by a dashed arc just outside the circle
# the way once around: a dashed arc seven eighths of the way round, with an arrow head at its end
import numpy as np
Ra = R + 34
th = np.radians(np.linspace(67.5, 67.5 - 315, 400))         # clockwise, seven eighths of a turn, the gap centred at the top
ax.plot(cx + Ra * np.cos(th), cy + Ra * np.sin(th), color=TERRA, lw=2.4, ls=(0, (3, 3)))
tip = th[-1]
ax.annotate('', xy=(cx + Ra * np.cos(tip), cy + Ra * np.sin(tip)),
            xytext=(cx + Ra * np.cos(tip + np.radians(6)), cy + Ra * np.sin(tip + np.radians(6))),
            arrowprops=dict(arrowstyle='-|>', color=TERRA, lw=2.4, mutation_scale=34))
ax.text(cx, cy + R + 64, 'circumference = π', ha='center', va='bottom', fontsize=52, family='serif', color=TERRA)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
