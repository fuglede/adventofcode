from statistics import median

with open("input") as f:
    ls = f.read().strip().split("\n")

match = {"}": "{", "]": "[", ")": "(", ">": "<"}
score1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def score(l):
    stack = []
    for x in l:
        if x in score2:
            stack.append(x)
        elif stack.pop() != match[x]:
            return False, score1[x]
    return True, sum(score2[x] * 5 ** i for i, x in enumerate(stack))


# Part one
print(sum(s for valid, s in map(score, ls) if not valid))

# Part two
print(median(s for valid, s in map(score, ls) if valid))
