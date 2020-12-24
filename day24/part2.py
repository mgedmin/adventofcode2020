#!/usr/bin/python3
"""
--- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit. Every day, the
tiles are all flipped according to the following rules:

- Any black tile with zero or more than 2 black tiles immediately adjacent to
  it is flipped to white.
- Any white tile with exactly 2 black tiles immediately adjacent to it is
  flipped to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile
in question.

The rules are applied simultaneously to every tile; put another way, it is
first determined which tiles need to be flipped, then they are all flipped at
the same time.

In the above example, the number of black tiles that are facing up after the
given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208

After executing this process a total of 100 times, there would be 2208 black
tiles facing up.

How many tiles will be black after 100 days?
"""

import re
import sys
from collections import defaultdict


# The grid, oriented with East up top
#          E
#         ___
#     ___/   \___
#    /   \___/   \
# N  \___/   \___/  S
#    /   \___/   \
#    \___/   \___/
#        \___/
#          W
#
# Y axis goes east.  X axis goes south-east
direction = {
    'e': (0, 1),
    'w': (0, -1),
    'se': (1, 0),
    'sw': (1, -1),
    'ne': (-1, 1),
    'nw': (-1, 0),
}


def parse_directions(directions):
    x, y = 0, 0
    for step in re.findall('[ns]?[ew]', directions):
        dx, dy = direction[step]
        x += dx
        y += dy
    return x, y


def count_neighbours(state):
    neighbours = defaultdict(int)
    for (x, y), value in state.items():
        if value:
            for (dx, dy) in direction.values():
                neighbours[x+dx, y+dy] += 1
            neighbours[x, y] += 0  # autovivify, this is important
    return neighbours


def next_state(state):
    new_state = defaultdict(bool)
    neighbours = count_neighbours(state)
    for (x, y), value in neighbours.items():
        if state[x, y] and 1 <= value <= 2:
            new_state[x, y] = True
        elif not state[x, y] and value == 2:
            new_state[x, y] = True
    return new_state


tiles = defaultdict(bool)
with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    for line in f:
        x, y = parse_directions(line.strip())
        tiles[x, y] = not tiles[x, y]

for n in range(100):
    tiles = next_state(tiles)
print(sum(tiles.values()))
