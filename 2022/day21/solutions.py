import re

with open("input") as f:
    ls = f.read().strip().split("\n")

exec(
    "\n".join(
        "def " + re.sub("([a-z]{4})", r"\1()", l).replace(":", ": return") for l in ls
    )
)

# Part 1
print(root())

# Part 2
# The condition we are trying to check is mcnw() == wqdw(). Through
# a bit of experimentation, one finds that wqdw is constant in humn,
# while mcnw is monotone, so we can simply binary search on the latter.
target = wqdw()
low = 0
high = 10000000000000
while True:
    mid = (high + low) // 2

    def humn():
        return mid

    res = mcnw()
    if res == target:
        print(mid)
        break
    elif res < target:
        high = mid
    else:
        low = mid
