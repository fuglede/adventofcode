from vm import VM, read_program

p09 = read_program(9)
    
# Part one
vm = VM([1], p09)
print(next(vm))
        
# Part two
vm = VM([2], p09)
print(next(vm))
