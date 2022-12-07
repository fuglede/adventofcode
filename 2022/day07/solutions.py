from collections import defaultdict

with open("input") as f:
    ls = [x.strip() for x in f.readlines()]

sizes = defaultdict(int)
stack = []
for l in ls:
    if l.startswith("$ cd "):
        x = l[5:]
        if x == "/":
            stack = []
        elif x == "..":
            stack.pop()
        else:
            stack.append(x)
    elif l[0] != "$":
        a, _ = l.split()
        if a != "dir":
            for i in range(len(stack) + 1):
                path = "/" + "/".join(stack[:i])
                sizes[path] += int(a)


# Part 1
print(sum(filter(lambda v: v <= 100000, sizes.values())))

# Part 2
unused = 70000000 - sizes["/"]
need = 30000000 - unused
print(min(filter(lambda v: v >= need, sizes.values())))
