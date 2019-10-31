# Day 24, part 1+2
import networkx as nx
# Generate graph
G = nx.Graph()

with open('input') as f:
    es = [list(map(int, x.strip().split('/'))) for x in f.readlines()]

for e in es:
    G.add_edge(e[0], e[1], weight=-(e[0]+e[1]))


def extend_path(path, used_edges, value):
    v = path[-1]
    edges = [e for e in G.edges(v) if sorted(e) not in used_edges]
    for e in edges:
        newpath = path[:]
        newused = used_edges[:]
        newpath.append(e[1])
        newused.append(sorted(e))
        yield newpath, newused, value + e[0] + e[1]


length_and_strength = []
l = [([0], [], 0)]

while True:
    if not l:
        break
    p = l.pop()
    for sub in extend_path(*p):
        length_and_strength.append((len(sub[0]), sub[2]))
        l.append(sub)

# Part one
print(max(x[1] for x in length_and_strength))

# Part two
longest = max(length_and_strength)[0]
print(max(x[1] for x in length_and_strength if x[0] == longest))
