with open('input') as f:
    data = [int(x) for x in f.read().split()]


def parse(s):
    children = s[0]
    num_metas = s[1]
    s = s[2:]
    total = 0
    meta = []
    for _ in range(children):
        sub_total, sub_meta, s = parse(s)
        total += sub_total
        meta.append(sub_meta)
    total += sum(s[:num_metas])
    meta_sum = total if not children else sum(meta[i - 1] for i in s[:num_metas] if i <= len(meta))
    rest = s[num_metas:]
    return total, meta_sum, rest


result = parse(data)

# Part one
print(result[0])

# Part two
print(result[1])
