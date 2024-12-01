from collections import Counter

with open("input") as f:
    ls = f.read().strip().split("\n")

l1, l2 = zip(*[map(int, x.split()) for x in ls])

# Part 1
print(sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2))))

# Part 2
cs = Counter(l2)
print(sum(x * cs[x] for x in l1))
