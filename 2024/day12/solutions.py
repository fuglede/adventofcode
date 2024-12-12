import networkx as nx


with open("input") as f:
    board = {
        i + 1j * j: x
        for i, l in enumerate(f.read().strip().split("\n"))
        for j, x in enumerate(l)
    }

fourdir = {1, -1, 1j, -1j}
G = nx.Graph(
    (z, z + dz) for z in board for dz in fourdir if board[z] == board.get(z + dz)
)
G.add_nodes_from(board)

res1 = res2 = 0
for comp in nx.connected_components(G):
    wall = {(z, dz * 1j) for dz in fourdir for z in comp if z + dz not in comp}

    res1 += len(comp) * len(wall)
    res2 += len(comp) * sum((z + dz, dz) not in wall for (z, dz) in wall)

# Part 1
print(res1)

# Part 2
print(res2)
