from functools import partial

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


def addr(a, b, c, l):
    l[c] = l[a] + l[b]


def addi(a, b, c, l):
    l[c] = l[a] + b


def mulr(a, b, c, l):
    l[c] = l[a] * l[b]


def muli(a, b, c, l):
    l[c] = l[a] * b


def banr(a, b, c, l):
    l[c] = l[a] & l[b]


def bani(a, b, c, l):
    l[c] = l[a] & b


def borr(a, b, c, l):
    l[c] = l[a] | l[b]


def bori(a, b, c, l):
    l[c] = l[a] | b


def setr(a, b, c, l):
    l[c] = l[a]


def seti(a, b, c, l):
    l[c] = a


def gtir(a, b, c, l):
    l[c] = int(a > l[b])


def gtri(a, b, c, l):
    l[c] = int(l[a] > b)


def gtrr(a, b, c, l):
    l[c] = int(l[a] > l[b])


def eqir(a, b, c, l):
    l[c] = int(a == l[b])


def eqri(a, b, c, l):
    l[c] = int(l[a] == b)


def eqrr(a, b, c, l):
    l[c] = int(l[a] == l[b])


# Part one
ip = int(lines[0][4])

commands = []
for line in lines[1:]:
    f, a, b, c = line.split()
    commands.append(partial(eval(f), int(a), int(b), int(c)))

regs = [0, 0, 0, 0, 0, 0]
while True:
    c = regs[ip]
    if c >= len(commands):
        break
    commands[c](regs)
    regs[ip] += 1
print(regs[0])

# Part two
# By investigating the values in the registers for part one whenever the
# first register changes its value, one realizes that the program sets
# some value into the second register, then calculates the sum of all
# of its divisors. In our case, that value is 10551315 but this will
# depend on the input.
print(sum(i for i in range(1, 10551316) if 10551315 % i == 0))
