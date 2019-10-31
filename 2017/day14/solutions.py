import numpy as np
import networkx as nx


def knot_hash(s):
    lengths = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    arr = np.arange(256)
    arrlen = len(arr)
    skip_size = 0
    head = 0
    for _ in range(64):
        for l in lengths:
            newarr = np.copy(arr)
            for i in range(l):
                newarr[(head + i) % arrlen] = arr[(head + l - i - 1) % arrlen]
            arr = newarr
            head += l + skip_size
            skip_size += 1
    return ''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(arr.reshape(16, 16), axis=1))


# Part one
total = 0
for row in range(128):
    h = knot_hash(f'hfdlxzhv-{row}')
    binary = bin(int(h, 16))[2:].zfill(128)
    total += binary.count('1')
print(total)

# Part two
total = 0
used = np.zeros((128, 128), dtype=np.bool)
for row in range(128):
    h = knot_hash(f'hfdlxzhv-{row}')
    binary = bin(int(h, 16))[2:].zfill(128)
    idx = np.where(np.array(list(map(int, list(binary)))))
    used[row, idx] = True

G = nx.Graph()
for i in range(128):
    for j in range(128):
        if used[i, j]:
            G.add_node((i, j))
            if i > 0 and used[i-1, j]:
                G.add_edge((i-1, j), (i, j))
            if j > 0 and used[i, j-1]:
                G.add_edge((i, j-1), (i, j))
print(nx.number_connected_components(G))
