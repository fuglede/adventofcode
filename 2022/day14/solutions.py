with open("input") as f:
    ls = f.read().strip().split("\n")

rocks = set()
for l in ls:
    points = [list(map(int, p.split(","))) for p in l.split(" -> ")]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                rocks.add(x + y * 1j)


def solve(part1: bool):
    blocked = set(rocks)
    while True:
        z = 500
        while True:
            below_all = z.imag == maxy + 1
            if part1 and below_all:
                return len(blocked) - len(rocks)
            for dz in (1j, -1 + 1j, 1 + 1j):
                if (w := z + dz) not in blocked and not below_all:
                    z = w
                    break
            else:
                blocked.add(z)
                if z == 500:
                    return len(blocked) - len(rocks)
                break


# Part 1
print(solve(True))

# Part 2
print(solve(False))
