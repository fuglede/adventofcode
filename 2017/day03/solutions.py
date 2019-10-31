from math import sqrt
from collections import defaultdict

# Part one
n = 325489
row = (int(sqrt(n - 1)) + 1) // 2
corner = (row*2 + 1)**2
row_length = row * 2
centers = (corner - row_length//2 - row_length * i for i in range(4))
dist = min(abs(n - center) for center in centers)
print(dist + row)


def solve(inp):
    vals = defaultdict(int)
    vals[(0, 0)] = 1
    this_row = 0
    this_col = 0
    row_length = 0
    while True:
        row_length += 2
        this_row -= 1
        this_col += 1
        for c in range(4):
            for r in range(row_length):
                if c == 0:
                    this_row += 1
                if c == 1:
                    this_col -= 1
                if c == 2:
                    this_row -= 1
                if c == 3:
                    this_col += 1
                new_val = sum(vals[(this_row + i, this_col + j)] for i in (-1, 0, 1) for j in (-1, 0, 1))
                vals[(this_row, this_col)] = new_val
                if new_val > inp:
                    return new_val


print(solve(n))
