import re


def spin(s, n):
    return s[-n:] + s[:-n]


def exchange(s, n, m):
    temp = s[:]
    temp[m] = s[n]
    temp[n] = s[m]
    return temp


def partner(s, a, b):
    temp = s[:]
    i = s.index(a)
    j = s.index(b)
    temp[i] = b
    temp[j] = a
    return temp


def parse(s, c):
    if c[0] == 's':
        n = int(c[1:])
        return spin(s, n)
    if c[0] == 'x':
        r = re.findall(r'(\d+)/(\d+)', c[1:])
        n = int(r[0][0])
        m = int(r[0][1])
        return exchange(s, n, m)
    if c[0] == 'p':
        r = re.findall(r'(\w+)/(\w+)', c[1:])
        n = r[0][0]
        m = r[0][1]
        return partner(s, n, m)


with open('input') as f:
    commands = f.read().strip().split(',')

# Part one
programs = list('abcdefghijklmnop')
for c in commands:
    programs = parse(programs, c)
print(''.join(programs))

# Part two
programs = list('abcdefghijklmnop')
k = 1
while True:
    for c in commands:
        programs = parse(programs, c)
    if ''.join(programs) == 'abcdefghijklmnop':
        break
    k += 1

programs = list('abcdefghijklmnop')
for _ in range(1000000000 % k):
    for c in commands:
        programs = parse(programs, c)

print(''.join(programs))
