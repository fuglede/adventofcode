from itertools import permutations

with open('input') as f:
    lines = [x.strip().split() for x in f.readlines()]

d = {}
for s in lines:
    d[s[0], s[-1][:-1]] = -int(s[3]) if s[2] == 'lose' else int(s[3])

names = list(set(x[0] for x in lines))


def solve():
    best = -float('inf')
    for p in permutations(names):
        value = d[p[0], p[-1]] + d[p[-1], p[0]]
        for i in range(len(p) - 1):
            value += d[p[i], p[i+1]] + d[p[i + 1], p[i]]
        best = max(best, value)
    return best


# Part one
print(solve())

# Part two
for n in names:
    d['myself', n] = 0
    d[n, 'myself'] = 0
names += ['myself']
print(solve())
