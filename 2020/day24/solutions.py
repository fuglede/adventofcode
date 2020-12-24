from collections import Counter
import re

with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

ds = {'e':  2, 'se':  1 - 1j, 'sw': -1 - 1j,
      'w': -2, 'nw': -1 + 1j, 'ne':  1 + 1j}

# Part one
black = set()
for l in ls:
    black ^= {sum(ds[d] for d in re.findall('|'.join(ds), l))}

print(len(black))

# Part two
for _ in range(100):
    count = Counter(z + s for s in ds.values() for z in black)
    black = {w for w, n in count.items()
             if (w in black and 1 <= n <= 2) or (w not in black and n == 2)}

print(len(black))