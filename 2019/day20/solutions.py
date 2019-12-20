import networkx as nx

with open('input') as f:
    ls = f.readlines()

# Part one
portals = {}
for i in range(len(ls)):
    for j in range(len(ls[i])):
        # Vertical portals
        if ls[i][j].isupper() and i > 0 and ls[i-1][j].isupper():
            if i < len(ls)-1 and ls[i+1][j] == '.':
                portals[i+1, j] = set([ls[i][j], ls[i-1][j]])
            else:
                portals[i-2, j] = set([ls[i][j], ls[i-1][j]])
        # Horizontal portals
        elif ls[i][j].isupper() and j > 0 and ls[i][j-1].isupper():
            if j < len(ls[2])-1 and ls[i][j+1] == '.':
                portals[i, j+1] = set([ls[i][j], ls[i][j-1]])
            else:
                portals[i, j-2] = set([ls[i][j], ls[i][j-1]])

start = next(k for k, v in portals.items() if v == set(['A']))
end = next(k for k, v in portals.items() if v == set(['Z']))

G = nx.grid_2d_graph(len(ls), len(ls[0]))
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] != '.':
            G.remove_node((i, j))

for p1, portal1 in portals.items():
    for p2, portal2 in portals.items():
        if portal1 == portal2 and p1 != p2:
            G.add_edge(p1, p2)

print(nx.shortest_path_length(G, start, end))

# Part two
portal_is_outer = {p: p[0] in (2, len(ls)-3) or p[1] in (2, len(ls[2])-4) for p in portals}

# We're lazy and simply assume that the optimal solution uses no more than 100
# levels; if it does, we can simply increase the number.
G = nx.Graph()
for depth in range(100):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j] == '.':
                if ls[i-1][j] == '.':
                    G.add_edge((i, j, depth), (i-1, j, depth))
                if ls[i][j-1] == '.':
                    G.add_edge((i, j, depth), (i, j-1, depth))
                if (i, j) in portals:
                    for (i2, j2), portal in portals.items():
                        if portals[i, j] == portal and (i2, j2) != (i, j):
                            if not portal_is_outer[i, j]:
                                G.add_edge((i, j, depth), (i2, j2, depth+1))

print(nx.shortest_path_length(G, (*start, 0), (*end, 0)))
