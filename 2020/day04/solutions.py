import re


with open('input') as f:
    data = f.read()

passports = []
for block in data.split('\n\n'):
    parsed = re.findall(r'(\w+):(\S+)', block)
    passports.append({m[0]: m[1] for m in parsed})

# Part one
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid(passport):
    return not any(required - passport.keys())


print(sum(map(is_valid, passports)))


# Part two
def is_valid(passport):
    # Abuse exceptions for control flow
    try:
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002:
            return False
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            return False
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            return False
        hgt = passport['hgt']
        match = re.match(r'(\d+)(cm|in)', hgt)
        height, unit = match[1], match[2]
        if unit == 'cm':
            if not 150 <= int(height) <= 193:
                return False
        elif unit == 'in':
            if not 59 <= int(height) <= 76:
                return False
        else:
            return False
        hcl = passport['hcl']
        if hcl[0] != '#' or len(hcl) != 7:
            return False
        int(hcl[1:], 16)  # Raises exactly if the desired criterion fails
        ecl = passport['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        pid = passport['pid']
        if not pid.isdigit() or len(pid) != 9:
            return False
        return True
    except:
        return False


print(sum(map(is_valid, passports)))
