with open("input") as f:
    ls = f.read().strip().split("\n")


def joltage(a, to_choose):
    res = i = 0
    for end_index in range(len(a) - to_choose, len(a)):
        i = max(range(i, end_index + 1), key=a.__getitem__) + 1
        res = res * 10 + a[i - 1]
    return res


for to_choose in (2, 12):
    print(sum(joltage(list(map(int, l)), to_choose) for l in ls))
