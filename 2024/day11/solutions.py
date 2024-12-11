from collections import Counter

with open("input") as f:
    stones = Counter(map(int, f.read().split()))

for blinks in range(1, 76):
    new_stones = Counter()
    for n, num_stone in stones.items():
        if n == 0:
            new_stones[1] += num_stone
        elif len(s := str(n)) % 2 == 0:
            for m in int(s[: len(s) // 2]), int(s[len(s) // 2 :]):
                new_stones[m] += num_stone
        else:
            new_stones[2024 * n] += num_stone
    stones = new_stones
    if blinks in (25, 75):
        print(sum(new_stones.values()))
