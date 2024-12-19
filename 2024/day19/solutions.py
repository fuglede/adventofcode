from functools import cache


with open("input") as f:
    ls = f.read().strip().split("\n")

stripes, _, *patterns = ls
stripes = stripes.split(", ")


@cache
def is_possible(pattern, op):
    return not pattern or op(
        is_possible(pattern[len(stripe) :], op)
        for stripe in stripes
        if pattern.startswith(stripe)
    )


# Part 1 + 2
for op in any, sum:
    print(sum(is_possible(pattern, op) for pattern in patterns))
