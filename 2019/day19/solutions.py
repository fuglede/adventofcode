from collections import deque
from itertools import count

from vm import VM, read_program


ns = read_program(19)

# Part one
print(sum(next(VM(ns, deque([x, y]))) for x in range(50) for y in range(50)))


# A quick glance at the output suggest that the relevant y coordinate
# is at least 500, so we start our search there to avoid some edge
# cases near the origin
def solve():
    prev_first_x = 0
    rows = []
    for y in count(500):
        first_x = None
        if prev_first_x == None:
            prev_first_x = 0
        x = prev_first_x
        while True:
            inputs = deque([x, y])
            vm = VM(ns, inputs)
            output = next(vm)
            if output:
                if first_x == None:
                    first_x = x
                    if rows:
                        x = rows[-1][1] - 1
            else:
                if first_x != None:
                    rows.append((first_x, x))
                    if len(rows) > 100:
                        smallest_x = rows[-1][0]
                        biggest_x = rows[-100][1]
                        if biggest_x-smallest_x >= 100:
                            return smallest_x*10000+y-100+1
                    break
            x += 1
        prev_first_x = first_x


print(solve())
