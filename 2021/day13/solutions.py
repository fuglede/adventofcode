import matplotlib.pyplot as plt
import numpy as np

with open("input") as f:
    data = f.read().strip()

top, bottom = data.split("\n\n")
coords = np.array([list(map(int, l.split(","))) for l in top.split("\n")]).T
a = np.zeros((coords[0].max() + 1, coords[1].max() + 1), dtype=bool)
a[coords[0], coords[1]] = True

first = True
for l in bottom.split("\n"):
    lab, num = l.split(" ")[-1].split("=")
    num = int(num)
    a = (
        a[:num] | a[num + 1 :][::-1]
        if lab == "x"
        else a[:, :num] | a[:, num + 1 :][:, ::-1]
    )
    # Part one
    if first:
        first = False
        print(a.sum())

# Part two
plt.spy(a.T)
plt.show()
