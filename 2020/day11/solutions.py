from collections import defaultdict
from itertools import count, product


with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

state = {}
floor = set()
for row, line in enumerate(ls):
    for col, char in enumerate(line):
        z = row+col*1j
        if char == 'L':
            state[z] = False  # False = empty, True = occupied
        else:
            floor.add(z)

dirs = {z for (x, y) in product((-1, 0, 1), repeat=2) if (z := x+y*1j)}


def equilibrium(state, adjacent, limit):
    prev_num_occupied = None
    while (num_occupied := sum(state.values())) != prev_num_occupied:
        new_state = {}
        for z, v in state.items():
            adj = [state[a] for a in adjacent[z]]
            new_state[z] = sum(adj) < limit if v else not any(adj)
        prev_num_occupied = num_occupied
        state = new_state
    return num_occupied


# Part 1
adjacent = {z: [w for d in dirs if (w := z + d) in state] for z in state}
print(equilibrium(state, adjacent, 4))

# Part 2
adjacent = {z: [u for d in dirs if
                (u := next(w for i in count(1) if (w := z + i*d) not in floor))
                in state]
            for z in state}
print(equilibrium(state, adjacent, 5))
