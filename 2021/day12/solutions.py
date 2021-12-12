from collections import defaultdict

with open("input") as f:
    ls = f.read().strip().split("\n")

neighbours = defaultdict(set)
for l in ls:
    a, b = l.split("-")
    neighbours[a].add(b)
    neighbours[b].add(a)


def count_paths(u, seen, allow_double):
    if u == "end":
        return 1
    elif u.islower() and u in seen:
        if u == "start" or not allow_double:
            return 0
        allow_double = False
    return sum(count_paths(v, seen | {u}, allow_double) for v in neighbours[u])


# Part one
print(count_paths("start", set(), False))

# Part two
print(count_paths("start", set(), True))
