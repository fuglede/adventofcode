import re

with open('input') as f:
    data = f.readlines()

sizes = [[int(x) for x in re.findall(r'\d+', s)] for s in data]

# Part one
print(sum(2*s[0]*s[1] + 2*s[1]*s[2] + 2*s[2]*s[0] + s[0]*s[1]*s[2]/max(s) for s in sizes))

# Part two
print(sum(2*(sum(s) - max(s)) + s[0]*s[1]*s[2] for s in sizes))
