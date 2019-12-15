from collections import deque

import networkx as nx

from vm import VM, read_program


ns = read_program(15)

q = deque()
vm = VM(ns)
q.append((0, vm))
direction = {1: 1j, 2: -1j, 3: -1, 4: 1}
G = nx.Graph()

while q:
    loc, base_vm = q.pop()
    for d in range(1, 5):
        vm = base_vm.clone()
        vm.inputs = deque([d])
        output = next(vm)
        if output:
            new_loc = loc + direction[d]
            if new_loc not in G.nodes:
                if output == 2:
                    oxygen = new_loc
                q.append((new_loc, vm))
                G.add_edge(loc, new_loc)

# Part one
print(nx.shortest_path_length(G, 0, oxygen))

# Part two
print(nx.eccentricity(G, oxygen))
