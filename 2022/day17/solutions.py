with open("input") as f:
    data = f.read().strip()

pieces = [
    [0, 1, 2, 3],
    [-1j, 1, 1 - 1j, 1 - 2j, 2 - 1j],
    [-2j, 1 - 2j, 2, 2 - 1j, 2 - 2j],
    [0, -1j, -2j, -3j],
    [0, -1j, 1, 1 - 1j],
]
heights = [1, 3, 3, 4, 2]
widths = [4, 3, 3, 1, 2]


def solve(num_pieces):
    rocks = set(range(7))
    maxrocks = 0
    tops = {i: 0 for i in range(7)}
    seentops = {}

    skipped = False
    i = 0
    j = 0
    while i < num_pieces:
        piece = i % 5
        height = heights[piece]
        width = widths[piece]
        parts = pieces[piece]
        # Keep track of the location of the upper left corner of the piece
        loc = 2 + (maxrocks + height + 3) * 1j
        while True:
            if data[j % len(data)] == ">":
                if not {loc + p + 1 for p in parts} & rocks and width + loc.real != 7:
                    loc += 1
            else:
                if not {loc + p - 1 for p in parts} & rocks and loc.real != 0:
                    loc -= 1
            j += 1
            if {loc + p - 1j for p in parts} & rocks:
                placed = {loc + p for p in parts}
                for p in placed:
                    tops[p.real] = max(tops[p.real], p.imag)
                rocks |= placed
                maxrocks = max(maxrocks, max(z.imag for z in placed))
                # For part 2, we skip rocks if they appear to be cycling. We identify this
                # by looking at the pattern at the top; this isn't guaranteed to always
                # work but does work for the given input.
                mintops = min(tops.values())
                state = (
                    piece,
                    (j - 1) % len(data),
                    tuple(tops[i] - mintops for i in range(7)),
                )
                if not skipped and state in seentops:
                    skipped = True
                    prev_i, prev_max = seentops[state]
                    repeats = (num_pieces - i) // (i - prev_i)
                    i += (i - prev_i) * repeats
                    rocks_added = repeats * (maxrocks - prev_max)
                seentops[state] = (i, maxrocks)
                break
            loc -= 1j
        i += 1
    return maxrocks + rocks_added


# Part 1
print(solve(2022))

# Part 2
print(solve(1000000000000))
