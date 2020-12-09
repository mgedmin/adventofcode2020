#!/usr/bin/python3
"""
--- Part Two ---

After some careful analysis, you believe that exactly one instruction is
corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is
supposed to be a jmp. (No acc instructions were harmed in the corruption of
this boot code.)

The program is supposed to terminate by attempting to execute an instruction
immediately after the last instruction in the file. By changing exactly one jmp
or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a
single-instruction infinite loop, never leaving that instruction. If you change
almost any of the jmp instructions, the program will still eventually find
another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4),
the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to
run the instruction below the last instruction in the file. With this change,
after the program terminates, the accumulator contains the value 8 (acc +1, acc
+1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to
nop) or nop (to jmp). What is the value of the accumulator after the program
terminates?
"""

import sys
from collections import defaultdict


ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def parse_inst(line):
    inst, arg = line.split()
    assert inst in [ACC, JMP, NOP]
    return (inst, int(arg))


class InfiniteLoop(Exception):
    pass


def execute(code, patch):
    acc = 0
    ip = 0
    executed = defaultdict(bool)
    while ip < len(code):
        if executed[ip]:
            raise InfiniteLoop('infinite loop detected')
        inst, arg = patch.get(ip, code[ip])
        executed[ip] = True
        if inst == NOP:
            ip += 1
        elif inst == ACC:
            acc += arg
            ip += 1
        elif inst == JMP:
            ip += arg
    return acc


def solve(code):
    for offset, (inst, arg) in enumerate(code):
        try:
            if inst == NOP:
                return execute(code, {offset: (JMP, arg)})
            elif inst == JMP:
                return execute(code, {offset: (NOP, arg)})
        except InfiniteLoop:
            pass


with open('input' if len(sys.argv) < 2 else sys.argv[1]) as fp:
    code = [parse_inst(line) for line in fp]


print(solve(code))
