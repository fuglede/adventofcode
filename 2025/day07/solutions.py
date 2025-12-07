"""Solution by treating each splitter individually.

Here, we note that how many beams enter a splitter depends only on the
ones above it, and immediately to its left/right. Moreover, once we find
a splitter directly above a given splitter, we now that we can stop
looking further up that column, since that splitter will block any beams
from higher up.

By noting that no two splitters are ever horizontally adjacent, we can
simplify the iteration logic a good deal.
"""

with open("input") as f:
    ls = f.read().strip().split("\n")

splitters = [col for l in ls for col, x in enumerate(l) if x == "^"]
entering = [1] + [0] * (len(splitters) - 1)

for i, si in enumerate(splitters):
    for j, sj in enumerate(splitters[:i][::-1]):
        if si == sj:
            break
        if abs(si - sj) == 1:
            entering[i] += entering[i - j - 1]

# Part 1
print(sum(b > 0 for b in entering))

# Part 2
print(sum(entering) + 1)
