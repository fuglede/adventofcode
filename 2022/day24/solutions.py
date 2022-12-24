from collections import defaultdict
from math import lcm

import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

# Create a dictionary of blizzards by time
rows = len(ls)
cols = len(ls[0])
inner = {(i, j): ls[i+1][j+1] for i in range(rows - 2) for j in range(cols - 2)}

bbt = defaultdict(set)
steps = lcm(rows - 2, cols - 2)
blizzards = set()
for i in range(rows - 2):
    for j in range(cols - 2):
        t = 0
        if inner[i, j] == '<':
            for _ in range(steps):
                bbt[t].add((i, j))
                j -= 1
                j %= cols - 2
                t += 1
        if inner[i, j] == '>':
            for _ in range(steps):
                bbt[t].add((i, j))
                j += 1
                j %= cols - 2
                t += 1
        if inner[i, j] == '^':
            for _ in range(steps):
                bbt[t].add((i, j))
                i -= 1
                i %= rows - 2
                t += 1
        if inner[i, j] == 'v':
            for _ in range(steps):
                bbt[t].add((i, j))
                i += 1
                i %= rows - 2
                t += 1

# Create a graph of all possible moves including time in
# the state. Also include super sinks/sources for the
# start/end
times = 1000
for i in range(times):
    bbt[i] = bbt[i % steps]
G = nx.DiGraph()
for t1, t2 in zip(range(times), range(1, times)):
    G.add_edge((t1, 'start'), (t2, 'start'))
    G.add_edge((t1, 'end'), (t2, 'end'))
    for i1 in range(rows - 2):
        for j1 in range(cols - 2):
            if (i1, j1) in bbt[t1]:
                continue
            if (i1, j1) not in bbt[t2]:
                G.add_edge((t1, (i1, j1)), (t2, (i1, j1)))
            if i1 > 0 and (i1 - 1, j1) not in bbt[t2]:
                G.add_edge((t1, (i1, j1)), (t2, (i1-1, j1)))
            if i1 < rows - 2 and (i1 + 1, j1) not in bbt[t2]:
                G.add_edge((t1, (i1, j1)), (t2, (i1+1, j1)))
            if j1 > 0 and (i1, j1 - 1) not in bbt[t2]:
                G.add_edge((t1, (i1, j1)), (t2, (i1, j1 -1)))
            if j1 < cols - 2 and (i1, j1 + 1) not in bbt[t2]:
                G.add_edge((t1, (i1, j1)), (t2, (i1, j1 +1)))

for i in range(times):
    if (i+1, (0, 0)) in G.nodes:
        G.add_edge((i, 'start'), (i+1, (0, 0)))

for i in range(times):  # For part 2
    if (i, (0, 0)) in G.nodes:
        G.add_edge((i, (0, 0)), (i+1, 'mid'))
    G.add_edge((i+1, 'mid'), 'mid')

for i in range(times):
    if (i, (rows-3, cols-3)) in G.nodes:
        G.add_edge((i, (rows-3, cols-3)), (i+1,'end'))
        G.add_edge((i-1, 'end'), (i, (rows-3, cols-3)))
    G.add_edge((i, 'end'), 'end')

# Time to actually solve the problem

# Part 1
time1 = nx.shortest_path_length(G, (0, 'start'), 'end') - 1

print(time1)

# Part 2
time2 = nx.shortest_path_length(G, (time1, 'end'), 'mid') - 1
time3 = nx.shortest_path_length(G, (time1+time2, 'start'), 'end') - 1
print(time1+time2+time3)

