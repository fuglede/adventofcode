from collections import defaultdict
from math import ceil


with open('input') as f:
    ws = [l.replace(',', '').split() for l in f.readlines()]

d = {}
for w in ws:
    a = []
    i = 0
    while i < len(w)-3:
        a.append((w[i+1], int(w[i])))
        i += 2
    d[w[-1]] = (int(w[-2]), a)


def minbyel(el, needed, stock):
    if needed < stock[el]:
        return 0, 0
    if el == 'ORE':
        return needed, needed
    needed = needed - stock[el]
    produced, reaction = d[el]
    runs = ceil(needed / produced)
    scaled_reaction = [(a, runs*b) for a, b in reaction]
    ore = 0
    for elp, np in scaled_reaction:
        p, eo = minbyel(elp, np, stock)
        ore += eo
        stock[elp] += p - np
    return produced * runs, ore


# Part one
stock = defaultdict(int)
_, res = minbyel('FUEL', 1, stock)
print(res)

# Part two
lo = 0
hi = 1000000000000
while hi != lo + 1:
    stock = defaultdict(int)
    stock['ORE'] = 1000000000000
    half = lo + (hi - lo) // 2
    _, res = minbyel('FUEL', half, stock)
    if res > 0:
        hi = half
    else:
        lo = half
print(hi)
