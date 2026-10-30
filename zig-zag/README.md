# Is Zig-Zag Better Than Stumbling Around?

Article: [https://belindata.com/projects/zig-zag.html](https://belindata.com/projects/zig-zag.html) (coming soon)

- `zigzag_trajectory.py`: Card image: an exact 2D Zig-Zag trajectory for the standard normal target, in belindata colours.
- `card_zigzag_thesis.jpg`: that image (the card image until 30 October 2026)
- `dark_room_card.py`, `card_zigzag_darkroom.jpg`: card image since 30 October 2026: the dark room from the interactive below, explored by the string of lights, as a still (`python dark_room_card.py card_zigzag_darkroom.jpg 8 30.3 0 6`, needs `numpy` and `Pillow`).
- `dark_room.html`: interactive "The Dark Room": two identical dark rooms, explored by a flashlight (random-walk Metropolis–Hastings) and a string of lights (Zig-Zag, switching rate max(0, θᵢ∂ᵢU), approximated in small time steps (turn with probability 1 − exp(−λ·dt)), not one of the exact variants; walls bounce). Wherever an explorer spends time, the room lights up. Fair race: same distance per second, same amount of light. Open it in any browser.
- `the_race.html`: interactive "The Race": Metropolis–Hastings vs Zig-Zag in 1D on a Gaussian or a Cauchy target, started in the middle or far out. Three Zig-Zag variants as in the thesis: ZZ_CDF (exact inversion of the integrated rate), ZZ_M (Poisson thinning with an upper bound: exact affine bound for the Gaussian, local constant bound for Cauchy), ZZ_ODE (switching time found numerically with RK4, step 0.1). Three fairness rules: same number of steps K, same number of density/rate evaluations, or same computing time (per-step cost measured live on the viewer's device). Shows the last steps, the histogram against the target and the W₁ distance (on the visible range) over the chosen budget.

Python scripts need `numpy`, `matplotlib` and `Pillow` (`pip install -r ../requirements.txt`).
