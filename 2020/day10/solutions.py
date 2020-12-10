from collections import Counter, defaultdict


with open('input') as f:
    ns = [int(line.strip()) for line in f.readlines()]

ns = [0] + sorted(ns) + [max(ns) + 3]

# Part one
diffs = Counter(j - i for i, j in zip(ns, ns[1:]))
print(diffs[1]*diffs[3])

# Part two
# paths[i] is the number of ways to reach i'th adapter from 0
paths = defaultdict(int)
paths[0] = 1
for i in range(1, len(ns)):
    for j in range(i)[::-1]:
        if ns[i] - ns[j] > 3:
            break
        paths[i] += paths[j]

print(paths[len(ns)-1])
