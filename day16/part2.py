#!/usr/bin/python3
"""
--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those
tickets entirely. Use the remaining valid tickets to determine which field is
which.

Using the valid ranges for each field, determine what order the fields appear
on the tickets. The order is consistent between all tickets: if seat is the
third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must be
row, the second position must be class, and the third position must be seat;
you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket
that start with the word departure. What do you get if you multiply those six
values together?
"""

import sys
import typing
from typing import List


class Field(typing.NamedTuple):
    name: str
    ranges: List[range]

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name

    def validate(self, value):
        return any(value in range for range in self.ranges)


def parse_field_definition(line):
    name, _, rest = line.partition(': ')
    ranges = []
    for r in rest.split(' or '):
        lo, _, hi = r.partition('-')
        ranges.append(range(int(lo), int(hi) + 1))
    return Field(name, ranges)


def possible_fields(value, fields):
    return {
        field for field in fields if field.validate(value)
    }


with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    fields = []
    for line in f:
        line = line.strip()
        if not line:
            break
        field = parse_field_definition(line)
        fields.append(field)
        if '-v' in sys.argv:
            print(f"field {field.name}: {field.ranges}")
    assert next(f).strip() == "your ticket:"
    my_ticket = [int(field) for field in next(f).split(',')]
    assert next(f).strip() == ""
    assert next(f).strip() == "nearby tickets:"
    possible_fields_for_each_position = [
        possible_fields(value, fields)
        for value in my_ticket
    ]
    assert all(possible_fields_for_each_position)  # all sets are nonempty
    for n, line in enumerate(f, 1):
        ticket = [int(field) for field in line.split(',')]
        possible_fields_for_this_ticket = [
            possible_fields(value, fields)
            for value in ticket
        ]
        if not all(possible_fields_for_this_ticket):
            continue  # skip invalid tickets
        for idx, (possible, new) in enumerate(
            zip(possible_fields_for_each_position,
                possible_fields_for_this_ticket)
        ):
            possible.intersection_update(new)
            if not possible and '-v' in sys.argv:
                print(f"Ticket {n} makes field {idx} impossible!")


if '-v' in sys.argv:
    for idx, possible in enumerate(possible_fields_for_each_position):
        print(f"{idx + 1} could be {possible}")


to_be_assigned = list(enumerate(possible_fields_for_each_position))
assignments = {}

while to_be_assigned:
    to_be_assigned.sort(key=lambda item: len(item[1]), reverse=True)
    idx, possible = to_be_assigned.pop(-1)
    if len(possible) == 0:
        sys.exit(f"field {idx + 1} is impossible!")
    if len(possible) > 1:
        sys.exit(f"field {idx + 1} is ambiguous!")
    assert len(possible) == 1
    field = next(iter(possible))
    assignments[idx] = field
    if '-v' in sys.argv:
        print(f"field {idx + 1} is {field.name}")
    for idx, possible in to_be_assigned:
        possible.remove(field)


result = 1
for idx, value in enumerate(my_ticket):
    field = assignments[idx]
    if field.name.startswith('departure'):
        if '-v' in sys.argv:
            print(f"{field.name} (field {idx + 1}): {my_ticket[idx]}")
        result *= my_ticket[idx]

print(result)
