from collections import Counter, defaultdict

with open("input") as f:
    data = f.read().strip()

top, bottom = data.split("\n\n")
rules = {}
for l in bottom.split("\n"):
    (a, b), right = l.split(" -> ")
    rules[(a, b)] = right

# Part one
s = top
for j in range(10):
    new_s = s[0]
    for a, b in zip(s, s[1:]):
        new_s += rules[(a, b)] + b
    s = new_s

counts = Counter(s).values()
print(max(counts) - min(counts))

# Part two
pair_counts = Counter(zip(top, top[1:]))
for _ in range(40):
    new_pair_counts = defaultdict(int)
    for a, b in pair_counts:
        insert = rules[(a, b)]
        new_pair_counts[(a, insert)] += pair_counts[(a, b)]
        new_pair_counts[(insert, b)] += pair_counts[(a, b)]
    pair_counts = new_pair_counts

letter_counts = defaultdict(int, {top[0]: 1})
for (_, letter), count in pair_counts.items():
    letter_counts[letter] += count

counts = letter_counts.values()
print(max(counts) - min(counts))
