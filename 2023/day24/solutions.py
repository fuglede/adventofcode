import re
from itertools import combinations

import numpy as np
from z3 import Int, IntVector, Solver

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]

# Part 1
lo = 200000000000000
hi = 400000000000000

res = 0
for n1, n2 in combinations(ns, 2):
    p1, p2, _, dp1, dp2, _ = n1
    q1, q2, _, dq1, dq2, _ = n2
    sp = dp2 / dp1
    sq = dq2 / dq1
    if sp == sq:
        continue
    x, y = np.linalg.solve([[-sp, 1], [-sq, 1]], [p2 - sp * p1, q2 - sq * q1])
    if (x - p1) / dp1 < 0 or (x - q1) / dq1 < 0:
        continue
    if lo <= x <= hi and lo <= y <= hi:
        res += 1

print(res)

# Part 2
q1, q2, q3, dq1, dq2, dq3 = IntVector("sol", 6)
ts = IntVector("t", len(ns))
s = Solver()

for t, (p1, p2, p3, dp1, dp2, dp3) in zip(ts, ns):
    s.add(q1 + t * dq1 == p1 + t * dp1)
    s.add(q2 + t * dq2 == p2 + t * dp2)
    s.add(q3 + t * dq3 == p3 + t * dp3)

s.check()
m = s.model()

print(sum(m[v].as_long() for v in (q1, q2, q3)))
