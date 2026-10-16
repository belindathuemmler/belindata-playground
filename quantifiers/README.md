# One for All, All for One: ∀, ∃ and Friends

Article: [https://belindata.com/projects/quantifiers.html](https://belindata.com/projects/quantifiers.html) (in progress)

- `four_musketeers.html`: the interactive from the article as a standalone page: hand out swords, hats and horses, tick who covers whom, and watch ∀, ∃, ∃!, ∄ and the two orders ∃∀ / ∀∃ turn true or false.
- `quantifiers_card.py`: the card image: ∀ε ∃δ (a different δ for each ε) next to ∃δ ∀ε (one δ for all of them)
- `quantifiers_card_musketeers.py`: an alternative card image, the four symbols with musketeer hats (not used on the site for now)
- `card_quantifiers.jpg`: the image as used on the site
- `eps_delta_diagrams.html`: the two inline-SVG diagrams that used to sit in the Math Writing article, kept for the future page

Plan for the page (agreed 2026-10-16): the four signs ∀x P(x), ∃x P(x), ∃!x P(x) = ∃x (P(x) ∧ ∀y (P(y) ⇒ y = x)), ∄x P(x) ≡ ¬∃x P(x) ≡ ∀x ¬P(x); negation rules ¬∀ = ∃¬, ¬∃ = ∀¬; order: ∃y∀x ⇒ ∀x∃y but not back (everyone has a mother vs. a mother of everyone); musketeer reading: one for all = ∃∀, all for one = ∀∃, exactly one = ∃!, none = ∄; interactive idea: four musketeers with sword/hat/horse toggles and clickable statements that turn true/false. Also the example that shows what the order does: ∀ε ∃δ (with |x−y|<δ ⇒ |f(x)−f(y)|<ε) is uniform continuity, ∃δ ∀ε is satisfied on ℝ only by constant functions. Kept out of the teaser on purpose.

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
