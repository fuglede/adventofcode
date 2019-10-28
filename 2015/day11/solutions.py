def increase(s, i):
    if s[i] == 'z':
        s[i] = 'a'
        increase(s, i - 1)
    else:
        s[i] = chr(ord(s[i]) + 1)


def has_three_straight(s):
    streak = 1
    for i in range(1, len(s)):
        if ord(s[i-1]) == ord(s[i]) - 1:
            streak += 1
            if streak == 3:
                return True
        else:
            streak = 1
    return False


def has_no_iou(s):
    return 'i' not in s and 'o' not in s and 'u' not in s


def has_double_pair(s):
    in_pair = True
    pairs = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            if in_pair:
                pairs += 1
                if pairs == 2:
                    return True
                in_pair = False
            else:
                in_pair = True
        else:
            in_pair = True
    return False


def solve(s):
    while True:
        increase(s, len(s)-1)
        if has_three_straight(s) and has_no_iou(s) and has_double_pair(s):
            return ''.join(s)


# Part one
s = list('hxbxwxba')
print(solve(s))

# Part two
print(solve(s))
