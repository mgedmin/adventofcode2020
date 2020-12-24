#!/usr/bin/python3
"""
--- Part Two ---

Due to what you can only assume is a mistranslation (you're not exactly fluent
in Crab), you are quite surprised when the crab starts arranging many cups in a
circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the
remaining cups are just numbered in an increasing fashion starting from the
number after the highest number in your list and proceeding one by one until
one million is reached. (For example, if your labeling were 54321, the cups
would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one
million is reached.) In this way, every number from one through one million is
used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you
realize the small crab isn't going to do merely 100 moves; the crab is going to
do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will
end up immediately clockwise of cup 1. You can have them if you predict what
the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792;
multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do
you get if you multiply their labels together?
"""

import sys
import time


with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    cups = [int(c) for c in next(f).strip()]


orig_max_cup = max(cups)

the_range = range(orig_max_cup + 1, 1_000_001)
cups.append(the_range)
max_cup = 1_000_000


start = last = time.time()
for n in range(10_000_000):
    if isinstance(cups[0], range):
        current = the_range.start
        # XXX: this fails after 250000 iterations:
        # 250,000 [999974] ETA: 108h 45min 2s
        # Traceback (most recent call last):
        #   File "./part2.py", line 51, in <module>
        #     new_range = range(the_range[4], the_range.stop)
        # IndexError: range object index out of range
        new_range = range(the_range[4], the_range.stop)
        cups = list(the_range[:4]) + [new_range] + cups[1:]
        the_range = new_range
    current = cups[0]
    pick_up = cups[1:4]
    current = cups[0]
    destination = current - 1
    if destination == 0:
        if '-v' in sys.argv:
            print(f'ROLLOVER: {n}')
        destination = max_cup
    while destination in pick_up:
        destination -= 1
        if destination == 0:
            if '-v' in sys.argv:
                print(f'ROLLOVER: {n}')
            destination = max_cup

    if destination == max_cup:
        where = cups.index(the_range) + 1
    else:
        where = cups.index(destination) + 1
    assert where > 4
    cups = cups[4:where] + pick_up + cups[where:] + [current]

    if n % 100 == 0 and '-v' in sys.argv:
        now = time.time()
        if now - last > 1:
            elapsed = now - start
            eta = elapsed * 10_000_000 / n
            print(f'{n:,} [{len(cups)}] ETA: {eta // 60 // 60:.0f}h'
                  f' {eta // 60 % 60:.0f}min {eta % 60:.0f}s')
            last = now

where = cups.index(1)
cups = (cups[where + 1:where + 3] + cups[:2])[:2]
if '-v' in sys.argv:
    print(*cups)
print(cups[0] * cups[1])
