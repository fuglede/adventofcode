import hashlib
from itertools import count


def make_hash(room, i):
    s = (room+str(i)).encode('ascii')
    return hashlib.md5(s).hexdigest()


room = 'ugkcyxxp'

# Part one
password = []
for i in count():
    h = make_hash(room, i)
    if h[:5] == '00000':
        password.append(h[5])
        if len(password) == 8:
            break
print(str.join('', password))

# Part two
found = set()
password = ['']*8
for i in count():
    h = make_hash(room, i)
    if h[:5] == '00000':
        index = int(h[5], 16)
        if index < 8 and index not in found:
            password[index] = h[6]
            found.add(index)
            if len(found) == 8:
                break
print(str.join('', password))
