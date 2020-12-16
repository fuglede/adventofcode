import math
import re

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

ranges = [list(map(int, re.findall('\d+', x))) for x in ls[:20]]
your = np.array([int(x) for x in ls[22].split(',')], dtype=np.int64)
nearby = [list(map(int, re.findall('\d+', x))) for x in ls[25:]]

# Part one
valid = set()
for t1, t2, t3, t4 in ranges:
    valid |= set(range(t1, t2 + 1))
    valid |= set(range(t3, t4 + 1))

print(sum(n for l in nearby for n in l if n not in valid))

# Part two
valids = [l for l in nearby if all(n in valid for n in l)]
loc = [[all((t1 <= l[j] <= t2) or (t3 <= l[j] <= t4) for l in valids)
        for t1, t2, t3, t4 in ranges]
       for j in range(20)]
m = maximum_bipartite_matching(csr_matrix(loc))
print(your[m[:6]].prod())
