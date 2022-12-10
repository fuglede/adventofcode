with open("input") as f:
    ls = f.read().strip().split("\n")

xs = [1]
for l in ls:
    x = xs[-1]
    xs.append(x)
    if a := l[5:]:
        xs.append(x + int(a))

# Part 1
print(sum(i * xs[i - 1] for i in (20, 60, 100, 140, 180, 220)))

# Part 2
for i, x in enumerate(xs):
    print("█" if abs(i % 40 - x) <= 1 else " ", end="" if (i + 1) % 40 else "\n")
