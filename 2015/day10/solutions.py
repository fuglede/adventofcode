def expand(s):
    new_s = ''
    c = 0
    curr = s[0]
    for i in range(len(s)):
        if (i > 0 and s[i] != curr):
            new_s += f'{c}{s[i-1]}'
            curr = s[i]
            c = 0
        c += 1
    new_s += f'{c}{curr}'
    return new_s


# Part one
s = '1321131112'
for _ in range(40):
    s = expand(s)
print(len(s))

# Part two
s = '1321131112'
for _ in range(50):
    s = expand(s)
print(len(s))
