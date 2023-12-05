from functools import reduce
from itertools import count

with open("input") as f:
    data = f.read().strip()

seed_line, *maps = data.split("\n\n")
seeds = list(map(int, seed_line.split(":")[1].split()))

fs = []
finvs = []
for m in maps:
    ns = [list(map(int, l.split())) for l in m.split("\n")[1:]]

    def f(x, ns=ns):
        return next(
            (
                target + x - source
                for target, source, n in ns
                if source <= x < source + n
            ),
            x,
        )

    def finv(x, ns=ns):
        return next(
            (
                target + x - source
                for source, target, n in ns
                if source <= x < source + n
            ),
            x,
        )

    fs.append(f)
    finvs.append(finv)


def compose(*F):
    return reduce(lambda f, g: lambda x: f(g(x)), F)


# Part 1
print(min(map(compose(*fs[::-1]), seeds)))


# Part 2
def is_needed(n):
    return any(x <= n < x + y for x, y in zip(seeds[::2], seeds[1::2]))


is_seed_loc = compose(is_needed, compose(*finvs))
print(next(filter(is_seed_loc, count())))
