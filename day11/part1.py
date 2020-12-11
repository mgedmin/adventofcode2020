#!/usr/bin/env python3
"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is
a ferry that goes directly to the tropical island where you can finally start
your vacation. As you reach the waiting area to board the ferry, you realize
you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You
make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an
empty seat (L), or an occupied seat (#). For example, the initial seat layout
might look like this:

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

Now, you just need to model the people who will be arriving shortly.
Fortunately, people are entirely predictable and always follow a simple set of
rules. All decisions are based on the number of occupied seats adjacent to a
given seat (one of the eight positions immediately up, down, left, right, or
diagonal from the seat). The following rules are applied to every seat
simultaneously:

- If a seat is empty (L) and there are no occupied seats adjacent to it, the
  seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also
  occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes
occupied:

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

After a second round, the seats with four or more occupied adjacent seats
become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further
applications of these rules cause no seats to change state! Once people stop
moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?
"""

import sys


def count_occupied(seats):
    return sum(row.count('#') for row in seats)


def count_adjacent_occupied(r, c, seats):
    return sum(
        1
        for rr in range(r-1, r+2)
        for cc in range(c-1, c+2)
        if not (r == rr and c == cc)
        and 0 <= rr < len(seats)
        and 0 <= cc < len(seats[rr])
        and seats[rr][cc] == '#'
    )


def apply_rules(seats):
    result = []
    for r, row in enumerate(seats):
        result_row = []
        for c, cell in enumerate(row):
            if cell == 'L' and count_adjacent_occupied(r, c, seats) == 0:
                cell = '#'
            elif cell == '#' and count_adjacent_occupied(r, c, seats) >= 4:
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
