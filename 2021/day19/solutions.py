import re
from collections import defaultdict
from itertools import combinations, permutations, product

import numpy as np

with open("input") as f:
    data = f.read().strip()

scanners = []
for d in data.split("\n\n"):
    ls = d.split("\n")[1:]
    a = np.array([list(map(int, re.findall("-?\d+", x))) for x in ls])
    scanners.append(a)

# Generate the 24 rotations
rotations = []
for permutation in permutations((0, 1, 2), 3):
    for signs in product((-1, 1), repeat=3):
        if np.linalg.det(a := np.diag(signs)[:, permutation]) > 0:
            rotations.append(a)


def overlaps(i, j):
    for rotation in rotations:
        count = defaultdict(int)
        for beacon1 in scanners[i]:
            for beacon2 in scanners[j]:
                position = tuple(beacon1 - beacon2 @ rotation)
                count[position] += 1
                if count[position] == 12:
                    return position, position + scanners[j] @ rotation


stack = [0]
done = set()
positions = [(0, 0, 0)]
while stack:
    i = stack.pop()
    done.add(i)
    for j in set(range(len(scanners))) - done:
        if overlap := overlaps(i, j):
            position, translated = overlap
            positions.append(position)
            scanners[j] = translated
            stack.append(j)

# Part one
print(len(set(tuple(s) for scanner in scanners for s in scanner)))

# Part two
print(
    max(
        sum(abs(x1 - x2) for x1, x2 in zip(s1, s2))
        for s1, s2 in combinations(positions, 2)
    )
)
