# We rewrite the program to Python code in order to make it fast enough
# to get a solution to part two in finite time. The only thing to realize
# is that once instruction 28 is hit, the program will halt if register 0
# equals register 5. Values of register 5 are referred to as "halters" in
# the solution below. The only other addition is a check if we are getting
# repeated values for the halters.
# Note that the values used below will be specific to my inputs and the
# solution will not work out-of-the-box for other inputs.
halters = []
e = 0
seen_d = set()
while True:
    d = e | 65536
    if d in seen_d:
        break
    seen_d.add(d)
    e = 13159625
    while True:
        c = d & 255
        e = c + e
        e &= 16777215
        e *= 65899
        e &= 16777215
        if 256 > d:
            halters.append(e)
            break
        else:
            d //= 256

# Part one
print(halters[0])

# Part two
print(halters[-1])
