"""Card image for the Lie bracket: a car parallel-parks. It can only drive and steer, yet it ends up
shifted sideways, the direction of the Lie bracket [steer, drive]. Usage: python lie_bracket_parking.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.transforms import Affine2D

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, GREY = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#CFC6C9'
CAR_L, CAR_W = 1.0, 0.46

W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off'); ax.set_aspect('equal')
ax.set_xlim(-3.1, 3.1); ax.set_ylim(-0.95, 2.52)

def car(x, y, theta, color, edge_alpha, fill_alpha, lw=2.2):
    rgb = matplotlib.colors.to_rgb(color)
    box = FancyBboxPatch((-CAR_L / 2, -CAR_W / 2), CAR_L, CAR_W, boxstyle='round,pad=0,rounding_size=0.12',
                         fc=(*rgb, fill_alpha), ec=(*rgb, edge_alpha), lw=lw)
    box.set_transform(Affine2D().rotate(theta).translate(x, y) + ax.transData)
    ax.add_patch(box)

# kerb and parked cars
ax.plot([-3.0, 3.0], [-0.42, -0.42], color=GREY, lw=3)
car(-1.9, -0.1, 0, GREY, 1, 0.6)
car(1.9, -0.1, 0, GREY, 1, 0.6)

# gentle S-shaped path of the car centre from the street lane into the gap (reversing)
t = np.linspace(0, 1, 400)
px = 2.4 * (1 - t)
py = -0.1 + 0.95 * (1 + np.cos(np.pi * t)) / 2
ax.plot(px, py, color=TERRA, lw=1.6, ls=(0, (4, 4)), alpha=0.7)
for k, tk in enumerate([0.0, 0.35, 0.65]):
    i = int(tk * (len(t) - 1))
    theta = np.arctan2(py[i + 1] - py[i], px[i + 1] - px[i]) + np.pi
    car(px[i], py[i], theta, TERRA, 0.35 + 0.2 * k, 0.05)
car(0.0, -0.1, 0, TERRA, 1, 0.85)

# directions: the car can drive (and steer), the bracket moves it sideways
ax.annotate('', xy=(0.95, -0.1), xytext=(0.0, -0.1), arrowprops=dict(arrowstyle='->', color=PLUM, lw=2.4))
ax.text(1.0, -0.03, 'drive', color=PLUM, fontsize=17, family='serif', style='italic')
ax.annotate('', xy=(-0.85, -0.1), xytext=(-0.85, 0.85), arrowprops=dict(arrowstyle='->', color=TERRA, lw=2.4, ls='--'))
ax.text(-0.95, 0.95, '[steer, drive]', ha='right', color=TERRA, fontsize=17, family='serif', style='italic')
ax.text(0, 1.95, r'$[X, Y] = XY - YX$', ha='center', fontsize=34, color=TERRA, family='serif')
ax.text(0, 1.45, 'steer + drive  →  sideways', ha='center', fontsize=19, color=PLUM, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
