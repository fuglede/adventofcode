with open("input") as f:
    ls = f.readlines()


# Part one
depth = hor = 0

for l in ls:
    command, x = l.split()
    x = int(x)
    if command == "forward":
        hor += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x

print(hor * depth)

# Part two
depth = hor = aim = 0

for l in ls:
    command, x = l.split()
    x = int(x)
    if command == "forward":
        hor += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x

print(hor * depth)
