import numpy as np


# Part 1
def gen_perms(a):
    yield a
    b = np.rot90(a)
    yield b
    b = np.rot90(b)
    yield b
    b = np.rot90(b)
    yield b
    b = np.fliplr(a)
    yield b
    b = np.rot90(b)
    yield b
    b = np.rot90(b)
    yield b
    b = np.rot90(b)
    yield b


def str_to_array(s):
    s = s.replace('/', '')
    s = s.replace('.', '0')
    s = s.replace('#', '1')
    l = len(s)
    d = int(np.sqrt(l))
    return np.array(list(map(int, list(s)))).reshape(d, d)


with open('input2') as f:
    p2 = [[str_to_array(y) for y in x.strip().split(' => ')] for x in f.readlines()]
with open('input3') as f: 
    p3 = [[str_to_array(y) for y in x.strip().split(' => ')] for x in f.readlines()]


def expand(a):
    ps = p2 if a.shape[0] == 2 else p3
    for m in gen_perms(a):
        for p in ps:
            if np.all(m == p[0]):
                return p[1]


def split(a):
    if a.shape[0] % 2 == 0:
        i = np.arange(2, a.shape[0], 2)
    else:
        i = np.arange(3, a.shape[0], 3)
    return np.array([np.hsplit(x, i) for x in np.vsplit(a, i)])


def step(a):
    s = split(a)
    l = len(s)
    return np.vstack(
        [np.hstack([expand(s[i][j]) for j in range(l)])
         for i in range(l)]
    )


# Part one
a = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
for _ in range(5):
    a = step(a)
print(np.sum(a))

# Part two
a = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
for _ in range(18):
    a = step(a)
print(np.sum(a))