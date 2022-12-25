with open("input") as f:
    ls = f.read().strip().split("\n")

asint = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
assnafu = {4: "-", 3: "=", 2: "2", 1: "1", 0: "0"}

f = sum(sum(5**i * asint[x] for i, x in enumerate(l[::-1])) for l in ls)
fuel = f  # Copying the value just to make a bonus solution below
s = ""
while fuel != 0:
    rem = fuel % 5
    s += assnafu[rem]
    if rem > 2:
        fuel += 5 - rem
    fuel //= 5
print(s[::-1])


# Bonus z3 solution that requires less thought
from z3 import Int, Solver

digits = [Int(f"x{i}") for i in range(50)]
s = Solver()
for digit in digits:
    s.add(-2 <= digit, digit <= 2)
s.add(f == sum(5**i * digit for i, digit in enumerate(digits[::-1])))
s.check()
assnafu = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
print("".join(assnafu[s.model()[digit].as_long()] for digit in digits))
