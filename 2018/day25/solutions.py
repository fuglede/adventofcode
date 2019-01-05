import re

import networkx as nx
import numpy as np


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ps = np.array([[int(x) for x in re.findall(r'-?\d+', s)] for s in lines])

g = nx.Graph()

for i1, p1 in enumerate(ps):
    for i2, p2 in enumerate(ps):
        if np.sum(np.abs(p1 - p2)) <= 3:
            g.add_edge(i1, i2)

print(sum(1 for _ in nx.connected_components(g)))