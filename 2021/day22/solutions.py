from math import prod
import re

import numpy as np
from tqdm import tqdm

with open("input") as f:
    ls = f.read().strip().split("\n")

boxes = [list(map(int, re.findall("-?\d+", x))) for x in ls]
switches = [l.split()[0] == "on" for l in ls]
switched_boxes = list(zip(switches, boxes))

# Part one
a = np.zeros((100, 100, 100))
for switch, box in switched_boxes[:20]:
    box = np.array(box) + 50
    a[box[0] : box[1] + 1, box[2] : box[3] + 1, box[4] : box[5] + 1] = switch
print(a.sum())


# Part two
# We implement inclusion-exclusion with a twist. The inclusion-exclusion principle
# says that the volume of a union is given by the sum of the volumes of the
# intersection of all subsets of the given sets, counted with parity. This works well
# here, since the intersection of any number of boxes is itself a box. The twist is
# that we don't just have a union but also occasionally remove boxes altogether. This
# doesn't change the algorithm much as we simply avoid adding the removed boxes back.
# It's a bit slow so we use tqdm to show progress.
def intersection(boxes):
    x1, x2 = max(x[0] for x in boxes), min(x[1] for x in boxes)
    y1, y2 = max(x[2] for x in boxes), min(x[3] for x in boxes)
    z1, z2 = max(x[4] for x in boxes), min(x[5] for x in boxes)
    if x1 <= x2 and y1 <= y2 and z1 <= z2:
        return (x1, x2, y1, y2, z1, z2)


def volume(box):
    return prod(box[i + 1] - box[i] + 1 for i in (0, 2, 4))


seen = []
for switch, box in tqdm(switched_boxes):
    seen += [
        (overlap, -sign)
        for seen_box, sign in seen
        if (overlap := intersection([box, seen_box]))
    ]
    if switch:
        seen.append((box, 1))
print(sum(sign * volume(box) for box, sign in seen))
