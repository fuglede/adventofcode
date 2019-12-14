from collections import deque

from vm import VM, read_program

p09 = read_program(9)
    
# Part one
vm = VM(p09, deque([1]))
print(next(vm))
        
# Part two
vm = VM(p09, deque([2]))
print(next(vm))
