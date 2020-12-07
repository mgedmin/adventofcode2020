#!/usr/bin/env python3
"""
--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices,
but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

- faded blue bags contain 0 other bags.
- dotted black bags contain 0 other bags.
- vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black
  bags.
- dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black
  bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 +
1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper
than this example; be sure to count all of the bags, even if the nesting
becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

import sys


def parse_rule(line):
    outer, _, inner = line.rstrip().partition(' bags contain ')
    if inner == 'no other bags.':
        return outer, []
    return outer, [
        (int(part.partition(' ')[0]),
         part.partition(' ')[-1].rstrip('bags.').strip())
        for part in inner.split(', ')
    ]


def parse_rules(lines):
    rules = {}
    for line in lines:
        outer, inner = parse_rule(line)
        if outer in rules:
            raise SyntaxError(f'duplicate rule: {outer}')
        rules[outer] = inner
    return rules


def count_bags(outer, rules, memo=None):
    if memo is not None and outer in memo:
        return memo[outer]
    inner = rules[outer]
    answer = sum(count * (1 + count_bags(bag, rules, memo))
                 for count, bag in inner)
    if memo is not None:
        memo[outer] = answer
    return answer


def main():
    with open('input' if len(sys.argv) < 2 else sys.argv[1]) as f:
        rules = parse_rules(f)

    memo = {}
    print(count_bags('shiny gold', rules, memo))


if __name__ == "__main__":
    main()
