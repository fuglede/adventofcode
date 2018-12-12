import numba as nb
import numpy as np

serial = 1723
square = np.zeros((300, 300))
for x in range(1, 301):
    for y in range(1, 301):
        rack = x + 10
        power = rack * y
        power += serial
        power *= rack
        power = (power // 100) % 10
        power -= 5
        square[x-1, y-1] = power

# Part one
best_m = 0
for x in range(300 - 2):
    for y in range(300 - 2):
        m = square[x:x+3, y:y+3].sum()
        if m > best_m:
            res = (x+1, y+1)
            best_m = m
print(res)


# Part two
@nb.jit
def find_largest():
    best_m = 0
    for i in range(1, 300):
        for x in range(300 - i + 1):
            for y in range(300 - i + 1):
                m = square[x:x+i, y:y+i].sum()
                if m > best_m:
                    res = (x+1, y+1, i)
                    best_m = m
    return res


print(find_largest())
