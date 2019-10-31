with open('input') as f:
    n = f.read().strip()

# Part one
print(sum(int(n[i]) for i in range(len(n)) if n[i] == n[(i + 1) % len(n)]))

# Part two
print(sum(int(n[i]) for i in range(len(n)) if n[i] == n[(i + len(n) // 2) % len(n)]))
