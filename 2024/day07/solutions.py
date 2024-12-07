from itertools import product
from operator import add, mul
import re

with open("input") as f:
    ns = [list(map(int, re.findall("\\d+", l))) for l in f.read().strip().split("\n")]


def solve(part2):
    worked = 0
    all_ops = [mul, add]
    if part2:
        all_ops.append(lambda a, b: int(str(a) + str(b)))
    for nums in ns:
        test, start, *rest = nums
        for ops in product(*[all_ops for _ in range(len(rest))]):
            res = start
            for num, op in zip(rest, ops):
                res = op(res, num)
            if res == test:
                worked += res
                break
    return worked


# Part 1
print(solve(False))

# Part 2
print(solve(True))
