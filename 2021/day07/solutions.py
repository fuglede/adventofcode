from math import comb
from statistics import median

with open("input") as f:
    ns = list(map(int, f.read().strip().split(",")))


# Part one
print(sum(abs(n - median(ns)) for n in ns))

# Part two
print(
    min(sum(comb(abs(n - i) + 1, 2) for n in ns) for i in range(min(ns), max(ns) + 1))
)
