# Day 8, parts 1+2
from collections import defaultdict


regs = defaultdict(int)
with open('input') as f:
    insts = [x.strip().split() for x in f.readlines()]
max_held = 0
for parts in insts:
    dep_reg = parts[4]
    cond = eval(str(regs[dep_reg]) + str.join(' ', parts[5:7]))
    if cond:
        if parts[1] == 'inc':
            regs[parts[0]] += int(parts[2])
        else:
            regs[parts[0]] -= int(parts[2])
        if regs[parts[0]] > max_held:
            max_held = regs[parts[0]]

# Part one
print(max(regs.values()))

# Part two
print(max_held)
