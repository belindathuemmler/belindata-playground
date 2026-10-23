# A Bracket and a Man Called Lie

Article: [https://belindata.com/projects/lie-bracket.html](https://belindata.com/projects/lie-bracket.html) (in progress)

- `parking_lot.html`: the interactive from the article as a standalone page. A car with two controls, steer and drive (bicycle model, exact arcs); the prepared sequences show the commutator square (steer, drive, unsteer, reverse: a turn, the bracket [steer, drive]) and one parking wiggle (a sideways shift, [[steer, drive], drive]). Open it in any browser.
- `lie_bracket_parking.py`: Card image for the Lie bracket: a car parallel-parks. It can only drive and steer, yet it ends up shifted sideways, the direction of the Lie bracket [steer, drive].
- `card_lie_bracket.jpg`: the image as used on the site

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
