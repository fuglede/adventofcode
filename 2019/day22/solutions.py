import re

with open('input') as f:
    ls = [l.strip() for l in f.readlines()]
    ws = [l.split() for l in ls]
    ns = [list(map(int, re.findall('-?\d+', x))) for x in ls]


# Part one
def cut(l, s):
    return l[s:] + l[:s]


def deal_with_inc(l, s):
    new_l = [0]*len(l)
    i = 0
    for c in range(len(l)):
        new_l[i] = l[c]
        i = (i + s) % len(l)
    return new_l


def deal_into_new(l):
    return l[::-1]


l = list(range(10007))
for w, n in zip(ws, ns):
    if w[0] == 'cut':
        l = cut(l, n[0])
    elif w[0] == 'deal' and w[1] == 'with':
        l = deal_with_inc(l, n[0])
    else:
        l = deal_into_new(l)

print(l.index(2019))


# Various helpers for modular arithmetic stolen from StackOverflow
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


# Part two
# We want to calculate the inverse of the operation above, then
# apply it a whole lot of times. The key insight is that each
# of the inverse operations is an affine transformation
#   x |-> a*x+b % length,
# so we just need to find (a, b) corresponding to the entire shuffle,
# then apply that a large number of times.
length = 119315717514047
rounds = 101741582076661
a, b = (1, 0)
for i, (w, n) in list(enumerate(zip(ws, ns)))[::-1]:
    if w[0] == 'cut':
        a, b = a, b + n[0]
    elif w[0] == 'deal' and w[1] == 'with':
        m = modinv(n[0], length)
        a, b = a*m, b*m
    else:
        a, b = -a, -b-1
    a %= length
    b %= length

# At this point we have a and b, and just need to calculate the power
# of x |-> a*x+b % length. This is itself an affine transformation,
# whose coefficients we need to find. It is easy to see by induction
# that the n'th power is
#   x |-> a^n x + a^{n-1}b + a^{n-2}n + ... + ab + b % length
# whose slope is a^n and whose intercept is
#   b(1 + a + ... + a^{n-1}) = b * (a^n-1) * (a-1)^{-1}
am = pow_mod(a, rounds, length)
bm = b*(pow_mod(a, rounds, length)-1) * modinv(a-1, length)
print((am*2020 + bm) % length)
