from collections import deque

from vm import VM, read_program

ns = read_program(17)

# Part one
vm = VM(ns)
x = 0
y = 0
scaffolds = set()
field = {}
for output in vm:
    field[y+x*1j] = output
    if output == 35:
        scaffolds.add(y + x*1j)
    if output == 10:
        y += 1
        x = 0
    else:
        x += 1

print(sum(x.real*x.imag for x in scaffolds
          if x+1 in scaffolds and x-1 in scaffolds and x+1j in scaffolds and x-1j in scaffolds))

# Part two
# We first take a look at the map and based on that, manually
# determine what the routines must look like.
max_x = int(max(z.real for z in scaffolds))
max_y = int(max(z.imag for z in scaffolds))
for x in range(max_x+1):
    for y in range(max_y+1):
        print(chr(field[x+y*1j]), end='')
    print()

M = 'A,B,A,C,B,A,C,B,A,C\n'
A = 'L,12,L,12,L,6,L,6\n'
B = 'R,8,R,4,L,12\n'
C = 'L,12,L,6,R,12,R,8\n'
video = 'n\n'
inputs = deque(map(ord, M+A+B+C+video))
vm = VM(ns, inputs)
vm[0] = 2
for output in vm:
    pass
print(output)
