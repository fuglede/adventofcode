import re

from lark import Lark


with open('input') as f:
    data = f.read()

rules, messages = data.split('\n\n')
messages = messages.split()


def solve(rules):
    rules = 'start: t0\n' + re.sub(r'(\d+)', r't\1', rules)
    parser = Lark(rules)
    valid = len(messages)
    for message in messages:
        try:
            parser.parse(message)
        except:
            valid -= 1
    return valid


# Part one
print(solve(rules))

# Part two
rules = rules\
    .replace('8: 42', '8: 42 | 42 8')\
    .replace('11: 42 31', '11: 42 31 | 42 11 31')
print(solve(rules))
