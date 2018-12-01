from collections import Counter

with open('input') as f:
    words = [x.strip() for x in f.readlines()]


def generate_nth_most_common(words, n):
    return str.join('', [Counter([w[i] for w in words]).most_common()[n][0] for i in range(8)])


# Part one
print(generate_nth_most_common(words, 1))

# Part two
print(generate_nth_most_common(words, -1))
