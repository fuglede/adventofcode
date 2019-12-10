from cmath import phase

with open('input') as f:
    ls = f.readlines()

asteroids = set(m + n*1j
                for n, row in enumerate(ls)
                for m, col in enumerate(row) if col == '#')

# Part one
visible = {a: set(phase((b-a)/1j) for b in asteroids if b != a)
           for a in asteroids}
a, v = max(visible.items(), key=lambda x: len(x[1]))
print(len(v))


# Part two
def solve(a):
    d = sorted((phase((b-a)/1j), abs(b-a), b) for b in asteroids if b != a)
    last_phase = None
    c = 0
    for this_phase, _, b in d:
        if this_phase != last_phase:
            last_phase = this_phase
            c += 1
            if c == 200:
                return b.real*100 + b.imag


print(solve(a))
