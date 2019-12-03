with open('input') as f:
    ls = [l.split(',') for l in f.readlines()]


def make_wire(l):
    c = 0
    i = 1
    directions = {'R': 1j, 'L': -1j, 'U': 1, 'D': -1}
    covered = {}
    for d in l:
        direction = directions[d[0]]
        for _ in range(int(d[1:])):
            c += direction
            if c not in covered:
                covered[c] = i
            i += 1
    return covered


wire1 = make_wire(ls[0])
wire2 = make_wire(ls[1])
crossings = set(wire1) & set(wire2)

# Part one
print(int(min(abs(c.real) + abs(c.imag) for c in crossings)))

# Part two
print(min(wire1[c] + wire2[c] for c in crossings))
