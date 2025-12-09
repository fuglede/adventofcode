from itertools import combinations, starmap, compress
from shapely import Polygon, box

with open("input") as f:
    ls = f.read().strip().split()

ns = [tuple(map(int, line.split(","))) for line in ls]

rects = [
    (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    for (x1, y1), (x2, y2) in combinations(ns, 2)
]
areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for (x1, y1, x2, y2) in rects]

# Part 1
print(max(areas))

# Part 2
poly = Polygon(ns)
print(max(compress(areas, map(poly.contains, starmap(box, rects)))))
