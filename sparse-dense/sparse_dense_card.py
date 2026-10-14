"""Card image for 'About Fat and Thin Matrices': a dense matrix (every entry a number) next to a sparse one
(almost all zeros, stored as just a few numbers). Usage: python sparse_dense_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C'
n = 18
rng = np.random.default_rng(5)
dense = rng.random((n, n))
sparse = np.zeros((n, n))
for i in range(n):                       # a band around the diagonal plus a few scattered entries,
    for j in (i - 1, i, i + 1):          # like the matrix of a grid or a network
        if 0 <= j < n:
            sparse[i, j] = 0.4 + 0.6 * rng.random()
for _ in range(8):
    sparse[rng.integers(n), rng.integers(n)] = 0.4 + 0.6 * rng.random()

cmap = LinearSegmentedColormap.from_list('b', ['#F7E3D9', CORAL, TERRA, PLUM])
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
for k, (M, title, note) in enumerate([(dense, 'dense (fat)', f'all {n * n} entries stored'),
                                      (sparse, 'sparse (thin)', f'only {int((sparse > 0).sum())} non-zeros stored')]):
    ax = fig.add_axes([0.08 + k * 0.48, 0.16, 0.36, 0.64])
    shown = np.where(M > 0, M, np.nan)
    ax.set_facecolor('white')
    ax.imshow(shown, cmap=cmap, vmin=0, vmax=1)
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True); ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which='minor', color='#E8DED8', lw=0.8)
    ax.tick_params(which='both', length=0); ax.set_xticks([]); ax.set_yticks([])
    for side in ax.spines.values():
        side.set_color(ROSE)
    fig.text(0.26 + k * 0.48, 0.85, title, ha='center', fontsize=26, color=PLUM, family='serif')
    fig.text(0.26 + k * 0.48, 0.07, note, ha='center', fontsize=21, color=DARK, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
