(python2.7)

<h3>Dobble_plane.py</h3>

Currently runs only in python terminal. <br>

Finite plane of 7x7 points is represented by shuffled *Dobble* type cards.

Each card has 8 pictures (represented here by numbers between 1 and 57), and every two cards have **exactly one** picture in common.
Now the cards will correspond to points and the pictures (numbers) in the cards correspond to lines. Ideal points and ideal lines are included.

**Usage:**

1. Open a python2 terminal.
2. Issue `execfile('dobble_plane.py')`
3. Type `p`.
4. For getting coordinates, ask e.g. `D18.xy` or `D18.x, D18.y`
5. Try `p.show(3)` to show line number 3 or `p.show(D02)` to see the point `D02` on the plane, etc.
