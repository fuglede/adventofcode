from itertools import count

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
blocked = {loc for loc, val in board.items() if val == "#"}
rounds = {loc for loc, val in board.items() if val == "O"}


def tilt(rounds, d=1):
    while True:
        free = board.keys() - rounds - blocked
        newrounds = {z - d if z - d in free else z for z in rounds}
        if newrounds == rounds:
            return newrounds
        rounds = newrounds


def load(rounds):
    return sum(100 - z.real for z in rounds)


def cycle(rounds):
    for d in (1, 1j, -1, -1j):
        rounds = tilt(rounds, d)
    return rounds


# Part 1
print(load(tilt(rounds)))


# Part 2
seen = []
for i in count():
    rounds = cycle(rounds)
    if rounds in seen:
        start = seen.index(rounds)
        break
    seen.append(rounds)


print(load(seen[(1000000000 - i) % (start - i) + i - 1]))
