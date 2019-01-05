import re


with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

ns = [[int(x) for x in re.findall(r'-?\d+', s)] for s in lines]

# Find all clay blocks
clay = set()
for l, n in zip(lines, ns):
    for a in range(n[1], n[2] + 1):
        if l[0] == 'x':
            clay.add((n[0], a))
        else:
            clay.add((a, n[0]))

miny = min(y for (x, y) in clay)
maxy = max(y for (x, y) in clay)


# We will let the liquid flow in steps. In each step we first flow downwards,
# then fill up from the bottom. At the end of each step, we may have one or more
# new springs that will be used as the starting points for further iterations.
# The inputs to each step are the spring to start flowing from, as well as the
# sets of settled (~) and flowing (|) liquids, up to this step.
def flow(spring, settled, flowing):
    springs = set()
    x, y = spring
    # Flow downwards
    while (x, y) not in clay:
        if y >= miny:
            flowing.add((x, y))
        if y >= maxy:
            return settled, flowing, springs
        y += 1
    # Start filling up
    while True:
        y -= 1
        new = {(x, y)}
        xleft = x
        # Do we have walls to our left?
        hasleft = False
        while (xleft, y + 1) in clay.union(settled):
            xleft -= 1
            if (xleft, y) in clay:
                hasleft = True
                break
            new.add((xleft, y))
        # Do we have walls to our right?
        xright = x
        hasright = False
        while (xright, y + 1) in clay.union(settled):
            xright += 1
            if (xright, y) in clay:
                hasright = True
                break
            new.add((xright, y))
        # If we have walls to our left and right, all blocks we just saw will contain
        # settled liquid.
        if hasleft and hasright:
            settled = settled.union(new)
        # If one of the walls are missing, the liquid is not settled, and we have
        # one or two new springs.
        if not hasleft:
            springs.add((xleft, y))
        if not hasright:
            springs.add((xright, y))
        if not hasleft or not hasright:
            flowing = flowing.union(new).difference(settled).difference(springs)
            break
    return settled, flowing, springs


# With that in place, we can simply start the simulation by keeping the springs
# in a queue.
springs = [(500, 0)]
settled = set()
flowing = set()
done_springs = set()
while springs:
    spring = springs.pop(0)
    if spring in done_springs:
        continue
    done_springs.add(spring)
    settled, flowing, new_springs = flow(spring, settled, flowing)
    springs += new_springs

# Part one
print(len(flowing.union(settled)))

# Part two
print(len(settled))
