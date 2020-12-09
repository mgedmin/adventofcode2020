#!/usr/bin/env python3
"""
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you
just found: you must find a contiguous set of at least two numbers in your list
which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the
invalid number from step 1, 127. (Of course, the contiguous set of numbers in
your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number
in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

import itertools
import sys
from collections import deque


with open('input' if len(sys.argv) < 2 else sys.argv[1]) as f:
    numbers = [int(line) for line in f]

window_size = 25 if len(sys.argv) < 3 else int(sys.argv[2])

window = deque(numbers[:window_size], window_size)

for n in numbers[window_size:]:
    if n not in map(sum, itertools.combinations(window, 2)):
        break
    window.append(n)
else:
    sys.exit('did not find the invalid number')


for a in range(len(numbers) - 1):
    for b in range(a+1, len(numbers)):
        s = sum(numbers[i] for i in range(a, b + 1))
        if n == s:
            print(min(numbers[a:b+1]) + max(numbers[a:b+1]))
            sys.exit()
        if s >= n:
            break
