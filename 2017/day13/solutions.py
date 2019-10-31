# Day 13, part 1
import numpy as np
import pandas as pd


df = pd.read_csv('input', header=None, sep=':')

# Part one
df.columns = ['depth', 'range']
df['caught'] = (df.depth % ((df.range-1)*2) == 0)
df_caught = df[df['caught']]
print((df_caught.depth*df_caught.range).sum())

# Part two
n = 10000000
possible = np.ones(n, dtype=np.bool)
for j in range(len(df)):
    row = df.iloc[j]
    idx = np.arange(-row.depth, n, 2*(row.range-1))
    possible[idx] = False
print(possible.argmax())
