from collections import defaultdict
from heapq import heappop, heappush
from itertools import count
from math import inf

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: int(x) for i, l in enumerate(ls) for j, x in enumerate(l)}
N, M = len(ls), len(ls[0])


def solve(part2):
    q = [(0, 0, 0, 0, 0)]
    best = defaultdict(lambda: inf)
    c = count()
    while q:
        dist, _, z, last_dz, dz_count = heappop(q)
        if z == N - 1 + 1j * (M - 1) and (not part2 or dz_count >= 4):
            return dist
        for dz in (1, -1, 1j, -1j):
            if dz == -last_dz:
                continue
            if part2 and last_dz and dz != last_dz and dz_count < 4:
                continue
            if dz == last_dz:
                this_dz_count = dz_count + 1
                if this_dz_count == (11 if part2 else 4):
                    continue
            else:
                this_dz_count = 1
            w = z + dz
            if w in board:
                new_dist = dist + board[w]
                if new_dist >= best[w, dz, this_dz_count]:
                    continue
                best[w, dz, this_dz_count] = new_dist
                heappush(q, (new_dist, next(c), w, dz, this_dz_count))


print(solve(False))
print(solve(True))
