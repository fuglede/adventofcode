import re

import numpy as np

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

is_on = np.zeros((1000, 1000), dtype=bool)
for l in lines:
    n = [int(x) for x in re.findall(r'\d+', l)]
    if 'on' in l:
        is_on[n[0]:n[2]+1, n[1]:n[3]+1] = 1
    elif 'off' in l:
        is_on[n[0]:n[2]+1, n[1]:n[3]+1] = 0
    else:
        is_on[n[0]:n[2]+1, n[1]:n[3]+1] = ~is_on[n[0]:n[2]+1, n[1]:n[3]+1]

print(np.sum(is_on))

brightness = np.zeros((1000, 1000), dtype=int)
for l in lines:
    n = [int(x) for x in re.findall(r'\d+', l)]
    if 'on' in l:
        brightness[n[0]:n[2]+1, n[1]:n[3]+1] += 1
    elif 'off' in l:
        brightness[n[0]:n[2]+1, n[1]:n[3]+1] -= 1
    else:
        brightness[n[0]:n[2]+1, n[1]:n[3]+1] += 2
    brightness[brightness < 0] = 0

print(np.sum(brightness))
