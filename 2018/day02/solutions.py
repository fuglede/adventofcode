from collections import Counter

with open('input') as f:
    words = [x.strip() for x in f.readlines()]

# Part one
twos = [2 in Counter(word).values() for word in words]
threes = [3 in Counter(word).values() for word in words]
print(sum(twos)*sum(threes))

# Part two
for w1 in words:
    for w2 in words:
        if sum(l1 == l2 for l1, l2 in zip(w1, w2)) == len(w1) - 1:
            print(''.join([l1 for l1, l2 in zip(w1, w2) if l1 == l2]))
