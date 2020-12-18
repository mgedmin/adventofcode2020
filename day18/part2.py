#!/usr/bin/python3
"""
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their
homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're
not the ones you're familiar with. Instead, addition is evaluated before
multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now
as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

- 1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
- 2 * 3 + (4 * 5) becomes 46.
- 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
- 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
- ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems
using these new rules?
"""

import sys
import re
import operator


def tokenize(expr):
    for token in re.split(r'(\d+|[+*()])', expr):
        if token.strip():
            yield token


def silly_eval(expr):
    ops = {'+': operator.add, '*': operator.mul}
    prio = {'+': 2, '*': 1, '(': 0}
    stack = []
    opstack = []
    for token in tokenize(expr):
        if token.isdigit():
            stack.append(int(token))
        elif token in ('+', '*'):
            while opstack and prio[token] < prio[opstack[-1]]:
                stack.append(ops[opstack.pop()](stack.pop(), stack.pop()))
            opstack.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            while opstack and opstack[-1] != '(':
                stack.append(ops[opstack.pop()](stack.pop(), stack.pop()))
            if not opstack:
                raise SyntaxError("unmatched )")
            assert opstack[-1] == '('
            opstack.pop()
        else:
            raise SyntaxError(f"{token} not allowed in expressions")
    while opstack:
        if opstack[-1] == '(':
            raise SyntaxError("unmatched (")
        stack.append(ops[opstack.pop()](stack.pop(), stack.pop()))
    assert len(stack) == 1
    return stack[0]


if __name__ == "__main__":
    with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
        print(sum(silly_eval(line) for line in f))
