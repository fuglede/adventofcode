from collections import defaultdict
from itertools import count

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


def solve():
    for a in count():
        p = 0
        output = []
        regs = defaultdict(int)
        regs['a'] = a
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
            elif ins[0] == 'out':
                output.append(regs[ins[1]])
                if regs[ins[1]] != ((len(output) + 1) % 2):
                    break
                # We optimistically assume that 100 steps is enough that the pattern will continue
                if len(output) == 100:
                    return a
            p += 1
        a += 1


print(solve())
