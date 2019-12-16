from numba import jit
import numpy as np


with open('input') as f:
    data = f.read().strip()

inp = list(map(int, data))


# Part one
def step(l):
    new = np.zeros(len(l), dtype=int)
    for i in range(len(l)):
        indices = (np.arange(1, len(l)+1) // (i+1)) % 4
        el = (l[indices == 1].sum() - l[indices == 3].sum())
        new[i] = abs(el) % 10
    return new


l = np.array(inp)
for _ in range(100):
    l = step(l)
print(''.join(map(str, l[:8])))


# Part two
# The key insight is that the 7-digit offset is in the second half of the
# elongated input. This means that we only need to bother with the bottom
# right block of the matrix which is the upper-triangular matrix of ones,
# so we simply apply this to the second half of the input vector 100 times.
@jit
def iterate(l):
    for _ in range(100):
        for j in range(1, len(l)):
            l[len(l)-j-1] = (l[len(l)-j] + l[len(l)-j-1]) % 10
    return l


l = np.array(inp*5000)
offset = int(''.join(map(str, inp[:7])))
l = iterate(l)
print(''.join(map(str, l[offset-len(l):offset-len(l)+8])))
