from queue import PriorityQueue


depth = 4080
mouth = (0, 0)
target = (14, 785)

geologic_index_cache = {}


def geologic_index(p):
    if p in geologic_index_cache:
        return geologic_index_cache[p]
    x, y = p
    if p == mouth or p == target:
        res = 0
    elif y == 0:
        res = x * 16807
    elif x == 0:
        res = y * 48271
    else:
        res = erosion_level((x - 1, y)) * erosion_level((x, y - 1))
    geologic_index_cache[p] = res
    return res


def erosion_level(p):
    return (geologic_index(p) + depth) % 20183


def erosion_type(p):
    return erosion_level(p) % 3


# Part one
print(sum(erosion_type((x, y)) for x in range(target[0] + 1) for y in range(target[1] + 1)))


# Part two
# 0: neither, 1: torch, 2: climbing gear
# 0: rocky, 1: wet, 2: narrow
def is_allowed_tool(p, tool):
    return erosion_type(p) != tool


def generate_actions(p, tool):
    this_type = erosion_type(p)
    for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new = (p[0] + dx, p[1] + dy)
        if new[0] < 0 or new[1] < 0:
            continue
        if is_allowed_tool(new, tool):
            yield (new, tool), 1
    for new_tool in range(3):
        if new_tool == tool:
            continue
        if is_allowed_tool(p, new_tool):
            yield (p, new_tool), 7


queue = PriorityQueue()
start_p = (0, 0)
start_tool = 1
start_time = 0
covered = {}

queue.put((start_time, (start_p, start_tool)))
while True:
    time, (p, tool) = queue.get()
    if (p, tool) == (target, 1):
        print(time)
        break
    if (p, tool) in covered:
        continue
    covered[(p, tool)] = time
    for (new_p, new_tool), effort in generate_actions(p, tool):
        queue.put((time + effort, (new_p, new_tool)))
