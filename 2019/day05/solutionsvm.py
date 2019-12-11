from vm import VM, read_program

p05 = read_program(5)

# Part one
vm = VM([1], p05)
print(vm.run_until_next_nonzero_output())

# Part two
vm = VM([5], p05)
print(next(vm))
