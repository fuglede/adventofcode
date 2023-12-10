from collections import deque
from itertools import product
from math import inf

import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")


board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
dirs = {
    "|": [1, -1],
    "-": [1j, -1j],
    "J": [-1, -1j],
    "F": [1, 1j],
    "S": [1, 1j],
    "7": [1, -1j],
    "L": [-1, 1j],
}
S = next(z for z, x in board.items() if x == "S")
seen = {S}
removed = set()
q = deque([(S, 0)])
while q:
    z, dist = q.popleft()
    for dz in dirs[board[z]]:
        newz = z + dz
        if newz not in seen:
            q.append((newz, dist + 1))
            seen.add(newz)
        # For part 2
        removed |= {2 * z, 2 * z + dz, 2 * z + 2 * dz}

# Part 1
print(dist)

# Part 2
# We create the grid graph corresponding to the board. We double the size of it
# to allow for squeezing in between pipes, and we pad it by additional rows and
# columns to make it possible to get around. Then "-1-1j" corresponds to a point
# on the outside, and we want to see which nodes can reach that point. Finally,
# we want to make sure that we only count "physical" nodes which after doubling
# are those that have even coordinates.
octdir = {-1, -1 + 1j, -1 - 1j, 1, 1 + 1j, 1 - 1j, -1j, 1j}
G = nx.Graph()
for i in range(-1, 2 * len(ls) + 1):
    for j in range(-1, 2 * len(ls[0]) + 1):
        for dz in octdir:
            z = i + 1j * j
            G.add_edge(z, z + dz)
for z in removed:
    G.remove_node(z)

print(
    sum(
        z.real % 2 == 0 and z.imag % 2 == 0
        for z in set.union(*(x for x in nx.connected_components(G) if -1 - 1j not in x))
    )
)
