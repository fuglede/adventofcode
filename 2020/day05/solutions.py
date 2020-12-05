import re

with open('input') as f:
    ls = [x.strip() for x in f.readlines()]


def binary(w):
    w = re.sub('[FL]', '0', w)
    w = re.sub('[BR]', '1', w)
    return int(w, 2)


# Part one
print(max(map(binary, ls)))

# Part two
all_ids = list(map(binary, ls))
for seat in sorted(all_ids):
    if seat + 1 not in all_ids and seat + 2 in all_ids:
        print(seat + 1)
        break
