from collections import defaultdict
from math import lcm

import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

# Generate for each time step the set of free squares
rows = len(ls) - 2
cols = len(ls[0]) - 2
inner = {j + i * 1j: ls[i + 1][j + 1] for i in range(rows) for j in range(cols)}
directions = {"<": -1, ">": 1, "^": -1j, "v": 1j}
blizzards_by_time = defaultdict(set)
steps = lcm(rows, cols)

for z in inner:
    if dz := directions.get(inner[z]):
        for t in range(steps):
            blizzards_by_time[t].add(z)
            z += dz
            z = (z.real % cols) + (z.imag % rows) * 1j

start = -1j
end = cols - 1 + rows * 1j
free = {k: (inner.keys() - v) | {start, end} for k, v in blizzards_by_time.items()}

# Since the sets are all rather small, we can just explicitly generate the
# graph of possible moves. To represent being able to exit at any time, we
# introduce a time-independent "super end node" (and similarly a "super
# start node" for part 2.
G = nx.DiGraph()
for t1 in range(steps):
    G.add_edge((t1, start), "superstart")
    G.add_edge((t1, end), "superend")
    t2 = (t1 + 1) % steps
    G.add_edges_from(
        ((t1, z), (t2, w))
        for z in free[t1]
        for w in {z + dz for dz in (0, 1, -1, -1j, 1j)} & free[t2]
    )

# Part 1
time1 = nx.shortest_path_length(G, (0, start), "superend") - 1
print(time1)

# Part 2
time2 = nx.shortest_path_length(G, (time1 % steps, end), "superstart") - 1
time3 = nx.shortest_path_length(G, ((time1 + time2) % steps, start), "superend") - 1
print(time1 + time2 + time3)
