with open('input') as f:
    lines = [l.strip() for l in f.readlines()]

# Part one
t = 0
for l in lines:
    t += 2
    escaped = False
    for s in l:
        if not escaped and s == '\\':
            escaped = True
        elif escaped:
            if s == '\\' or s == '"':
                t += 1
            elif s == 'x':
                t += 3
            escaped = False
print(t)

# Part two
t = 0
for l in lines:
    t += 2
    for s in l:
        if s == '\\' or s == '"':
            t += 1
print(t)
