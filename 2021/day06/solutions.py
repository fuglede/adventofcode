with open("input") as f:
    counts = list(map(f.read().count, "012345678"))


for i in range(256):
    counts[(i + 7) % 9] += counts[i % 9]
    if i + 1 in (80, 256):
        print(sum(counts))
