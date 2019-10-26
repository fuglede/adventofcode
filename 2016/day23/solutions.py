from collections import defaultdict
from math import factorial


with open('input') as f:
    lines = [l.strip().split() for l in f.readlines()]
for l in lines:
    try:
        l[1] = int(l[1])
    except:
        pass
    try:
        l[2] = int(l[2])
    except:
        pass


def run(regs, p=0):
    old_b = 0
    while True:
        if p >= len(lines):
            return regs['a']
        ins = lines[p]
        if ins[0] == 'cpy':
            regs[ins[2]] = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
        elif ins[0] == 'inc':
            regs[ins[1]] += 1
        elif ins[0] == 'dec':
            regs[ins[1]] -= 1
        elif ins[0] == 'jnz':
            val = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
            skip = ins[2] if isinstance(ins[2], int) else regs[ins[2]]
            if val != 0:
                p += skip - 1
        elif ins[0] == 'tgl':
            to_change = p + regs[ins[1]]
            if to_change < len(lines):
                l = lines[to_change]
                if len(l) == 2:
                    if l[0] == 'inc':
                        l[0] = 'dec'
                    else:
                        l[0] = 'inc'
                if len(l) == 3:
                    if l[0] == 'jnz':
                        if not isinstance(l[2], int):
                            l[0] = 'cpy'
                    else:
                        l[0] = 'jnz'

        p += 1


# Part one
regs = defaultdict(int)
regs['a'] = 7
print(run(regs))

# Part two
# By watching the values of the registers whenever the value of regs['b']
# changes, it becomes apparent that the output above is 7!, but with an
# added value of regs['d'] * regs['c'] once regs['d'] is set again, in
# my case, 7! + 91 * 73. The exact same values of regs['c'] and regs['d']
# will be used in the case, where regs['a'] starts out being 12.
print(factorial(12) + 91 * 73)
