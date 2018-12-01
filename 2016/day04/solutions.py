import re
from collections import Counter

with open('input') as f:
    rooms = [x.strip() for x in f.readlines()]


def split(room):
    match = re.match('([^\d]+)(\d+)\[(\w+)\]', room)
    groups = match.groups(0)
    return groups[0], int(groups[1]), groups[2]


# Part one
def check(room):
    code, num, check = split(room)
    code = sorted([a for a in code if a != '-'])
    most_common = Counter(code).most_common(5)
    return num if [a[0] for a in most_common] == list(check) else 0


print(sum(check(room) for room in rooms))


# Part two
def rotate_name(name, rot):
    new_name = []
    for letter in name:
        c = ord(letter) - (65+32)
        new_c = (c + rot) % 26
        new_name.append(chr(new_c + 65 + 32))
    return str.join('', new_name)


for room in rooms:
    code, num, check = split(room)
    rotated = rotate_name(code, num)
    if 'north' in rotated:
        print(num, rotated)
