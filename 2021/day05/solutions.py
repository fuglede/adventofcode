from collections import defaultdict
import re

with open("input") as f:
    ns = [list(map(int, re.findall("\d+", x))) for x in f.readlines()]


def cmp(a, b):
    return (a > b) - (a < b)


for part1 in (True, False):
    seen = set()
    overlap = set()
    for x1, y1, x2, y2 in ns:
        ds = cmp(x2, x1) + cmp(y2, y1) * 1j
        if abs(ds) != 1 and part1:
            continue
        new = {x1 + y1 * 1j + i * ds for i in range((abs(x2 - x1) or abs(y2 - y1)) + 1)}
        overlap |= seen & new
        seen |= new
    print(len(overlap))
