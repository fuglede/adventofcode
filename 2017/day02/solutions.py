with open(r'input') as f:
    ns = [[int(n) for n in x.strip().split()] for x in f.readlines()]

# Part one
print(sum(max(l) - min(l) for l in ns))

# Part two
s = 0
for l in ns:
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] % l[j] == 0:
                s += l[i] // l[j]
print(s)
