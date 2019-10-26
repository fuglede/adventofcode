with open('input') as f:
    lines = [l.strip().split() for l in f.readlines()]


def rotate(s, direction, amount):
    amount = amount % len(s)
    if direction == 'right':
        return s[-amount:] + s[:-amount]
    else:
        return s[amount:] + s[:amount]


def rotate_based(s, direction, c):
    index = s.index(c)
    amount = index + 1
    if index >= 4:
        amount += 1
    return rotate(s, direction, amount)


def swap_letters(s, a, b):
    i = s.index(a)
    j = s.index(b)
    return swap_position(s, i, j)


def swap_position(s, i, j):
    a = s[i]
    b = s[j]
    if i < j:
        return s[:i] + b + s[i+1:j] + a + s[j+1:]
    else:
        return s[:j] + a + s[j+1:i] + b + s[i+1:]


def reverse(s, i, j):
    return s[:i] + s[i:j+1][::-1] + s[j+1:]


def move(s, i, j):
    l = list(s)
    c = l[i]
    del l[i]
    l.insert(j, c)
    return ''.join(l)


def scramble(s, lines):
    for l in lines:
        if l[0] == 'rotate':
            if l[1] == 'based':
                s = rotate_based(s, 'right', l[6])
            else:
                s = rotate(s, l[1], int(l[2]))
        elif l[0] == 'swap':
            if l[1] == 'letter':
                s = swap_letters(s, l[2], l[5])
            else:
                s = swap_position(s, int(l[2]), int(l[5]))
        elif l[0] == 'reverse':
            s = reverse(s, int(l[2]), int(l[4]))
        elif l[0] == 'move':
            s = move(s, int(l[2]), int(l[5]))
    return s


def unscramble(s, lines):
    # Loop over all instructions and in each case perform the instruction
    # inverse to the one we would normally perform
    for l in lines[::-1]:
        if l[0] == 'rotate':
            if l[1] == 'based':
                # Inverting this one amounts to figuring out what index, the
                # character was originally at. Since there's only 8 possibilities
                # for our given input, we simply map those out.
                c = l[6]
                i = s.index(c)
                m = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1}
                s = rotate(s, 'left', m[i])
            else:
                s = rotate(s, 'left' if l[1] == 'right' else 'right', int(l[2]))
        elif l[0] == 'swap':
            if l[1] == 'letter':
                s = swap_letters(s, l[2], l[5])
            else:
                s = swap_position(s, int(l[2]), int(l[5]))
        elif l[0] == 'reverse':
            s = reverse(s, int(l[2]), int(l[4]))
        elif l[0] == 'move':
            s = move(s, int(l[5]), int(l[2]))
    return s


print(scramble('abcdefgh', lines))
print(unscramble('fbgdceah', lines))
