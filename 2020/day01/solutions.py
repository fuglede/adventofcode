from itertools import combinations
import numpy as np


with open('input') as f:
    ns = list(map(int, (x.strip() for x in f.readlines())))


# Part one
for a in combinations(ns, 2):
    if sum(a) == 2020:
        print(np.product(a))
        break


# Part two
for a in combinations(ns, 3):
    if sum(a) == 2020:
        print(np.product(a))
        break
