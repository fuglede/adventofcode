with open('input') as f:
    ns = list(map(int, (x.strip() for x in f.readlines())))


def fuel(m):
    return m // 3 - 2


# Part one
print(sum(map(fuel, ns)))

# Part two
total = 0
for n in ns:
    while True:
        n = fuel(n)
        if n <= 0:
            break
        total += n
print(total)
