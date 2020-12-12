with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

data = [(line[0], int(line[1:])) for line in ls]
dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
rot = {'L': 1j, 'R': -1j}


# Part one
loc = 0
d = 1
for a, value in data:
    if a in dirs:
        loc += dirs[a] * value
    elif a in rot:
        d *= rot[a] ** (value/90)
    else:
        loc += d * value

print(abs(loc.real) + abs(loc.imag))

# Part two
loc = 0
waypoint = 10 + 1j
for a, value in data:
    if a in dirs:
        waypoint += dirs[a] * value
    elif a in rot:
        waypoint *= rot[a] ** (value/90)
    else:
        loc += waypoint * value

print(abs(loc.real) + abs(loc.imag))
