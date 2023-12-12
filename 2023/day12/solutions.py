from functools import cache

with open("input") as f:
    ws = [l.split() for l in f.read().strip().split("\n")]


@cache
def num_solutions(s, sizes, num_done_in_group=0):
    if not s:
        # Is this a solution? Did we handle and close all groups?
        return not sizes and not num_done_in_group
    num_sols = 0
    # If next letter is a "?", we branch
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            # Extend current group
            num_sols += num_solutions(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                # If we were in a group that can be closed, close it
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += num_solutions(s[1:], sizes[1:])
            else:
                # If we are not in a group, move on to next symbol
                num_sols += num_solutions(s[1:], sizes)
    return num_sols


rows = [(w1, tuple(map(int, w2.split(",")))) for w1, w2 in ws]

# Part 1
print(sum(num_solutions(group + ".", sizes) for group, sizes in rows))

# Part 2
print(sum(num_solutions("?".join([group] * 5) + ".", sizes * 5) for group, sizes in rows))
