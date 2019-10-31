# Day 23, part 1
from collections import defaultdict


registers = defaultdict(int)
address = 0
muls = 0
with open('input') as f:
    commands = [x.strip() for x in f.readlines()]

while True:
    try:
        command = commands[address]
    except:
        break
    split = command.split()
    try:
        c, reg, val = split
    except:
        c, reg = split
    try:
        val = int(val)
    except:
        val = registers[val]
    if c == 'set':
        registers[reg] = val
    elif c == 'add':
        registers[reg] += val
    elif c == 'sub':
        registers[reg] -= val
    elif c == 'mul':
        muls += 1
        registers[reg] *= val
    elif c == 'int':
        print(registers[reg])
        break
    elif c == 'jnz':
        val1 = split[1]
        try:
            val1 = int(val1)
        except:
            val1 = registers[val1]
        if val1 != 0:
            address += val - 1
    address += 1
print(muls)


# Part two
# Manually decoding the program, one finds that it does nothing
# but calculate the number of composite numbers in np.arange(106700, 123700, 17)
def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


primes = 0
xs = range(106700, 123700, 17)
for x in xs:
    if is_prime(x):
        primes += 1
print(len(xs) - primes + 1)
