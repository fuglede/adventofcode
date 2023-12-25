import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

G = nx.Graph()
for l in ls:
    v, *us = l.split()
    G.add_edges_from((v[:-1], u) for u in us)

G.remove_edges_from(nx.minimum_edge_cut(G))
a, b = nx.connected_components(G)
print(len(a) * len(b))
