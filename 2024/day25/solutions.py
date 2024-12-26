from itertools import combinations

with open("input") as f:
    gs = f.read().strip().split("\n\n")

# Part 1
print(
    sum(
        not any(x1 == x2 == "#" for x1, x2 in zip(g1, g2))
        for g1, g2 in combinations(gs, 2)
    )
)
