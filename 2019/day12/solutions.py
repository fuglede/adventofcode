from itertools import count
import re

import numpy as np


with open('input') as f:
    ns = np.array([list(map(int, re.findall('-?\d+', x))) for x in f.readlines()])

state0 = np.stack([ns, np.zeros((4, 3), dtype=int)])

# Part one
state = state0.copy()
for _ in range(1000):
    state[1] += np.sign(state[0] - state[0, :, None]).sum(1)
    state[0] += state[1]
print(abs(state).sum(2).prod(0).sum())


# Part two
# Here, we first of all make use of the fact that the three directions
# are independent, so we need to find cycles for each of them and use
# that to determine the overall cycle length. Moreover, since the process
# is reversible, the cycles will start at time 0, and the overall cycle
# length is simply the lowest common multiple of all of them.
def find_axis_cycle_length(ax):
    state_ax = state0[:, :, ax].copy()
    for i in count(1):
        state_ax[1] += np.sign(state_ax[0] - state_ax[0, :, None]).sum(1)
        state_ax[0] += state_ax[1]
        if np.array_equal(state_ax, state0[:, :, ax]):
            return i


print(np.lcm.reduce(list(map(find_axis_cycle_length, range(3)))))
