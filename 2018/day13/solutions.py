with open('input') as f:
    lines = f.readlines()

tracks = {x + y*1j: t for y, l in enumerate(lines) for x, t in enumerate(l)}
dirs = {'>': 1, '<': -1, '^': -1j, 'v': 1j}


def make_carts():
    return [[pos, dirs[d], 0] for pos, d in tracks.items() if d in dirs]


def move_cart(cart):
    track = tracks[cart[0]]
    if track == '+':
        if cart[2] == 0:
            cart[1] *= -1j
        elif cart[2] == 2:
            cart[1] *= 1j
        cart[2] = (cart[2] + 1) % 3
    elif track in ('/', '\\'):
        cart[1] *= 1j
        if (cart[1].imag and track == '/') or (cart[1].real and track == '\\'):
            cart[1] *= -1
    cart[0] += cart[1]


# Part one
def part_one():
    carts = make_carts()
    while True:
        for cart in carts:
            move_cart(cart)
            if any(c for c in carts if c != cart and c[0] == cart[0]):
                return cart[0]


print(part_one())


# Part two
def part_two():
    carts = make_carts()
    while True:
        if len(carts) == 1:
            return carts[0][0]
        carts.sort(key=lambda cart: cart[0].imag)
        for cart in carts:
            move_cart(cart)
            crashed = [c for c in carts if c != cart and c[0] == cart[0]]
            if crashed:
                carts = [c for c in carts if c != cart and c != crashed[0]]


print(part_two())
