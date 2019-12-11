"""This contains the general purpose IntCode VM used for several puzzles during
this year's Advent of Code. Most of the puzzles can be solved through simpler
means, but in this module we try to capture all necessary functionality as we
move along, while trying to make guesses at where to make it extensible.
"""
from collections import defaultdict, deque
from itertools import cycle, permutations
from math import inf


class VM:
    def __init__(self, inputs, program):
        self.inputs = deque(inputs)
        self.p = defaultdict(int, enumerate(program))
        self.i = 0
        self.base = 0
        self.it = self.run()
        self.opcode_counter = defaultdict(int)

    def __getitem__(self, index):
        if index < 0:
            raise RuntimeError('Negative memory access attempted.')
        return self.p[index]

    def __setitem__(self, index, val):
        self.p[index] = val

    def __iter__(self):
        return self.it

    def __next__(self):
        return next(self.it)

    def run(self):
        while True:
            cmd = str(self[self.i]).zfill(5)
            opcode = int(cmd[3:])
            modes = {k: int(cmd[3 - k]) for k in (1, 2, 3)}
            addrs = {}
            self.opcode_counter[cmd] += 1
            for k in (1, 2, 3):
                try:
                    if modes[k] == 0:
                        addrs[k] = self[self.i+k]
                    elif modes[k] == 1:
                        addrs[k] = self.i+k
                    elif modes[k] == 2:
                        addrs[k] = self[self.i+k]+self.base
                except IndexError:
                    pass
            if opcode == 1:
                self[addrs[3]] = self[addrs[1]] + self[addrs[2]]
                self.i += 4
            elif opcode == 2:
                self[addrs[3]] = self[addrs[1]] * self[addrs[2]]
                self.i += 4
            elif opcode == 3:
                self[addrs[1]] = self.inputs.popleft()
                self.i += 2
            elif opcode == 4:
                yield self[addrs[1]]
                self.i += 2
            elif opcode == 5:
                self.i = self[addrs[2]] if self[addrs[1]] != 0 else self.i + 3
            elif opcode == 6:
                self.i = self[addrs[2]] if self[addrs[1]] == 0 else self.i + 3
            elif opcode == 7:
                self[addrs[3]] = int(self[addrs[1]] < self[addrs[2]])
                self.i += 4
            elif opcode == 8:
                self[addrs[3]] = int(self[addrs[1]] == self[addrs[2]])
                self.i += 4
            elif opcode == 9:
                self.base += self[addrs[1]]
                self.i += 2
            elif opcode == 99:
                return
            else:
                raise RuntimeError(f'Invalid opcode: {opcode}')

    def add_input(self, value):
        self.inputs.append(value)

    def run_until_next_output(self):
        return next(self)

    def run_until_next_nonzero_output(self):
        return next(o for o in self if o != 0)

    def run_until_halt(self):
        for _ in self:
            pass


def read_program(day):
    with open(f'day{day:02d}/input') as f:
        return list(map(int, f.read().split(',')))
