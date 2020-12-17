from itertools import product

with open('input') as f:
    ls = [line.strip() for line in f.readlines()]


def extend_range(index, active):
    coords = [a[index] for a in active]
    return range(min(coords) - 1, max(coords) + 2)


ds = list(product((-1, 0, 1), repeat=4))
ds.remove((0, 0, 0, 0))


def solve(part_two):
    active = {(x, y, 0, 0)
              for x, l in enumerate(ls)
              for y, c in enumerate(l) if c == '#'}
    for _ in range(6):
        new_active = set()
        new = product(
            extend_range(0, active),
            extend_range(1, active),
            extend_range(2, active),
            extend_range(3, active) if part_two else [0]
        )
        for x, y, z, w in new:
            count = sum((x + dx, y + dy, z + dz, w + dw) in active
                        for dx, dy, dz, dw in ds)
            if (
                ((x, y, z, w) in active and count in (2, 3)) or
                ((x, y, z, w) not in active and count == 3)
            ):
                new_active.add((x, y, z, w))
        active = new_active
    return len(active)


# Part one
print(solve(False))

# Part one
print(solve(True))
