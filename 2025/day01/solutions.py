with open("input") as f:
    ls = f.read().strip().split("\n")

# Part 1
dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    dial += move if d == "R" else -move
    dial %= 100
    s += dial == 0
print(s)

# Part 2
dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    for _ in range(move):
        dial += 1 if d == "R" else -1
        dial %= 100
        s += dial == 0
print(s)
