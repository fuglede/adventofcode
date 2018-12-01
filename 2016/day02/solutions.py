with open('input') as f:
    dirs = [x.strip() for x in f.readlines()]


# Part one
def location_to_key(loc):
    return loc[0]*3 + loc[1] + 1


location = [1, 1]
keys = []
for d in dirs:
    for x in d:
        if x == 'L':
            location[1] = max(location[1]-1, 0)
        if x == 'U':
            location[0] = max(location[0]-1, 0)
        if x == 'R':
            location[1] = min(location[1]+1, 2)
        if x == 'D':
            location[0] = min(location[0]+1, 2)
    keys.append(location_to_key(location))
print(keys)

# Part two
location = (-2, 0)
keys = []
key_map = {
    (0, 2): 1,
    (-1, 1): 2,
    (0, 1): 3,
    (1, 1): 4,
    (-2, 0): 5,
    (-1, 0): 6,
    (0, 0): 7,
    (1, 0): 8,
    (2, 0): 9,
    (-1, -1): 'A',
    (-1, 0): 'B',
    (-1, 1): 'C',
    (0, -2): 'D'
}
left_edges = [(-2, 0), (-1, 1), (0, 2), (-1, -1), (0, -2)]
right_edges = [(2, 0), (1, 1), (0, 2), (1, -1), (0, -2)]
top_edges = [(-2, 0), (-1, 1), (0, 2), (1, 1), (2, 0)]
bottom_edges = [(-2, 0), (-1, -1), (0, -2), (1, -1), (2, 0)]
for d in dirs:
    for x in d:
        new_loc = list(location)
        if x == 'L':
            if location not in left_edges:
                new_loc[0] -= 1
        if x == 'U':
            if location not in top_edges:
                new_loc[1] += 1
        if x == 'R':
            if location not in right_edges:
                new_loc[0] += 1
        if x == 'D':
            if location not in bottom_edges:
                new_loc[1] -= 1
        location = tuple(new_loc)
    keys.append(key_map[location])
print(keys)
