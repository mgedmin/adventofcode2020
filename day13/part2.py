#!/usr/bin/python3
"""
--- Part Two ---

The shuttle company is running a contest: one gold coin for anyone that can
find the earliest timestamp such that the first bus ID departs at that time and
each subsequent listed bus ID departs at that subsequent minute. (The first
line in your input is no longer relevant.)

For example, suppose you have the same list of bus IDs as above:

7,13,x,x,59,x,31,19

An x in the schedule means there are no constraints on what bus IDs must depart
at that time.

This means you are looking for the earliest timestamp (called t) such that:

- Bus ID 7 departs at timestamp t.
- Bus ID 13 departs one minute after timestamp t.
- There are no requirements or restrictions on departures at two or three
  minutes after timestamp t.
- Bus ID 59 departs four minutes after timestamp t.
- There are no requirements or restrictions on departures at five minutes after
  timestamp t.
- Bus ID 31 departs six minutes after timestamp t.
- Bus ID 19 departs seven minutes after timestamp t.

The only bus departures that matter are the listed bus IDs at their specific
offsets from t. Those bus IDs can depart at other times, and other bus IDs can
depart at those times. For example, in the list above, because bus ID 19 must
depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7
will always also be departing with bus ID 19 at seven minutes after timestamp
t.

In this example, the earliest timestamp at which this occurs is 1068781:

time     bus 7   bus 13  bus 59  bus 31  bus 19
1068773    .       .       .       .       .
1068774    D       .       .       .       .
1068775    .       .       .       .       .
1068776    .       .       .       .       .
1068777    .       .       .       .       .
1068778    .       .       .       .       .
1068779    .       .       .       .       .
1068780    .       .       .       .       .
1068781    D       .       .       .       .
1068782    .       D       .       .       .
1068783    .       .       .       .       .
1068784    .       .       .       .       .
1068785    .       .       D       .       .
1068786    .       .       .       .       .
1068787    .       .       .       D       .
1068788    D       .       .       .       D
1068789    .       .       .       .       .
1068790    .       .       .       .       .
1068791    .       .       .       .       .
1068792    .       .       .       .       .
1068793    .       .       .       .       .
1068794    .       .       .       .       .
1068795    D       D       .       .       .
1068796    .       .       .       .       .
1068797    .       .       .       .       .

In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes
after t). This is fine; the only requirement on that minute is that bus ID 19
departs then, and it does.

Here are some other examples:

- The earliest timestamp that matches the list 17,x,13,19 is 3417.
- 67,7,59,61 first occurs at timestamp 754018.
- 67,x,7,59,61 first occurs at timestamp 779210.
- 67,7,x,59,61 first occurs at timestamp 1261476.
- 1789,37,47,1889 first occurs at timestamp 1202161486.

However, with so many bus IDs in your list, surely the actual earliest
timestamp will be larger than 100000000000000!

What is the earliest timestamp such that all of the listed bus IDs depart at
offsets matching their positions in the list?
"""

import itertools
import math
import sys


def extended_euclid(a, b):
    """Returns (x, y) where a*x + b * y == math.gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return (old_s, old_t)


with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    next(f)  # ignore first line
    buses = []
    remainders = []
    for idx, bus in enumerate(next(f).rstrip().split(',')):
        if bus != 'x':
            buses.append(int(bus))
            remainders.append(-idx)


# I'm afraid we'll have to use math here.  I have a feeling the Chinese
# Remainder Theorem is relevant here.

# Can we assume the bus route numbers are all pairwise coprime?
for a, b in itertools.combinations(buses, 2):
    assert math.gcd(a, b) == 1
    x, y = extended_euclid(a, b)
    assert a * x + b * y == 1

# Yes we can, good.

while len(buses) > 1:
    n1, n2 = buses[:2]
    a1, a2 = remainders[:2]

    m1, m2 = extended_euclid(n1, n2)
    assert m1 * n1 + m2 * n2 == 1
    x = a1 * m2 * n2 + a2 * m1 * n1
    x %= n1 * n2
    if '-v' in sys.argv:
        print(f"{x} == {a1} (mod {n1})")
        print(f"{x} == {a2} (mod {n2})")
    assert x % n1 == a1 % n1
    assert x % n2 == a2 % n2

    buses = [n1 * n2] + buses[2:]
    remainders = [x] + remainders[2:]

print(remainders[0])
