from heapq import heappop, heappush
from itertools import chain, count

import networkx as nx


with open('input') as f:
    ls = [x.strip() for x in f.readlines()]


def make_graph(ls):
    G = nx.grid_2d_graph(len(ls), len(ls[0]), create_using=nx.Graph)
    for x in range(len(ls)):
        for y in range(len(ls[0])):
            if ls[x][y] == '#':
                G.remove_node((x, y))
    return G


def generate_location_lookup(ls):
    starts = []
    locs = {}
    for x in range(len(ls)):
        for y in range(len(ls[0])):
            if ls[x][y] == '@':
                starts.append((x, y))
            if ls[x][y] not in {'.', "#"} and not ls[x][y].isupper():
                locs[ls[x][y]] = (x, y)
    return tuple(starts), locs


def generate_key_requirements(g, ls, starts, locs, locs_set):
    required_keys = {}
    for l1 in chain(starts, locs.values()):
        for l2 in locs_set:
            if l1 == l2:
                continue
            try:
                path = nx.shortest_path(g, l1, locs[l2])
                required_keys[l1, l2] = (set(str.lower(ls[d[0]][d[1]]) for d in path if ls[d[0]][d[1]].isupper()),
                                         len(path)-1)
            except nx.NetworkXNoPath:
                pass
    return required_keys


def accessible(g, loc, keys, locs_set, required_keys):
    for l in locs_set - keys:
        required = required_keys.get((loc, l))
        if required and not required[0] - keys:
            yield l, required[1]


def solve(ls):
    starts, loc_lookup = generate_location_lookup(ls)
    locs_set = set(loc_lookup) - set(['@'])
    g = make_graph(ls)
    required_keys = generate_key_requirements(g, ls, starts, loc_lookup, locs_set)
    counter = count()
    heap = [(0, next(counter), starts, set())]
    seen = set()
    while True:
        length, _, locations, keys = heappop(heap)
        s = ''.join(keys)
        if (locations, s) in seen:
            continue
        seen.add((locations, s))
        if len(keys) == len(locs_set):
            return length
        for i, loc in enumerate(locations):
            for key, len_to_key in accessible(g, loc, keys, locs_set, required_keys):
                new_length = length + len_to_key
                new_loc = loc_lookup[key]
                new_ls = list(locations)
                new_ls[i] = new_loc
                new_ls = tuple(new_ls)
                new_keys = set(keys) | set([key])
                heappush(heap, (new_length, next(counter), new_ls, new_keys))


# Part one
print(solve(ls))

# Part two
starts, _ = generate_location_lookup(ls)
start = starts[0]
for i in (-1, 0, 1):
    ls[start[0]+i] = ls[start[0]+i][:start[1]-1] + ('@#@' if i else '###') + ls[start[0]+i][start[1]+2:]

print(solve(ls))
