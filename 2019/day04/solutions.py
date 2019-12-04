start = 245182
end = 790572


def two_adjacent(d, part_one):
    s = str(d)
    return any(s[i] == s[i+1] and
               (part_one or
                ((i == len(s) - 2 or s[i+1] != s[i+2]) and (i == 0 or s[i-1] != s[i])))
               for i in range(len(s) - 1))


def increasing(d):
    s = str(d)
    return sorted(s) == list(s)


# Part one
print(sum(two_adjacent(d, True) and increasing(d) for d in range(start, end)))

# Part two
print(sum(two_adjacent(d, False) and increasing(d) for d in range(start, end)))
