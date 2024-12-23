import networkx as nx


with open("input") as f:
    ls = f.read().strip().split("\n")

G = nx.Graph(l.split("-") for l in ls)
cliques = list(nx.enumerate_all_cliques(G))

# Part 1
print(sum(len(c) == 3 and any(x[0] == 't' for x in c) for c in cliques))

# Part 2
print(",".join(sorted(cliques[-1])))
