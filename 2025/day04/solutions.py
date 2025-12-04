with open("input") as f:
    ls = f.read().strip().split("\n")

paper = {i + 1j * j for i, l in enumerate(ls) for j, c in enumerate(l) if c == "@"}
octdir = {1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}
removed = []
while to_remove := {z for z in paper if len({z + dz for dz in octdir} & paper) < 4}:
    removed.append(len(to_remove))
    paper -= to_remove

# Part 1
print(removed[0])

# Part 2
print(sum(removed))
