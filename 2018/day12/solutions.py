with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

# Part one
state = lines[0][15:]
rules = {l[:5]: l[-1] for l in lines[2:]}
first = 0

for _ in range(20):
    state = '...' + state + '...'
    first -= 1
    new = ''
    for i in range(len(state)-4):
        s = state[i:i+5]
        new += rules[s]
    state = new
print(sum(i+first for i, s in enumerate(state) if s == '#'))

# Part two
# First, realize that the sum above grows with 21000 for each 1000 steps and starts at 480
print(50000000000//1000*21000+480)
