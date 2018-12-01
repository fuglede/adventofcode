import itertools

import numpy as np
import pandas as pd


# Part one
df = pd.read_csv('input', header=None)
print(df.sum()[0])


# Part two
def find_first_duplicate(a):
    # If we were to just go through the list of changes once,
    # we would just be interested in its cumulative sum. We
    # then note the following relationship on subsequent passes
    # through the list of changes:
    #   pass0 = cumsum
    #   pass1 = pass0 + pass0[-1] = cumsum + cumsum[-1]
    #   pass2 = pass1 + pass1[-1] = cumsum + (cumsum + cumsum[-1])[-1]
    #                             = cumsum + 2*cumsum[-1]
    #   ...
    # and in general, by induction, the i'th pass is just cumsum + i*cumsum[-1].
    cs = np.cumsum(a)
    seen = set()
    for i in itertools.count():
        freqs = cs + i*cs[-1]
        for b in freqs:
            if b in seen:
                return b
            seen.add(b)


print(find_first_duplicate(df.values))
