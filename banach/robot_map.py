"""
Robots Aiming for Banach Fixed Points
=====================================

Value iteration for a robot in a 3x3 room, and a numerical look at why it
converges: the Bellman optimality operator is a contraction in the supremum
norm, so Banach's fixed-point theorem applies.

The room (y = 0 is the bottom row):

    +-----+-----+-----+
    |     |  B  |     |    B = charging station (absorbing, +2 per tick)
    +-----+-----+-----+
    |     |#####|     |    # = wall
    +-----+-----+-----+
    |  R  |     |     |    R = robot start
    +-----+-----+-----+

Moves: up, right, down, left. Every move costs 1 battery point (reward -1);
moving into the wall or the edge of the room means staying in place.

This mirrors the interactive demo on https://belindata.com/playground.html#banach
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

SIZE = 3
GAMMA = 0.8
WALL = 4         # centre cell, index = x + SIZE * y
STATION = 7      # top middle
START = 0        # bottom left
STEP_REWARD = -1.0
STATION_REWARD = 2.0

MOVES = {"↑": (0, 1), "→": (1, 0), "↓": (0, -1), "←": (-1, 0)}


def target(cell: int, move: tuple[int, int]) -> int:
    """Cell reached from `cell` with `move`; bumping into wall or edge means staying."""
    x, y = cell % SIZE + move[0], cell // SIZE + move[1]
    if not (0 <= x < SIZE and 0 <= y < SIZE):
        return cell
    nxt = x + SIZE * y
    return cell if nxt == WALL else nxt


def q_values(v: np.ndarray, cell: int) -> np.ndarray:
    """One-step lookahead for every move: reward + GAMMA * value of the next cell."""
    return np.array([STEP_REWARD + GAMMA * v[target(cell, m)] for m in MOVES.values()])


def bellman(v: np.ndarray) -> np.ndarray:
    """The Bellman optimality operator T."""
    tv = np.zeros_like(v)
    for cell in range(SIZE * SIZE):
        if cell == WALL:
            continue
        if cell == STATION:
            tv[cell] = STATION_REWARD + GAMMA * v[cell]
        else:
            tv[cell] = q_values(v, cell).max()
    return tv


def value_iteration(v0: np.ndarray, rounds: int) -> list[np.ndarray]:
    """Iterates V_0, T(V_0), T^2(V_0), ..."""
    vs = [v0]
    for _ in range(rounds):
        vs.append(bellman(vs[-1]))
    return vs


def sup_norm(v: np.ndarray) -> float:
    return float(np.max(np.abs(v)))


def greedy_policy(v: np.ndarray) -> dict[int, str]:
    """Best move(s) per cell; ties are kept."""
    names = list(MOVES)
    policy = {}
    for cell in range(SIZE * SIZE):
        if cell in (WALL, STATION):
            continue
        q = q_values(v, cell)
        best = [names[a] for a in np.flatnonzero(q > q.max() - 1e-9)]
        policy[cell] = " ".join(best)
    return policy


def print_room(v: np.ndarray, policy: dict[int, str]) -> None:
    for y in reversed(range(SIZE)):
        row = []
        for x in range(SIZE):
            cell = x + SIZE * y
            if cell == WALL:
                row.append(f"{'#####':^14}")
            elif cell == STATION:
                row.append(f"{'B ' + format(v[cell], '.2f'):^14}")
            else:
                row.append(f"{format(v[cell], '.2f') + ' ' + policy[cell]:^14}")
        print("|" + "|".join(row) + "|")


def main() -> None:
    n = SIZE * SIZE
    rounds = 40

    # The fixed point V*, computed to machine precision
    v_star = value_iteration(np.zeros(n), 2000)[-1]
    assert np.allclose(bellman(v_star), v_star)

    print(f"Optimal value function V* and greedy policy (gamma = {GAMMA}):\n")
    print_room(v_star, greedy_policy(v_star))

    # 1) Error of value iteration, starting from an empty map
    vs = value_iteration(np.zeros(n), rounds)
    errors = [sup_norm(v - v_star) for v in vs]
    print("\nError ||V_k - V*|| of value iteration from V_0 = 0:")
    for k in range(6):
        ratio = "" if k == 0 else f"   ratio {errors[k] / errors[k - 1]:.3f}"
        print(f"  k = {k}: {errors[k]:7.4f}{ratio}")

    # 2) Contraction check: two arbitrary guesses U, V, the gap shrinks by at least GAMMA
    rng = np.random.default_rng(seed=1)
    worst_ratio = 0.0
    for _ in range(10_000):
        u, v = rng.uniform(-50, 50, n), rng.uniform(-50, 50, n)
        u[WALL] = v[WALL] = 0.0
        worst_ratio = max(worst_ratio, sup_norm(bellman(u) - bellman(v)) / sup_norm(u - v))
    print(f"\nLargest observed ||TU - TV|| / ||U - V|| over 10,000 random pairs: "
          f"{worst_ratio:.4f} (theory: <= {GAMMA})")

    # 3) Two different starting guesses forget where they started
    optimist = value_iteration(np.full(n, 30.0), rounds)
    pessimist = value_iteration(np.full(n, -30.0), rounds)
    gaps = [sup_norm(a - b) for a, b in zip(optimist, pessimist)]

    # Plot: errors on a log scale are a straight line with slope log(GAMMA)
    k = np.arange(rounds + 1)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.semilogy(k, errors, "o-", ms=3.5, color="#DF7654", label=r"$\|V_k - V^*\|_\infty$ (from $V_0 = 0$)")
    ax.semilogy(k, gaps, "s-", ms=3.5, color="#874C62", label=r"$\|T^k U - T^k V\|_\infty$ (two guesses $\pm 30$)")
    ax.semilogy(k, errors[0] * GAMMA ** k, "--", color="#6E6266", lw=1, label=r"$\gamma^k \cdot \|V_0 - V^*\|_\infty$")
    ax.set_xlabel("round of thinking $k$")
    ax.set_ylabel("sup-norm distance (log scale)")
    ax.set_title(f"Bellman operator as a contraction, $\\gamma = {GAMMA}$")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()

    out = Path(__file__).parent / "figures" / "convergence.png"
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, dpi=160)
    print(f"\nPlot saved to {out.relative_to(Path(__file__).parent)}")


if __name__ == "__main__":
    main()
