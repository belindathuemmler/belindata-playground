"""Card image: Möbius strip in the belindata logo gradient, with the chart grid (u, v) drawn on it."""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

out = sys.argv[1]
elev, azim = float(sys.argv[2]), float(sys.argv[3])

def phi(u, v):
    """Möbius strip: centre circle of radius 1, half-width 0.4."""
    r = 1 + 0.4 * v * np.cos(u / 2)
    return r * np.cos(u), r * np.sin(u), 0.4 * v * np.sin(u / 2)

# Logo gradient: lilac → apricot → coral → plum
cmap = LinearSegmentedColormap.from_list('logo', ['#D8A9BF', '#F4C98F', '#EE9779', '#DF7654', '#B77A8A', '#D8A9BF'])

# Chart grid: every cell of the (u, v) map becomes one tile on the strip
u = np.linspace(0, 2 * np.pi, 73)
v = np.linspace(-1, 1, 9)
U, V = np.meshgrid(u, v)
X, Y, Z = phi(U, V)

W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor('#FAF8F5')
ax = fig.add_axes([-0.1, -0.3, 1.2, 1.6], projection='3d')
ax.set_facecolor('#FAF8F5')
ax.set_axis_off()
ax.view_init(elev=elev, azim=azim)

# Colour by u (logo gradient), with gentle two-sided lighting so both "sides" stay bright
Uc = (U[:-1, :-1] + U[1:, 1:]) / 2
Vc = (V[:-1, :-1] + V[1:, 1:]) / 2
du = np.stack(phi(Uc + 1e-4, Vc)) - np.stack(phi(Uc, Vc))
dv = np.stack(phi(Uc, Vc + 1e-4)) - np.stack(phi(Uc, Vc))
n = np.cross(du, dv, axis=0); n /= np.linalg.norm(n, axis=0)
light = np.array([0.3, -0.5, 0.8]); light /= np.linalg.norm(light)
lam = np.abs(np.tensordot(light, n, axes=1))
base = cmap(Uc / (2 * np.pi))
colors = base.copy()
colors[..., :3] = base[..., :3] * (0.82 + 0.18 * lam[..., None]) + 0.06
colors = np.clip(colors, 0, 1)
ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1, edgecolor='#FFFFFF', linewidth=0.7, antialiased=True, shade=False)

ax.set_box_aspect((1, 1, 0.5))
lim = 1.25
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-0.6, 0.6)
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor(), pil_kwargs={'quality': 92})
