from itertools import count
from math import prod
import re

import numpy as np

with open("input") as f:
    ns = [list(map(int, re.findall("-?\\d+", x))) for x in f.read().strip().split("\n")]

# Part 1
w = 101
h = 103
qs = [0, 0, 0, 0]
for px, py, vx, vy in ns:
    px = (px + 100 * vx) % w
    py = (py + 100 * vy) % h
    if px != w // 2 and py != h // 2:
        qs[(px > w // 2) + 2 * (py > h // 2)] += 1
print(prod(qs))

# Part 2
zs = np.array([px + 1j * py for px, py, _, _ in ns])
vs = np.array([vx + 1j * vy for _, _, vx, vy in ns])
max_has_neighbour = 0

for t in count(1):
    zs = np.array([int(z.real) % w + (int(z.imag) % h) * 1j for z in zs + vs])
    zs_set = set(zs)
    num_has_neighbour = sum(z + dz in zs_set for z in zs for dz in (1, -1, 1j, -1j))
    if num_has_neighbour > max_has_neighbour:
        max_has_neighbour = num_has_neighbour
        a = np.zeros((h, w), dtype=int)
        a[zs.imag.astype(int), zs.real.astype(int)] = 1
        print(t)
        print("\n".join("".join(" ■"[x] for x in row) for row in a))
        print()
