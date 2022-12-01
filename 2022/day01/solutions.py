with open("input") as f:
    data = f.read().strip()

groups = data.split("\n\n")
group_sums = [sum(map(int, group.split("\n"))) for group in groups]

# Part 1
print(max(group_sums))

# Part 2
print(sum(sorted(group_sums)[-3:]))
