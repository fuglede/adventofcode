with open('input') as f:
    ps = [x.strip().split() for x in f.readlines()]

# Part one
print(sum(len(p) == len(set(p)) for p in ps))

# Part two
valids = 0
for l in ps:
    new_l = [''.join(sorted(p)) for p in l]
    if len(new_l) == len(set(new_l)):
        valids += 1
print(valids)
