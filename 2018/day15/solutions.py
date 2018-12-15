from itertools import count
from collections import deque
import os

import matplotlib.pyplot as plt

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


class Unit:
    hp = 200
    is_alive = True


class Goblin(Unit):
    pass


class Elf(Unit):
    pass


class Board:
    def __init__(self, lines):
        self.field = {}
        self.num_elves = 0
        for y, l in enumerate(lines):
            for x, t in enumerate(l):
                if t == 'G':
                    self.field[(x, y)] = Goblin()
                elif t == 'E':
                    self.field[(x, y)] = Elf()
                    self.num_elves += 1
                else:
                    self.field[(x, y)] = t
        self._height = len(lines)
        self._width = len(lines[0])
        self.elf_attack = 3

    def _turn_order(self):
        units = [(pos, u) for pos, u in self.field.items() if isinstance(u, Unit)]
        return sorted(units, key=lambda x: (x[0][1], x[0][0]))

    def _find_target(self, pos, unit):
        squares = deque([pos])
        visited = set()
        path_to = {pos: []}
        while squares:
            square = squares.popleft()
            if square in visited:
                continue
            visited.add(square)
            for (dx, dy) in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                new = (square[0] + dx, square[1] + dy)
                if new in visited or new not in self.field:
                    continue
                if new not in path_to:
                    path_to[new] = list(path_to[square])
                    path_to[new].append(new)
                at_loc = self.field[new]
                if isinstance(unit, Goblin) and isinstance(at_loc, Elf) or isinstance(unit, Elf) and isinstance(at_loc, Goblin):
                    return new, path_to[new]
                elif at_loc == '.':
                    squares.append(new)
        return pos, [pos]

    def _take_step(self, pos, unit):
        target, path = self._find_target(pos, unit)
        if len(path) == 1:
            return pos
        self.field[path[0]] = unit
        self.field[pos] = '.'
        return path[0]

    def render(self):
        def render_square(s):
            if isinstance(s, Goblin):
                return 'G'
            if isinstance(s, Elf):
                return 'E'
            return s
        return '\n'.join(''.join(render_square(self.field[(x, y)]) for x in range(self._width)) for y in range(self._height))

    def render_image(self):
        def make_color(s):
            if isinstance(s, Goblin):
                return (.8, 0, 0)
            elif isinstance(s, Elf):
                return (0, .8, 0)
            elif s == '#':
                return (.2, .2, .2)
            else:
                return (.8, .8, .8)
        fig, ax = plt.subplots(1, 1)
        plt.axis('off')
        ax.imshow([[make_color(self.field[(x, y)]) for x in range(self._width)] for y in range(self._height)])
        return fig

    def _attack(self, pos, unit):
        target_type = Goblin if isinstance(unit, Elf) else Elf
        targets = []
        for (dx, dy) in ((0, -1), (-1, 0), (1, 0), (0, 1)):
            target_pos = (pos[0] + dx, pos[1] + dy)
            target = self.field[target_pos]
            if isinstance(target, target_type):
                targets.append((target_pos, target))
        if targets:
            target = min(targets, key=lambda target: target[1].hp)
            if target_type == Goblin:
                target[1].hp -= self.elf_attack
            else:
                target[1].hp -= 3
            if target[1].hp <= 0:
                target[1].is_alive = False
                self.field[target[0]] = '.'

    def do_round(self):
        units = self._turn_order()
        for unit in units:
            if not unit[1].is_alive:
                continue
            goblins = [u for u in self.field.values() if isinstance(u, Goblin)]
            elves = [u for u in self.field.values() if isinstance(u, Elf)]
            num_survivors = len(elves)
            if not goblins:
                return sum(u.hp for u in elves), num_survivors
            if not elves:
                return sum(u.hp for u in goblins), num_survivors
            pos = self._take_step(unit[0], unit[1])
            self._attack(pos, unit[1])


# Part one
b = Board(lines)
for i in count():
    res = b.do_round()
    if res:
        print(i*res[0])
        break

# Part two
for ap in count():
    b = Board(lines)
    b.elf_attack = ap
    for i in count():
        res = b.do_round()
        if res:
            break
    if res[1] == b.num_elves:
        print(i*res[0])
        break

# Make a pretty video for part one
b = Board(lines)
os.makedirs('anim')
for i in count():
    res = b.do_round()
    fig = b.render_image()
    fig.savefig(f'anim/{i:02d}.png', dpi=200, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    if res:
        break
