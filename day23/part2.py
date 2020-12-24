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


class arrangement(dict):
    def __missing__(self, idx):
        return idx + 1


start = last = time.time()

with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    cups = [int(c) for c in next(f).strip()]


clockwise = arrangement()
for a, b in zip(cups, cups[1:]):
    clockwise[a] = b

orig_max_cup = max(cups)
clockwise[cups[-1]] = orig_max_cup + 1
max_cup = 1_000_000
clockwise[max_cup] = cups[0]

current = cups[0]
for n in range(10_000_000):
    pick_up = [clockwise[current]]
    for m in range(2):
        pick_up.append(clockwise[pick_up[-1]])
    assert len(pick_up) == 3
    after = clockwise[pick_up[-1]]

    destination = current - 1
    if destination == 0:
        destination = max_cup
    while destination in pick_up:
        destination -= 1
        if destination == 0:
            destination = max_cup

    after_dest = clockwise[destination]
    clockwise[current] = after
    clockwise[destination] = pick_up[0]
    clockwise[pick_up[-1]] = after_dest
    current = after

    if n % 1000 == 0 and '-v' in sys.argv:
        now = time.time()
        if now - last > 1:
            elapsed = now - start
            # The problem with this estimation is that the data structure gets
            # slower as it gets larger.
            eta = elapsed * 10_000_000 / n - elapsed
            print(f'{n:,}'
                  f' ETA: {eta // 60 % 60:.0f}min {eta % 60:.0f}s')
            last = now

cups = [clockwise[1]]
cups.append(clockwise[cups[-1]])
if '-v' in sys.argv:
    print(*cups)
print(cups[0] * cups[1])
