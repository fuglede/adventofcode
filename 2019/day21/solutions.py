from collections import deque

from vm import VM, read_program


ns = read_program(21)


def run(inputs):
    for output in VM(ns, deque(map(ord, inputs))):
        pass
    return output


# Part one
# We want to jump if there is land in four steps, but a hole
# in one of the next three steps, i.e.
#   J = D AND ((NOT A) OR (NOT B) OR (NOT C))
inputs = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""
print(run(inputs))

# Part two
# We now want to also ensure that there is land at either
# 5 steps or 8 steps, i.e. something like
#    J = D AND ((NOT A) OR (NOT B) OR (NOT C)) AND (H OR E)
inputs = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT D T
OR H T
OR E T
AND T J
RUN
"""
print(run(inputs))
