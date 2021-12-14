from collections import Counter, defaultdict

with open("input") as f:
    data = f.read().strip()

top, bottom = data.split("\n\n")
rules = {}
for l in bottom.split("\n"):
    left, right = l.split(" -> ")
    rules[left] = right

# Part one
s = top
for j in range(10):
    new_s = s[0]
    for i in range(len(s) - 1):
        new_s += rules[s[i : i + 2]] + s[i + 1]
    s = new_s

counts = Counter(s).values()
print(max(counts) - min(counts))

# Part two
pair_counts = Counter(top[i : i + 2] for i in range(len(top) - 1))
for _ in range(40):
    new_pair_counts = defaultdict(int)
    for pair in pair_counts:
        insert = rules[pair]
        new_pair_counts[pair[0] + insert] += pair_counts[pair]
        new_pair_counts[insert + pair[1]] += pair_counts[pair]
    pair_counts = new_pair_counts
letter_counts = defaultdict(int)
for (letter, _), count in pair_counts.items():
    letter_counts[letter] += count
letter_counts[top[-1]] += 1
counts = letter_counts.values()
print(max(counts) - min(counts))
