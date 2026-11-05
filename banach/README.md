# Robots Aiming for Banach Fixed Points

Why does reinforcement learning work, at least in theory? Because the robot's
thinking rule (the Bellman operator) is a **contraction**, and Banach's fixed-point
theorem, a second-semester theorem, then guarantees a unique true value map and
geometric convergence to it.

This folder contains a small Python implementation that accompanies the
article and interactive demo on
[belindata.com/projects/banach.html](https://belindata.com/projects/banach.html).

## The setup

A robot in a 3×3 room wants to reach its charging station:

```
+-----+-----+-----+
|     |  B  |     |    B = charging station (+2 per tick, absorbing)
+-----+-----+-----+
|     |#####|     |    # = wall
+-----+-----+-----+
|  R  |     |     |    R = robot start
+-----+-----+-----+
```

The robot can move up, right, down or left. Every move costs 1 battery point;
moving into the wall or the edge of the room means staying in place. The
discount factor is γ = 0.8.

The robot's "map" is the value function `V`, one number per cell. Value
iteration improves it with the Bellman operator

$$(TV)(s) = \max_a \big[ R(s,a) + \gamma \, V(s') \big].$$

## Why the error shrinks

Compare the map with the truth `V*` in any cell. Both are computed by the
same formula, so the reward cancels:

$$|(TV)(s) - V^*(s)| \le \gamma \, \max_{s'} |V(s') - V^*(s')|.$$

The error after one round is at most γ times the error before. That is the
contraction property `‖TU − TV‖∞ ≤ γ ‖U − V‖∞`, and Banach's theorem turns it
into a guarantee: exactly one fixed point `V* = TV*`, reached from *any* starting
guess, with `‖V_k − V*‖∞ ≤ γ^k ‖V_0 − V*‖∞`.

## What the script does

`robot_map.py`

1. computes `V*` and the greedy (optimal) policy,
2. runs value iteration from an empty map and prints the error per round
   (10 → 8 → 6.4 → …, ratio exactly 0.8),
3. checks the contraction numerically on 10,000 random pairs of guesses,
4. plots both the error to `V*` and the gap between two very different guesses
   on a log scale, where geometric convergence is a straight line.

![Convergence plot](figures/convergence.png)

## Interactive

`robots_map.html` is the robot demo from the article as a standalone page: open it in any browser.

`the_chain.html` is Banach's iteration as a picture of the contraction chain: f(x) = x/2 + 1 applied to two points x and y, one row per round (six rows); drag x and y in the top row or roll a random start, and the distance between them halves in every row, (½)^k · |x − y|, while both columns walk to the fixed point 2.

`robots_table.html` is the Bellman operator on a visible table: a robot in a corridor of five cells (station in cell 5, every step costs 1, arrival pays 10, left out of cell 1 bumps into the wall), Q with four rows and two actions, random start; tap an entry to see its line of the equation with today's numbers, apply one round of T, and watch the largest change per round and the distance to Q* shrink by the factor γ = 0.8 while the arrows settle on the way to the station.

## Run it

```bash
pip install -r ../requirements.txt
python robot_map.py
```

Requires Python 3.9 or newer.

## Where the guarantee ends

All of this holds in an idealized world: finitely many states, a known model,
and a table of values. Real walking robots learn from noisy experience and
approximate `V` with neural networks. There the projected Bellman operator is in
general no longer a contraction, and Banach alone is not enough.

## Further reading

- Walter Rudin, *Principles of Mathematical Analysis* (3rd ed., 1976), Theorem 9.23:
  the contraction principle as taught in a second-semester analysis course.
- Andrew Ng, *Machine Learning Specialization* (Coursera / DeepLearning.AI),
  where this exploration started.

## License

MIT, see [LICENSE](LICENSE).
