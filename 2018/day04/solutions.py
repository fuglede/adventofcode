from collections import Counter, defaultdict
from datetime import datetime, timedelta
import re

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

lines.sort()
minute = defaultdict(list)
for l in lines:
    n = [int(x) for x in re.findall(r'\d+', l)]
    if len(n) == 6:
        guard = n[5]
    if 'asleep' in l:
        asleep = datetime(n[0], n[1], n[2], n[3], n[4])
    if 'wakes' in l:
        now = datetime(n[0], n[1], n[2], n[3], n[4])
        t0 = asleep
        while t0 < now:
            minute[guard].append(t0.minute)
            t0 += timedelta(minutes=1)

# Part one
guard1 = max(minute.items(), key=lambda x: len(x[1]))[0]
minute1 = Counter(minute[guard1]).most_common(1)[0][0]
print(guard1 * minute1)

# Part two
guard2, minutes = max(minute.items(), key=lambda m: Counter(m[1]).most_common()[0][1])
minute2 = Counter(minutes).most_common(1)[0][0]
print(guard2 * minute2)
