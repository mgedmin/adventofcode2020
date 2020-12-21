#!/usr/bin/python3
"""
--- Part Two ---

Now that you've isolated the inert ingredients, you should have enough
information to figure out which ingredient contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.

Arrange the ingredients alphabetically by their allergen and separate them by
commas to produce your canonical dangerous ingredient list. (There should not
be any spaces in your canonical dangerous ingredient list.) In the above
example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous
ingredient list?
"""

import sys


foods = []

with open("input" if len(sys.argv) < 2 else sys.argv[1]) as f:
    for line in f:
        ingredients = line.partition(' (contains ')[0].split()
        allergens = line.partition(' (contains ')[-1].rstrip(')\n').split(', ')
        assert len(ingredients) >= len(allergens)
        foods.append((ingredients, allergens))


possibilities = {}  # allergen -> set of possible ingredients
for ingredients, allergens in foods:
    for allergen in allergens:
        if allergen not in possibilities:
            possibilities[allergen] = set(ingredients)
        else:
            possibilities[allergen].intersection_update(ingredients)


assignments = {}  # allergen -> ingredient
rev_assignments = {}  # ingredient -> allergen
while True:
    for allergen, possible_ingredients in possibilities.items():
        if len(possible_ingredients) == 1:
            [ingredient] = possible_ingredients
            assignments[allergen] = ingredient
            rev_assignments[ingredient] = allergen
            break
    else:
        break
    del possibilities[allergen]
    for other_allergen, other_possibilities in possibilities.items():
        other_possibilities.difference_update(possible_ingredients)


assert possibilities == {}


print(
    ','.join(
        ingredient for allergen, ingredient in sorted(assignments.items())
    )
)
