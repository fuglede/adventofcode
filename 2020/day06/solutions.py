with open('input') as f:
    data = f.read().strip()

groups = data.split('\n\n')

# Part one
print(sum(len(set(g.replace('\n', ''))) for g in groups))

# Part two
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))
