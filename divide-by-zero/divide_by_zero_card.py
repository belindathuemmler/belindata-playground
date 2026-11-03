"""Card image for 'Never Divide by Zero!': the classic 'proof' that 2 = 1 in five lines, with the hidden division by zero. Needs the Windows font Segoe Script for the handwritten verdict (any script font will do).
Usage: python divide_by_zero_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#DF7654', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W)

# five lines instead of seven: the squaring and the subtraction of b^2 are folded into one step
steps = [r'$a = b$', r'$a^2 - b^2 = ab - b^2$', r'$(a+b)(a-b) = b(a-b)$', r'$a + b = b$', r'$2 = 1$']
y0, dy = 4.15, 0.84
ax.text(3.7, y0 + 0.86, r'Let $a, b \in \mathbb{R}$ with', ha='center', fontsize=34, color=DARK, family='serif')
for k, st in enumerate(steps):
    col = TERRA if k == len(steps) - 1 else DARK
    ax.text(3.7, y0 - k * dy, st, ha='center', fontsize=34, color=col, family='serif')
    if k < len(steps) - 1:   # the sign sits on the line it introduces: equivalences, all but one
        ax.text(1.3, y0 - (k + 1) * dy, r'$\Leftrightarrow$', ha='center', fontsize=40, color=TERRA if k == 2 else DARK, family='serif')
# the forbidden step
ax.annotate('', xy=(5.95, y0 - 3 * dy + 0.22), xytext=(5.95, y0 - 2 * dy - 0.08),
            arrowprops=dict(arrowstyle='->', color=TERRA, lw=2.8))
ax.text(6.3, y0 - 2 * dy, r'$\div\,(a-b)$', fontsize=34, color=TERRA, family='serif')   # same baseline and size as the line it acts on
ax.text(5.2, y0 - 4 * dy - 0.05, '→ zero points', ha='left', fontsize=52, color=ROSE, family='Segoe Script')   # handwriting, like a marker on the exam sheet
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
