from collections import namedtuple, defaultdict

with open('input') as f:
    lines = [x.strip().split() for x in f.readlines()]

Instruction = namedtuple('Instruction', ['low', 'high'])

bots = defaultdict(list)
instructions = {}
outputs = {}
stack = []

for l in lines:
    if l[0] == 'value':
        bot = int(l[5])
        bots[bot].append(int(l[1]))
        if len(bots[bot]) == 2:
            stack.append(bot)
    else:
        instructions[int(l[1])] = Instruction((l[5], int(l[6])), (l[10], int(l[11])))

while stack:
    bot = stack.pop()
    instruction = instructions[bot]
    low = min(bots[bot])
    high = max(bots[bot])
    if high == 61 and low == 17:
        print(bot)
    if instruction.low[0] == 'bot':
        bots[instruction.low[1]].append(low)
        if len(bots[instruction.low[1]]) == 2:
            stack.append(instruction.low[1])
    else:
        outputs[instruction.low[1]] = low
    if instruction.high[0] == 'bot':
        bots[instruction.high[1]].append(high)
        if len(bots[instruction.high[1]]) == 2:
            stack.append(instruction.high[1])
    else:
        outputs[instruction.high[1]] = high
    if 0 in outputs and 1 in outputs and 2 in outputs:
        print(outputs[0] * outputs[1] * outputs[2])
        break
    bots[bot] = []
