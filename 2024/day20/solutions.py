from itertools import combinations

import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

G = nx.grid_2d_graph(len(ls), len(ls[0]))
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        p = (i, j)
        if x == "#":
            G.remove_node(p)
        elif x == "S":
            start = p

dist = nx.single_source_dijkstra_path_length(G, start)


def solve(cheat_dist):
    return sum(
        (d := abs(p1 - q1) + abs(p2 - q2)) <= cheat_dist and d2 - d1 - d >= 100
        for ((p1, p2), d1), ((q1, q2), d2) in combinations(dist.items(), 2)
    )


# Part 1
print(solve(2))

# Part 2
print(solve(20))
