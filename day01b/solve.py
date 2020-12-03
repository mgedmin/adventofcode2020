#!/usr/bin/python3
with open('input') as f:
    numbers = [int(line) for line in f]
numbers_as_set = set(numbers)
for i, a in enumerate(numbers):
    for b in numbers[i + 1:]:
        c = 2020 - a - b
        if c in numbers_as_set:
            print(a * b * c)
