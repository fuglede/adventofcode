from math import prod


with open("input") as f:
    data = f.read().strip()

res = 0
for l in data.split("\n\n")[-1].split("\n"):
    rxc, *nums = l.split()
    res += prod(map(int, rxc[:-1].split("x"))) >= 7 * sum(map(int, nums))

print(res)
