with open('input') as f:
    initial_instructions = list(map(int, (x.strip() for x in f.readlines())))

def solve(part_two):
    instructions = list(initial_instructions)
    steps = 0
    head = 0
    while head >= 0 and head < len(instructions):
        instruction = instructions[head]
        instructions[head] += -1 if part_two and instruction >= 3 else 1
        head += instruction
        steps += 1
    return steps

# Part one
print(solve(False))

# Part two
print(solve(True))
