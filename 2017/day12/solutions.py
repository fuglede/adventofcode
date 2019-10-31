# Day 12, part 1
import re

import networkx as nx


with open('input') as f:
    ls = [x.strip() for x in f.readlines()]

G = nx.Graph()

for l in ls:
    vfrom = list(map(int, re.findall(r'^\d+', l)))[0]
    vto = list(map(int, re.findall(r'\s(\d+)', l)))
    for v in vto:
        G.add_edge(vfrom, v)

# Part one
print(len(list(nx.connected_components(G))[0]))

# Part two
print(len(list(nx.connected_components(G))))
