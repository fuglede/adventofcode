from dataclasses import dataclass
from itertools import chain, combinations


weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]


@dataclass
class Player:
    damage: int
    armor: int
    hp: int


def game_won(player, enemy):
    while True:
        enemy.hp -= max(player.damage - enemy.armor, 1)
        if enemy.hp < 0:
            return True
        player.hp -= max(enemy.damage - player.armor, 1)
        if player.hp < 0:
            return False


def make_combinations():
    for w in combinations(weapons, 1):
        for a in chain(combinations(armors, 0), combinations(armors, 1)):
            for r in chain(combinations(rings, 0), combinations(rings, 1), combinations(rings, 2)):
                yield [w[0][i] + sum(armor[i] for armor in a) + sum(ring[i] for ring in r) for i in range(3)]


# Part one
best = float('inf')
for c in make_combinations():
    cost, damage, armor = c
    player = Player(damage, armor, 100)
    enemy = Player(8, 2, 100)
    if game_won(player, enemy):
        best = min(best, cost)
print(best)

# Part two
best = -float('inf')
for c in make_combinations():
    cost, damage, armor = c
    player = Player(damage, armor, 100)
    enemy = Player(8, 2, 100)
    if not game_won(player, enemy):
        best = max(best, cost)
print(best)
