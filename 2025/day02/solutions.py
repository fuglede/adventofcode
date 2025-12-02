with open("input") as f:
    data = f.read().strip()

res1 = res2 = 0

for l in data.split(","):
    start, end = l.split("-")
    for i in range(int(start), int(end) + 1):
        s = str(i)
        mid = len(s) // 2
        if len(s) % 2 == 0 and s[:mid] == s[mid:]:
            res1 += i
        if any(s == s[:l] * (len(s) // l) for l in range(1, mid + 1)):
            res2 += i

# Part 1
print(res1)

# Part 2
print(res2)
