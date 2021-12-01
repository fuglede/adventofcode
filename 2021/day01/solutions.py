with open("input") as f:
    ns = list(map(int, (x.strip() for x in f.readlines())))


# Part one
print(sum(n1 < n2 for n1, n2 in zip(ns, ns[1:])))

# Part two
# Note that a + b + c < b + c + d iff a < d
print(sum(n1 < n2 for n1, n2 in zip(ns, ns[3:])))
