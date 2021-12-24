from z3 import If, Int, Optimize

# Some analysis is required before we start here. First of all, we notice that all of
# the 14 checks are very similar:
#
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 11,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 16, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 12,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 11, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 13,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 12, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -5,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 12, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -3,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 12, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 14,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 2,  mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 15,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 11, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -16, eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 4,  mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 14,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 12, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 1,  add x 15,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 9,  mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -7,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 10, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -11, eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 11, mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -6,  eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 6,  mul y x, add z y,
# inp w, mul x 0, add x z, mod x 26, div z 26, add x -11, eql x w, eql x 0, mul y 0, add y 25, mul y x, add y 1, mul z y, mul y 0, add y w, add y 15, mul y x, add z y
#
# Up to some parameters changing, every operation is the same. Let us track the changing parameters
a = [1, 1, 1, 26, 26, 1, 1, 26, 1, 1, 26, 26, 26, 26]
b = [11, 12, 13, -5, -3, 14, 15, -16, 14, 15, -7, -11, -6, -11]
c = [16, 11, 12, 12, 12, 2, 11, 4, 12, 9, 10, 11, 6, 15]


# Let us also denote the i'th input digit w[i]. Then each iteration boils down to the following:
#
# x = 0
# x += z
# x %= 26
# z //= a[i]
# x += b[i]
# x = int(x == w[i])
# x = int(x == 0)
# y = 0
# y += 25
# y *= x
# y += 1
# z *= y
# y = 0
# y += w[i]
# y += c[i]
# y *= x
# z += y
#
# This boils down to the following, noting in particular that the equality check is turned into
# an inequality check by x = int(x == 0), and that the two branches obtained by considering
# the cases of x == 0 and x == 1 separately, both simplify greatly:
#
# if (z % 26) != w[i] - b[i]:
#     z //= a[i]
#     z = z*26 + w[i] + c[i]
# else:
#     z //= a[i]
#
# In particular, the full program can be written as follows:
#
# z = 0
# for wi, ai, bi, ci in zip(w, a, b, c):
#    z = z // ai if z % 26 + bi == wi else z // ai * 26 + wi + ci
#
# It is possible to further simplify this a bit further by noting that z // 1 is the same as z,
# that a[i] is 1 exactly when b[i] is positive, and that when b[i] is positive, it is always
# greater than 10, meaning that (z % 26) != w[i] - b[i] is always True. Notably, this means
# that in 7 of the 14 cases, z gains an additional digit when seen as a base 26 integer, so
# that it _has_ to hit the "else" case in the remaining 7 cases to ever have a chance to be
# zero at the end of the day. This additional constraint limits the number of possible values
# of each w[i] enough that they can be searched directly. In practice, we don't have to
# bother with any of this, since the above form is already enough that it can be handled by Z3.
def solve(part1):
    s = Optimize()
    # Define the variables whose values are to be determined. At the end of the day, these
    # values are to be maximized or minimized. Z3 can handle multiple objectives and by default
    # treats them in the order they are declared.
    w = [Int(f"w{i}") for i in range(14)]
    for wi in w:
        # Restrict each w[i] to be between 1 and 9.
        s.add(wi >= 1, wi <= 9)
        (s.maximize if part1 else s.minimize)(wi)
    # Convert the final piece of Python above to operations on the Z3 variables.
    z = 0
    for wi, ai, bi, ci in zip(w, a, b, c):
        z = If(z % 26 + bi == wi, z / ai, z / ai * 26 + wi + ci)
    # Require that after all steps, z is 0.
    s.add(z == 0)
    s.check()
    # Convert the now optimal values into a 14-digit number.
    return sum(10 ** (13 - i) * s.model()[wi].as_long() for i, wi in enumerate(w))


print(solve(True))
print(solve(False))
