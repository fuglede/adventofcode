import numpy as np


banks = np.array([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11], dtype=np.int)
seen_banks = []
num_banks = len(banks)
cycles = 0
while True:
    seen_banks.append(np.copy(banks))
    highest = np.argmax(banks)
    blocks = banks[highest]
    rounds = blocks // num_banks
    extra = blocks % num_banks
    indices = (highest + 1 + np.arange(extra)) % (num_banks)
    banks[highest] = 0
    banks[indices] += 1
    banks += np.repeat(rounds, num_banks)
    if any(np.all(old_banks == banks) for old_banks in seen_banks):
        break

# Part one
print(len(seen_banks))

# Part two
print(len(seen_banks) - np.argmax([np.all(old_banks == banks) for old_banks in seen_banks]))
