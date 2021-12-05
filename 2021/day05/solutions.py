from collections import defaultdict
import re

with open("input") as f:
    ns = [list(map(int, re.findall("\d+", x))) for x in f.readlines()]


def cmp(a, b):
    return (a > b) - (a < b)


for part1 in (True, False):
    d = defaultdict(int)
    for x1, y1, x2, y2 in ns:
        dx = cmp(x2, x1)
        dy = cmp(y2, y1)
        if part1 and dx and dy:
            continue
        for i in range((abs(x1 - x2) or abs(y1 - y2)) + 1):
            d[(x1 + i * dx, y1 + i * dy)] += 1
    print(sum(x > 1 for x in d.values()))
