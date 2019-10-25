from collections import defaultdict

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


def run(regs):
    p = 0
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
            if val != 0:
                p += ins[2] - 1
        p += 1


regs = defaultdict(int)
print(run(regs))

regs = defaultdict(int)
regs['c'] = 1
print(run(regs))
