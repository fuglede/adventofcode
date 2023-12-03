import math
import re
from collections import defaultdict

with open("input") as f:
    ls = f.read().strip().split("\n")


good_ids = 0
total_power = 0
for l in ls:
    parts = re.sub("[;,:]", "", l).split()
    colormax = defaultdict(int)
    for count, color in zip(parts[2::2], parts[3::2]):
        colormax[color] = max(colormax[color], int(count))
    if colormax["red"] <= 12 and colormax["green"] <= 13 and colormax["blue"] <= 14:
        good_ids += int(parts[1])
    total_power += math.prod(colormax.values())

# Part 1
print(good_ids)

# Part 2
print(total_power)
