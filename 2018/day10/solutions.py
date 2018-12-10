import re

import numpy as np


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ns = np.array([[int(x) for x in re.findall(r'-?\d+', s)] for s in lines])
p = ns[:, :2]
v = ns[:, 2:]

upper_bound = 200000
p_t = np.copy(p)
max_dist = np.empty(upper_bound)
for i in range(upper_bound):
    max_dist[i] = np.ptp(p_t)
    p_t += v
best_t = np.argmin(max_dist)
a = p + best_t * v

a -= np.min(a, 0)
d = np.max(a, 0) + 1
sky = np.zeros(d)
sky[tuple(a.T)] = 1

# Part one
for l in map(''.join, np.where(sky.T, '#', ' ')):
    print(l)

# Part two
print(best_t)