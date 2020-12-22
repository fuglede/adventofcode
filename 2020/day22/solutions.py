from collections import deque
from math import prod


with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

old_p1 = deque(map(int, ls[1:26]))
old_p2 = deque(map(int, ls[28:]))


def score(winner):
    return sum(map(prod, enumerate(reversed(winner), 1)))


# Part one
p1 = deque(old_p1)
p2 = deque(old_p2)

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

print(score(p1 or p2))


# Part two
def game(p1, p2):
    seen = set()
    while p1 and p2:
        conf = (tuple(p1), tuple(p2))
        if conf in seen:
            return True, p1
        seen.add(conf)
        c1 = p1.popleft()
        c2 = p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            p1_won, _ = game(deque(list(p1)[:c1]),
                             deque(list(p2)[:c2]))
        else:
            p1_won = c1 > c2
        if p1_won:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    return p1_won, p1 or p2


_, winner = game(deque(old_p1), deque(old_p2))
print(score(winner))
