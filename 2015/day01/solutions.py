with open('input') as f:
    data = f.read()

# Part one
print(data.count('(') - data.count(')'))


# Part two
print(next(i for i in range(len(data)) if data[:i].count('(') - data[:i].count(')') == -1))
