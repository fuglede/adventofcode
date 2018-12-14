# Part one
scores = [3, 7]
current = [0, 1]
i = 505961
while len(scores) < i + 10:
    digits = scores[current[0]] + scores[current[1]]
    scores += [int(i) for i in str(digits)]
    current[0] = (1 + current[0] + scores[current[0]]) % len(scores)
    current[1] = (1 + current[1] + scores[current[1]]) % len(scores)
print(''.join(map(str, scores[i:i+10])))

# Part two
scores = [3, 7]
current = [0, 1]
i = '505961'
while True:
    digits = scores[current[0]] + scores[current[1]]
    scores += [int(i) for i in str(digits)]
    s = str(''.join(map(str, scores[-8:])))
    index = s.find(i)
    if index != -1:
        print(index + len(scores) - 8)
        break
    current[0] = (1 + current[0] + scores[current[0]]) % len(scores)
    current[1] = (1 + current[1] + scores[current[1]]) % len(scores)
