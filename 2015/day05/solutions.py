from collections import Counter

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


lower_case = list(map(chr, range(65+32, 65+32+26)))

# Part one
doubles = set(a*2 for a in lower_case)
forbidden = {'ab', 'cd', 'pq', 'xy'}


def is_nice(w):
    c = Counter(w)
    return c['a'] + c['e'] + c['i'] + c['o'] + c['u'] > 2 \
        and any(x in w for x in doubles) \
        and not any(x in w for x in forbidden)


print(sum(map(is_nice, lines)))

# Part two
pairs = [a + b for a in lower_case for b in lower_case]
triples = [a + b + a for a in lower_case for b in lower_case]


def is_nice_2(w):
    return any(w.count(p) > 1 for p in pairs) and any(t in w for t in triples)


print(sum(map(is_nice_2, lines)))
