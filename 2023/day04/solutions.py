import re

import numpy as np

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall(r"\d+", x))) for x in ls]
wins = [len(set(n[11:]) & set(n[1:11])) for n in ns]

# Part 1
print(sum(2 ** (w - 1) for w in wins if w > 0))

# Part 2
cards = np.ones(len(ns))
for i in range(len(cards)):
    cards[i + 1 : i + wins[i] + 1] += cards[i]

print(cards.sum())

# Part 2 again, but considering the game as a nilpotent evolution for no real reason
N = len(ns)
rows, cols = np.ogrid[:N, :N]
mat = (cols > rows) & (cols <= rows + np.array(wins)[:, np.newaxis])
print((np.linalg.inv(np.eye(N) - mat) @ np.ones(N)).sum())
