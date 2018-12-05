with open('input') as f:
    data = f.read().strip()


# Part one
def react(polymer):
    result = []
    for l in polymer:
        if result and ord(result[-1]) - ord(l) in (-32, 32):
            result.pop()
        else:
            result.append(l)
    return result


print(len(react(data)))


# Part two
def react_char(polymer, i):
    return react(a for a in polymer if ord(a) % 32 - 1 != i)


print(min(len(react_char(data, i)) for i in range(25)))
