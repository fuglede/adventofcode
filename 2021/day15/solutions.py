import networkx as nx
import numpy as np

with open("input") as f:
    data = f.read().strip()


def solve(a):
    G = nx.grid_2d_graph(*a.shape, create_using=nx.DiGraph)
    for _, v, d in G.edges(data=True):
        d["weight"] = a[v]
    source, *_, target = G.nodes
    return nx.shortest_path_length(G, source, target, weight="weight")


# Part one
a = np.array([list(map(int, l)) for l in data.split()])
print(solve(a))

# Part two
a = np.block([[a + i + j for i in range(5)] for j in range(5)])
a[a > 9] -= 9
print(solve(a))
