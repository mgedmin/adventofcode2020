#!/usr/bin/python3
"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster
than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning;
rather than giving a route directly to safety, it produced extremely circuitous
instructions. When the captain uses the PA system to ask if anyone can help,
you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring at
them for a few minutes, you work out what they probably mean:

- Action N means to move north by the given value.
- Action S means to move south by the given value.
- Action E means to move east by the given value.
- Action W means to move west by the given value.
- Action L means to turn left the given number of degrees.
- Action R means to turn right the given number of degrees.
- Action F means to move forward by the given value in the direction the ship
  is currently facing.

The ship starts by facing east. Only the L and R actions change the direction
the ship is facing. (That is, if the ship is facing east and the next
instruction is N10, the ship would move north 10 units, but would still move
east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

- F10 would move the ship 10 units east (because the ship starts by facing
  east) to east 10, north 0.
- N3 would move the ship 3 units north to east 10, north 3.
- F7 would move the ship another 7 units east (because the ship is still facing
  east) to east 17, north 3.
- R90 would cause the ship to turn right by 90 degrees and face south; it
  remains at east 17, north 3.
- F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the
absolute values of its east/west position and its north/south position) from
its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan
distance between that location and the ship's starting position?
"""

import sys


with open('input' if len(sys.argv) < 2 else sys.argv[1]) as f:
    instructions = f.readlines()


# Coordinate system: x axis is positive pointing east, y axis is positive
# pointing north, heading is degrees left from the x axis, 0 = east, 90 =
# north, 180 = west, 270 = south

x = y = heading = 0
for instruction in instructions:
    command = instruction[0]
    arg = int(instruction[1:])
    if command == 'N' or command == 'F' and heading == 90:
        y += arg
    elif command == 'E' or command == 'F' and heading == 0:
        x += arg
    elif command == 'W' or command == 'F' and heading == 180:
        x -= arg
    elif command == 'S' or command == 'F' and heading == 270:
        y -= arg
    elif command == 'L':
        heading += arg
        heading %= 360
        assert heading in {0, 90, 180, 270}
    elif command == 'R':
        heading -= arg
        heading %= 360
        assert heading in {0, 90, 180, 270}
    else:
        raise ValueError(f'bad command: {instruction}')
    if '-v' in sys.argv:
        print(f"{x=}, {y=}, {heading=}")

print(abs(x) + abs(y))
