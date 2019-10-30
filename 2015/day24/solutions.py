from itertools import combinations, count
import numpy as np


with open('input') as f:
    lines = [int(l.strip()) for l in f.readlines()]


# We optimistically assume that if a partion works for group 1,
# then it also works for the two remaining groups. There is no
# reason to assume that this would work in general, but would be
# a natural thing to do when setting up the exercise. Turns out
# it works.
def solve(part_one):
    s = sum(lines)
    target = s // 3 if part_one else s // 4
    for i in count():
        c = combinations(lines, i)
        m = float('inf')
        for g1 in c:
            if sum(g1) != target:
                continue
            m = min(m, np.product(g1))
        if m < float('inf'):
            return m


print(solve(True))
print(solve(False))
