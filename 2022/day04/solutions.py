import re

with open("input") as f:
    ls = f.readlines()

ns = [list(map(int, re.findall("\d+", x))) for x in ls]
ranges = [(set(range(n1, n2 + 1)), set(range(n3, n4 + 1))) for n1, n2, n3, n4 in ns]

# Part 1
print(sum(s1 <= s2 or s2 <= s1 for s1, s2 in ranges))

# Part 2
print(sum(not s1.isdisjoint(s2) for s1, s2 in ranges))
