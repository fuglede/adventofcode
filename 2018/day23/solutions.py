import re

import networkx as nx
import numpy as np
from scipy.optimize import linprog


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ns = np.array([[int(x) for x in re.findall(r'-?\d+', s)] for s in lines])

pos = ns[:, :3]
r = ns[:, 3]

# Part one
print(np.sum(np.sum(np.abs(pos - pos[np.argmax(r)]), 1) <= np.max(r)))

# Part two
# First we will find the nanobots whose signals overlap. We do this by
# creating a graph whose vertices are nanobots and whose edges are between
# nanobots whose signals overlap. Then, since the point of interest is one
# lying in the intersection of the largest number of nanobot signal areas,
# we can find those nanobots as the maximal clique in the graph. This is
# sort of broken since it assumes that the maximum is unique (which I simply
# checked out of band), and that pairwise intersecting L^1 spheres have a
# common intersection, which is simply /not/ true in general in R^3.
g = nx.Graph()
for i, (p1, r1) in enumerate(zip(pos, r)):
    for j, (p2, r2) in enumerate(zip(pos, r)):
        if np.sum(np.abs(p1 - p2)) <= r1 + r2:
            g.add_edge(i, j)
cliques = list(nx.clique.find_cliques(g))
max_clique = max(enumerate(cliques), key=lambda x: len(x[1]))[1]

# Now, knowing the relevant nanobots, we will use linear programming to
# find the coordinate minimizing the L^1 distance to the origin. That is,
# we want to find
#    min_x |x1| + |x2| + |x3|
# constrained by
#    |x1 - c1| + |x2 - c2| + |x3 - c3| <= s
# for each nanobot with position (c1, c2, c3) and signal strength s. We
# can turn this into a linear problem by introducing six variables to
# represent the positive and negative parts of x,
#   x1 = t11 - t12,
#   x2 = t21 - t22,
#   x3 = t31 - t32,
# and, for each nanobot, six variables to represent the absolute values,
#   x1 - c1 = d11 - d12,
#   x2 - c2 = d21 - d22, and
#   x3 - c3 = d31 - d32.
# Then, relying on some details about the simplex algorithm, the full
# linear problem becomes
#   min_t min(t11 + ... + t32)
# constrained by
#   d11 + d12 + d21 + d22 + d31 + d32 <= s,
#   t11 + t12 - d11 + d12 = c1,
#   t21 + t22 - d21 + d22 = c2,
#   t31 + t32 - d31 + d32 = c3,
#   tij >= 0, and
#   dij >= 0.
# This is readily solved using SciPy's LP solver, noting that the vertices
# of the simplex must necessarily have integral coordinates.
num_vars = 6 * len(pos) + 6

# Define objective function
c = np.zeros(num_vars)
c[:6] = 1

# Define constraints
A_ub = np.zeros((len(pos), num_vars))
b_ub = np.zeros(len(pos))
A_eq = np.zeros((3 * len(pos), num_vars))
b_eq = np.zeros(3 * len(pos))
for i, (p, s) in enumerate(zip(pos, r)):
    # Skip the nanobots not present in the overlap
    if i not in max_clique:
        continue
    A_eq[3*i, 0:2] = 1
    A_eq[3*i, 6*(i+1)] = -1
    A_eq[3*i, 6*(i+1) + 1] = 1

    A_eq[3*i + 1, 2:4] = 1
    A_eq[3*i + 1, 6*(i+1) + 2] = -1
    A_eq[3*i + 1, 6*(i+1) + 3] = 1

    A_eq[3*i + 2, 4:6] = 1
    A_eq[3*i + 2, 6*(i+1) + 4] = -1
    A_eq[3*i + 2, 6*(i+1) + 5] = 1
    b_eq[3*i:3*i + 3] = p

    A_ub[i, 6*(i+1):6*(i+2)] = 1
    b_ub[i] = s

result = linprog(c, A_ub, b_ub, A_eq, b_eq, options={'maxiter': 10000000})
print(int(result.fun))
