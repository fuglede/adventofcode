with open('input') as f:
    ns = [int(line) for line in f.readlines()]

# Part one
for i, n in enumerate(ns):
    if i < 25:
        continue
    prev = ns[i-25:i]
    if not any(n == n1 + n2 for n1 in prev for n2 in prev):
        print(n)
        break

# Part two
for size in range(2, len(ns)):
    for i in range(len(ns) - size):
        s = ns[i:i+size]
        if sum(s) == n:
            print(min(s) + max(s))
