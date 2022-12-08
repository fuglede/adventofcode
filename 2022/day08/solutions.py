from itertools import count
from math import inf, prod

with open("input") as f:
    ls = f.read().strip().split("\n")

rows = len(ls)
cols = len(ls[0])
grid = {i + j * 1j: int(ls[i][j]) for i in range(rows) for j in range(cols)}

# Part 1
def is_visible(z):
    row = int(z.real)
    col = int(z.imag)
    to_check = {-1j: col, 1j: cols - col - 1, -1: row, 1: rows - row - 1}
    return any(
        all(grid[z + i * dz] < grid[z] for i in range(1, n + 1))
        for dz, n in to_check.items()
    )


print(sum(map(is_visible, grid)))

# Part 2
def score(z):
    return prod(
        next(
            i - (h == inf)
            for i in count(1)
            if (h := grid.get(z + i * dz, inf)) >= grid[z]
        )
        for dz in (-1j, 1j, -1, 1)
    )


print(max(map(score, grid)))
