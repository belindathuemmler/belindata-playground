"""Card image for 'Silence = No Questions?': a tutor asks "Any questions?", the room stays silent,
yet almost everybody has one. Usage: python silence_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, GREY = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#CFC6C9'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off'); ax.set_aspect('equal')
ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W)

# speech bubble of the tutor
bubble = FancyBboxPatch((3.35, 4.45), 3.3, 0.85, boxstyle='round,pad=0.12,rounding_size=0.35', fc='white', ec=PLUM, lw=2)
ax.add_patch(bubble)
ax.plot([4.7, 4.95, 5.2], [4.33, 4.0, 4.33], color=PLUM, lw=2)
ax.text(5.0, 4.87, 'Any questions?', ha='center', va='center', fontsize=25, color=PLUM, family='serif', style='italic')

# the silent room: every student has a question, nobody asks it
rng = np.random.default_rng(3)
xs = np.linspace(1.4, 8.6, 7)
for row, y in enumerate([2.85, 1.45]):
    for k, x in enumerate(xs + (0.0 if row == 0 else 0.55)):
        if x > 9.2:
            continue
        ax.add_patch(Circle((x, y), 0.26, fc=ROSE, alpha=0.75, ec='none'))
        ax.add_patch(FancyBboxPatch((x - 0.38, y - 0.85), 0.76, 0.5, boxstyle='round,pad=0,rounding_size=0.2', fc=ROSE, alpha=0.45, ec='none'))
        understood = (row, k) in [(0, 2), (1, 4)]
        if not understood:
            ax.text(x + 0.33, y + 0.35, '?', fontsize=21, color=TERRA, alpha=0.85, family='serif', weight='bold')
ax.text(7.05, 4.72, '…', ha='left', fontsize=30, color=GREY, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
