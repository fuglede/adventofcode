with open('input') as f:
    words = [x.strip() for x in f.readlines()]


# Part one
def supports_tls(s):
    in_bracket = False
    has_abba = False
    state = 0
    for letter in s:
        if letter == '[':
            in_bracket = True
            state = 0
        elif letter == ']':
            in_bracket = False
            state = 0
        elif state == 0:
            a = letter
            state = 1
        elif state == 1:
            if a != letter:
                b = letter
                state = 2
            else:
                a = letter
                state = 1
        elif state == 2:
            if b == letter:
                state = 3
            else:
                if prev_letter != letter:
                    a = prev_letter
                    b = letter
                    state = 2
                else:
                    state = 1
                    a = letter
        elif state == 3:
            if a == letter:
                if in_bracket:
                    return False
                else:
                    has_abba = True
                    state = 0
            else:
                if prev_letter != letter:
                    a = prev_letter
                    b = letter
                    state = 2
                else:
                    state = 1
                    a = letter
        prev_letter = letter
    return has_abba


assert supports_tls('abba[mnop]qrst')
assert not supports_tls('abcd[bddb]xyyx')
assert not supports_tls('aaaa[qwer]tyui')
assert supports_tls('ioxxoj[asdfgh]zxcvbn')

print(sum([supports_tls(w) for w in words]))


# Part two
def supports_ssl(s):
    in_bracket = False
    state = 0
    abas = []
    babs = []
    for i, letter in enumerate(s):
        if letter == '[':
            in_bracket = True
        elif letter == ']':
            in_bracket = False
        elif not in_bracket:
            if len(s) > i+2 and letter != s[i+1] and letter == s[i+2]:
                abas.append((letter, s[i+1]))
        elif in_bracket:
            if len(s) > i+2 and letter != s[i+1] and letter == s[i+2]:
                babs.append((s[i+1], letter))
    return bool(set(abas).intersection(babs))


assert supports_ssl('aba[bab]xyz')
assert not supports_ssl('xyx[xyx]xyx')
assert supports_ssl('aaa[kek]eke')
assert supports_ssl('zazbz[bzb]cdb')

print(sum([supports_ssl(w) for w in words]))
