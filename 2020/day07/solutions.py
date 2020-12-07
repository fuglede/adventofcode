import networkx as nx


with open('input') as f:
    data = [x.strip().split() for x in f.readlines()]


rules = {}
for w in data:
    parent = w[0] + w[1]
    i = 4
    contains = []
    while i < len(w) and w[i] != 'no':
        count = int(w[i])
        child = w[i+1] + w[i+2]
        contains.append((count, child))
        i += 4
    rules[parent] = contains


# Part one
G = nx.DiGraph()
for parent, contains in rules.items():
    for _, child in contains:
        G.add_edge(child, parent)

print(len(nx.predecessor(G, 'shinygold')) - 1)


# Part two
def num_bags(color):
    return 1 + sum(count * num_bags(child) for count, child in rules[color])


print(num_bags('shinygold') - 1)
