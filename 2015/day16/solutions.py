with open('input') as f:
    lines = [x.strip().replace(':', '').replace(',', '').split() for x in f.readlines()]

d = {}
for l in lines:
    d[int(l[1])] = {l[2]: int(l[3]), l[4]: int(l[5]), l[6]: int(l[7])}

goal = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}


# Part one
for aunt, items in d.items():
    if all(goal[item] == count for (item, count) in items.items()):
        print(aunt)
        break


# Part two
lt = {'cats', 'trees'}
gt = {'pomeranians', 'goldfish'}
for aunt, items in d.items():
    found = True
    for (item, count) in items.items():
        if item in lt:
            if count <= goal[item]:
                found = False
                break
        elif item in gt:
            if count >= goal[item]:
                found = False
                break
        else:
            if count != goal[item]:
                found = False
                break
    if found:
        print(aunt)
        break
