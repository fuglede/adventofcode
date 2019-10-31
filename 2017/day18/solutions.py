from collections import defaultdict, deque


with open('input') as f:
    commands = [x.strip() for x in f.readlines()]

# Part one
registers = defaultdict(int)
sound = 0
address = 0

while address < len(commands):
    command = commands[address]
    split = command.split()
    if len(split) == 3:
        c, reg, val = split
    else:
        if split[0] == 'snd':
            c, val = split
        else:
            c, reg = split
    try:
        val = int(val)
    except:
        val = registers[val]
    if c == 'set':
        registers[reg] = val
    elif c == 'add':
        registers[reg] += val
    elif c == 'mul':
        registers[reg] *= val
    elif c == 'mod':
        registers[reg] %= val
    elif c == 'snd':
        sound = val
    elif c == 'rcv':
        if registers[reg] != 0:
            registers[reg] = sound
            break
    elif c == 'jgz':
        if registers[reg] > 0:
            address += val - 1
    address += 1

print(sound)

# Day 18, part 12
registers_0 = defaultdict(int)
registers_0['p'] = 0
registers_1 = defaultdict(int)
registers_1['p'] = 1
queue_0 = deque()
queue_1 = deque()
address_0 = 0
address_1 = 0
waiting_0 = False
waiting_1 = False
firstactive = True
sent_1 = 0

while True:
    if waiting_0 and waiting_1:
        break
    address = address_0 if firstactive else address_1
    registers = registers_0 if firstactive else registers_1
    command = commands[address]
    split = command.split(' ')
    if len(split) == 3:
        if split[0] == 'jgz':
            c = 'jgz'
            val1 = split[1]
            try:
                val1 = int(val1)
            except:
                val1 = registers[val1]
            val2 = split[2]
            try:
                val2 = int(val2)
            except:
                val2 = registers[val2]
        else:
            c, reg, val = split
    else:
        if split[0] == 'snd':
            c, val = split
        else:
            c, reg = split
    try:
        val = int(val)
    except:
        val = registers[val]
    if reg == '1':
        break
    if c == 'set':
        registers[reg] = val
    elif c == 'add':
        registers[reg] += val
    elif c == 'mul':
        registers[reg] *= val
    elif c == 'mod':
        registers[reg] %= val
    elif c == 'snd':
        if firstactive:
            queue_1.append(val)
        else:
            sent_1 += 1
            queue_0.append(val)
    elif c == 'rcv':
        if firstactive:
            if not queue_0:
                waiting_0 = True
                address -= 1
            else:
                waiting_0 = False
                registers[reg] = queue_0.popleft()
        else:
            if not queue_1:
                waiting_1 = True
                address -= 1
            else:
                waiting_1 = False
                registers[reg] = queue_1.popleft()
    elif c == 'jgz':
        if val1 > 0:
            address += val2 - 1
    address += 1
    if firstactive:
        address_0 = address
    else:
        address_1 = address
    firstactive = not firstactive

print(sent_1)
