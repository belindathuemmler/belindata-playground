# A Bracket and a Man Called Lie

Article: [https://belindata.com/projects/lie-bracket.html](https://belindata.com/projects/lie-bracket.html) (in progress)

- `parking_lot.html`: the two interactives from the article as one standalone page. The Parking Lot: a car with two controls, steer (X) and drive (Y), sliders for the size of a click, parking by hand, and two prepared sequences: X,Y,−X,−Y (= [X,Y], a turn) and X,Y,−Y,−X (always closes). The Bracket Fields: every bracket spelled out as moves and played step by step, then start and end compared. Open it in any browser.
- `lie_bracket_parking.py`: Card image for the Lie bracket: a car parallel-parks. It can only drive and steer, yet it ends up shifted sideways, the direction of the Lie bracket [steer, drive].
- `card_lie_bracket.jpg`: the image as used on the site

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
