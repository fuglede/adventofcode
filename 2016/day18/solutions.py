def generate_row(prev):
    this_row = []
    for i in range(len(prev)):
        left = prev[i-1] if i != 0 else False
        center = prev[i]
        right = prev[i+1] if i != len(prev) - 1 else False
        new = (left and center and not right) or\
              (center and right and not left) or\
              (left and not center and not right) or\
              (not left and not center and right)
        this_row.append(new)
    return this_row


def solve(inp, num_rows):
    rows = [[x == '^' for x in inp]]
    while len(rows) != num_rows:
        rows.append(generate_row(rows[-1]))
    return num_rows*len(inp) - sum(sum(x) for x in rows)


inp = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
print(solve(inp, 40))
print(solve(inp, 400000))
