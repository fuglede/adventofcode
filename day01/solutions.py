import numpy as np
import pandas as pd


# Part one
df = pd.read_csv('input', header=None)
print(df.sum()[0])


# Part two
def find_first_duplicate(changes):
    freqs = np.cumsum(changes)
    seen = set()
    while True:
        for b in freqs:
            if b in seen:
                return b
            seen.add(b)
        freqs += changes[0] + freqs[-1] - freqs[0]


print(find_first_duplicate(df.values))
