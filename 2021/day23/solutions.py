from heapq import heappop, heappush

# We treat the problem as a search problem. The search state is represented by the list of
# occupied positions. Each position is represented as a tuple whose first element is
# either "corr" or one of "A", "B", "C", "D". The second element is the position (0-10)
# in the corridor in the first case, and the distance from the top of the room for the
# room positions. The positions are ordered by the type of the amphipod. For part one,
# this means that the state is a list of 8 tuples, the first two of which are the
# positions of the amber amphipods, for example.

room_loc = {"A": 2, "B": 4, "C": 6, "D": 8}
mults = {"A": 1, "B": 10, "C": 100, "D": 1000}


def home_is_free(state, home):
    """Returns True iff the given home (e.g. "A") is available for moving in."""
    count = len(state) // 4
    proper_home = {x: range(i * count, (i + 1) * count) for i, x in enumerate("ABCD")}
    return not any(
        piece[0] == home and i not in proper_home[home] for i, piece in enumerate(state)
    )


def replace_piece(state, new_piece, i):
    """Generate a new state with one of the amphipods replaced."""
    new_state = list(state)
    new_state[i] = new_piece
    return tuple(new_state)


def move_to_corridor(state, to_check, loc, position):
    """Moves along the corridor and yields free positions and their distance."""
    for j in to_check:
        if ("corr", j) in state:
            return
        if j not in room_loc.values():
            yield ("corr", j), abs(j - room_loc[loc]) + position + 1


def action_single_piece(state, i, home):
    """For a single amphipod, generates all possible new positions and their distances."""
    piece = state[i]
    loc, position = piece
    can_move_to_home = home_is_free(state, home)
    # If in a home but unable to get out
    if loc in "ABCD" and any((loc, j) in state for j in range(position)):
        return
    # If in own home
    if loc == home and can_move_to_home:
        return
    # Move to left and right corridors if in a home
    if loc in "ABCD":
        for to_check in (
            range(room_loc[loc] - 1, -1, -1),
            range(room_loc[loc] + 1, 11),
        ):
            yield from move_to_corridor(state, to_check, loc, position)
    # Move to home
    if can_move_to_home:
        first_available = max(
            j for j in range(len(state) // 4) if (home, j) not in state
        )
        # Ensure that passage is clear: Determine corridor locations that should be free
        if loc in "ABCD":
            corr_to_check = range(
                min(room_loc[loc], room_loc[home]),
                max(room_loc[loc], room_loc[home]) + 1,
            )
            distance = (
                abs(room_loc[loc] - room_loc[home]) + first_available + position + 2
            )
        else:
            corr_to_check = set(
                range(min(position, room_loc[home]), max(position, room_loc[home]) + 1)
            ) - {position}
            distance = abs(position - room_loc[home]) + first_available + 1
        if not any(("corr", j) in state for j in corr_to_check):
            yield (home, first_available), distance


def actions(state, homes):
    """For a given state, generates all states that can be reached from here."""
    for i in range(len(state)):
        home = homes[i]
        mult = mults[home]
        for new_piece, length in action_single_piece(state, i, home):
            yield replace_piece(state, new_piece, i), mult * length


def solve(start_state):
    q = [(0, start_state)]
    homes = "".join(x * (len(start_state) // 4) for x in "ABCD")
    visited = set()
    while q:
        dist, state = heappop(q)
        if state in visited:
            continue
        if "".join(s[0] for s in state) == homes:
            print(dist)
            break
        visited.add(state)
        for new_state, new_dist in actions(state, homes):
            heappush(q, (dist + new_dist, new_state))


# Part one
# #############
# #...........#
# ###B#A#B#C###
#   #D#A#D#C#
#   #########
solve(
    (
        # A locations
        ("B", 0),
        ("B", 1),
        # B locations
        ("A", 0),
        ("C", 0),
        # C locations
        ("D", 0),
        ("D", 1),
        # D locations
        ("A", 1),
        ("C", 1),
    )
)


# Part two
# #############
# #...........#
# ###B#A#B#C###
#   #D#C#B#A#
#   #D#B#A#C#
#   #D#A#D#C#
#   #########
solve(
    (
        # A locations
        ("B", 0),
        ("B", 3),
        ("C", 2),
        ("D", 1),
        # B locations
        ("A", 0),
        ("B", 2),
        ("C", 0),
        ("C", 1),
        # C locations
        ("B", 1),
        ("D", 0),
        ("D", 2),
        ("D", 3),
        # D locations
        ("A", 1),
        ("A", 2),
        ("A", 3),
        ("C", 3),
    )
)
