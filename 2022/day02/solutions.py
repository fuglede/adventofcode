with open("input") as f:
    ls = f.readlines()


def score(l, part1):
    x1, x2 = l.split()
    l1 = "ABC".index(x1)
    l2 = "XYZ".index(x2)
    play = l2 if part1 else (l1 + l2 + 2) % 3
    won = (l2 - l1 + 1) % 3 if part1 else l2
    return 1 + play + 3 * won


# Part 1
print(sum(score(l, True) for l in ls))

# Part 2
print(sum(score(l, False) for l in ls))
