from itertools import count
from sympy.ntheory.modular import solve_congruence


with open('input') as f:
    ls = [line.strip() for line in f.readlines()]

earliest = int(ls[0])
bus_times = [(-i, int(x)) for i, x in enumerate(ls[1].split(',')) if x != 'x']
_, busses = zip(*bus_times)

# Part one
print(next((time - earliest)*bus
           for time in count(earliest) for bus in busses
           if time % bus == 0))

# Part two
print(solve_congruence(*bus_times)[0])
