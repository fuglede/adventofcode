from collections import defaultdict
from math import lcm, prod

# We manually include our input; it's small enough
# that that's much easier than writing something to
# parse it.
ops = [
    lambda l: l * 13,
    lambda l: l + 2,
    lambda l: l + 1,
    lambda l: l + 8,
    lambda l: l * l,
    lambda l: l + 4,
    lambda l: l * 17,
    lambda l: l + 5,
]
divs = [19, 3, 11, 17, 5, 2, 13, 7]
if_trues = [2, 4, 7, 6, 0, 2, 4, 3]
if_falses = [7, 5, 3, 1, 5, 0, 1, 6]


def solve(num_rounds, part1):
    monkeys = [
        [75, 75, 98, 97, 79, 97, 64],
        [50, 99, 80, 84, 65, 95],
        [96, 74, 68, 96, 56, 71, 75, 53],
        [83, 96, 86, 58, 92],
        [99],
        [60, 54, 83],
        [77, 67],
        [95, 65, 58, 76],
    ]
    i = 0
    # The lcm below could have just been prod; all elements in
    # `divs` are prime, so it comes out as the same thing.
    # For part 1, it's unnecessary entirely, but it helps keep
    # the numbers small for part 2.
    lcm_divs = lcm(*divs)
    inspected = defaultdict(int)
    for _ in range(num_rounds):
        for i, (monkey, op, div, if_true, if_false) in enumerate(
            zip(monkeys, ops, divs, if_trues, if_falses)
        ):
            while monkey:
                item = monkey.pop()
                inspected[i] += 1
                new = op(item) % lcm_divs
                if part1:
                    new //= 3
                monkeys[if_false if new % div else if_true].append(new)
    return prod(sorted(inspected.values())[-2:])


# Part 1
print(solve(20, True))

# Part 2
print(solve(10_000, False))
