import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: int(x) for i, l in enumerate(ls) for j, x in enumerate(l)}

G = nx.DiGraph(
    (z, z + dz)
    for z, h in board.items()
    for dz in (1, -1, 1j, -1j)
    if board.get(z + dz) == h + 1
)


zeros, nines = [[z for z, x in board.items() if x == v] for v in (0, 9)]
paths = [list(nx.all_simple_paths(G, z1, z2)) for z1 in zeros for z2 in nines]

# Part 1
print(sum(map(any, paths)))

# Part 2
print(sum(map(len, paths)))
