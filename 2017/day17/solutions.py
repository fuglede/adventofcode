# Part one
l = [0]
i = 1
n = 369
head = 0
for _ in range(2017):
    head += n
    head %= len(l)
    l.insert(head + 1, i)
    head += 1
    i += 1
print(l[l.index(2017) + 1])

# Part two
i = 1
res = 0
n = 369
head = 0
for k in range(50000000):
    head += n
    head %= i
    if head == 0:
        res = i
    head += 1
    i += 1
print(res)
