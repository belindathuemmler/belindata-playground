"""Card image for 'How Parenthood Feels to Me (Sometimes)': a game screen seen through a parent's eyes, with task cards flying in from all directions, small while far away and large when they arrive, and children shouting in between. Needs the Windows font Segoe Script for the handwritten remark (any script font will do).
Usage: python parenthood_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
NIGHT, IVORY, PLUM, ROSE, CORAL, TERRA, SAGE, APRICOT, DARK = '#181315', '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#ACAA91', '#F4C98F', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(NIGHT)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(NIGHT); ax.axis('off')
ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W)
CX, CY = 5.0, 2.75   # where the tasks come from

# speed lines from the vanishing point
for a in np.linspace(0, 2 * np.pi, 36, endpoint=False):
    ax.plot([CX + 0.5 * np.cos(a), CX + 8 * np.cos(a)], [CY + 0.5 * np.sin(a), CY + 8 * np.sin(a)], color=PLUM, lw=1.2, alpha=0.3)

# task cards: text, direction in degrees (0 = to the right), distance from the vanishing point, tilt, fill, text colour, font size
# near the middle they are still small, at the edge they have arrived
tasks = [('snack!', 75, 0.55, 0, ROSE, DARK, 8),
         ('dentist', 215, 0.6, 0, SAGE, DARK, 8),
         ('shoes?', 320, 0.7, 0, IVORY, DARK, 9),
         ('Dinner?', 172, 1.45, 4, ROSE, DARK, 15),
         ('Sign the school form', 8, 1.9, -3, IVORY, DARK, 15),
         ('Present by Saturday', 118, 1.75, -4, APRICOT, DARK, 17),
         ('Washing machine is done', 247, 1.85, 3, SAGE, DARK, 19),
         ('Milk is out', 152, 3.35, 6, IVORY, DARK, 27),
         ('Order the groceries', 203, 3.3, -5, APRICOT, DARK, 25),
         ('Hang up the washing', 333, 3.1, 5, ROSE, DARK, 25),
         ('Pick up from the playdate', 30, 2.9, -7, TERRA, IVORY, 25)]
for text, deg, r, tilt, fill, col, fs in tasks:
    a = np.radians(deg)
    ax.text(CX + r * np.cos(a), CY + r * np.sin(a), text, ha='center', va='center', rotation=tilt, fontsize=fs, color=col,
            family='sans-serif', weight='bold', bbox=dict(boxstyle='round,pad=0.45', fc=fill, ec=NIGHT, lw=2))

# the soundtrack: shouts from every direction, without a card, because nobody wrote them down. Text, x, y, tilt, colour, font size
shouts = [('“Mum!”', 1.35, 2.85, 9, TERRA, 36),
          ('“Dad!”', 8.95, 2.7, -7, CORAL, 32),
          ('“I’m hungry!”', 4.7, 5.05, -2, CORAL, 26),
          ('“MUUUM!”', 1.45, 0.42, 5, CORAL, 26),
          ('“AAAAH!”', 6.95, 2.0, -10, TERRA, 20),
          ('“Mum?”', 4.3, 3.6, 6, CORAL, 12),
          ('“Dad!”', 5.95, 3.62, -5, TERRA, 11)]
for text, x, y, tilt, col, fs in shouts:
    ax.text(x, y, text, ha='center', va='center', rotation=tilt, fontsize=fs, color=col, family='sans-serif', weight='bold')

# head-up display
ax.text(0.35, 5.02, '07:40', fontsize=30, color=IVORY, family='monospace', weight='bold')
ax.text(9.65, 5.02, 'open tasks: 23', ha='right', fontsize=22, color=IVORY, family='monospace')
ax.text(9.65, 0.3, '… and it is only 7:40', ha='right', fontsize=38, color=ROSE, family='Segoe Script')   # handwriting, like a sigh
fig.savefig(out, dpi=100, facecolor=NIGHT, pil_kwargs={'quality': 92})
print('ok')
