import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: int(x) for i, l in enumerate(ls) for j, x in enumerate(l)}
fourdir = (1, -1, 1j, -1j)

G = nx.DiGraph()
for z, h in board.items():
    for dz in fourdir:
        if board.get(z + dz, -1) == h + 1:
            G.add_edge(z, z + dz)

zeros = [z for z, x in board.items() if x == 0]
nines = [z for z, x in board.items() if x == 9]
paths = [list(nx.all_simple_edge_paths(G, z1, z2)) for z1 in zeros for z2 in nines]

# Part 1
print(sum(map(any, paths)))

# Part 2
print(sum(map(len, paths)))
