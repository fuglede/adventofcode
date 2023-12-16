with open("input") as f:
    ls = f.read().strip().split("\n")

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}


def energized(entry, d):
    q = [(entry - d, d)]
    seen = set()
    while q:
        z, d = q.pop()
        if (z, d) in seen:
            continue
        seen.add((z, d))
        newz = z + d
        if newz not in board:
            continue
        match board[newz]:
            case "|" if d.imag:
                new_dir = [1, -1]
            case "-" if d.real:
                new_dir = [1j, -1j]
            case "/":
                new_dir = [(d * 1j).conjugate()]
            case "\\":
                new_dir = [(d * -1j).conjugate()]
            case _:
                new_dir = [d]
        q += [(newz, newd) for newd in new_dir]
    return len({x[0] for x in seen}) - 1


# Part 1
print(energized(0, 1j))

# Part 2
N, M = len(ls), len(ls[0])
entries = [(i, 1j) for i in range(N)]
entries += [(i + (M - 1) * 1j, -1j) for i in range(N)]
entries += [(i * 1j, 1) for i in range(M)]
entries += [(N - 1 + i * 1j, -1) for i in range(M)]
print(max(energized(*x) for x in entries))
