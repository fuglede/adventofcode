import networkx as nx

with open("input") as f:
    gs = f.read().strip().split("\n\n")

rules = [tuple(map(int, l.split("|"))) for l in gs[0].split("\n")]
updates = [tuple(map(int, l.split(","))) for l in gs[1].split("\n")]

unsorted_updates = {
    update
    for update in updates
    if any(
        a in update and b in update and update.index(a) > update.index(b)
        for a, b in rules
    )
}

# Part 1
print(
    sum(
        update[len(update) // 2] for update in updates if update not in unsorted_updates
    )
)

# Part 2
sorted_updates = [
    list(
        nx.topological_sort(
            nx.DiGraph((a, b) for a, b in rules if a in update and b in update)
        )
    )
    for update in unsorted_updates
]

print(sum(update[len(update) // 2] for update in sorted_updates))
