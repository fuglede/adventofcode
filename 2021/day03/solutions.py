with open("input") as f:
    ls = f.read().splitlines()

n = len(ls[0])


def one_counts(nums):
    return [sum(num[i] == "1" for num in nums) for i in range(n)]


# Part one
counts = one_counts(ls)
most_common = sum(2 ** (n - i - 1) * (counts[i] > len(ls) / 2) for i in range(n))
print(most_common * (2 ** n + ~most_common))


# Part two
def rating(comp):
    left = set(ls)
    for i in range(n):
        counts = one_counts(left)
        criterion = int(comp(len(left) / 2, counts[i]))
        left -= set(l for l in left if int(l[i]) != criterion)
        if len(left) == 1:
            (result,) = left
            return int(result, 2)


print(rating(float.__le__) * rating(float.__gt__))
