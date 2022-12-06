from itertools import count

with open("input") as f:
    data = f.read()


def solve(length):
    return next(i for i in count() if len(set(data[i - length : i])) == length)


# Part 1
print(solve(4))

# Part 2
print(solve(14))
