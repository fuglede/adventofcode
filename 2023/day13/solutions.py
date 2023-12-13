import numpy as np

with open("input") as f:
    gs = f.read().strip().split("\n\n")


def find_mirror(a, mismatch):
    for i in range(1, len(a)):
        n = min(i, len(a) - i)
        if np.sum(a[:i][::-1][:n] ^ a[i:][:n]) == mismatch:
            return i


# Part 1 + 2
for mismatch in (0, 1):
    tot = 0
    for g in gs:
        a = np.array([[x == "#" for x in l] for l in g.split()])
        tot += (
            100 * row
            if (row := find_mirror(a, mismatch))
            else find_mirror(a.T, mismatch)
        )
    print(tot)
