import networkx as nx


G = nx.read_edgelist('input', delimiter=')', create_using=nx.DiGraph)

# Part one
print(sum(len(nx.ancestors(G, v)) for v in G))

# Part two
print(nx.shortest_path_length(G.to_undirected(), 'YOU', 'SAN') - 2)
