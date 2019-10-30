from collections import defaultdict

with open('input') as f:
    lines = [l.strip().replace(',', '').split() for l in f.readlines()]


def run(regs):
    p = 0
    while True:
        if p >= len(lines):
            return regs['b']
        ins = lines[p]
        if ins[0] == 'inc':
            regs[ins[1]] += 1
        elif ins[0] == 'tpl':
            regs[ins[1]] *= 3
        elif ins[0] == 'hlf':
            regs[ins[1]] //= 2
        elif ins[0] == 'jmp':
            p += int(ins[1]) - 1
        elif ins[0] == 'jie':
            if regs[ins[1]] % 2 == 0:
                p += int(ins[2]) - 1
        elif ins[0] == 'jio':
            if regs[ins[1]] == 1:
                p += int(ins[2]) - 1
        p += 1


# Part one
regs = defaultdict(int)
print(run(regs))

# Part two
regs = defaultdict(int)
regs['a'] = 1
print(run(regs))
