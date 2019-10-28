from collections import defaultdict


with open('input') as f:
    lines = [x.strip().split() for x in f.readlines()]


def get_distance(v, tt, tr, maxt):
    t = 0
    d = 0
    while True:
        for _ in range(tt):
            d += v
            t += 1
            if t == maxt:
                return d
        t += tr
        if t >= maxt:
            return d


# Part one
best = -float('inf')
for l in lines:
    distance = get_distance(int(l[3]), int(l[6]), int(l[-2]), 2503)
    best = max(best, distance)
print(best)

# Part two
points = defaultdict(int)
for t in range(1, 2504):
    best = -float('inf')
    winners = []
    for l in lines:
        distance = get_distance(int(l[3]), int(l[6]), int(l[-2]), t)
        if distance >= best:
            if distance == best:
                winners.append(l[0])
            else:
                winners = [l[0]]
            best = max(best, distance)
    for winner in winners:
        points[winner] += 1
print(max(points.values()))
