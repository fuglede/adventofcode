with open("input") as f:
    ls, moves = f.read().strip().split("\n\n")

dirs = {"^": -1, "v": 1, "<": -1j, ">": 1j}
moves = [dirs[x] for x in moves.replace("\n", "")]


def solve(part2):
    walls = set()
    boxes = set()

    for i, l in enumerate(ls.split("\n")):
        for j, x in enumerate(l):
            z = i + j * (2j if part2 else 1j)
            match x:
                case "#":
                    walls |= {z, z + 1j} if part2 else {z}
                case "O":
                    boxes.add(z)
                case "@":
                    robot = z

    for dz in moves:
        to_move = set()
        to_check = [robot + dz]
        while to_check:
            z = to_check.pop()
            is_right_side = part2 and (left := z - 1j) in boxes
            if z in boxes or is_right_side:
                to_move.add(left if is_right_side else z)
                to_check.append(z + dz)
                if part2 and dz.real:
                    other = left if is_right_side else z + 1j
                    to_check.append(other + dz)
            elif z in walls:
                break
        else:
            boxes -= to_move
            boxes |= {w + dz for w in to_move}
            robot += dz
    tot = sum(boxes)
    return tot.real * 100 + tot.imag


# Part 1
print(solve(False))

# Part 2
print(solve(True))
