from collections import defaultdict
import re

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ns = [[int(x) for x in re.findall(r'\d+', s)] for s in lines]


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


all_ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

ins = ns[:3043:4]
ops = ns[1:3043:4]
outs = ns[2:3043:4]


def possible_ops(i, op, o):
    ops = set()
    for t in all_ops:
        copy = list(i)
        t(op[1], op[2], op[3], copy)
        if copy == o:
            ops.add(t)
    return ops


# Part one
print(sum(len(possible_ops(*v)) >= 3 for v in zip(ins, ops, outs)))

# Part two
ops_by_number = {}
could_be = defaultdict(set)

for i, op, o in zip(ins, ops, outs):
    res = possible_ops(i, op, o)
    could_be[op[0]] = could_be[op[0]].union(res)

while len(ops_by_number) != 16:
    for (k, v) in could_be.items():
        if len(v) == 1:
            ops_by_number[k] = new = v.pop()
            for vals in could_be.values():
                vals.discard(new)

program = ns[3046:]
regs = [0, 0, 0, 0]
for o in program:
    ops_by_number[o[0]](o[1], o[2], o[3], regs)
print(regs[0])
