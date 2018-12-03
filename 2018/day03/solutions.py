import numpy as np
import re

with open('input') as f:
    claims = [x.strip() for x in f.readlines()]

counts = np.zeros((1000, 1000))
fabric = np.zeros((1000, 1000))
no_overlaps = set(range(1, len(claims) + 1))

for i, claim in enumerate(claims):
    m = re.search('(\d+),(\d+): (\d+)x(\d+)', claim)
    column = int(m.group(1))
    row = int(m.group(2))
    width = int(m.group(3))
    height = int(m.group(4))

    counts[row:row+height, column:column+width] += 1

    overlapping = set(fabric[row:row+height, column:column+width].ravel())
    if overlapping != {0}:
        no_overlaps.remove(i + 1)
    for a in overlapping.intersection(no_overlaps):
        no_overlaps.remove(a)
    fabric[row:row+height, column:column+width] = i + 1

# Part one
print((counts > 1).sum())

# Part two
print(no_overlaps)
