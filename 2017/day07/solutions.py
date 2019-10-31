import re


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


class Program:
    def __init__(self, weight, holding):
        self.weight = weight
        self.holding = holding

    def __str__(self):
        return f'weight: {self.weight}, holding: {self.holding}'

    def total_weight(self):
        if len(self.holding) == 0:
            return self.weight
        return self.weight + sum(data[p].total_weight() for p in self.holding)


data = {}
for i in range(len(lines)):
    name, weight = re.findall(r'(\w+) \((\d+)\)', lines[i])[0]
    holding = re.findall(r'\s(\w+)', lines[i])
    data[name] = Program(int(weight), holding)


# Part one
held = set()
for k, v in data.items():
    held = held.union(v.holding)

root = next(k for k in data if k not in held)
print(root)

# Part two
unbalanced = next(k for k, v in data.items() if len(set(data[x].total_weight() for x in v.holding)) > 1 and k != root)
holding_weights = [data[x].total_weight() for x in data[unbalanced].holding]
for x in data[unbalanced].holding:
    if len([y for y in holding_weights if y == data[x].total_weight()]) == 1:
        mismatch = data[x].total_weight() - next(y for y in holding_weights if y != data[x].total_weight())
        print(data[x].weight - mismatch)
