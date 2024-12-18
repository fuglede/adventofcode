import networkx as nx

with open("input") as f:
    ns = [tuple(map(int, l.split(","))) for l in f.read().strip().split("\n")]


G = nx.grid_2d_graph(71, 71)

for i, p in enumerate(ns):
    G.remove_node(p)
    if i == 1023:
        # Part 1
        print(nx.shortest_path_length(G, (0, 0), (70, 70)))
    elif not nx.has_path(G, (0, 0), (70, 70)):
        # Part 2
        print(p)
        break
