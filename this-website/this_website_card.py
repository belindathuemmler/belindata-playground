"""Card image for 'This Website, Technically Explained': the folder of the website as a tree of files, with the list of cards, projects.js, picked out in colour.
Usage: python this_website_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, TERRA, CORAL, DARK, MUTED, LILAC = '#FAF8F5', '#874C62', '#B77A8A', '#DF7654', '#EE9779', '#1F1A1C', '#6E6266', '#D8A9BF'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_xlim(0, W); ax.set_ylim(H, 0)   # pixel coordinates, y pointing down
MONO = 'DejaVu Sans Mono'

# ---- the folder as a tree ----
tree = [
    (0, 'belindata.com/', DARK, 'bold'),
    (1, 'index.html', DARK, 'normal'),
    (1, 'playground.html', DARK, 'normal'),
    (1, 'projects/', DARK, 'bold'),
    (2, 'pi.html', MUTED, 'normal'),
    (2, 'silence.html', MUTED, 'normal'),
    (2, '…', MUTED, 'normal'),
    (1, 'assets/', DARK, 'bold'),
    (2, 'projects.js', TERRA, 'bold'),
    (2, 'images, fonts', MUTED, 'normal'),
]
x0, y0, dy, ind = 392, 86, 66, 72
ys = [y0 + k * dy for k in range(len(tree))]
for (lvl, name, col, wt), y in zip(tree, ys):
    ax.text(x0 + lvl * ind + 32, y, name, fontsize=35, color=col, family=MONO, weight=wt, va='center')
# the branches: one vertical line per folder, one short horizontal line per entry
def branch(parent, children):
    lvl = tree[parent][0]
    x = x0 + lvl * ind + 8
    ax.plot([x, x], [ys[parent] + 26, ys[children[-1]]], color=ROSE, lw=3, solid_capstyle='round')
    for c in children:
        ax.plot([x, x + ind - 6], [ys[c], ys[c]], color=ROSE, lw=3, solid_capstyle='round')
branch(0, [1, 2, 3, 7]); branch(3, [4, 5, 6]); branch(7, [8, 9])
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
