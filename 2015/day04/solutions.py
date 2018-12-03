from collections import defaultdict
import hashlib
from itertools import count


def make_hash(a, i):
    s = (a+str(i)).encode('ascii')
    return hashlib.md5(s).hexdigest()


# Part one
for i in count():
    if make_hash('iwrupvqb', i)[:5] == '00000':
        print(i)
        break

# Part two
for i in count():
    if make_hash('iwrupvqb', i)[:6] == '000000':
        print(i)
        break
