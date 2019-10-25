from collections import deque


def is_empty(x, y):
    a = x*x + 3*x + 2*x*y + y + y*y
    a += 1362
    return bin(a).count('1') % 2 == 0


def surrounding(x, y):
    """Generates all locations that can be reached from the current location."""
    for dx in (-1, 1):
        if x + dx >= 0 and is_empty(x + dx, y):
            yield (x + dx, y)
    for dy in (-1, 1):
        if y + dy >= 0 and is_empty(x, y + dy):
            yield (x, y + dy)


def solve(part_one: bool):
    q = deque()
    q.append(((1, 1), 0))
    visited = {(1, 1)}
    length = 0
    while q:
        p, length = q.popleft()
        if part_one and p == (31, 39):
            return length
        if not part_one and length == 51:
            return len(visited)
        visited.add(p)
        for s in surrounding(*p):
            if s not in visited:
                q.append((s, length + 1))


print(solve(True))
print(solve(False))
