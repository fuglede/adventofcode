with open('input') as f:
    ns = list(map(int, f.read().split(',')))


def run(inp):
    p = list(ns)
    i = 0
    while True:
        cmd = str(p[i]).zfill(5)
        opcode = int(cmd[3:])
        p1 = p[i + 1] if int(cmd[2]) else p[p[i + 1]]
        try:
            p2 = p[i + 2] if int(cmd[1]) else p[p[i + 2]]
        except IndexError:
            pass
        if opcode == 1:
            p[p[i + 3]] = p1 + p2
            i += 4
        elif opcode == 2:
            p[p[i + 3]] = p1 * p2
            i += 4
        elif opcode == 3:
            p[p[i + 1]] = inp
            i += 2
        elif opcode == 4:
            if p1 != 0:
                return p1
            i += 2
        elif opcode == 5:
            i = p2 if p1 != 0 else i + 3
        elif opcode == 6:
            i = p2 if p1 == 0 else i + 3
        elif opcode == 7:
            p[p[i + 3]] = int(p1 < p2)
            i += 4
        elif opcode == 8:
            p[p[i + 3]] = int(p1 == p2)
            i += 4


# Part one
print(run(1))

# Part two
print(run(5))
