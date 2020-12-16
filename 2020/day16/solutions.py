import math
import re

with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

ranges = [list(map(int, re.findall('\d+', x))) for x in ls[:20]]
your = [int(x) for x in ls[22].split(',')]
nearby = [list(map(int, re.findall('\d+', x))) for x in ls[25:]]

# Part one
valid = set()
for t1, t2, t3, t4 in ranges:
    valid |= set(range(t1, t2 + 1))
    valid |= set(range(t3, t4 + 1))

print(sum(n for l in nearby for n in l if n not in valid))

# Part two
valids = [l for l in nearby if all(n in valid for n in l)]

# domain[i] = domain of possible placements of i'th field;
# a priori all of range(20).
# First run: Remove value from domain if invalid
domain = {
    i: {j for j in range(20) if
        all((t1 <= l[j] <= t2) or (t3 <= l[j] <= t4) for l in valids)}
    for i, (t1, t2, t3, t4) in enumerate(ranges)
}

# Second run: Through inspection, it's clear that we can identify
# values one at a time (as opposed to having to solve a more
# general constraint satisfaction problem). Since comparison of
# sets is based on inclusion, we can simply sort the domains.
model = {}  # model[i] = placement of i'th field
for k, values in sorted(domain.items(), key=lambda x: x[1]):
    model[k], = values - set(model.values())

# Fields of interest are the top 6 in the input
print(math.prod(your[v] for k, v in model.items() if k < 6))
