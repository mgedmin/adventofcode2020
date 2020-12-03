#!/usr/bin/python3
with open('input') as f:
    numbers = [int(line) for line in f]
numbers_as_set = set(numbers)
for a in numbers:
    if 2020 - a in numbers_as_set:
        b = 2020 - a
        print(a * b)
        break
