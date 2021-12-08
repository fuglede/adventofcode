from itertools import groupby

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

with open("input") as f:
    ls = f.read().strip().split("\n")

# Part one
print(
    sum(len(word) in (2, 3, 4, 7) for l in ls for word in l.split(" | ")[1].split(" "))
)

# Part two
a_g = "abcdefg"
digits = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}
# We will use the word length to narrow down possibilities, so first group the
# dictionary keys above by their length.
with_length = {k: set.intersection(*map(set, v)) for k, v in groupby(digits, len)}


def deduce(left):
    # Map each letter to its possible segment. To begin with, any segment is possible,
    # and we will slowly narrow down the possibilities.
    possible = {x: set(a_g) for x in a_g}
    for word in left:
        # Use the word length to limit the possible segments for each letter.
        for letter in with_length[len(word)]:
            possible[letter] &= set(word)
    # At this point we might still have letters with multiple possible segments, but
    # the challenge tells us that there's a unique solution, so we simply pick a
    # matching in the bipartite graph mapping letters to segments.
    graph = csr_matrix([[x in possible[y] for x in a_g] for y in a_g])
    matching = maximum_bipartite_matching(graph)
    return {a_g[i]: a_g[m] for i, m in enumerate(matching)}


def make_num(right, wmap):
    return int("".join(str(digits["".join(sorted(wmap[x] for x in w))]) for w in right))


s = 0
for l in ls:
    left, right = l.split(" | ")
    wmap = deduce(left.split(" "))
    s += make_num(right.split(" "), wmap)
print(s)
