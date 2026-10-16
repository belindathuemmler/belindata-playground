# belindata playground

The code behind [The Playground](https://belindata.com/playground.html) on belindata.com: one folder per card.

- Where an article has an **interactive**, its folder holds the same interactive as a standalone HTML page. Open it in any browser, no installation needed.
- The **Python** scripts compute the card images and figures. Every image is computed from a formula: the Koch curve, the Möbius strip, an exact Zig-Zag path, Steiner symmetrization, parallel parking as a Lie bracket, and so on.
- `banach/` also contains a small reinforcement-learning experiment: value iteration as a Banach fixed-point iteration, with a numerical check of the contraction.

| Card | Folder | Interactive | Python |
|---|---|---|---|
| [Easy Writing “Mathematisch”](https://belindata.com/projects/math-writing.html) | [`math-writing/`](math-writing/) | [`moser_circle.html`](math-writing/moser_circle.html), [`four_solutions.html`](math-writing/four_solutions.html) | `math_writing_card.py` |
| [How Much Does a Flat Square Weigh?](https://belindata.com/projects/hausdorff.html) | [`hausdorff/`](hausdorff/) | [`koch_curve.html`](hausdorff/koch_curve.html) | `koch_curve.py` |
| [Robots Aiming for Banach Fixed Points](https://belindata.com/projects/banach.html) | [`banach/`](banach/) | [`robots_map.html`](banach/robots_map.html) |  |
| [Measuring on Curved Surfaces](https://belindata.com/projects/curved-surfaces.html) | [`curved-surfaces/`](curved-surfaces/) |  | `logo_twin_trefoil.py`, `moebius_chart_grid.py` |
| [Why the Circle Wins](https://belindata.com/projects/isoperimetric.html) | [`isoperimetric/`](isoperimetric/) | [`same_fence.html`](isoperimetric/same_fence.html) | `steiner_symmetrization.py`, `coming_soon_cards.py` |
| [True Mathematicians by Heart](https://belindata.com/projects/true-mathematicians.html) | [`true-mathematicians/`](true-mathematicians/) |  | `true_mathematicians_card.py` |
| [Silence = No Questions?](https://belindata.com/projects/silence.html) | [`silence/`](silence/) | [`any_questions.html`](silence/any_questions.html) | `silence_card.py` |
| [Playing With Knots](https://belindata.com/projects/knot-twins.html) | [`knot-twins/`](knot-twins/) | [`knots.html`](knot-twins/knots.html) | `reidemeister_card.py`, `knot_moves_check.py` |
| [Is Zig-Zag Better Than Stumbling Around?](https://belindata.com/projects/zig-zag.html) | [`zig-zag/`](zig-zag/) |  | `zigzag_trajectory.py` |
| [AI vs. Me: A Data Analysis Duel](https://belindata.com/projects/me-vs-ai.html) | [`me-vs-ai/`](me-vs-ai/) |  | `dashboard_card.py`, `coming_soon_cards.py` |
| [How a Machine Understands Similar Questions](https://belindata.com/projects/embeddings.html) | [`embeddings/`](embeddings/) |  | `coming_soon_cards.py` |
| [A Bracket and a Man Called Lie](https://belindata.com/projects/lie-bracket.html) | [`lie-bracket/`](lie-bracket/) |  | `lie_bracket_parking.py` |
| [Open the Shell. Which Shell?](https://belindata.com/projects/shell.html) | [`shell/`](shell/) |  | `shell_api_cards.py` |
| [What Is an API?](https://belindata.com/projects/api.html) | [`api/`](api/) |  | `shell_api_cards.py` |
| [Never Divide by Zero!](https://belindata.com/projects/divide-by-zero.html) | [`divide-by-zero/`](divide-by-zero/) |  | `divide_by_zero_card.py` |
| [The Golden Ratio Hides in a Pattern](https://belindata.com/projects/golden-ratio.html) | [`golden-ratio/`](golden-ratio/) |  | `fibonacci_card.py` |
| [The Needle in the ODE Haystack](https://belindata.com/projects/ode-haystack.html) | [`ode-haystack/`](ode-haystack/) |  | `ode_numerics_cards.py` |
| [Two Answers I Owed My Examiner](https://belindata.com/projects/numerics-exam.html) | [`numerics-exam/`](numerics-exam/) |  | `ode_numerics_cards.py` |
| [Eigenvalues, Finally Explained](https://belindata.com/projects/eigenvalues.html) | [`eigenvalues/`](eigenvalues/) |  | `eigenvalues_card.py` |
| [= or ⇔? Nerdy, but It Matters](https://belindata.com/projects/equals-iff.html) | [`equals-iff/`](equals-iff/) |  | `equals_iff_card.py` |
| [One for All, All for One: ∀, ∃ and Friends](https://belindata.com/projects/quantifiers.html) | [`quantifiers/`](quantifiers/) | [`four_musketeers.html`](quantifiers/four_musketeers.html) | `quantifiers_card.py` |
| [A Car From Above: My First Lesson in 3D Visualization](https://belindata.com/projects/car-from-above.html) | [`car-from-above/`](car-from-above/) |  | `car_from_above_card.py` |
| [About Fat and Thin Triangles](https://belindata.com/projects/triangles.html) | [`triangles/`](triangles/) |  | `triangles_card.py` |
| [About Fat and Thin Matrices](https://belindata.com/projects/sparse-dense.html) | [`sparse-dense/`](sparse-dense/) |  | `sparse_dense_card.py` |
| [The Binomial Formulas in Pictures](https://belindata.com/projects/binomial.html) | [`binomial/`](binomial/) |  | `binomial_card.py` |

Scripts that draw several cards at once live in [`cards/`](cards/).

## Requirements

`numpy` and `matplotlib` for the Python scripts (`pip install -r requirements.txt`, Python 3.9 or newer). The interactive pages load Tailwind and KaTeX from a CDN and need nothing else.

## About

The belindata logo itself is an AI-generated image inspired by a twisted ribbon; `curved-surfaces/logo_twin_trefoil.py` renders the mathematical object behind it. All code here was written with AI assistance (Claude) and checked by me. MIT license.
