from itertools import combinations
from math import dist, prod

from scipy.cluster.hierarchy import DisjointSet

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [tuple(map(int, l.split(","))) for l in ls]
edges = sorted(combinations(ns, 2), key=lambda pair: dist(*pair))

ds = DisjointSet(ns)
for edge in edges:
    if edge == edges[1000]:
        print(prod(sorted(map(len, ds.subsets()))[-3:]))
    ds.merge(*edge)
    if ds.n_subsets == 1:
        break

print(prod(next(zip(*edge))))
