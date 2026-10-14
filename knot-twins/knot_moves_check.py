import numpy as np, itertools
N = 480
t = np.linspace(0, 2*np.pi, N, endpoint=False)
wrap = lambda a: ((a + np.pi) % (2*np.pi)) - np.pi
BASES = {
 'unknot': lambda t: np.stack([1.2*np.cos(t), 1.2*np.sin(t), 0*t], 1),
 'trefoil': lambda t: np.stack([0.45*(np.sin(t)+2*np.sin(2*t)), 0.45*(np.cos(t)-2*np.cos(2*t)), -np.sin(3*t)], 1),
 'eight': lambda t: np.stack([0.45*(2+np.cos(2*t))*np.cos(3*t), 0.45*(2+np.cos(2*t))*np.sin(3*t), np.sin(4*t)], 1)}

def curve(name, s1, s2, t1, t2, push, gs=0.3, plat=0.4, edge=0.72, la=4.0):
    P = BASES[name](t); Q = P.copy()
    c = P[:, :2].mean(0)
    d = np.roll(P, -1, 0) - np.roll(P, 1, 0); L = np.linalg.norm(d[:, :2], axis=1)
    T = d[:, :2]/L[:, None]; Nn = np.stack([-T[:, 1], T[:, 0]], 1)
    Nn *= np.sign(((c-P[:, :2])*Nn).sum(1))[:, None]
    speed = L/(2*2*np.pi/N)
    i1 = int(round((t1 % (2*np.pi))/(2*np.pi)*N)) % N
    rho = 0.4; delta = rho*np.pi/(3*speed[i1])
    u = wrap(t-t1)/delta; m = np.abs(u) < 1; ph = np.pi*(u[m]+1)
    Q[m, :2] += s1*rho*(np.sin(ph)[:, None]*T[m] - (1-np.cos(ph))[:, None]*Nn[m]); Q[m, 2] += s1*0.6*u[m]
    i2 = int(round((t2 % (2*np.pi))/(2*np.pi)*N)) % N
    v = c - P[i2, :2]; v /= np.linalg.norm(v)
    d2 = wrap(t-t2); g = np.exp(-(d2/gs)**2)
    a_ = np.abs(d2); lift = np.where(a_ <= plat, 1.0, np.where(a_ >= edge, 0.0, 0.5*(1+np.cos(np.pi*(a_-plat)/(edge-plat)))))
    Q[:, :2] += (s2*push*g)[:, None]*v[None, :]; Q[:, 2] += s2*la*lift
    return Q

def crossings(P):
    n = len(P); out = []
    for i in range(n):
        a, b = P[i], P[(i+1) % n]
        for j in range(i+2, n):
            if i == 0 and j == n-1: continue
            c_, d_ = P[j], P[(j+1) % n]
            r = b[:2]-a[:2]; s = d_[:2]-c_[:2]; den = r[0]*s[1]-r[1]*s[0]
            if abs(den) < 1e-12: continue
            w = c_[:2]-a[:2]; ta = (w[0]*s[1]-w[1]*s[0])/den; tb = (w[0]*r[1]-w[1]*r[0])/den
            if 0 <= ta < 1 and 0 <= tb < 1:
                za = a[2]+ta*(b[2]-a[2]); zb = c_[2]+tb*(d_[2]-c_[2])
                out.append(((i+ta, j+tb) if za > zb else (j+tb, i+ta)))  # (over, under)
    return out

def tricolourable(cr):
    n = len(cr)
    if n == 0: return False
    gaps = sorted(range(n), key=lambda k: cr[k][1]); pos = [cr[k][1] for k in gaps]; rank = {k: j for j, k in enumerate(gaps)}
    def arc(p):
        for j in range(n-1, -1, -1):
            if p >= pos[j]: return j
        return n-1
    cons = [(arc(cr[k][0]), (rank[k]-1) % n, rank[k]) for k in range(n)]
    for col in itertools.product(range(3), repeat=n-1):
        col = (0,)+col
        if len(set(col)) < 2: continue
        if all(len({col[o], col[a], col[b]}) in (1, 3) for o, a, b in cons): return True
    return False

def determinant(cr):
    n = len(cr)
    if n == 0: return 1
    gaps = sorted(range(n), key=lambda k: cr[k][1]); pos = [cr[k][1] for k in gaps]; rank = {k: j for j, k in enumerate(gaps)}
    def arc(p):
        for j in range(n-1, -1, -1):
            if p >= pos[j]: return j
        return n-1
    M = np.zeros((n, n))
    for k in range(n):
        o, a, b = arc(cr[k][0]), (rank[k]-1) % n, rank[k]
        M[k, o] += 2; M[k, a] -= 1; M[k, b] -= 1
    return int(round(abs(np.linalg.det(M[1:, 1:])))) if n > 1 else 1

def base_crossing_params(name):
    return sorted(set(round(x*2*np.pi/N, 2) for c in crossings(BASES[name](t)) for x in c))

CFG = {'unknot': (0, np.pi/2, 2.9, {}), 'trefoil': (np.pi, np.pi/3, 1.6, {}), 'eight': (0, np.pi, 1.5, dict(gs=0.2, plat=0.28, edge=0.48))}
grid = [0, 0.25, 0.5, 0.75, 1.0]
for name, (t1, t2, push, kw) in CFG.items():
    dets = set(); cnts = set()
    for s1 in grid:
        for s2 in grid:
            cr = crossings(curve(name, s1, s2, t1, t2, push, **kw))
            dets.add(determinant(cr)); cnts.add(len(cr))
    cr = crossings(curve(name, 1, 1, t1, t2, push, **kw))
    print(name, 'determinants over all slider positions:', sorted(dets), '| crossing counts:', sorted(cnts), '| tricolourable at (1,1):', tricolourable(cr))
