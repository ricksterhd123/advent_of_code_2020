import re

def get_passports(string):
    count = 0
    passport = []
    for line in string.split('\n'):
        if not line:
            count += 1
        else:
            if len(passport) <= count:
                passport.append([])
            passport[count] += line.split(" ")
    return passport

# part A
def validate_passport1(passport):
    count = 0
    attribs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid not needed
    for x in passport:
        for attrib in attribs:
            if x.find(attrib) != -1:
                count += 1
    return count == 7

# part B
def validate_passport2(passport):
    byr_count = 0
    iyr_count = 0
    eyr_count = 0
    hgt_count = 0
    hcl_count = 0
    ecl_count = 0
    pid_count = 0

    for x in passport:
        byr_m = re.match(r'byr:([0-9]+)', x)
        iyr_m = re.match(r'iyr:([0-9]+)', x)
        eyr_m = re.match(r'eyr:([0-9]+)', x)
        hgt_m = re.match(r'hgt:([0-9]+)(cm|in)', x)
        hcl_m = re.match(r'hcl:#([0-9a-f]+)', x)
        ecl_m = re.match(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', x)
        pid_m = re.match(r'pid:([0-9]+)', x)

        if byr_m:
            byr = int(byr_m.group(1))
            if byr >= 1920 and byr <= 2020: # invert
                byr_count += 1
        elif iyr_m:
            iyr = int(iyr_m.group(1))
            if iyr >= 2010 and iyr <= 2020:    # invert
                iyr_count += 1
        elif eyr_m:
            eyr = int(eyr_m.group(1))
            if eyr >= 2020 and eyr <= 2030: 
                eyr_count += 1
        elif hgt_m:
            hgt = int(hgt_m.group(1))
            hgt_fmt = hgt_m.group(2)
            if hgt_fmt == 'cm' and (hgt >= 150 and hgt <= 193):
                hgt_count += 1
            if hgt_fmt == 'in' and (hgt >= 59 and hgt <= 76):
                hgt_count += 1
        elif hcl_m:
            hcl = hcl_m.group(1)
            if len(hcl) == 6:
                hcl_count += 1
        elif ecl_m:
            ecl_count += 1
        elif pid_m:
            pid = pid_m.group(1)
            if len(pid) == 9:
                pid_count += 1

    return byr_count == 1 and iyr_count == 1 and \
        eyr_count == 1 and hgt_count == 1 and \
        hcl_count == 1 and ecl_count == 1 and pid_count == 1

def validate_passports(fn, passports):
    return list(filter(fn, passports))

if __name__ == '__main__':    
    with open('day_04.txt', 'r') as f:
        passports = get_passports(f.read())
        print(len(validate_passports(validate_passport1, passports)))
        print(len(validate_passports(validate_passport2, passports)))