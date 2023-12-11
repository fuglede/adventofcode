from itertools import combinations

with open("input") as f:
    ls = f.read().strip().split("\n")

galaxies = {(i, j) for i, l in enumerate(ls) for j, x in enumerate(l) if x == "#"}
pairs = list(combinations(galaxies, 2))
# Note that in our input, no rows are empty, so we only keep track of the empty columns
x2s = {x2 for _, x2 in galaxies}
empty = set(range(max(x2s))) - x2s


def dist(x1, x2, y1, y2, scale):
    cols = set(range(x2, y2, 1 if y2 > x2 else -1))
    return abs(x1 - y1) + abs(x2 - y2) + len(empty & cols) * scale


# Part 1
print(sum(dist(*x, *y, 1) for x, y in pairs))

# Part 2
print(sum(dist(*x, *y, 999_999) for x, y in pairs))
