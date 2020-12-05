#!/usr/bin/env python3
"""
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding
pass in your list. However, there's a catch: some of the seats at the very
front and back of the plane don't exist on this aircraft, so they'll be missing
from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and
-1 from yours will be in your list.

What is the ID of your seat?
"""


def parse_seat(line):
    return int(line.translate({ord('B'): '1', ord('F'): '0',
                               ord('R'): '1', ord('L'): '0'}), 2)


if __name__ == "__main__":
    with open('input') as f:
        seats = list(map(parse_seat, f))

missing = set(range(min(seats), max(seats)+1)) - set(seats)
print(missing)
