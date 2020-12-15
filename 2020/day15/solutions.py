from collections import defaultdict
from itertools import count


with open('input') as f:
    ns = list(map(int, f.read().split(',')))


def solve(iteration):
    d = defaultdict(list)
    for i in count(1):
        if i <= len(ns):
            new = ns[i-1]
        elif len(d[last_spoken]) == 1:
            new = 0
        else:
            new = d[last_spoken][-1] - d[last_spoken][-2]
        if i == iteration:
            return new
        d[new].append(i)
        last_spoken = new


# Part one
print(solve(2020))

# Part two
print(solve(30_000_000))
