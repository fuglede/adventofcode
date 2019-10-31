import re

import numpy as np

with open('input') as f:
    ls = [x.strip().split() for x in f.readlines()]

ps_initial = []
vs_initial = []
As_initial = []
for l in ls:
    p, v, a = [list(map(int, re.findall('<(.+?)>', x)[0].split(','))) for x in l]
    ps_initial.append(np.array(p))
    vs_initial.append(np.array(v))
    As_initial.append(np.array(a))
ps = np.array(ps_initial)
vs = np.array(vs_initial)
As = np.array(As_initial)


def step(ps, vs, As):
    vs += As
    ps += vs


# Part one
# We simply let this run for a while without thinking too much about how
# long it's necessary to do this.
for _ in range(10000):
    step(ps, vs, As)

print(np.argmin(np.sum(np.abs(ps), 1)))

# Part two
ps = np.array(ps_initial)
vs = np.array(vs_initial)
As = np.array(As_initial)
for _ in range(10000):
    step(ps, vs, As)
    els, counts = np.unique(ps, axis=0, return_counts=True)
    dupes = els[np.where(counts != 1)]
    for l in dupes:
        indices = np.where(np.all(ps == l, axis=1))[0]
        ps = np.delete(ps, indices, axis=0)
        vs = np.delete(vs, indices, axis=0)
        As = np.delete(As, indices, axis=0)
print(len(ps))
