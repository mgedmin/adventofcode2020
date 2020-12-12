#!/usr/bin/python3
"""
--- Part Two ---

Before you can give the destination to the captain, you realize that the actual
action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to
the ship's position:

- Action N means to move the waypoint north by the given value.
- Action S means to move the waypoint south by the given value.
- Action E means to move the waypoint east by the given value.
- Action W means to move the waypoint west by the given value.
- Action L means to rotate the waypoint around the ship left
  (counter-clockwise) the given number of degrees.
- Action R means to rotate the waypoint around the ship right (clockwise) the
  given number of degrees.
- Action F means to move forward to the waypoint a number of times equal to the
  given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The
waypoint is relative to the ship; that is, if the ship moves, the waypoint
moves with it.

For example, using the same instructions as above:

- F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10
  units north), leaving the ship at east 100, north 10. The waypoint stays 10
  units east and 1 unit north of the ship.
- N3 moves the waypoint 3 units north to 10 units east and 4 units north of the
  ship. The ship remains at east 100, north 10.
- F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28
  units north), leaving the ship at east 170, north 38. The waypoint stays 10
  units east and 4 units north of the ship.
- R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4
  units east and 10 units south of the ship. The ship remains at east 170,
  north 38.
- F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110
  units south), leaving the ship at east 214, south 72. The waypoint stays 4
  units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting
position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""

import sys


with open('input' if len(sys.argv) < 2 else sys.argv[1]) as f:
    instructions = f.readlines()


# Coordinate system: x axis is positive pointing east, y axis is positive
# pointing north, heading is degrees left from the x axis, 0 = east, 90 =
# north, 180 = west, 270 = south

x = y = 0
wx = 10
wy = 1
for instruction in instructions:
    command = instruction[0]
    arg = int(instruction[1:])
    if command == 'N':
        wy += arg
    elif command == 'E':
        wx += arg
    elif command == 'W':
        wx -= arg
    elif command == 'S':
        wy -= arg
    elif command == 'L':
        while arg > 0:
            arg -= 90
            wx, wy = -wy, wx
        assert arg == 0
    elif command == 'R':
        while arg > 0:
            arg -= 90
            wx, wy = wy, -wx
        assert arg == 0
    elif command == 'F':
        x += wx * arg
        y += wy * arg
    else:
        raise ValueError(f'bad command: {instruction}')
    if '-v' in sys.argv:
        print(f"{x=}, {y=}, {wx=}, {wy=}")

print(abs(x) + abs(y))
