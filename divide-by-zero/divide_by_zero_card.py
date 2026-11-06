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

# five lines instead of seven: a = b moves into the first line, the squaring and the subtraction of b^2 are folded into one step
# a, b must not be zero: otherwise a + b = b only says a = 0, and the last step (dividing 2b = b by b) would not be allowed either
steps = [r'$a^2 - b^2 = ab - b^2$', r'$(a+b)(a-b) = b(a-b)$', r'$a + b = b$', r'$2b = b$', r'$2 = 1$']
y0, dy = 4.15, 0.84
# first line in pieces: the words and the R are set larger, so that they match the height of the formula letters
head = [('Let', 42, 0.2), (r'$a, b \in$', 34, 0.1), ('ℝ', 42, 0.1), (r'$\setminus\, \{0\}$', 34, 0.2), ('with', 42, 0.2), (r'$a = b$', 34, 0)]   # text, size, gap after it
fig.canvas.draw(); rend = fig.canvas.get_renderer()
widths = []
for s, fs, _ in head:
    t = ax.text(0, 0, s, fontsize=fs, family='serif'); widths.append(t.get_window_extent(rend).width / W * 10); t.remove()
x = 3.7 - (sum(widths) + sum(g for _, _, g in head)) / 2
for (s, fs, g), w in zip(head, widths):
    ax.text(x, y0 + 0.86, s, ha='left', fontsize=fs, color=DARK, family='serif'); x += w + g
GOOD, BAD = TERRA, PLUM   # colour code: allowed steps terracotta; everything wrong (forbidden step, broken equivalence, false result, verdict) in the plum family
for k, st in enumerate(steps):
    col = BAD if k == len(steps) - 1 else DARK
    ax.text(3.7, y0 - k * dy, st, ha='center', fontsize=34, color=col, family='serif')
    if k < len(steps) - 1:   # the sign sits on the line it introduces: equivalences, all but one
        ax.text(1.3, y0 - (k + 1) * dy, r'$\Leftrightarrow$', ha='center', fontsize=40, color=BAD if k == 1 else DARK, family='serif')
# what is done to each line, noted behind a comment bar on the line it acts on, all in the same size
notes = [(1, r'$\div\,(a-b)$', BAD), (2, r'$a = b$', GOOD), (3, r'$\div\, b$', GOOD)]
for k, note, col in notes:
    ax.plot([5.98, 5.98], [y0 - k * dy - 0.13, y0 - k * dy + 0.42], color=col, lw=2.8, solid_capstyle='round')
    ax.text(6.3, y0 - k * dy, note, fontsize=34, color=col, family='serif')   # same baseline and size as the line it acts on
ax.text(5.2, y0 - 4 * dy - 0.05, '→ zero points', ha='left', fontsize=52, color=ROSE, family='Segoe Script')   # handwriting, like a marker on the exam sheet
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
