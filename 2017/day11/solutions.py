import numpy as np


# Day 11, part 1
def navigate(x, direction):
    if direction == 's':
        return [x[0], x[1] - 2]
    elif direction == 'n':
        return [x[0], x[1] + 2]
    elif direction == 'se':
        return [x[0] + 1, x[1] - 1]
    elif direction == 'sw':
        return [x[0] - 1, x[1] - 1]
    elif direction == 'nw':
        return [x[0] - 1, x[1] + 1]
    elif direction == 'ne':
        return [x[0] + 1, x[1] + 1]


def distance(x):
    if np.abs(x[0]) > np.abs(x[1]):
        return np.abs(x[0])
    vert = np.abs(np.abs(x[0]) - np.abs(x[1]))
    return vert / 2 + np.min(np.abs(x))


with open('input') as f:
    path = f.read().strip().split(',')

x = [0, 0]
maxd = 0
for d in path:
    x = navigate(x, d)
    maxd = max(maxd, distance(x))

# Part one
print(distance(x))

# Part two
print(maxd)
