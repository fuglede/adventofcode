from itertools import combinations
from operator import and_, or_, xor

import networkx as nx
from z3 import BitVec, Extract, Solver, sat, unsat

with open("input") as f:
    gs = [g.split("\n") for g in f.read().strip().split("\n\n")]

# Part 1
# Complete hack: Convert the input to Python, then execute it.
for line in gs[0]:
    l = line.split(": ")
    exec(f"def {l[0]}(): return {int(l[1])}")

str_to_op = {"AND": "and", "XOR": "^", "OR": "or"}
for line in gs[1]:
    l = line.split()
    exec(f"def {l[4]}(): return {l[0]}() {str_to_op[l[1]]} {l[2]}()")

print(sum(eval(f"z{i:02}()") * 2**i for i in range(46)))

# Part 2
# For later, it will be convenient to track the distance from a broken
# register, so we will set up a graph for that purpose.
G = nx.Graph()

# The plan is to fix the circuit by identifying bits of z that are broken
# one at a time. We will use Z3 to decide whether there exists inputs x, y, z
# such that x + y = z, with gates doing what they are supposed to, but such
# that the j'th bit of z is different from the value in the register z{j}.
# Once such a bit is found, we will try all swaps of the target registers
# until the bit is fixed.
x = BitVec("x", 46)
y = BitVec("y", 46)
z = BitVec("z", 46)

regs = {l.split()[4] for l in gs[1]}
var_by_name = {reg: BitVec(reg, 1) for reg in regs}
var_by_name |= {f"x{i:02}": Extract(i, i, x) for i in range(46)}
var_by_name |= {f"y{i:02}": Extract(i, i, y) for i in range(46)}

# Create all left hand sides once and for all, but keep the targets separate,
# so we can swap them later.
lhs = []
targets = []
str_to_op = {"AND": and_, "OR": or_, "XOR": xor}

for line in gs[1]:
    l = line.split()
    G.add_edge(l[4], l[0])
    G.add_edge(l[4], l[2])
    lhs.append(str_to_op[l[1]](var_by_name[l[0]], var_by_name[l[2]]))
    targets.append(var_by_name[l[4]])


def check(bit, swapped_targets):
    # Is it possible to construct inputs x, y, and z such that x + y = z, and such that
    # all gates do what they are supposed to, such that the first j - 1 bits of z match
    # those of the corresponding z registers, but still the value of the j'th bit
    # of z is different from the value in the register z{j}?
    s = Solver()
    s.add(x + y == z)
    for v, t in zip(lhs, swapped_targets):
        s.add(v == t)
    for i in range(bit):
        s.add(Extract(i, i, z) == var_by_name[f"z{i:02}"])
    s.add(Extract(bit, bit, z) != var_by_name[f"z{bit:02}"])
    return s.check()


fixes = set()
for bit in range(45):
    # Is there an error on bit j?
    if check(bit, targets) == sat:
        # Try all swaps. Favor changes that are closer to the broken bit; this isn't
        # strictly necessary but does speed the whole thing up a lot.
        regs_by_dist = [t for l in nx.bfs_layers(G, f"z{bit:02}") for t in l if t in regs]
        for s1, s2 in combinations(regs_by_dist, 2):
            t1 = var_by_name[s1]
            t2 = var_by_name[s2]
            swapped_targets = [t2 if t == t1 else t1 if t == t2 else t for t in targets]
            if check(bit, swapped_targets) == unsat:
                # Swapping s1 and s2 did the job. Keep the swapped targets.
                fixes |= {s1, s2}
                targets = swapped_targets
                break

print(",".join(sorted(fixes)))
