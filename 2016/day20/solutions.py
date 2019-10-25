import networkx as nx


with open('input') as f:
    sets = [list(map(int, l.strip().split('-'))) for l in f.readlines()]

# Create a graph whose vertices are the intervals and for which there
# is an edge between two vertices exactly if they overlap (or neighbour
# each other)
G = nx.Graph()
for i, s in enumerate(sets):
    G.add_node(i)
    for j in range(i + 1, len(sets)):
        other = sets[j]
        if (s[0] <= other[0] and s[1] >= other[0]) or\
           (other[0] <= s[0] and other[1] >= s[0]) or\
           (s[0] >= other[0] and s[1] <= other[1]) or\
           (other[0] >= s[0] and other[1] <= s[1]) or\
           (s[1] == other[0] - 1) or\
           (other[1] == s[0] - 1):
            G.add_edge(i, j)

# Find the index of a set containing the IP 0
first = next(i for i, s in enumerate(sets) if s[0] == 0)

# Find its connected component and take the smallest IP not
# appearing within
conn = next(x for x in nx.connected_components(G) if first in x)
print(max(sets[s][1] for s in conn) + 1)

# For each connecte component, count the number of disallowed IPs
disallowed = 0
for c in nx.connected_components(G):
    disallowed += max(sets[s][1] for s in c) - min(sets[s][0] for s in c) + 1
print(4294967295 + 1 - disallowed)
