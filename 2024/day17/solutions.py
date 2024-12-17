from itertools import count

program = [2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]


def run(A):
    ptr = 0
    B = 0
    C = 0
    result = []
    while True:
        try:
            ins = program[ptr]
            op = program[ptr + 1]
        except:
            return result

        combo = [0, 1, 2, 3, A, B, C][op]

        match ins:
            case 0:
                A >>= combo
            case 1:
                B ^= op
            case 2:
                B = combo % 8
            case 3 if A:
                ptr = op - 2
            case 4:
                B ^= C
            case 5:
                result.append(combo % 8)
            case 6:
                B = A >> combo
            case 7:
                C = A >> combo
        ptr += 2


# Part 1
print(",".join(map(str, run(30344604))))


# Part 2
mid = int(next(A for i in count() if len(run(A := 10**i)) == len(program))) * 10
width = mid
spacing = width // 100
for matching_digits in range(1, len(program) + 1):
    mid = next(
        A
        for A in range(mid - width, mid + width, spacing)
        if len(res := run(A)) == len(program)
        and res[-matching_digits:] == program[-matching_digits:]
    )
    spacing //= 10
    width //= 10
    if spacing <= 10:
        spacing = 1
    if width <= 10000:
        width = 100000

print(mid)
