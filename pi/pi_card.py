"""Card image for the π card: a circle of diameter 1 squeezed between a hexagon inside and a hexagon outside,
with the bounds 3 < π < 2√3. Usage: python pi_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, PLUM, CORAL = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#874C62', '#EE9779'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect('equal')

cx, cy, R = W * 0.33, H * 0.52, 250
ang = np.radians(np.arange(6) * 60)
inner = np.c_[cx + R * np.cos(ang), cy + R * np.sin(ang)]
Rc = R / np.cos(np.radians(30))
outer = np.c_[cx + Rc * np.cos(ang + np.radians(30)), cy + Rc * np.sin(ang + np.radians(30))]
ax.add_patch(Polygon(outer, closed=True, fill=False, edgecolor=PLUM, lw=3.5))
ax.add_patch(Circle((cx, cy), R, facecolor=(0.93, 0.59, 0.47, 0.15), edgecolor=TERRA, lw=4.5))
ax.add_patch(Polygon(inner, closed=True, fill=False, edgecolor=DARK, lw=3.5))
ax.plot([cx - R, cx + R], [cy, cy], color='#6E6266', lw=1.8, ls=(0, (4, 4)))
ax.text(cx, cy + 16, r'$d = 1$', ha='center', va='bottom', fontsize=24, color='#6E6266')

x0 = W * 0.62
ax.text(x0, H * 0.70, r'$3 \;<\; \pi \;<\; 2\sqrt{3}$', ha='left', va='center', fontsize=46, color=DARK)
ax.text(x0, H * 0.54, 'inside: 6 sides of ½', ha='left', va='center', fontsize=26, family='serif', color=DARK)
ax.text(x0, H * 0.45, 'outside: 6 sides of 1/√3', ha='left', va='center', fontsize=26, family='serif', color=PLUM)
ax.text(x0, H * 0.28, 'then double the corners:', ha='left', va='center', fontsize=24, family='serif', color=TERRA)
ax.text(x0, H * 0.19, r'$6 \to 12 \to 24 \to 48 \to 96$', ha='left', va='center', fontsize=28, color=TERRA)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
