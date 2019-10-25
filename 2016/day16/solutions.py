def expand(a):
    b = a[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
    return f'{a}0{b}'


def checksum(s):
    if len(s) % 2 == 1:
        return s
    else:
        new_s = ''.join('1' if s[2*i] == s[2*i+1] else '0' for i in range(len(s)//2))
        return checksum(new_s)


def solve(l):
    s = '11011110011011101'
    while len(s) < l:
        s = expand(s)
    return checksum(s[:l])


print(solve(272))
print(solve(35651584))
