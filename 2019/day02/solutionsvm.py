from vm import VM, read_program

ns = read_program(2)


def run_with_inputs(n1, n2):
    vm = VM([], ns)
    vm[1], vm[2] = n1, n2
    vm.run_until_halt()
    return vm[0]


# Part one
print(run_with_inputs(12, 2))


# Part two
def solve():
    for n1 in range(1, 100):
        for n2 in range(1, 100):
            o = run_with_inputs(n1, n2)
            if o == 19690720:
                return 100*n1 + n2


print(solve())
