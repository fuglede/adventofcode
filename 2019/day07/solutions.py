from math import inf
from itertools import count, permutations


with open('input') as f:
    ns = list(map(int, f.read().split(',')))


def run():
    p = list(ns)
    i = 0
    while True:
        cmd = str(p[i]).zfill(5)
        opcode = int(cmd[3:])
        mode1 = int(cmd[2])
        mode2 = int(cmd[1])
        try:
            p1 = p[i + 1] if int(cmd[2]) else p[p[i + 1]]
        except IndexError:
            pass
        try:
            p2 = p[i + 2] if int(cmd[1]) else p[p[i + 2]]
        except IndexError:
            pass
        if opcode == 1:
            p[p[i + 3]] = p1 + p2
            i += 4
        elif opcode == 2:
            p[p[i + 3]] = p1 * p2
            i += 4
        elif opcode == 3:
            p[p[i + 1]] = yield
            i += 2
        elif opcode == 4:
            yield p1
            i += 2
        elif opcode == 5:
            i = p2 if p1 != 0 else i + 3
        elif opcode == 6:
            i = p2 if p1 == 0 else i + 3
        elif opcode == 7:
            p[p[i + 3]] = int(p1 < p2)
            i += 4
        elif opcode == 8:
            p[p[i + 3]] = int(p1 == p2)
            i += 4
        elif opcode == 99:
            return


# Part one
m = -inf
for perm in permutations(range(5)):
    signal = 0
    for i in range(5):
        gen = run()
        next(gen)
        gen.send(perm[i])
        signal = gen.send(signal)
    m = max(m, signal)

print(m)

# Part two
m = -inf
for perm in permutations(range(5, 10)):
    gens = []

    # Send the given inputs only once
    for phase in perm:
        gen = run()
        next(gen)
        gens.append(gen)
        gen.send(phase)

    # From then on, only use outputs of amplifiers as inputs
    signal = 0
    try:
        while True:
            for gen in gens:
                signal = gen.send(signal)
            for gen in gens:
                next(gen)
    except StopIteration:
        m = max(m, signal)

print(m)
