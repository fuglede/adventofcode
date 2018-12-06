from collections import defaultdict
import re

import numpy as np


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ns = [[int(x) for x in re.findall(r'\d+', s)] for s in lines]
ns = np.array(ns)

b = np.max(ns) + 1
a = np.array([[x, y] for x in range(-b, 2*b) for y in range(-b, 2*b)])


# Part one
def nearest(p):
    s = np.sum(np.abs(p - ns), 1)
    w = np.where(s == np.min(s))[0]
    return w[0] if len(w) == 1 else None


inf = set()
for n in range(-b, 2*b):
    x = np.array([n, -b])
    inf.add(nearest(x))
    x = np.array([n, 2*b])
    inf.add(nearest(x))
    x = np.array([-b, n])
    inf.add(nearest(x))
    x = np.array([2*b, n])
    inf.add(nearest(x))

area = defaultdict(int)
for p in a:
    area[nearest(p)] += 1

print(max(v for (k, v) in area.items() if k is not None and k not in inf))

# Part two
print(sum([np.sum(np.abs(p - ns)) < 10000 for p in a]))
