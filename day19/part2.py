#!/usr/bin/python3
"""
--- Part Two ---

As you look over the list of messages, you realize your matching rules aren't
quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with the
following:

8: 42 | 42 8
11: 42 31 | 42 11 31

This small change has a big impact: now, the rules do contain loops, and the
list of messages they could hypothetically match is infinite. You'll need to
determine how these changes affect which messages are valid.

Fortunately, many of the rules are unaffected by this change; it might help to
start by looking at which rules always match the same set of values and how
those rules (especially rules 42 and 31) are used by the new versions of rules
8 and 11.

(Remember, you only need to handle the rules you have; building a solution that
could handle any hypothetical combination of rules would be significantly more
difficult.)

For example:

42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

Without updating rules 8 and 11, these rules only match three messages:
bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba.

However, after updating rules 8 and 11, a total of 12 messages match:

    bbabbbbaabaabba
    babbbbaabbbbbabbbbbbaabaaabaaa
    aaabbbbbbaaaabaababaabababbabaaabbababababaaa
    bbbbbbbaaaabbbbaaabbabaaa
    bbbababbbbaaaaaaaabbababaaababaabab
    ababaaaaaabaaab
    ababaaaaabbbaba
    baabbaaaabbaaaababbaababb
    abbbbabbbbaaaababbbbbbaaaababb
    aaaaabbaabaaaaababaa
    aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
    aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

After updating rules 8 and 11, how many messages completely match rule 0?
"""

import re
import sys
from typing import Dict, List


class Rule:
    def build_regexp(self, rules: Dict[int, 'Rule'], max_length: int) -> str:
        pass


class CharRule(Rule):
    def __init__(self, c: str) -> None:
        self.c = c

    def build_regexp(self, rules: Dict[int, Rule], max_length: int) -> str:
        return re.escape(self.c)

    def __repr__(self):
        return repr(self.c)


class SeqRule(Rule):
    def __init__(self, rules: List[int]) -> None:
        self.rules = rules

    def build_regexp(self, rules: Dict[int, Rule], max_length: int) -> str:
        return ''.join(rules[rule_id].build_regexp(rules, max_length)
                       for rule_id in self.rules)

    def __repr__(self):
        return ' '.join(map(repr, self.rules))


class AltRule(Rule):
    def __init__(self, alternatives: List[Rule]) -> None:
        self.alternatives = alternatives

    def build_regexp(self, rules: Dict[int, Rule], max_length: int) -> str:
        alt_regexes = [
            alt.build_regexp(rules, max_length) for alt in self.alternatives
        ]
        if len(alt_regexes) == 1:
            return alt_regexes[0]
        if all(len(regex) == 1 for regex in alt_regexes):
            return '[%s]' % ''.join(alt_regexes)
        return '(%s)' % '|'.join(alt_regexes)

    def __repr__(self):
        return ' | '.join(map(repr, self.alternatives))


class OneOrMore(Rule):
    def __init__(self, rule_id: int) -> None:
        self.rule_id = rule_id

    def build_regexp(self, rules: Dict[int, Rule], max_length: int) -> str:
        return '(%s)+' % rules[self.rule_id].build_regexp(rules, max_length)

    def __repr__(self):
        return '(%s)+' % repr(self.rule_id)


class MatchedPairs(Rule):

    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right

    def build_regexp(self, rules: Dict[int, Rule], max_length: int) -> str:
        # Ha ha this is an irregular grammar that cannot be converted to a
        # regexp!  But we can cheat!
        left_re = rules[self.left].build_regexp(rules, max_length)
        right_re = rules[self.right].build_regexp(rules, max_length)
        return '(%s)' % '|'.join(
            '(%s){%d}(%s){%d}' % (left_re, n, right_re, n)
            for n in range(1, max_length // 2 + 1)
        )

    def __repr__(self):
        return f'{self.left} {self.right} | {self.left} (self) {self.right}'


def build_validator(rules, max_length):
    return re.compile(
        '^' + rules[0].build_regexp(rules, max_length) + '$'
    ).match


def parse_rules(f):
    rules = {}
    for line in f:
        line = line.strip()
        if not line:
            break
        rule_id, _, definition = line.partition(': ')
        if definition.startswith('"') and definition.endswith('"'):
            c = definition[1:-1]
            assert len(c) == 1
            rule = CharRule(c)
        else:
            alternatives = [
                SeqRule([int(r) for r in part.split()])
                for part in definition.split(' | ')
            ]
            rule = AltRule(alternatives)
        rules[int(rule_id)] = rule
    return rules


if __name__ == "__main__":
    with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
        rules = parse_rules(f)
        # manual patch!
        rules[8] = OneOrMore(42)
        rules[11] = MatchedPairs(42, 31)
        messages = [line.strip() for line in f]
        max_length = max(map(len, messages))
        valid_message = build_validator(rules, max_length)
        n = sum(1 for line in messages if valid_message(line))
    print(n)
