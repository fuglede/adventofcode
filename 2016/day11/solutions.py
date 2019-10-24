from collections import defaultdict, deque
from itertools import combinations

# Set up our puzzle inputs by hand. We use a representation very similar to
# that used for illustration in the problem. I'm sure a more efficient
# representation exists
root_part_1 = (('0G', 1), ('0M', 1), ('1G', 1), ('2G', 1), ('1M', 2), ('2M', 2),
               ('3G', 3), ('3M', 3), ('4G', 3), ('4M', 3))
root_part_2 = (('0G', 1), ('0M', 1), ('1G', 1), ('2G', 1), ('1M', 2), ('2M', 2),
               ('3G', 3), ('3M', 3), ('4G', 3), ('4M', 3), ('5M', 1), ('5G', 1),
               ('6M', 1), ('6G', 1))


# We will solve the problem by breadth-first search from the given starting
# configuration. When considering a new vertex, we will generate all possible
# new configurations from that point.
def possible_actions(setup, floor):
    """
    Finds all possible configurations that can be reached in a
    single step from the current configuration. Here, setup is
    the configuration of generators/chips, and floor is the floor
    that the elevator is currently at.
    """
    # Get indices of all elements on the same floor as the elevator.
    movable = [i for i, el in enumerate(setup) if el[1] == floor]
    singles = movable
    doubles = combinations(movable, 2)
    result = []

    def is_valid(el, new_setup, floor):
        """Determines if a new possible configuration is valid."""
        generators = {t[0] for t in new_setup if t[1] == floor and t[0][1] == 'G'}
        if el[0][1] == 'M':
            if generators and f'{el[0][0]}G' not in generators:
                return False
        else:
            chips = {t for t in new_setup if t[1] == floor and t[0][1] == 'M'}
            if chips and not generators:
                return False
        return True

    def make_setup_single(offset, el):
        """Creates a new configuration with a single element moved."""
        new_el = (el[0], floor + offset)
        if is_valid(el, setup, floor + offset):
            new_setup = list(setup)
            new_setup[s] = new_el
            return tuple(new_setup), floor + offset

    def make_setup_double(offset, el1, el2):
        """Creates a new configuration with two elements moved."""
        new_el1 = (el1[0], floor + offset)
        new_el2 = (el2[0], floor + offset)
        el1_moved = list(setup)
        el1_moved[s1] = new_el1
        el2_moved = list(setup)
        el2_moved[s2] = new_el2
        if is_valid(new_el1, el2_moved, floor + offset) and is_valid(new_el2, el1_moved, floor + offset):
            new_setup = list(setup)
            new_setup[s1] = new_el1
            new_setup[s2] = new_el2
            return tuple(new_setup), floor + offset

    for s in singles:
        el = setup[s]
        if el[1] != 1:
            new = make_setup_single(-1, el)
            if new:
                yield new
        if el[1] != 4:
            new = make_setup_single(1, el)
            if new:
                yield new
    for d in doubles:
        s1, s2 = d
        el1 = setup[s1]
        el2 = setup[s2]
        if floor != 1:
            new = make_setup_double(-1, el1, el2)
            if new:
                yield new
        if floor != 4:
            new = make_setup_double(1, el1, el2)
            if new:
                yield new


# As it turns out, simply breadth-first searching the above will take much
# longer than we want, and we do need to prune further. The way we do so is
# by realizing that from a given vertex, the distance to the target vertex
# in which all devices are on the fourth floor, is invariant under permutation
# of all types. As such, we can consider the vertices only up to the equivalence
# relation defined by letting two vertices be equivalent if they can be obtained
# by permuting the types. In practice, we could do this in a few different ways.
# Perhaps the simplest is to mark all vertices belonging to an equivalence
# class during the search, but that turns out to be just as inefficient. More
# prudent turns out to be to define a canonical element in each equivalence
# class and use that (which is equivalent to defining a hash function on a general
# vertex which factors and defines a hash function on the set of equivalence
# classes).
def make_canonical(setup):
    """Creates the canonical representation of a given configuration."""
    seen = {}
    n = len(setup)//2
    key = defaultdict(int)
    for s in setup:
        key[s[0][0]] += 2**(s[1]-1)
    i = 0
    new_setup = []
    for s in sorted(setup, key=lambda x: key[x[0][0]]):
        label = s[0][0]
        if label not in seen:
            seen[label] = i
            i += 1
        new_setup.append((f'{seen[label]}{s[0][1]}', s[1]))
    sorted_setup = sorted(new_setup, key=lambda x: (x[1], x[0][0], x[0][1]))
    return tuple(sorted_setup)


# At this point, we have what we need to solve the problem
def solve(root):
    start = root, 1
    # We keep track of the current path length as part of our BFS queue.
    q = deque([(start, 0)])
    visited = set()
    # Also keep track of the current largest length to provide a status.
    prev_length = 0
    while q:
        state, length = q.popleft()
        if length != prev_length:
            prev_length = length
            print(f'Length: {length}, queue size: {len(q)}, visited vertices: {len(visited)}')
        if all(el[1] == 4 for el in state[0]):
            print(f'Result: {length}')
            break
        new = list(possible_actions(*state))
        for n in new:
            c = (make_canonical(n[0]), n[1])
            if c not in visited:
                q.append((c, length + 1))
                visited.add(c)


# Run this on my puzzle input
solve(root_part_1)
solve(root_part_2)
