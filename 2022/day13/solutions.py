with open("input") as f:
    data = f.read().strip()


def cmp(a, b):
    """Returns 1 of a > b, -1 if a < b, 0 if a == b"""
    match a, b:
        case int(), int():
            return (a > b) - (a < b)
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            return next(filter(bool, map(cmp, a, b)), cmp(len(a), len(b)))


pairs = [[*map(eval, pair.split())] for pair in data.split("\n\n")]

# Part 1
print(sum(i for i, pair in enumerate(pairs, 1) if cmp(*pair) == -1))


# Part 2
def count_le(packet):
    return sum(cmp(packet, x) == 1 for pair in pairs for x in pair) + 1


print(count_le([[2]]) * (count_le([[6]]) + 1))
