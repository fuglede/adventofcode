from collections import defaultdict
from heapq import heappop, heappush
import re

with open("input") as f:
    ls = f.read().strip().split("\n")

flows = {}
neighbours = defaultdict(list)
for l in ls:
    this = l.split()[1]
    flow = int(re.findall("\d+", l)[0])
    flows[this] = flow
    for neighbour in l.split()[9:]:
        neighbours[this].append(neighbour.replace(",", ""))


# We solve both parts by searching in the space of states consisting of
# the current location(s), the current time, and which valves have been
# opened. We use a priority queue to always search from the currently
# best known state. To make sure that we get the best possible state
# once we get to the end time, we add a penalty to any given move; the
# value of the penalty must be chosen so that we don't spend forever
# searching the early times, and so that we don't get to the end so fast
# that the solution isn't optimal; for the given input, 100 does the job.
penalty = 100


# Part 1
def actions(state):
    score, loc, time, opened = state
    for neighbour in neighbours[loc]:
        yield (score + penalty, neighbour, time + 1, opened)
    if loc not in opened and flows[loc] != 0:
        new_opened = opened | {loc}
        yield (
            score - (30 - time - 1) * flows[loc] + penalty,
            loc,
            time + 1,
            new_opened,
        )


q = [(0, "AA", 0, frozenset())]
seen = {q[0]}
while q:
    state = heappop(q)
    score, _, time, _ = state
    if time == 30:
        print(30 * penalty - score)
        break
    for new_state in actions(state):
        if new_state in seen:
            continue
        seen.add(new_state)
        heappush(q, new_state)


# Part 2
def actions2(state):
    score, loc, loc2, time, opened = state
    # Both move
    for neighbour in neighbours[loc]:
        for neighbour2 in neighbours[loc2]:
            yield (score + penalty, neighbour, neighbour2, time + 1, opened)
    # Both open
    if (
        loc != loc2
        and loc not in opened
        and loc2 not in opened
        and flows[loc] != 0
        and flows[loc2] != 0
    ):
        new_opened = opened | {loc, loc2}
        yield (
            score
            - (26 - time - 1) * flows[loc]
            - (26 - time - 1) * flows[loc2]
            + penalty,
            loc,
            loc2,
            time + 1,
            new_opened,
        )
    # We open, elephant moves
    if loc not in opened and flows[loc] != 0:
        new_opened = opened | {loc}
        for neighbour2 in neighbours[loc2]:
            yield (
                score - (26 - time - 1) * flows[loc] + penalty,
                loc,
                neighbour2,
                time + 1,
                new_opened,
            )
    # We move, elephant opens
    if loc2 not in opened and flows[loc2] != 0:
        new_opened = opened | {loc2}
        for neighbour in neighbours[loc]:
            yield (
                score - (26 - time - 1) * flows[loc2] + penalty,
                neighbour,
                loc2,
                time + 1,
                new_opened,
            )


q = [(0, "AA", "AA", 0, frozenset())]
seen = {q[0]}
while q:
    state = heappop(q)
    score, _, _, time, _ = state
    if time == 26:
        print(26 * penalty - score)
        break
    for new_state in actions2(state):
        if new_state in seen:
            continue
        seen.add(new_state)
        heappush(q, new_state)
