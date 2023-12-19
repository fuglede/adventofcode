import re
from itertools import product
from multiprocessing import Pool

import numpy
from numba import njit
from tqdm import tqdm

with open("input") as f:
    rules, parts = [g.split("\n") for g in f.read().strip().split("\n\n")]


@njit
def A(x, m, a, s):
    return x + m + a + s


@njit
def R(x, m, a, s):
    return 0


for l in rules:
    name, workflow = l.split("{")
    workflow = workflow[:-1].replace(":", ": return ")
    if name == "in":
        name = "_in"
    rule_parts = [f"{x}(x,m,a,s)" for x in workflow.split(",")]
    s = f"@njit\ndef {name}(x,m,a,s):\n"
    for i, part in enumerate(rule_parts):
        if i == 0:
            pre = "if "
        elif i == len(rule_parts) - 1:
            pre = "else: return "
        else:
            pre = "elif "
        s += f"    {pre}{part}\n"
    exec(s)

# Part 1
print(sum(eval(f"_in({g[1:-1]})") for g in parts))

# Part 2
split_points = {k: [1, 4001] for k in "xmas"}

for l in rules:
    for prop, op, val in re.findall(r"(\w+)(<|>)(\d+)", l):
        val = int(val) if op == "<" else int(val) + 1
        split_points[prop].append(val)

split_points = {k: sorted(v) for k, v in split_points.items()}
ranges = {
    k: numpy.array([(n1, n2 - n1) for n1, n2 in zip(v, v[1:])])
    for k, v in split_points.items()
}
rx, rm, ra, rs = [ranges[c] for c in "xmas"]


@njit
def num_accepted(x, m, a, s, nx, nm, na, ns):
    return nx * nm * na * ns * (_in(x, m, a, s) > 0)


@njit
def do_many_jit(x, nx):
    tot = 0
    for m, nm in rm:
        for a, na in ra:
            for s, ns in rs:
                tot += num_accepted(x, m, a, s, nx, nm, na, ns)
    return tot


# )
def do_many(xnx):
    return do_many_jit(*xnx)


with Pool() as p:
    print(sum(tqdm(p.imap(do_many, rx), total=len(rx))))
