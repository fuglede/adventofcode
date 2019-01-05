from itertools import count


class Group:
    def __init__(self, army, units, unit_hp, immunities, weaknesses, attack_damage, attack_type, initiative):
        self.army = army
        self.units = units
        self.unit_hp = unit_hp
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative

    def effective_power(self):
        return self.units * self.attack_damage

    def calc_damage(self, group):
        factor = 1
        if self.attack_type in group.immunities:
            factor = 0
        elif self.attack_type in group.weaknesses:
            factor = 2
        return factor * self.effective_power()

    def select_target(self, possible_targets):
        possible_targets = [p for p in possible_targets if self.calc_damage(p) > 0]
        if not possible_targets:
            return None
        return max(possible_targets, key=lambda group: (self.calc_damage(group), group.effective_power(), group.initiative))

    def attack(self, group):
        return group.receive_damage(self.calc_damage(group))

    def receive_damage(self, damage):
        units_lost = damage // self.unit_hp
        self.units = max(self.units - units_lost, 0)
        return units_lost > 0


def select_targets(immune_system, infection):
    remaining_immune_system = [g for g in immune_system if g.units > 0]
    remaining_infection = [g for g in infection if g.units > 0]
    targets = {}
    for g in sorted(immune_system + infection, key=lambda group: (-group.effective_power(), -group.initiative)):
        possible_targets = remaining_immune_system if g.army == 'infection' else remaining_infection
        target = g.select_target(possible_targets)
        if target:
            targets[g] = target
            possible_targets.remove(target)
    return targets


def attack(immune_system, infection):
    targets = select_targets(immune_system, infection)
    units_lost = False
    for g in sorted(immune_system + infection, key=lambda group: -group.initiative):
        if g in targets:
            units_lost |= g.attack(targets[g])
    return units_lost


for boost in count():
    im1 = Group('immune system', 597, 4458, [], [], 73, 'slashing', 6)
    im2 = Group('immune system', 4063, 9727, [], ['radiation'], 18, 'radiation', 9)
    im3 = Group('immune system', 2408, 5825, ['fire', 'radiation'], ['slashing'], 17, 'slashing', 2)
    im4 = Group('immune system', 5199, 8624, ['fire'], [], 16, 'radiation', 15)
    im5 = Group('immune system', 1044, 4485, [], ['bludgeoning'], 41, 'radiation', 3)
    im6 = Group('immune system', 4890, 9477, ['cold'], ['fire'], 19, 'slashing', 7)
    im7 = Group('immune system', 1280, 10343, [], [], 64, 'cold', 19)
    im8 = Group('immune system', 609, 6435, [], [], 86, 'cold', 17)
    im9 = Group('immune system', 480, 2750, [], ['cold'], 57, 'fire', 11)
    im10 = Group('immune system', 807, 4560, ['fire', 'slashing'], ['bludgeoning'], 56, 'radiation', 8)

    in1 = Group('infection', 1237, 50749, ['cold', 'slashing', 'bludgeoning'], ['radiation'], 70, 'radiation', 12)
    in2 = Group('infection', 4686, 25794, ['cold', 'slashing'], ['bludgeoning'], 10, 'bludgeoning', 14)
    in3 = Group('infection', 1518, 38219, [], ['slashing', 'fire'],  42, 'radiation', 16)
    in4 = Group('infection', 4547, 21147, ['radiation'], ['fire'], 7, 'slashing', 4)
    in5 = Group('infection', 1275, 54326, ['cold'], [], 65, 'cold', 20)
    in6 = Group('infection', 436, 36859, ['fire', 'cold'], [], 164, 'fire', 18)
    in7 = Group('infection', 728, 53230, [], ['radiation', 'bludgeoning'], 117, 'fire', 5)
    in8 = Group('infection', 2116, 21754, [], [], 17, 'bludgeoning', 10)
    in9 = Group('infection', 2445, 21224, ['cold'], [], 16, 'cold', 13)
    in10 = Group('infection', 3814, 22467, [], ['bludgeoning', 'radiation'], 10, 'cold', 1)

    immune_system = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10]
    infection = [in1, in2, in3, in4, in5, in6, in7, in8, in9, in10]
    for g in immune_system:
        g.attack_damage += boost

    while not all(g.units == 0 for g in immune_system) and not all(g.units == 0 for g in infection):
        if not attack(immune_system, infection):
            break

    # Part one
    if boost == 0:
        print(sum(g.units for g in immune_system + infection))

    # Part two
    if sum(g.units for g in infection) == 0:
        print(sum(g.units for g in immune_system))
        break
