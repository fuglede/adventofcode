from collections import deque
from itertools import chain, combinations
import sys

from vm import VM, read_program

ns = read_program(25)

# We first play the actual game to figure out what items exist and where
# the locked door is; to play the game, run `python -m day25.solutions -i`
if len(sys.argv) > 1 and sys.argv[1] == '-i':
    inputs = deque([])
    vm = VM(ns, inputs)
    while True:
        o = next(vm.it)
        if o is not None:
            print(chr(o), end='')
        elif not inputs:
            inp = input() + '\n'
            for c in map(ord, inp):
                inputs.append(c)


# Now, loop over all possible combinations of items to drop. If we are neither
# too heavy or too light, that means we're done.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


items = ['spool of cat6', 'asterisk', 'jam', 'shell', 'astronaut ice cream', 'space heater',
         'klein bottle', 'space law space brochure']

for dropped_items in powerset(items):
    inputs = deque([])
    vm = VM(ns, inputs)
    commands = """west
north
take jam
east
south
take asterisk
south
take klein bottle
east
take spool of cat6
west
north
north
west
north
take astronaut ice cream
north
east
south
take space law space brochure
north
west
south
south
south
east
south
west
take shell
east
east
take space heater
west
north
west
south
west
"""
    for item in dropped_items:
        commands += f'drop {item}\n'
    commands += 'south\n'
    for c in map(ord, commands):
        inputs.append(c)
    outputs = []
    try:
        for o in vm:
            if o is not None:
                outputs.append(chr(o))
    except IndexError:
        pass
    s = ''.join(outputs)
    if 'lighter' not in s and 'heavier' not in s:
        print(s)
        break
