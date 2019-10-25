class Elf:
    pass


def solve(n, part_one):
    # Set up linked list of elves
    for i in range(n):
        elf = Elf()
        elf.index = i + 1
        if i == 0:
            first = elf
        else:
            elf.prev = prev
            prev.next = elf
        prev = elf
    # Link together the two ends of the circle
    first.prev = elf
    elf.next = first
    num_left = n
    # Find the elf opposite to the first elf, for use in part two
    opposite = first
    for _ in range(num_left // 2):
        opposite = opposite.next
    active = first
    while True:
        to_steal_from = active.next if part_one else opposite
        num_left -= 1
        to_steal_from.prev.next = to_steal_from.next
        to_steal_from.next.prev = to_steal_from.prev
        # Note that the elf opposite from the next elf sites exactly one
        # or two places to the left of the elf that was previously the opposite,
        # depending on parity.
        opposite = opposite.next if num_left % 2 == 1 else opposite.next.next
        active = active.next
        # We're done if the newly active elf sits next only to itself
        if num_left == 1:
            return active.index


n = 3004953
print(solve(n, True))
print(solve(n, False))
