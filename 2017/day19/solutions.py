with open('input') as f:
    pipes = [x[:-2] for x in f.readlines()]

i = 0
j = pipes[0].index('|')
c = '|'
d = 'd'
steps = 0
route = []

while c != ' ':
    steps += 1
    if c == '|' or c == '-':
        pass
    elif c == '+':
        if d == 'd' or d == 'u':
            d = 'l' if pipes[i][j-1] != ' ' else 'r'
        else:
            d = 'u' if pipes[i-1][j] != ' ' else 'd'
    else:
        route.append(c)
    if d == 'd':
        i += 1
    elif d == 'u':
        i -= 1
    elif d == 'r':
        j += 1
    elif d == 'l':
        j -= 1
    c = pipes[i][j]

# Part one
print(''.join(route))

# Part two
print(steps)
