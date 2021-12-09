from math import prod

import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")


# Part one
G = nx.grid_2d_graph(len(ls), len(ls[0]))
depth = {(i, j): int(ls[i][j]) for i, j in G.nodes}
print(
    sum(
        depth[v] + 1
        for v in G.nodes
        if all(depth[v] < depth[u] for u in G.neighbors(v))
    )
)

# Part two
G.remove_nodes_from(k for k, v in depth.items() if v == 9)
print(prod(sorted(map(len, nx.connected_components(G)))[-3:]))
