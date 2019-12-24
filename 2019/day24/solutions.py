from collections import defaultdict


with open('input') as f:
    ls = [l.strip() for l in f.readlines()]


# Part one
def step(d):
    new_d = defaultdict(int)
    for y in range(5):
        for x in range(5):
            z = x + 1j * y
            adjacent = d[z+1] + d[z-1] + d[z+1j] + d[z-1j]
            if d[z] == 1 and adjacent != 1:
                new_d[z] = 0
            elif d[z] == 0 and adjacent in (1, 2):
                new_d[z] = 1
            else:
                new_d[z] = d[z]
    return new_d


def equal(d1, d2):
    for x in range(5):
        for y in range(5):
            z = x + 1j*y
            if d1[z] != d2[z]:
                return False
    return True


def rating(d):
    s = 0
    i = 0
    for y in range(5):
        for x in range(5):
            s += d[x + 1j*y]*2**i
            i += 1
    return s


def solve():
    d = defaultdict(int)
    for y in range(len(ls)):
        for x in range(len(ls[y])):
            if ls[y][x] == '#':
                d[x + 1j*y] = 1
    seen = []
    while True:
        seen.append(d)
        new_d = step(d)
        if any(equal(old_d, new_d) for old_d in seen):
            return rating(new_d)
        d = new_d


print(solve())


# Part two
def all_adjacent(z, level):
    adjacent = [(z-1, level), (z+1, level), (z-1j, level), (z+1j, level)]
    adjacent = [(w, level) for (w, level) in adjacent if 0 <= w.real <= 4 and 0 <= w.imag <= 4 and w != 2+2j]
    if z.real == 0:
        adjacent += [(1+2j, level+1)]
    if z.real == 4:
        adjacent += [(3+2j, level+1)]
    if z.imag == 0:
        adjacent += [(2+1j, level+1)]
    if z.imag == 4:
        adjacent += [(2+3j, level+1)]
    if z.real == 1 and z.imag == 2:
        adjacent += [(0, level-1), (0+1j, level-1), (0+2j, level-1), (0+3j, level-1), (0+4j, level-1)]
    if z.real == 3 and z.imag == 2:
        adjacent += [(4, level-1), (4+1j, level-1), (4+2j, level-1), (4+3j, level-1), (4+4j, level-1)]
    if z.real == 2 and z.imag == 1:
        adjacent += [(0, level-1), (1, level-1), (2, level-1), (3, level-1), (4, level-1)]
    if z.real == 2 and z.imag == 3:
        adjacent += [(4j, level-1), (1+4j, level-1), (2+4j, level-1), (3+4j, level-1), (4+4j, level-1)]
    return set(adjacent)


def step2(d):
    min_level = min(w[1] for w in d)-1
    max_level = max(w[1] for w in d)+1
    new_d = defaultdict(int)
    for level in range(min_level, max_level+1):
        for y in range(5):
            for x in range(5):
                z = x + 1j * y
                if z == 2+2j:
                    continue
                adjacent = sum(d[w] for w in all_adjacent(z, level))
                if d[z, level] == 1 and adjacent != 1:
                    new_d[z, level] = 0
                elif d[z, level] == 0 and adjacent in (1, 2):
                    new_d[z, level] = 1
                else:
                    new_d[z, level] = d[z, level]
    return new_d


def solve2():
    d = defaultdict(int)
    for y in range(len(ls)):
        for x in range(len(ls[y])):
            if ls[y][x] == '#':
                d[x + 1j*y, 0] = 1
    for _ in range(200):
        d = step2(d)
    return sum(d.values())


print(solve2())
