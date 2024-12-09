with open("input") as f:
    ns = list(map(int, f.read().strip()))

# Part 1
disk = []
for i, n in enumerate(ns):
    disk += [None if i % 2 else i // 2] * n

head = ns[0]
while head < len(disk):
    if disk[head]:
        head += 1
    elif num := disk.pop():
        disk[head] = num

print(sum(i * n for i, n in enumerate(disk)))

# Part 2
blocks = []
head = 0
for i, n in enumerate(ns):
    if not i % 2:
        blocks.append((i // 2, head, head + n))
    head += n

for to_move in range(i // 2, -1, -1):
    block = next(b for b in blocks if b[0] == to_move)
    _, start, end = block
    space_needed = end - start
    for i, ((_, _, end1), (_, start2, _)) in enumerate(zip(blocks, blocks[1:])):
        if end1 == end:
            break
        if start2 - end1 >= space_needed:
            blocks.insert(i + 1, (to_move, end1, end1 + space_needed))
            blocks.remove(block)
            break

print(
    sum(
        block_id * index
        for block_id, start, end in blocks
        for index in range(start, end)
    )
)
