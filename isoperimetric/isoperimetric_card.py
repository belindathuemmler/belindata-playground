"""Card image for 'Why the Circle Wins', dark like the interactives on the page:
one rope of length L = 18 unrolled at the top, and below it, side by side and to scale,
three fields fenced with that rope: rectangle 8 x 1 < square 4.5 x 4.5 < circle.
Usage: python isoperimetric_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
DARK_BG, IVORY, CORAL, TERRA, WHEAT, ROPE, ROPE_DARK = '#181315', '#FAF8F5', '#EE9779', '#DF7654', '#F4C98F', '#C9A66B', '#7A5A33'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(DARK_BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_aspect('equal')
ax.set_xlim(-11.0, 11.0); ax.set_ylim(-5.0, 22.0 * H / W - 5.0)   # one scale for the rope and the fields

L = 18.0
a, b = 8.0, 1.0                 # thin rectangle: 2(a + b) = 18
s = L / 4                       # square: 4s = 18
r = L / (2 * np.pi)             # circle: 2πr = 18


def rope(xs, ys, fill=None):
    """A rope: a tan line with dark twists; optionally the field inside it."""
    if fill is not None:
        ax.fill(xs, ys, color=fill, alpha=0.85, lw=0)
    ax.plot(xs, ys, color=ROPE, lw=7, solid_joinstyle='round', solid_capstyle='round')
    ax.plot(xs, ys, color=ROPE_DARK, lw=7, dashes=(1.4, 1.4), solid_capstyle='butt')


# the rope, unrolled
y_r = 5.2
rope(np.array([-L / 2, L / 2]), np.array([y_r, y_r]))
ax.text(0, y_r + 0.35, 'one rope, length $L = 18$', ha='center', va='bottom', fontsize=36, color=IVORY, family='serif')

# the same rope around three fields, side by side, standing on one line
floor = -1.5
t = np.linspace(0, 2 * np.pi, 400)
fields = [  # (name, centre x, outline, area)
    ('rectangle', -6.6, (np.array([-a / 2, a / 2, a / 2, -a / 2, -a / 2]), floor + np.array([0, 0, b, b, 0])), a * b),
    ('square', 0.3, (np.array([-s / 2, s / 2, s / 2, -s / 2, -s / 2]), floor + np.array([0, 0, s, s, 0])), s * s),
    ('circle', 6.8, (r * np.cos(t), floor + r + r * np.sin(t)), np.pi * r * r),
]
for name, cx, (xs, ys), area in fields:
    rope(cx + xs, ys, fill=WHEAT)
    win = name == 'circle'
    ax.text(cx, floor - 0.5, name, ha='center', va='top', fontsize=32, color=CORAL if win else IVORY, family='serif')
    ax.text(cx, floor - 1.5, f'area {area:.2f}'.replace('.00', ''), ha='center', va='top', fontsize=38, color=CORAL if win else IVORY, family='serif', weight='bold' if win else 'normal')
for x in (-3.15, 3.55):   # growing area
    ax.text(x, floor - 1.5, '<', ha='center', va='top', fontsize=40, color=IVORY, family='serif')

fig.savefig(out, dpi=100, facecolor=DARK_BG, pil_kwargs={'quality': 92})
print('ok')
