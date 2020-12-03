#!/usr/bin/env python3
"""
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of
a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following
slopes, you start at the top-left corner and traverse the map all the way to
the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on
each of the listed slopes?

"""

with open('input') as f:
    the_map = [line.rstrip() for line in f]


def count_trees(dx, dy):
    x = 0
    trees = 0
    for row in the_map[::dy]:
        if row[x] == '#':
            trees += 1
        x = (x + dx) % len(row)
    return trees


trees = [
    count_trees(dx=1, dy=1),
    count_trees(dx=3, dy=1),
    count_trees(dx=5, dy=1),
    count_trees(dx=7, dy=1),
    count_trees(dx=1, dy=2),
]

answer = 1
for t in trees:
    answer *= t

print(answer)
