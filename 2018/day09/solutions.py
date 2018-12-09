from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    before: 'Node'
    after: 'Node'


def best_score(num_players, num_marbles):
    scores = defaultdict(int)
    player = 0
    current = Node(0, None, None)
    current.before = current
    current.after = current
    for placed in range(1, num_marbles + 1):
        if placed % 23 == 0:
            scores[player] += placed
            for _ in range(7):
                current = current.before
            before = current.before
            after = current.after
            scores[player] += current.value
            before.after = after
            after.before = before
            current = after
        else:
            before = current.after
            after = before.after
            new = Node(placed, before, after)
            before.after = new
            after.before = new
            current = new
        player = player % num_players + 1
    return max(scores.values())


# Part one
print(best_score(473, 70904))

# Part two
print(best_score(473, 7090400))
