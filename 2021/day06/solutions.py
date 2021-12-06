from collections import Counter

with open("input") as f:
    counts = Counter(map(int, f.read().strip().split(",")))


for i in range(256):
    counts[(i + 7) % 9] += counts[i % 9]
    if i + 1 in (80, 256):
        print(sum(counts.values()))
