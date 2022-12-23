from collections import Counter
from itertools import count

with open("input") as f:
    ls = f.read().strip().split("\n")

elves = {i + j * 1j for j, l in enumerate(ls) for i, x in enumerate(l) if x == "#"}
to_check = [
    (-1j, (-1j - 1, -1j, -1j + 1)),
    (1j, (1j - 1, 1j, 1j + 1)),
    (-1, (-1 - 1j, -1, -1 + 1j)),
    (1, (1 - 1j, 1, 1 + 1j)),
]
alldir = (-1j - 1, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1)


def move(elves, to_check):
    new_loc = {}
    elves_moved = False  # Used for part 2
    for elf in elves:
        if not any(elf + e in elves for e in alldir):
            new_loc[elf] = elf
        else:
            for direction, nb in to_check:
                if not any(elf + e in elves for e in nb):
                    new_loc[elf] = elf + direction
                    break
            # If no criterion matches, we stay put. This doesn't appear to
            # be documented in the problem text but can be deduced from the
            # examples.
            else:
                new_loc[elf] = elf
    counts = Counter(new_loc.values())
    new_elves = set()
    for elf in elves:
        proposed = new_loc[elf]
        if proposed == elf or counts[proposed] > 1:
            new_elves.add(elf)
        else:
            new_elves.add(proposed)
            elves_moved = True
    to_check = to_check[1:] + [to_check[0]]
    return new_elves, to_check, elves_moved


for i in count(1):
    elves, to_check, moved = move(elves, to_check)

    # Part one
    if i == 10:
        reals = {z.real for z in elves}
        imags = {z.imag for z in elves}
        print(
            (max(reals) - min(reals) + 1) * (max(imags) - min(imags) + 1) - len(elves)
        )

    # Part two
    if not moved:
        print(i)
        break
