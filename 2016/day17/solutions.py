from collections import deque
import hashlib


def md5_first_four(s):
    return hashlib.md5(s.encode()).hexdigest()[:4]


def get_available(loc):
    s, x, y = loc
    if x == 4 and y == 4:
        return
    for i, c in enumerate(md5_first_four(s)):
        if c in {'b', 'c', 'd', 'e', 'f'}:
            if i == 0 and y != 1:
                yield (s + 'U', x, y - 1)
            elif i == 1 and y != 4:
                yield (s + 'D', x, y + 1)
            elif i == 2 and x != 1:
                yield (s + 'L', x - 1, y)
            elif i == 3 and x != 4:
                yield (s + 'R', x + 1, y)


def solve(inp, part_one):
    q = deque()
    root = (inp, 1, 1)
    q.append(root)
    visited = set()
    longest = 0
    while q:
        loc = q.popleft()
        if loc[1] == 4 and loc[2] == 4:
            if part_one:
                return loc[0][len(inp):]
            else:
                longest = max(longest, len(loc[0]) - len(inp))
        for new_loc in get_available(loc):
            if new_loc[0] not in visited:
                visited.add(new_loc[0])
                q.append(new_loc)
    return longest


inp = 'awrkjxxr'
print(solve(inp, True))
print(solve(inp, False))
