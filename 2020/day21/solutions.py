"""
Slightly weird one, this one: From the Reddit megathread, it seems like most
people solved part 1 by making the assumption that the given list of foods is
sufficient to produce a unique map from allergens to ingredients, or that at
least, some combination of not-necessarily-complete reductions of the domains
of each allergen is enough. In particular, most of the solutions would fail on
an input like

    alkdjq fqlkmc lkamsda (contains fertilizer, cyanide)
    fqlkmc lkamsda (contains fertilizer, cyanide)

either by triggering an infinite loop, or by giving an answer of 5 where the
correct answer as the puzzle is stated is 1.

Now indeed, in part 2, we're given the additional information that there is
indeed a unique map; had this information been given already in part 1, those
simpler solutions would be guaranteed to work in general, and part 1 is really
much easier.

I'm not exactly a fan of the puzzles where one can drastically reduce the
difficulty of a puzzle by pulling an additional assumption out of the air and
even if I did indeed initially solve this puzzle by making arbitrary guesses,
I figured I'd give a general solution here instead. That is, in part 1, rather
than restricting the domains in an arbitrary way and checking a posteriori
uniqueness of the solutions, we simply use z3 to find /all/ solutions.
"""
import re

from z3 import Distinct, Int, Or, sat, Solver


with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

foods = []
all_ingredients = set()
all_allergens = set()
for l in ls:
    ingredients, allergens = l.split('contains')
    ingredients = re.findall(r'\w+', ingredients)
    allergens = re.findall(r'\w+', allergens)
    all_ingredients |= set(ingredients)
    all_allergens |= set(allergens)
    foods.append((ingredients, allergens))

# Part one
# z3 likes integers, so we create enumerate the ingredients and use
# the indices when solving.
allergen_vars = {a: Int(a) for a in all_allergens}
all_vars = allergen_vars.values()
int_to_ingredient = dict(enumerate(all_ingredients))
ingredient_to_int = dict(map(reversed, int_to_ingredient.items()))

s = Solver()
s.add(Distinct(*all_vars))
# Convert statements into constraints.
for ingredients, allergens in foods:
    for a in allergens:
        var = allergen_vars[a]
        s.add(Or([var == ingredient_to_int[i] for i in ingredients]))

# Keep track of ingredients that appear in any solution.
appear_in_some_solution = set()

# While there is a satisfying model, add its values to the set above, then
# add the constraint that any further models must be different from the one we
# just found. As we will be informed in part 2, there's actually only a single
# solution, and this loop will have only a single iteration.
while s.check() == sat:
    model = s.model()
    appear_in_some_solution |= set(model[a].as_long() for a in all_vars)
    s.add(Or([a != model[a] for a in all_vars]))

print(sum(ingredient_to_int[i] not in appear_in_some_solution
          for ingredients, _ in foods
          for i in ingredients))

# Part two
solution = {k: int_to_ingredient[model[a].as_long()]
            for k, a in allergen_vars.items()}

print(','.join(v for _, v in sorted(solution.items())))
