import networkx as nx

with open("input") as f:
    ls = f.read().strip().split("\n")

fourdir = (1, -1, 1j, -1j)

G = nx.DiGraph()

for i, l in enumerate(ls):
    for j, x in enumerate(l):
        if x == "#":
            continue
        z = i + 1j * j
        if x == "S":
            start = (z, 1j)
        if x == "E":
            end = z
        for dz in fourdir:
            G.add_node((z, dz))

for z, dz in G.nodes:
    if (z + dz, dz) in G.nodes:
        G.add_edge((z, dz), (z + dz, dz), weight=1)
    for rot in -1j, 1j:
        G.add_edge((z, dz), (z, dz * rot), weight=1000)

for dz in fourdir:
    G.add_edge((end, dz), "end", weight=0)

# Part 1
print(nx.shortest_path_length(G, start, "end", weight="weight"))

# Part2
print(
    len(
        {
            z
            for path in nx.all_shortest_paths(G, start, "end", weight="weight")
            for z, _ in path[:-1]
        }
    )
)
