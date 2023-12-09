import re

import numpy as np

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = np.array([list(map(int, re.findall(r"-?\d+", x))) for x in ls])


# Part 1+2
for a in (ns, np.flip(ns, 1)):
    print(np.sum([np.diff(a, k)[:,-1] for k in range(ns.shape[1])]))
