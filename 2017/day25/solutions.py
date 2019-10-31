import numpy as np

# Part one
state = 'A'
steps = 12208951
tape = np.zeros(2*steps)
cursor = steps
for k in range(steps):
    val = tape[cursor]
    if state == 'A':
        if val == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'B'
        elif val == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'E'
    elif state == 'B':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
        elif val == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'A'
    elif state == 'C':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'D'
        elif val == 1:
            tape[cursor] = 0
            cursor += 1
            state = 'C'
    elif state == 'D':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif val == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 'F'
    elif state == 'E':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'A'
        elif val == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 'C'
    elif state == 'F':
        if val == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'E'
        elif val == 1:
            tape[cursor] = 1
            cursor += 1
            state = 'A'
print(np.sum(tape))
