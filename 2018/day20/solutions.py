import networkx as nx


with open('input') as f:
    data = list(f.read().strip())

dirs = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}


def parse(current, data, g, room_stack, end_stack, already_done):
    if len(data) in already_done:
        return
    already_done.add(len(data))
    while data:
        s = data.pop(0)
        if s in 'NSEW':
            g.add_edge(current, current + dirs[s])
            current += dirs[s]
        elif s == '(':
            room_stack.append(current)
            end_stack.append([])
        elif s == '|' or s == ')':
            end_stack[-1].append(current)
            current = room_stack[-1]
            if s == ')':
                room_stack.pop()
                ends = end_stack.pop()
                for end in set(ends):
                    parse(end, list(data), g, room_stack, end_stack, already_done)
                return


g = nx.Graph()
parse(0, data, g, [], [], set())

# Part one
print(max(nx.shortest_path_length(g, 0).values()))

# Part two
print(sum(length >= 1000 for length in nx.shortest_path_length(g, 0).values()))
