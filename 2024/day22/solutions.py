from collections import defaultdict
import numpy as np

with open("input") as f:
    ns = list(map(int, f.read().strip().split("\n")))


def hsh(secret):
    for _ in range(2000):
        secret ^= secret << 6 & 0xFFFFFF
        secret ^= secret >> 5 & 0xFFFFFF
        secret ^= secret << 11 & 0xFFFFFF
        yield secret


secrets = list(map(list, map(hsh, ns)))

# Part 1
print(sum(s[-1] for s in secrets))

# Part 2
result = defaultdict(int)
for n in ns:
    ss = [s % 10 for s in hsh(n)]
    diffs = np.diff(ss)
    changes = set()
    for i in range(1996):
        if (change := tuple(diffs[i : i + 4])) not in changes:
            changes.add(change)
            result[change] += ss[i + 4]

print(max(result.values()))
