from collections import deque

from vm import VM, read_program

p05 = read_program(5)

# Part one
vm = VM(p05, deque([1]))
print(vm.run_until_next_nonzero_output())

# Part two
vm = VM(p05, deque([5]))
print(next(vm))
