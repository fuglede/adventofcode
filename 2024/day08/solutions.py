from collections import defaultdict
from itertools import permutations

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
antennas = defaultdict(list)
for z, x in board.items():
    if x not in (".", "#"):
        antennas[x].append(z)

# Part 1
antinodes = {
    2 * z2 - z1 for zs in antennas.values() for z1, z2 in permutations(zs, 2)
} & board.keys()
print(len(antinodes))

# Part 2
antinodes = set()
for zs in antennas.values():
    for z1, z2 in permutations(zs, 2):
        z = z2
        while z in board:
            antinodes.add(z)
            z += z2 - z1
print(len(antinodes))
