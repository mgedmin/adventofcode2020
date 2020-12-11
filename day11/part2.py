#!/usr/bin/env python3
"""
--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just
care about adjacent seats - they care about the first seat they can see in each
of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider
the first seat in each of those eight directions. For example, the empty seat
below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any
of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or
more visible occupied seats for an occupied seat to become empty (rather than
four or more from the previous rules). The other rules still apply: empty seats
that see no occupied seats become occupied, seats matching no rule don't
change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area
to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches
equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming
empty, once equilibrium is reached, how many seats end up occupied?
"""

import sys


def count_occupied(seats):
    return sum(row.count('#') for row in seats)


def next_seat_occupied_in_direction(r, c, dr, dc, seats):
    assert dr != 0 or dc != 0
    while True:
        r += dr
        c += dc
        if not 0 <= r < len(seats):
            return False
        if not 0 <= c < len(seats[r]):
            return False
        if seats[r][c] == '#':
            return True
        if seats[r][c] == 'L':
            return False


def count_visible_occupied(r, c, seats):
    return sum(
        1
        for dr in range(-1, 2)
        for dc in range(-1, 2)
        if not (dr == dc == 0)
        and next_seat_occupied_in_direction(r, c, dr, dc, seats)
    )


def apply_rules(seats):
    result = []
    for r, row in enumerate(seats):
        result_row = []
        for c, cell in enumerate(row):
            if cell == 'L' and count_visible_occupied(r, c, seats) == 0:
                cell = '#'
            elif cell == '#' and count_visible_occupied(r, c, seats) >= 5:
                cell = 'L'
            result_row.append(cell)
        result.append(''.join(result_row))
    return result


def main():
    with open('input' if len(sys.argv) < 2 else sys.argv[1]) as f:
        seats = [line.strip() for line in f]

    while (next_iteration := apply_rules(seats)) != seats:
        seats = next_iteration

    if '-v' in sys.argv:
        print('\n'.join(seats))
    print(count_occupied(seats))


if __name__ == "__main__":
    main()
