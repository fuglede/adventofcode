import numpy as np
import re

with open('input') as f:
    commands = [x.strip() for x in f.readlines()]

# Part one

board = np.zeros((6, 50))


def run_command(command):
    if command.startswith('rect'):
        match = re.search('(\d+)x(\d+)', command)
        groups = match.groups(0)
        wide = int(groups[0])
        tall = int(groups[1])
        board[:tall, :wide] = 1
    elif command.startswith('rotate'):
        match = re.search('=(\d+) by (\d+)', command)
        groups = match.groups(0)
        num = int(groups[0])
        shift = int(groups[1])
        if 'row' in command:
            board[num] = np.roll(board[num], shift)
        else:
            board[:, num] = np.roll(board[:, num], shift)


for command in commands:
    run_command(command)

print(board.sum())

# Part two
for i in range(10):
    print()
    print(board[:, 5*i:5*i+5])
