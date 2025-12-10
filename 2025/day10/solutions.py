"""
The solution below is really one in which the solution for part 2 has been
retroactively applied to part 1 as well, simply because it was a fun thing to do.

Really, part 1 is likely always best solved by a combinatorial/path based solution like
(bidirectional) BFS or an SAT/SMT solver like Z3, whereas part 2 is very naturally
expressed as an integer linear program.

The solution below takes that part 2 solution, and extends it by also formulating
part 1 as an integer linear program. Here's how that works: In both parts, we want to
solve a linear equation 𝐴𝑥 = 𝑏 such that 𝑥 is minimal in some sense. In part 1, we
are solving over 𝔽₂ = {0, 1} and require that 𝑥 has minimal Hamming weight, and in
part 2, we require that 𝑥 consists of positive integers and has minimal sum. Integer
programming solvers like the HiGHS-based solver in SciPy that we use below like
integers better but can be forced to work over the binaries by adding additional
variables. Concretely, for part 1, instead of solving 𝐴𝑥 = 𝑏 over 𝔽₂, we instead
allow 𝑥 to be an integer, and introduce new integer variables 𝑡 and solve
𝐴𝑥 − 2𝑡 = 𝑏, still just minimizing the sum of 𝑥. This works because 2𝑡 vanishes over
𝔽₂, and because any optimal integer solution will values of 𝑥 in {0, 1}. In other
words, to solve part 1, we take our part 2 solution and simply add a handful of useful
auxiliary variables to encode the fact that the matrix equation is now modulo 2.

While we're at it, note that part 1 is actually the well-known “syndrome decoding”
problem, also known as “maximum-likelihood decoding”.
"""

import numpy as np
from scipy.optimize import linprog


with open("input") as f:
    ls = f.read().strip().split("\n")

tasks = []
for l in ls:
    toggles, *buttons, counters = l.split()
    toggles = [x == "#" for x in toggles[1:-1]]
    moves = [set(map(int, b[1:-1].split(","))) for b in buttons]
    counters = list(map(int, counters[1:-1].split(",")))
    tasks.append((toggles, moves, counters))


def solve(goal, moves, part1):
    n, m = len(moves), len(goal)
    c = [1] * n
    A_eq = [[i in move for move in moves] for i in range(m)]
    bounds = [(0, None)] * n
    if part1:
        c += [0] * m
        A_eq = np.hstack([A_eq, -2 * np.eye(m)])
        bounds += [(None, None)] * m
    return linprog(c, A_eq=A_eq, b_eq=goal, bounds=bounds, integrality=True).fun


# Part 1
print(sum(solve(goal, moves, True) for goal, moves, _ in tasks))

# Part 2
print(sum(solve(goal, moves, False) for _, moves, goal in tasks))
