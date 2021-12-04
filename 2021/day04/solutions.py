with open("input") as f:
    data = f.read().strip()

calls, *board_input = data.split("\n\n")

# Represent each board as a list of 10 sets of possible win conditions
boards = []
for b in board_input:
    this_board = []
    board = b.split("\n")
    this_board = [list(map(int, line.split())) for line in board]
    this_board += list(map(list, zip(*this_board)))
    boards.append(list(map(set, this_board)))


left = set(range(len(boards)))  # For part 2
called = set()
for m in map(int, calls.split(",")):
    called.add(m)
    for j in set(left):
        board = boards[j]
        if any(to_check.issubset(called) for to_check in board):
            left.discard(j)
            if not len(left) % (len(boards) - 1):
                print(sum(set.union(*board[:5]) - set(called)) * m)
