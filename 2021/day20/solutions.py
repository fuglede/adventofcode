from collections import defaultdict

with open("input") as f:
    data = f.read().strip()

top, bottom = data.split("\n\n")
enhancement = [x == "#" for x in top]
inp = defaultdict(
    bool,
    {
        i + 1j * j: x == "#"
        for i, l in enumerate(bottom.split("\n"))
        for j, x in enumerate(l)
    },
)

dirs = (1 + 1j, 1, 1 - 1j, 1j, 0, -1j, -1 + 1j, -1, -1 - 1j)


def step(grid, value_at_infinity):
    z1, *_, z2 = grid
    out = defaultdict(lambda: value_at_infinity)
    for x in range(int(z1.real) - 1, int(z2.real) + 2):
        for y in range(int(z1.imag) - 1, int(z2.imag) + 2):
            z = x + 1j * y
            head = sum(2 ** i * grid[z + dz] for i, dz in enumerate(dirs))
            out[z] = enhancement[head]
    return out


# Part one
print(sum(step(step(inp, True), False).values()))

# Part two
for i in range(50):
    inp = step(inp, not i % 2)
print(sum(inp.values()))
