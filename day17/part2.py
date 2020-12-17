#!/usr/bin/python3
"""
--- Part Two ---

For some reason, your simulated results don't match what the experimental
energy source engineers expected. Apparently, the pocket dimension actually has
four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer
4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a
hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where
any of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at
x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region
of cubes. Furthermore, the same rules for cycle updating still apply: during
each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even
though the pocket dimension is 4-dimensional, this initial state represents a
small 2-dimensional slice of it. (In particular, this initial state defines a
3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following
configurations, where the result of each cycle is shown layer-by-layer at each
given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....

After the full six-cycle boot process completes, 848 cubes are left in the
active state.

Starting with your given initial configuration, simulate six cycles in a
4-dimensional space. How many cubes are left in the active state after the
sixth cycle?
"""

import sys
from collections import defaultdict


def empty_state(cell_type=bool):
    return defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(cell_type))))


def init_state(initial):
    state = empty_state()
    for y, row in enumerate(initial):
        for x, cell in enumerate(row):
            state[x][y][0][0] = (cell == '#')
    return state


def count_neighbours(state):
    neighbours = empty_state(int)
    for x in state:
        for y in state[x]:
            for z in state[x][y]:
                for w in state[x][y][z]:
                    if state[x][y][z][w]:
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                for dz in range(-1, 2):
                                    for dw in range(-1, 2):
                                        neighbours[x+dx][y+dy][z+dz][w+dw] += 1
                        # Note: it's important that the cell
                        # neighbours[x][y][z][w] exists even if its value gets
                        # reset back to 0!
                        neighbours[x][y][z][w] -= 1
    return neighbours


def next_state(state):
    new_state = empty_state()
    neighbours = count_neighbours(state)
    for x in neighbours:
        for y in neighbours[x]:
            for z in neighbours[x][y]:
                for w in neighbours[x][y][z]:
                    if state[x][y][z][w] and neighbours[x][y][z][w] in (2, 3):
                        new_state[x][y][z][w] = True
                    elif not state[x][y][z][w] and neighbours[x][y][z][w] == 3:
                        new_state[x][y][z][w] = True
    return new_state


def count_cubes(state):
    return sum(
        state[x][y][z][w]
        for x in state
        for y in state[x]
        for z in state[x][y]
        for w in state[x][y][z]
    )


with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    initial = [line.strip() for line in f]


state = init_state(initial)
for n in range(6):
    state = next_state(state)

print(count_cubes(state))
