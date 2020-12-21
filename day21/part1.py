#!/usr/bin/python3
"""
--- Day 21: Allergen Assessment ---

You reach the train's last stop and the closest you can get to your vacation
island without getting wet. There aren't even any boats here, but nothing can
stop you now: you build a raft. You just need a few days' worth of food for
your journey.

You don't speak the local language, so you can't read any ingredients lists.
However, sometimes, allergens are listed in a language you do understand. You
should be able to use this information to determine which ingredient contains
which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line.
Each line includes that food's ingredients list followed by some or all of the
allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero
or one allergen. Allergens aren't always marked; when they're listed (as in
(contains nuts, shellfish) after an ingredients list), the ingredient that
contains each listed allergen will be somewhere in the corresponding
ingredients list. However, even if an allergen isn't listed, the ingredient
that contains that allergen could still be present: maybe they forgot to label
it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

The first food in the list has four ingredients (written in a language you
don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might
contain other allergens, a few allergens the food definitely contains are
listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of
the allergens in any food in your list. In the above example, none of the
ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the
number of times any of these ingredients appear in any ingredients list
produces 5: they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in
your list. How many times do any of those ingredients appear?
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


count = 0
for ingredients, allergens in foods:
    for ingredient in ingredients:
        if ingredient not in rev_assignments:
            if '-v' in sys.argv:
                print(ingredient)
            count += 1

print(count)
