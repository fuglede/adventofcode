# Input = target area: x=281..311, y=-74..-54
xmin = 281
xmax = 311
ymin = -74
ymax = -54


def hits(vx, vy):
    x = y = 0
    # Add a few sanity checks to ensure termination and one for performance
    while not (x > xmax or y < ymin or (vx == 0 and not xmin <= x <= xmax)):
        x += vx
        y += vy
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
        vy -= 1
        vx = max(0, vx - 1)


# We make a few remarks to bound the space of velocities to consider:
# If vx < 1, we never move towards our target
# If vx > xmax or vy < ymin, we overshoot in our first step
# If vy > -ymin, then we overshoot in the y-direction the step after we return to 0
valid = [
    vy for vx in range(1, xmax + 1) for vy in range(ymin, 1 - ymin) if hits(vx, vy)
]

# Part one
# Note that the height achieved for a given positive vy is vy + (vy - 1) + ... + 1 = vy*(vy + 1)/2
print(max(vy * (vy + 1) // 2 for vy in valid if vy > 0))

# Part two
print(len(valid))
