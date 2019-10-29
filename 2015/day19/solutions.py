from collections import defaultdict
import re

with open('input') as f:
    lines = [x.strip().split() for x in f.readlines()]

replacements = [(x[0], x[2]) for x in lines[:-2]]
initial = lines[-1][0]


# Part one
def make_combinations(s):
    combinations = set()
    for r in replacements:
        for m in re.finditer(r[0], s):
            yield s[:m.start()] + r[1] + s[m.end():]


print(len(set(make_combinations(initial))))


# Part two
# Apparently, the greedy approach works just fine.
def make_removals(initial):
    combinations = set()
    for r in replacements:
        for m in re.finditer(r[1], initial):
            yield initial[:m.start()] + r[0] + initial[m.end():]


s = initial
i = 0
while s != 'e':
    shortest_len = float('inf')
    for removal in make_removals(s):
        if len(removal) < shortest_len:
            shortest_len = len(removal)
            shortest = removal
    s = shortest
    i += 1
print(i)
