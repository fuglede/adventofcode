with open("input") as f:
    ls = f.read().splitlines()

ranges = []
ingrs = []
for l in ls:
    if "-" in l:
        a, b = l.split("-")
        ranges.append([int(a), int(b)])
    elif l:
        ingrs.append(int(l))

# Part 1
print(sum(any(start <= i <= end for start, end in ranges) for i in ingrs))

# Part 2
# Merge ranges
ranges.sort()
merged = []
for start, end in ranges:
    if not merged or merged[-1][1] < start - 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
print(sum(end - start + 1 for start, end in merged))
