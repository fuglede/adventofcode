with open("input") as f:
    ls = f.read().split("\n")


maze = {
    i + j * 1j: x == "."
    for j, l in enumerate(ls[:-3])
    for i, x in enumerate(l)
    if x != " "
}
commands = ls[-2].replace("L", ",L,").replace("R", ",R,").split(",")


def password(loc, direction):
    return (
        1000 * (loc.imag + 1)
        + 4 * (loc.real + 1)
        + {1: 0, 1j: 1, -1: 2, -1j: 3}[direction]
    )


# Part 1
direction = 1
loc = next(x for x in range(150) if maze.get(x))

for command in commands:
    match command:
        case "L":
            direction *= -1j
        case "R":
            direction *= 1j
        case _:
            for _ in range(int(command)):
                new_loc = loc
                while True:
                    new_loc += direction
                    new_loc = (new_loc.real % 150) + (new_loc.imag % 200) * 1j
                    if new_loc in maze:
                        break
                if not maze[new_loc]:
                    break
                loc = new_loc

print(password(loc, direction))

# Part 2
# Our die looks like this:
#
#   A B
#   C
# D E
# F
#
sides = {}
for z in maze:
    match (z.real // 50, z.imag // 50):
        case (1, 0):
            sides[z] = "A"
        case (2, 0):
            sides[z] = "B"
        case (1, 1):
            sides[z] = "C"
        case (0, 2):
            sides[z] = "D"
        case (1, 2):
            sides[z] = "E"
        case (0, 3):
            sides[z] = "F"

directions = {"left": 1, "right": -1, "bottom": -1j, "top": 1j}
left_top = {"A": 50, "B": 100, "C": 50 + 50j, "D": 100j, "E": 50 + 100j, "F": 150j}
right_top = {k: v + 49 for k, v in left_top.items()}
left_bottom = {k: v + 49j for k, v in left_top.items()}
# We explicitly keep track of where we end up by going out of bounds,
# and which orientation we have when we do so. For instance, if we
# go left from C, we enter through the top of D, and the imaginary
# offset from C should be the real offset in D.
portals = {
    "A": {-1: ("left", "D", "imag", "neg_imag"), -1j: ("left", "F", "real", "imag")},
    "B": {
        -1j: ("bottom", "F", "real", "real"),
        1: ("right", "E", "imag", "neg_imag"),
        1j: ("right", "C", "real", "imag"),
    },
    "C": {-1: ("top", "D", "imag", "real"), 1: ("bottom", "B", "imag", "real")},
    "D": {-1j: ("left", "C", "real", "imag"), -1: ("left", "A", "imag", "neg_imag")},
    "E": {1: ("right", "B", "imag", "neg_imag"), 1j: ("right", "F", "real", "imag")},
    "F": {
        -1: ("top", "A", "imag", "real"),
        1: ("bottom", "E", "imag", "real"),
        1j: ("top", "B", "real", "real"),
    },
}
base = {"left": left_top, "right": right_top, "bottom": left_bottom, "top": left_top}

direction = 1
loc = next(x for x in range(150) if maze.get(x))

for command in commands:
    match command:
        case "L":
            direction *= -1j
        case "R":
            direction *= 1j
        case _:
            for _ in range(int(command)):
                new_loc = loc + direction
                new_direction = direction
                if new_loc not in maze:
                    enter, new_side, fr, to = portals[sides[loc]][direction]
                    new_loc = base[enter][new_side]
                    offset = (loc.real if fr == 'real' else loc.imag) % 50
                    if to == "real":
                        new_loc += offset
                    elif to == "imag":
                        new_loc += offset * 1j
                    elif to == "neg_imag":
                        new_loc += (49 - offset) * 1j
    
                    new_direction = directions[enter]
                if not maze[new_loc]:
                    break
                loc = new_loc
                direction = new_direction

print(password(loc, direction))
