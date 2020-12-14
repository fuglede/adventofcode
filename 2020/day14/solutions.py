from itertools import product
import re


with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

ns = [list(map(int, re.findall('-?\d+', x))) for x in ls]


def solve(part_one):
    mem = {}
    for nums, l in zip(ns, ls):
        if l[:4] == 'mask':
            mask = l.split()[2]
        else:
            loc, value = nums
            if part_one:
                s = list(bin(value)[2:].zfill(len(mask)))
                for j, m in enumerate(mask):
                    if m != 'X':
                        s[j] = m
                value = int(''.join(s), 2)
                mem[loc] = value
            else:  # Part 2
                s = list(bin(loc)[2:].zfill(len(mask)))
                for j, m in enumerate(mask):
                    if m != '0':
                        s[j] = m
                expanded = expand(s)
                for new_s in expanded:
                    loc = int(''.join(new_s), 2)
                    mem[loc] = value
    return sum(mem.values())


def expand(s):
    xs = [i for i, x in enumerate(s) if x == 'X']
    for rep in product(['0', '1'], repeat=len(xs)):
        new_s = list(s)
        for i, new_val in zip(xs, rep):
            new_s[i] = new_val
        yield new_s


# Part one
print(solve(True))

# Part one
print(solve(False))
