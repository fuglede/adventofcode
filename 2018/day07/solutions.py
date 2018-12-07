from itertools import count

import networkx as nx


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

g = nx.DiGraph()
g.add_edges_from((l[5], l[36]) for l in lines)

# Part one
print(''.join(nx.lexicographical_topological_sort(g)))


# Part two
done_at = {}
s = ''
workers = 5
for t in count():
    done_now = [k for (k, v) in done_at.items() if v == t]
    for k in done_now:
        s += k
        workers += 1
        done_at.pop(k)
    if len(s) == 26:
        print(t)
        break
    available = sorted([n for n in g.nodes()
                        if n not in s and n not in done_at and all(e[0] in s for e in g.in_edges(n))])
    for new in available:
        if workers == 0:
            break
        workers -= 1
        done_at[new] = t + ord(new) - ord('A') + 61
