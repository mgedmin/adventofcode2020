#!/usr/bin/python3
"""
--- Part Two ---

Impressed, the Elves issue you a challenge: determine the 30000000th number
spoken. For example, given the same starting numbers as above:

- Given 0,3,6, the 30000000th number spoken is 175594.
- Given 1,3,2, the 30000000th number spoken is 2578.
- Given 2,1,3, the 30000000th number spoken is 3544142.
- Given 1,2,3, the 30000000th number spoken is 261214.
- Given 2,3,1, the 30000000th number spoken is 6895259.
- Given 3,2,1, the 30000000th number spoken is 18.
- Given 3,1,2, the 30000000th number spoken is 362.

Given your starting numbers, what will be the 30000000th number spoken?
"""

import sys


with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    numbers = [int(n) for n in next(f).split(',')]


last_turn = {}
last = None
for turn, number in enumerate(numbers, 1):
    if last is not None:
        last_turn[last] = turn - 1
    if '-v' in sys.argv:
        print(f'{turn}. {number}')
    last = number
for turn in range(turn+1, 30_000_000+1):
    if last not in last_turn:
        number = 0
    else:
        number = turn - 1 - last_turn[last]
    if '-v' in sys.argv:
        print(f'{turn}. {number}')
    last_turn[last] = turn - 1
    last = number

print(number)
