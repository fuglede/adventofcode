def score(s, part_one):
    nest_level = 0
    score = 0
    non_canc = 0
    garbage = False
    i = 0
    while i < len(s):
        c = s[i]
        if not garbage and c == '{':
            nest_level += 1
            score += nest_level
        elif not garbage and c == '}':
            nest_level -= 1
        elif not garbage and c == '<':
            garbage = True
        elif garbage and c == '>':
            garbage = False
        elif garbage and c == '!':
            i += 1
        elif garbage:
            non_canc += 1
        i += 1
    return score if part_one else non_canc


with open('input') as f:
    s = f.read().strip()

# Part one
print(score(s, True))

# Part two
print(score(s, False))
