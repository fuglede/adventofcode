from collections import deque
from itertools import cycle, permutations
from math import inf

from vm import VM, read_program


p07 = read_program(7)

# Part one
m = -inf
for perm in permutations(range(5)):
    vms = []
    signal = 0
    for phase in perm:
        vm = VM(p07)
        signal = next(VM(p07, deque([phase, signal])))
    m = max(m, signal)
print(m)

# Part two
m = -inf
for perm in permutations(range(5, 10)):
    vms = [VM(p07, deque([phase])) for phase in perm]
    signal = 0
    try:
        for i in cycle(range(5)):
            vms[i].inputs.append(signal)
            signal = next(vms[i])
    except StopIteration:
        m = max(m, signal)
print(m)
