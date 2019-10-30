from dataclasses import dataclass
import heapq


@dataclass
class Player:
    mana: int = 500
    hp: int = 50
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0
    armor: int = 0

    def __lt__(self, other):
        return True


@dataclass
class Enemy:
    damage: int = 9
    hp: int = 58

    def __lt__(self, other):
        return True


def solve(part_two):
    h = []
    heapq.heappush(h, (0, Player(), Enemy()))
    while True:
        mana_spent, player, enemy = heapq.heappop(h)

        # Copy player and enemy
        player = Player(player.mana, player.hp,
                        player.shield_timer, player.poison_timer, player.recharge_timer, 0)
        if part_two:
            player.hp -= 1
            if player.hp == 0:
                continue
        enemy = Enemy(enemy.damage, enemy.hp)

        # Apply effects
        def apply_effects(player, enemy, mana_spent):
            if player.shield_timer > 0:
                player.armor = 7
                player.shield_timer -= 1
            if player.poison_timer > 0:
                enemy.hp -= 3
                player.poison_timer -= 1
            if player.recharge_timer > 0:
                player.mana += 101
                player.recharge_timer -= 1
            if enemy.hp <= 0:
                return mana_spent

        # Magic missile
        p = apply_effects(player, enemy, mana_spent)
        if p:
            break
        if player.mana >= 53:
            new_mana_spent = mana_spent + 53
            new_player = Player(player.mana - 53, player.hp,
                                player.shield_timer, player.poison_timer, player.recharge_timer, 0)
            new_enemy = Enemy(enemy.damage, enemy.hp - 4)
            p = apply_effects(new_player, new_enemy, new_mana_spent)
            if p:
                return p
            new_player.hp -= max(enemy.damage - player.armor, 1)
            if new_player.hp > 0:
                heapq.heappush(h, (new_mana_spent, new_player, new_enemy))

        # Drain
        if player.mana >= 73:
            new_mana_spent = mana_spent + 73
            new_player = Player(player.mana - 73, player.hp + 2,
                                player.shield_timer, player.poison_timer, player.recharge_timer, 0)
            new_enemy = Enemy(enemy.damage, enemy.hp - 2)
            p = apply_effects(new_player, new_enemy, new_mana_spent)
            if p:
                return p
            new_player.hp -= max(enemy.damage - player.armor, 1)
            if new_player.hp > 0:
                heapq.heappush(h, (new_mana_spent, new_player, new_enemy))

        # Shield
        if player.mana >= 113 and player.shield_timer == 0:
            new_mana_spent = mana_spent + 113
            new_player = Player(player.mana - 113, player.hp,
                                6, player.poison_timer, player.recharge_timer, 0)
            new_enemy = Enemy(enemy.damage, enemy.hp)
            p = apply_effects(new_player, new_enemy, new_mana_spent)
            if p:
                return p
            new_player.hp -= max(enemy.damage - player.armor, 1)
            if new_player.hp > 0:
                heapq.heappush(h, (new_mana_spent, new_player, new_enemy))
        # Poison
        if player.mana >= 173 and player.poison_timer == 0:
            new_mana_spent = mana_spent + 173
            new_player = Player(player.mana - 173, player.hp,
                                player.shield_timer, 6, player.recharge_timer, 0)
            new_enemy = Enemy(enemy.damage, enemy.hp)
            p = apply_effects(new_player, new_enemy, new_mana_spent)
            if p:
                return p
            new_player.hp -= max(enemy.damage - player.armor, 1)
            if new_player.hp > 0:
                heapq.heappush(h, (new_mana_spent, new_player, new_enemy))
        # Recharge
        if player.mana >= 229 and player.recharge_timer == 0:
            new_mana_spent = mana_spent + 229
            new_player = Player(player.mana - 229, player.hp,
                                player.shield_timer, player.poison_timer, 5, 0)
            new_enemy = Enemy(enemy.damage, enemy.hp)
            p = apply_effects(new_player, new_enemy, new_mana_spent)
            if p:
                return p
            new_player.hp -= max(enemy.damage - player.armor, 1)
            if new_player.hp > 0:
                heapq.heappush(h, (new_mana_spent, new_player, new_enemy))


print(solve(False))
print(solve(True))
