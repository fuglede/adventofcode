with open('input') as f:
    p0 = list(map(int, f.read().split(',')))


def run(n1, n2):
    p = list(p0)
    i = 0
    p[1] = n1
    p[2] = n2
    while True:
        if p[i] == 1:
            p[p[i+3]] = p[p[i+1]] + p[p[i+2]]
        elif p[i] == 2:
            p[p[i+3]] = p[p[i+1]] * p[p[i+2]]
        elif p[i] == 99:
            return p[0]
        i += 4


print(run(12, 2))


# Part two
def solve():
    for n1 in range(100):
        for n2 in range(100):
            o = run(n1, n2)
            if o == 19690720:
                return 100 * n1 + n2


print(solve())
