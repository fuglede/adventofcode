from collections import deque

from scipy.optimize import curve_fit

with open("input") as f:
    ls = f.read().strip().split()

N = len(ls)
blocked = set()
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        if x == "S":
            start = i + 1j * j
        elif x == "#":
            blocked.add(i + 1j * j)


def counts():
    q = deque([(start, 0)])
    curr_dist = None
    evens = 1
    odds = 0
    seen = {start}
    while True:
        z, dist = q.popleft()
        if dist != curr_dist:
            curr_dist = dist
            yield (curr_dist, odds if curr_dist % 2 else evens)
        for dz in (-1, 1, -1j, 1j):
            w = z + dz
            w_mod_N = (w.real % N) + 1j * (w.imag % N)
            if w_mod_N in blocked or w in seen:
                continue
            seen.add(w)
            q.append((w, dist + 1))
            if dist % 2:
                evens += 1
            else:
                odds += 1


# For part 2, by looking at how the output of counts evolves for the test input,
# one quickly finds that it has behavior periodic with the size of the grid. By
# looking at the counts for each remainder, one finds that they are all quadratic
# polynomials after some initial noise. (This is easiest to see for the test input
# by looking at the counts that show up after all numbers of steps that are 0 mod 11.
# As such, we keep track of the counts for the residue class belong to our target,
# fit a quadratic polynomial, and once the predictions have stabilized for the
# actual input, we assume that we have the right answer.
def f(x, a, b, c):
    return a * x**2 + b * x + c


gen = counts()
to_hit = 26501365
period = N
preds = []
data = []
for i, num_locs in gen:
    # Part 1
    if i == 64:
        print(num_locs)
    # Part 2
    if i % period == to_hit % period:
        data.append((i, num_locs))
        if len(data) < 3:
            continue
        last_seen = data[-3:]
        fa, fb, fc = curve_fit(f, *zip(*last_seen))[0]
        pred = round(f(to_hit, fa, fb, fc))
        preds.append(pred)
        # We assume that we have converged if the same prediction shows up
        # three times in a row
        if len(preds) > 3 and len(set(preds[-3:])) == 1:
            print(preds[-1])
            break
