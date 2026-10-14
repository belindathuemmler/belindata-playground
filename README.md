# belindata figures

Python scripts behind the figures on [belindata.com](https://belindata.com). Every image is computed from a formula.

| Script | Figure | Usage |
|---|---|---|
| `logo_twin_trefoil.py` | The mathematical twin of the belindata logo: a ribbon along a trefoil knot | `python logo_twin_trefoil.py out.png 90 -90 1.45 0.6 0` (elev, azim, ribbon width, tilt, colour shift) |
| `moebius_chart_grid.py` | Möbius strip with the grid of a flat chart | `python moebius_chart_grid.py out.jpg 35 -60` (elev, azim) |
| `zigzag_trajectory.py` | Exact 2D Zig-Zag trajectory for a standard normal target | `python zigzag_trajectory.py out.jpg 11 30` (seed, time horizon) |
| `koch_curve.py` | Koch curve with its first construction steps | `python koch_curve.py out.jpg` |
| `steiner_symmetrization.py` | Steiner symmetrization of an irregular shape: same area, shorter boundary | `python steiner_symmetrization.py out.jpg` |
| `lie_bracket_parking.py` | Parallel parking as a Lie bracket: steer + drive gives a sideways move | `python lie_bracket_parking.py out.jpg` |
| `true_mathematicians_card.py` | An implication, its contraposition and a counterexample | `python true_mathematicians_card.py out.jpg` |
| `silence_card.py` | “Any questions?”: a silent room in which almost everybody has a question | `python silence_card.py out.jpg` |
| `shell_api_cards.py` | System shell vs. Python shell, and the API as a restaurant menu | `python shell_api_cards.py <output folder>` |
| `divide_by_zero_card.py` | The classic “proof” that 2 = 1 and its hidden division by zero | `python divide_by_zero_card.py out.jpg` |
| `fibonacci_card.py` | The Fibonacci substitution a → ab, b → a as rows of long and short tiles | `python fibonacci_card.py out.jpg` |
| `ode_numerics_cards.py` | A direction field with one solution curve; operator norm and gradient descent | `python ode_numerics_cards.py <output folder>` |
| `dashboard_card.py` | A Me-vs-AI dashboard with the real numbers from my IBM Data Analyst capstone | `python dashboard_card.py out.jpg` |
| `eigenvalues_card.py` | Eigenvectors that only stretch, and what λ does to e^(λt) | `python eigenvalues_card.py out.jpg` |
| `equals_iff_card.py` | = connects objects, ⇔ connects statements | `python equals_iff_card.py out.jpg` |
| `car_from_above_card.py` | A child’s drawing of a car from above, and the same car taken literally in 3D | `python car_from_above_card.py out.jpg` |
| `reidemeister_card.py` | The three Reidemeister moves of knot theory: twist, poke, slide | `python reidemeister_card.py out.jpg` |
| `triangles_card.py` | Flat, fat (spherical) and thin (hyperbolic) triangles and their angle sums | `python triangles_card.py out.jpg` |
| `sparse_dense_card.py` | A dense and a sparse matrix side by side | `python sparse_dense_card.py out.jpg` |
| `binomial_card.py` | The three binomial formulas as pictures | `python binomial_card.py out.jpg` |
| `coming_soon_cards.py` | Card images for upcoming notes: isoperimetry, mathematical writing, text embeddings, me vs. AI | `python coming_soon_cards.py <output folder>` |

The belindata logo itself is an AI-generated image inspired by a twisted ribbon. `logo_twin_trefoil.py` renders the mathematical object behind it.

## Interactive

- `knot_moves_check.py`: checks that the twist and poke moves of the “Playing With Knots” page are honest Reidemeister moves: the knot determinant stays 1 (unknot), 3 (trefoil) and 5 (figure-eight) for every slider position.

- `interactive/moser_circle.html`: the “1, 2, 4, 8, 16, … ?” animation (Moser's circle problem). Open it in any browser, no installation needed.

Requirements for the Python scripts: `numpy`, `matplotlib` (`pip install -r requirements.txt`). All code was written with AI assistance (Claude) and checked by me; MIT license.
