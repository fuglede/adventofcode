from math import inf, prod
import re

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("\d+", x))) for x in ls]


def solve(blueprint, total_time):
    # We find the optimum through exhaustive DFS. The only trick
    # necessary along the way is to collapse states that will
    # give rise to equivalent results.

    def actions(state):
        time, robots, ores = state
        new_time = time + 1
        time_left = total_time - time

        def new_state(new_robots, new_ores):
            new_ores = [new_ores[i] + robots[i] for i in range(4)]
            # As we can never use more than 4 ore, or 20 clay, or 20
            # obsidian at any given time, we can collapse some states
            # that represent more ore than we could ever use. For
            # instance, if we generate 4 clay per turn, there's no
            # reason to keep track of clay anymore.
            # time_left = 5, robots[0] = 4
            for i, max_usable in zip(range(3), (4, 20, 20)):
                ore_max_can_use = max_usable * time_left
                ore_will_get = robots[i] * (time_left - 1)
                new_ores[i] = min(new_ores[i], ore_max_can_use - ore_will_get)
            return (new_time, tuple(new_robots), tuple(new_ores))

        # As above, only build robots if we do not already have so many
        # that building another one doesn't make sense. If it's possible
        # to build a geode robot, doing so is always optimal, and we don't
        # have to worry about other possible actions.

        # Build geode robot
        if ores[0] >= blueprint[5] and ores[2] >= blueprint[6]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[5]
            new_ores[2] -= blueprint[6]
            new_robots = list(robots)
            new_robots[3] += 1
            yield new_state(new_robots, new_ores)
            return

        # Build ore robot
        if robots[0] < 4 and ores[0] >= blueprint[1]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[1]
            new_robots = list(robots)
            new_robots[0] += 1
            yield new_state(new_robots, new_ores)

        # Build clay robot
        if robots[1] < 20 and ores[0] >= blueprint[2]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[2]
            new_robots = list(robots)
            new_robots[1] += 1
            yield new_state(new_robots, new_ores)

        # Build obsidian robot
        if robots[2] < 20 and ores[0] >= blueprint[3] and ores[1] >= blueprint[4]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[3]
            new_ores[1] -= blueprint[4]
            new_robots = list(robots)
            new_robots[2] += 1
            yield new_state(new_robots, new_ores)

        # Do nothing
        yield new_state(robots, ores)

    # States are represented as (time, robots by type, ore by type)
    state = (0, (1, 0, 0, 0), (0, 0, 0, 0))
    seen = set()
    stack = [state]
    best = -inf
    while stack:
        state = stack.pop()
        time, robots, ores = state
        if time == total_time:
            if ores[3] > best:
                best = ores[3]
            continue
        for new_state in actions(state):
            if new_state in seen:
                continue
            seen.add(new_state)
            stack.append(new_state)
    return best


# Part 1
print(sum(blueprint[0] * solve(blueprint, 24) for blueprint in ns))

# Part 2
print(prod(solve(blueprint, 32) for blueprint in ns[:3]))
