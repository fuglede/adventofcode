import re

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("\\d+", x))) for x in ls]


def safe1(levels):
    return all(1 <= abs(n1 - n2) <= 3 for n1, n2 in zip(levels, levels[1:])) and (
        levels == sorted(levels) or levels == sorted(levels)[::-1]
    )


def safe2(levels):
    return any(safe1(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))


# Part 1
print(sum(safe1(levels) for levels in ns))

# Part 2
print(sum(safe2(levels) for levels in ns))
