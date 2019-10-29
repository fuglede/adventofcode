from collections import defaultdict


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

d = defaultdict(int)
for y in range(100):
    for x in range(100):
        d[x, y] = 1 if lines[y][x] == '#' else 0


def update(d, part_two):
    new_d = defaultdict(int)
    for x in range(100):
        for y in range(100):
            if part_two and x in {0, 99} and y in {0, 99}:
                new_d[x, y] = 1
            else:
                on = d[x-1, y-1] + d[x-1, y] + d[x-1, y+1] + d[x, y-1] + d[x, y+1] +\
                     d[x+1, y-1] + d[x+1, y] + d[x+1, y+1]
                if d[x, y]:
                    new_d[x, y] = 1 if on in {2, 3} else 0
                else:
                    new_d[x, y] = 1 if on == 3 else 0
    return new_d


# Part one
d1 = d
for _ in range(100):
    d1 = update(d1, False)
print(sum(d1.values()))

# Part two
d2 = d
for _ in range(100):
    d2 = update(d2, True)
print(sum(d2.values()))
