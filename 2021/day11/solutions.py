from itertools import count, product

with open("input") as f:
    ls = f.read().strip().split("\n")

board = {x + 1j * y: int(ls[x][y]) for (x, y) in product(range(10), repeat=2)}
dirs = {z for (x, y) in product((-1, 0, 1), repeat=2) if (z := x + y * 1j)}
adjacent = {w: {w + z for z in dirs} & set(board) for w in board}


def step(level):
    for w in level:
        level[w] += 1
    flashed = set()
    while True:
        flashing = {w for w, l in level.items() if l > 9} - flashed
        if not flashing:
            for w in flashed:
                level[w] = 0
            return len(flashed)
        flashed |= flashing
        for w in flashing:
            for z in adjacent[w]:
                level[z] += 1


# Part one
level = dict(board)
print(sum(step(level) for _ in range(100)))

# Part two
level = dict(board)
print(next(i for i in count(1) if step(level) == 100))
