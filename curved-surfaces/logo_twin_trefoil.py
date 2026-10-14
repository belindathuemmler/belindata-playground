"""belindata logo, rebuilt as mathematics: a ribbon along a trefoil knot, in the logo gradient."""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

out = sys.argv[1]
elev, azim = float(sys.argv[2]), float(sys.argv[3])
width = float(sys.argv[4]) if len(sys.argv) > 4 else 0.55
tilt = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0  # how far the band tips over where the knot climbs
cshift = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0  # where the colour gradient starts

def trefoil(t):
    """Trefoil knot, turned so that one lobe points up and two point down-left / down-right."""
    x = -(np.sin(t) + 2 * np.sin(2 * t))
    y = -(np.cos(t) - 2 * np.cos(2 * t))
    z = -np.sin(3 * t)
    # Logo proportions: wider, rounder lower lobes, a slimmer top lobe leaning slightly right
    low = np.clip(-y / 3, 0, 1)
    high = np.clip(y / 3, 0, 1)
    x = x * (1 + 0.22 * low) * (1 - 0.18 * high) + 0.45 * high ** 2
    y = y * (1 + 0.12 * high)
    return np.stack([x, y, z])

n_t, n_w = 1400, 10
t = np.linspace(0, 2 * np.pi, n_t)
C = trefoil(t)
T = np.gradient(C, t, axis=1); T /= np.linalg.norm(T, axis=0)
# Ribbon direction: perpendicular to the tangent and as flat as possible towards the viewer (z),
# tipped over where the knot climbs or falls (the crossings), so the band shows its edge there
z = np.array([0, 0, 1.0])[:, None]
Wd = np.cross(z.T, T.T).T; Wd /= np.linalg.norm(Wd, axis=0)
Nd = np.cross(T.T, Wd.T).T
ang = tilt * np.cos(3 * t)
D = np.cos(ang) * Wd + np.sin(ang) * Nd

s = np.linspace(-width / 2, width / 2, n_w)
P = C[:, :, None] + D[:, :, None] * s[None, None, :]   # 3 × n_t × n_w

# Colour along the knot: lower-left lobe lilac, crossings apricot, top lobe coral red, lower-right lobe orange/mauve
cmap = LinearSegmentedColormap.from_list('logo', ['#F7CF8F', '#E3B8E6', '#F9D58E', '#F08068', '#F6A35E', '#C995C2', '#F7CF8F'])
light = np.array([-0.4, 0.5, 0.75]); light /= np.linalg.norm(light)
view = np.array([np.cos(np.radians(elev)) * np.cos(np.radians(azim)),
                 np.cos(np.radians(elev)) * np.sin(np.radians(azim)),
                 np.sin(np.radians(elev))])

polys, cols = [], []
for i in range(n_t - 1):
    for j in range(n_w - 1):
        q = [P[:, i, j], P[:, i + 1, j], P[:, i + 1, j + 1], P[:, i, j + 1]]
        nrm = np.cross(q[1] - q[0], q[3] - q[0]); nrm /= np.linalg.norm(nrm) + 1e-12
        if nrm @ view < 0:
            nrm = -nrm                                  # two-sided ribbon
        diff = max(nrm @ light, 0)
        h = light + view; h /= np.linalg.norm(h)
        spec = max(nrm @ h, 0) ** 30
        # soft edge darkening across the ribbon, like the rounded logo band
        edge = 1 - 0.10 * (abs(s[j] + s[j + 1]) / width) ** 2
        base = np.array(cmap((t[i] / (2 * np.pi) + cshift) % 1.0)[:3])
        c = base * (0.90 + 0.12 * diff) * edge + 0.28 * spec
        polys.append(q); cols.append(np.clip(c, 0, 1))

fig = plt.figure(figsize=(6, 6), dpi=100)
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.set_axis_off()
ax.add_collection3d(Poly3DCollection(polys, facecolors=cols, edgecolors=cols, linewidths=0.3))
lim = 3.3
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
ax.set_box_aspect((1, 1, 1))
ax.set_proj_type('persp', focal_length=0.6)
ax.view_init(elev=elev, azim=azim)
fig.savefig(out, dpi=200, transparent=True)
