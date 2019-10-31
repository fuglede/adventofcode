# Part one
state_a = 116
state_b = 299
total = 0
for _ in range(40000000):
    state_a = state_a * 16807 % 2147483647
    state_b = state_b * 48271 % 2147483647
    if (state_a % 2**16) == (state_b % 2**16):
        total += 1
print(total)

# Part two
total = 0
state_a = 116
state_b = 299
matches_a = []
matches_b = []
while True:
    state_a = state_a * 16807 % 2147483647
    state_b = state_b * 48271 % 2147483647
    if state_a % 4 == 0:
        matches_a.append(state_a)
    if state_b % 8 == 0:
        matches_b.append(state_b)
    if len(matches_a) >= 5000000 and len(matches_b) >= 5000000:
        break
for i in range(5000000):
    if (matches_a[i] % 2**16) == (matches_b[i] % 2**16):
        total += 1
print(total)
