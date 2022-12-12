from math import inf

import networkx as nx


with open("input") as f:
    ls = f.read().strip().split("\n")

all_as = set()
elev = {}
for x, l in enumerate(ls):
    for y, char in enumerate(l):
        z = x + y * 1j
        elev[z] = ord(char)
        match char:
            case "S":
                s = z
                elev[z] = ord("a")
            case "E":
                e = z
                elev[z] = ord("z")
            case "a":  # Part 2
                all_as.add(z)

G = nx.DiGraph()
for z in elev:
    for dz in (1, -1, 1j, -1j):
        if elev.get(z + dz, inf) <= elev[z] + 1:
            G.add_edge(z, z + dz)

# Part 1
print(nx.shortest_path_length(G, s, e))

# Part 2
all_lengths = nx.shortest_path_length(G, target=e)
print(min(all_lengths.get(a, inf) for a in all_as))
