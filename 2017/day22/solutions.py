import numpy as np

# Part one
d = 'u'
# Make a sufficiently large area
m = np.zeros((10001, 10001))
i = 5000
j = 5000


def step(i, j, d):
    new_infs = 0
    c = m[i][j]
    if c == 1:
        if d == 'u':
            d = 'r'
        elif d == 'r':
            d = 'd'
        elif d == 'd':
            d = 'l'
        elif d == 'l':
            d = 'u'
        m[i][j] = 0
    else:
        new_infs += 1
        if d == 'u':
            d = 'l'
        elif d == 'l':
            d = 'd'
        elif d == 'd':
            d = 'r'
        elif d == 'r':
            d = 'u'
        m[i][j] = 1
    if d == 'u':
        i -= 1
    elif d == 'd':
        i += 1
    elif d == 'r':
        j += 1
    elif d == 'l':
        j -= 1
    return (i, j, d, new_infs)


with open('input') as f:
    mid = np.array([list(map(int, list(x.strip().replace('.', '0').replace('#', '1')))) for x in f.readlines()])

m[5000-12:5000+13, 5000-12:5000+13] = mid
infs = 0
for _ in range(10000):
    (i, j, d, new_infs) = step(i, j, d)
    infs += new_infs
print(infs)

# Part two, same story, different rules
d = 'u'
m = np.zeros((10001, 10001))
i = 5000
j = 5000


def step(i, j, d):
    new_infs = 0
    c = m[i][j]
    if c == 0:
        if d == 'u':
            d = 'l'
        elif d == 'l':
            d = 'd'
        elif d == 'd':
            d = 'r'
        elif d == 'r':
            d = 'u'
        m[i][j] = 1
    elif c == 1:
        new_infs += 1
        m[i][j] = 2
    elif c == 2:
        if d == 'u':
            d = 'r'
        elif d == 'r':
            d = 'd'
        elif d == 'd':
            d = 'l'
        elif d == 'l':
            d = 'u'
        m[i][j] = 3
    elif c == 3:
        if d == 'u':
            d = 'd'
        elif d == 'r':
            d = 'l'
        elif d == 'd':
            d = 'u'
        elif d == 'l':
            d = 'r'
        m[i][j] = 0
    if d == 'u':
        i -= 1
    elif d == 'd':
        i += 1
    elif d == 'r':
        j += 1
    elif d == 'l':
        j -= 1
    return (i, j, d, new_infs)


with open('input') as f:
    mid = np.array([list(map(int, list(x.strip().replace('.', '0').replace('#', '2')))) for x in f.readlines()])
m[5000-12:5000+13, 5000-12:5000+13] = mid
infs = 0
for _ in range(10000000):
    (i, j, d, new_infs) = step(i, j, d)
    infs += new_infs
print(infs)
