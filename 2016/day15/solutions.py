from itertools import count


def solve(ns, ps):
    for i in count():
        if all((ps[k] + i + k + 1) % ns[k] == 0 for k in range(len(ns))):
            return i


print(solve([13, 19, 3, 7, 5, 17], [1, 10, 2, 1, 3, 5]))
print(solve([13, 19, 3, 7, 5, 17, 11], [1, 10, 2, 1, 3, 5, 0]))
