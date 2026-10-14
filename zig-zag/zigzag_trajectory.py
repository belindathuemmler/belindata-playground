"""Card image: an exact 2D Zig-Zag trajectory for the standard normal target, in belindata colours."""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out, seed, T = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
rng = np.random.default_rng(seed)

def zigzag_1d(x, theta, T):
    """Exact 1D Zig-Zag for N(0,1): rate max(0, theta*x), event times by inversion."""
    t, ts, xs = 0.0, [0.0], [x]
    while t < T:
        a = theta * x
        tau = -a + np.sqrt(max(a, 0.0) ** 2 + 2 * rng.exponential())
        tau = min(tau, T - t)
        t += tau
        x += theta * tau
        theta = -theta
        ts.append(t); xs.append(x)
    return np.array(ts), np.array(xs)

# For N(0, I) the coordinates are independent 1D Zig-Zag processes
t1, x1 = zigzag_1d(-4.6, 1.0, T)
t2, x2 = zigzag_1d(2.3, -1.0, T)
ts = np.union1d(t1, t2)
X, Y = np.interp(ts, t1, x1), np.interp(ts, t2, x2)

W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor('#FAF8F5')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor('#FAF8F5')
h = 3.4
ax.set_xlim(-h * W / H, h * W / H); ax.set_ylim(-h, h)
ax.set_aspect('equal'); ax.axis('off')

# Target density as soft filled contours
g = np.linspace(-7, 7, 400)
GX, GY = np.meshgrid(g, g)
Z = np.exp(-0.5 * (GX ** 2 + GY ** 2))
ax.contourf(GX, GY, Z, levels=np.linspace(0.02, 1, 9), cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
    'bd', ['#FAF8F5', '#E3C3CB']), alpha=0.9, zorder=0)
ax.contour(GX, GY, Z, levels=np.linspace(0.05, 0.95, 6), colors='#B77A8A', linewidths=1.3, alpha=0.55, zorder=1)

ax.plot(X, Y, color='#DF7654', lw=3.4, solid_joinstyle='miter', zorder=3)
ax.scatter([X[0]], [Y[0]], s=220, color='#874C62', zorder=4)
fig.savefig(out, dpi=100, facecolor=fig.get_facecolor(), pil_kwargs={'quality': 90})
print(len(ts), 'segments')
