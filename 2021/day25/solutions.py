from itertools import count

with open("input") as f:
    ls = f.read().strip().split("\n")


n = len(ls)
m = len(ls[0])
rights = {(i, j) for i in range(n) for j in range(m) if ls[i][j] == '>'}
downs = {(i, j) for i in range(n) for j in range(m) if ls[i][j] == 'v'}

def step(rights, downs):
    new_rights = set()
    new_downs = set()
    to_check = rights | downs
    for x, y in rights:
        new_loc = (x, (y + 1) % m)
        new_rights.add((x, y) if new_loc in to_check else new_loc)
    to_check = new_rights | downs
    for x, y in downs:
        new_loc = ((x + 1) % n, y)
        new_downs.add((x, y) if new_loc in to_check else new_loc)
    return new_rights, new_downs

for c in count(1):
    new_rights, new_downs = step(rights, downs)
    if rights == new_rights and downs == new_downs:
        print(c)
        break
    rights = new_rights
    downs = new_downs
