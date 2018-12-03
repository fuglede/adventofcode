import re
from collections import defaultdict

with open('input') as f:
    l = f.read()

# Part one
p = 0
pres = defaultdict(int)
pres[0] = 1
for a in l:
    if a == '^':
        p += 1j
    elif a == 'v':
        p -= 1j
    elif a == '>':
        p += 1
    elif a == '<':
        p -= 1
    pres[p] += 1

print(sum(v > 0 for v in pres.values()))

# Part two
p1 = p2 = 0
pres = defaultdict(int)
pres[0] = 2
for i, a in enumerate(l):
    if i % 2:
        if a == '^':
            p1 += 1j
        elif a == 'v':
            p1 -= 1j
        elif a == '>':
            p1 += 1
        elif a == '<':
            p1 -= 1
        pres[p1] += 1
    else:
        if a == '^':
            p2 += 1j
        elif a == 'v':
            p2 -= 1j
        elif a == '>':
            p2 += 1
        elif a == '<':
            p2 -= 1
        pres[p2] += 1

print(sum(v > 0 for v in pres.values()))
