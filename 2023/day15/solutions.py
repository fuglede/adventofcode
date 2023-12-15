from collections import defaultdict
from functools import reduce

with open("input") as f:
    ws = f.read().strip().split(",")


def hsh(w):
    return reduce(lambda x, s: (x + ord(s)) * 17 % 256, w, 0)


# Part 1
print(sum(map(hsh, ws)))

# Part 2
d = defaultdict(dict)
for w in ws:
    match w.strip("-").split("="):
        case x, n:
            d[hsh(x)][x] = int(n)
        case x,:
            d[hsh(x)].pop(x, "🎄")

print(
    sum(
        (k + 1) * i * value
        for k, v in d.items()
        for i, value in enumerate(v.values(), 1)
    )
)
