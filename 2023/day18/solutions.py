import numpy as np

with open("input") as f:
    ws = [l.split() for l in f.read().strip().split("\n")]

dirs = {"R": 1j, "L": -1j, "U": -1, "D": 1}


def solve(instructions):
    vs = np.array([dirs[d] * dist for d, dist in instructions])
    return abs(np.sum(np.cumsum(vs.real) * vs.imag)) + np.sum(np.abs(vs)) / 2 + 1


# Part 1
print(solve((d, int(length)) for d, length, _ in ws))

# Part 2
table = {"0": "R", "1": "D", "2": "L", "3": "U"}
print(solve((table[color[-2]], int(color[2:-2], 16)) for _, _, color in ws))
