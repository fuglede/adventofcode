from itertools import product
from math import prod

import networkx as nx
import numpy as np


with open('input') as f:
    data = f.read().strip()

blocks = data.split('\n\n')

mats = {}
for b in blocks:
    b = b.splitlines()
    n = int(b[0][5:9])
    mat = np.array([[c == '#' for c in l] for l in b[1:]])
    mats[n] = mat


def symmetries(mat):
    for _ in range(4):
        yield mat
        yield np.flipud(mat)
        mat = np.rot90(mat)


def match(mat1, mat2):
    for mat in symmetries(mat2):
        if (mat1[0] == mat[-1]).all():
            return (-1, 0), mat
        if (mat1[-1] == mat[0]).all():
            return (1, 0), mat
        if (mat1[:, -1] == mat[:, 0]).all():
            return (0, 1), mat
        if (mat1[:, 0] == mat[:, -1]).all():
            return (0, -1), mat


# Part one
G = nx.Graph()
for (i1, mat1), (i2, mat2) in product(mats.items(), repeat=2):
    if i1 > i2 and match(mat1, mat2):
        G.add_edge(i1, i2)

print(prod(k for k, v in G.degree() if v == 2))


# Part two
# Pick an arbitrary root image, DFS from that, and make sure to update
# the values of mats as we rotate/flip
root = next(iter(mats.keys()))  # 1489
stack = [(root, (0, 0))]  # [1489]
locs = {(0, 0): root}


while stack:
    i1, loc = stack.pop()
    for i2 in G[i1]:
        if i2 in locs.values():
            continue
        ds, mat = match(mats[i1], mats[i2])
        mats[i2] = mat
        new_loc = (loc[0] + ds[0], loc[1] + ds[1])
        stack.append((i2, new_loc))
        locs[new_loc] = i2

# Start making the combined "big" picture. Since the root was arbitrary,
# locs will probably contain negative coordinates, so we have to offset
# accordingly.
n = int(np.sqrt(len(mats)))
big = np.empty((n*8, n*8), dtype=np.bool)
offset_x = min(x for x, _ in locs)
offset_y = min(y for _, y in locs)

for i in range(n):
    for j in range(n):
        tile = locs[i + offset_x, j + offset_y]
        mat = mats[tile][1:-1, 1:-1]
        big[i*8:(i+1)*8, j*8:(j+1)*8] = mat

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
mask = np.array([[c == '#' for c in l] for l in monster])


def count_sea_monsters(big):
    s = 0
    for i in range(big.shape[0] - mask.shape[0]):
        for j in range(big.shape[1] - mask.shape[1]):
            masked = big[i:i+mask.shape[0], j:j+mask.shape[1]]
            if (masked >= mask).all():
                s += 1
    return s


count = max(map(count_sea_monsters, symmetries(big)))
print(big.sum() - count * mask.sum())
