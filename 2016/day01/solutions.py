with open('input') as f:
    data = f.read()
inputs = list(map(str.strip, data.split(',')))

# Part one
location = 0 + 0j
current_direction = 1j
for i in inputs:
    turn_direction = i[0]
    distance = int(i[1:])
    if turn_direction == 'R':
        current_direction *= -1j
    else:
        current_direction *= 1j
    location += current_direction * distance
print(abs(location.real) + abs(location.imag))


# Part two
def first_visited():
    location = 0 + 0j
    current_direction = 1j
    visited = set()
    for i in inputs:
        turn_direction = i[0]
        distance = int(i[1:])
        if turn_direction == 'R':
            current_direction *= -1j
        else:
            current_direction *= 1j
        for _ in range(distance):
            location += current_direction
            if location in visited:
                return abs(location.real) + abs(location.imag)
            visited.add(location)


print(first_visited())
