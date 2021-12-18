from functools import reduce
from itertools import product
from math import prod

with open("input") as f:
    ls = f.read().strip().split("\n")


# There are quite a few possible representations for this one. My original
# solution just treated the entire thing as a string and performed all
# transformations as replacements on a string. Really what we're looking at is
# a binary tree on which we want to perform a set of mostly local
# transformations. A simple way to work with those is to just treat each node
# as a Python object, with appropriate lookups from parents to/from children,
# but the "explode" action still becomes rather annoying, and easiest to handle
# by in-order traversal of the tree. Note also that we only really care about
# the values of the leaves in the tree.
# Here, what we do is use the standard 1-indexed array representation on the
# tree; vertices are indexed through
#         1
#     2       3
#   4   5   6   7
# We only need leaves, and only some of them, so we use a Python dict to work
# with the tree. This has some nice properties:
#  - The children of a node has index 2*i, 2*i+1 where i is the index of the
#    parent.
#  - The parent of a node has index i//2 where i is the index of the child.
#  - Using Python's bin to generate binary representations of each index,
#    iterating over nodes in increasing bin-order is the same as in-order
#    traversal.
#  - In the binary representation from bin, the length of the string is the
#    depth of a given node, while the remaining digits indicate whether we
#    are moving left or right in the tree, so adding two trees amounts to
#    replacing the outermost 1 with 10 and 11 for the left and right parts
#    respectively.
def make_dict(x, d=None, index=1):
    if d is None:
        d = {}
    if isinstance(x, int):
        d[index] = x
    else:
        make_dict(x[0], d, 2 * index)
        make_dict(x[1], d, 2 * index + 1)
    return d


def action(d):
    keys = sorted(d, key=bin)
    first, *_, last = keys
    # Explode
    for i in range(len(keys)):
        if keys[i] >= 32:
            k1, k2 = keys[i : i + 2]
            if k1 != first:
                d[keys[i - 1]] += d[k1]
            if k2 != last:
                d[keys[i + 2]] += d[k2]
            del d[k1]
            del d[k2]
            d[k1 // 2] = 0
            return True
    # Split
    for k in keys:
        v = d[k]
        if v >= 10:
            d[2 * k] = v // 2
            d[2 * k + 1] = v - v // 2
            del d[k]
            return True
    return False


def simplify(d):
    while action(d):
        pass
    return d


def add(d1, d2):
    return simplify(
        {int("10" + bin(k)[3:], 2): v for k, v in d1.items()}
        | {int("11" + bin(k)[3:], 2): v for k, v in d2.items()}
    )


def magnitude(d):
    return sum(v * prod(3 - int(digit) for digit in bin(k)[3:]) for k, v in d.items())


# Part one
dicts = list(map(make_dict, map(eval, ls)))
print(magnitude(reduce(add, dicts)))

# Part two
print(max(magnitude(add(d1, d2)) for d1, d2 in product(dicts, dicts) if d1 != d2))
