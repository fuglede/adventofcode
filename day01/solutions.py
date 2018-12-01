import numpy as np


# Part one
changes = np.genfromtxt('input', dtype=int)
print(changes.sum())


# Part two
def first_frequency_reached_twice(changes):
    freqs = np.cumsum(changes)
    seen = set()
    while True:
        for b in freqs:
            if b in seen:
                return b
            seen.add(b)
        freqs += changes[0] + freqs[-1] - freqs[0]


print(first_frequency_reached_twice(changes))
