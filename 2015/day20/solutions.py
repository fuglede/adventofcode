import numpy as np


n = 36000000

# Part one
presents = np.zeros(n//10)
for elf in range(1, n//10):
    for house in range(elf, n//10, elf):
        presents[house] += elf * 10
print(np.argmax(presents >= n))

# Part two
presents = np.zeros(n//10)
for elf in range(1, n//10):
    for house in range(elf, n//10, elf):
        presents[house] += elf * 11
        if house == 50*elf:
            break
print(np.argmax(presents >= n))
