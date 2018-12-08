with open('input') as f:
    data = [int(x) for x in f.read().split()]


def parse(s):
    children, num_metas, s = s[0], s[1], s[2:]
    total = 0
    sub_metas = []
    for _ in range(children):
        sub_total, sub_meta, s = parse(s)
        total += sub_total
        sub_metas.append(sub_meta)
    metas, s = s[:num_metas], s[num_metas:]
    total += sum(metas)
    meta_sum = total if not children else sum(sub_metas[i - 1] for i in metas if i <= len(sub_metas))
    return total, meta_sum, s


result = parse(data)

# Part one
print(result[0])

# Part two
print(result[1])
