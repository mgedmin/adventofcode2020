#!/usr/bin/python3
"""
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be
what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the
password policy rules from his old job at the sled rental place down the
street! The Official Toboggan Corporate Policy actually works a little
differently.

Each policy actually describes two positions in the password, where 1 means the
first character, 2 means the second character, and so on. (Be careful; Toboggan
Corporate Policies have no concept of "index zero"!) Exactly one of these
positions must contain the given letter. Other occurrences of the letter are
irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the
policies?
"""

import re


rx = re.compile(r'^(\d+)-(\d+) ([a-z]): (.*)$')

valid = 0
with open('input') as f:
    for line in f:
        m = rx.match(line.rstrip())
        # NB: positions are 1-based in the input file
        pos1 = int(m.group(1)) - 1
        pos2 = int(m.group(2)) - 1
        char = m.group(3)
        password = m.group(4)
        # I want a boolean exclusive or, and != is the next closest thing
        if (password[pos1] == char) != (password[pos2] == char):
            valid += 1

print(valid)
