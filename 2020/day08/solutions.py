with open('input') as f:
    ws = [line.strip().split() for line in f.readlines()]

instructions = [w[0] for w in ws]
values = [int(w[1]) for w in ws]


def run(insts, values):
    i = 0
    seen = set()
    acc = 0
    while True:
        # Part one
        if i in seen:
            return (False, acc)
        # Part two
        elif i == len(ws):
            return (True, acc)
        seen.add(i)
        inst = insts[i]
        value = values[i]
        if inst == 'acc':
            acc += value
        if inst == 'jmp':
            i += value
        else:
            i += 1


# Part one
_, acc = run(instructions, values)
print(acc)

# Part two
to_change = (i for i, x in enumerate(instructions) if x in ('nop', 'jmp'))
for i in to_change:
    new_instructions = list(instructions)
    new_instructions[i] = 'jmp' if instructions[i] == 'nop' else 'nop'
    halts, acc = run(new_instructions, values)
    if halts:
        break
print(acc)
