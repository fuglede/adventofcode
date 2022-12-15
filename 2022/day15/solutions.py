import re

from z3 import If, Int, Solver

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Part 1
beacons = set()
cants = set()
y = 2000000
for n in ns:
    sensor = (n[0], n[1])
    beacon = (n[2], n[3])
    beacons.add(beacon)
    dist = manhattan(sensor, beacon)
    length = dist - abs(sensor[1] - y)
    cants |= set((x, y) for x in range(sensor[0] - length, sensor[0] + length + 1))

print(len(cants - beacons))


# Part 2
def z3abs(x):
    return If(x >= 0, x, -x)


s = Solver()
x = Int("x")
y = Int("y")
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)
for n in ns:
    dist = manhattan((n[0], n[1]), (n[2], n[3]))
    s.add(z3abs(x - n[0]) + z3abs(y - n[1]) > dist)

s.check()
model = s.model()
print(model[x].as_long() * 4000000 + model[y].as_long())
