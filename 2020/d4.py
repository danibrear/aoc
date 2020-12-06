import re


def valid_byr(byr):
    if (len(byr) == 4):
        byr = int(byr)
        if byr >= 1920 and byr <= 2002:
            return True
    return False


def valid_iyr(iyr):
    if (len(iyr) == 4):
        iyr = int(iyr)
        if iyr >= 2010 and iyr <= 2020:
            return True
    return False


def valid_eyr(eyr):
    if (len(eyr) == 4):
        eyr = int(eyr)
        if eyr >= 2020 and eyr <= 2030:
            return True
    return False


def valid_hgt(hgt):
    if 'cm' in hgt:
        height = int(hgt.split('cm')[0])
        if height >= 150 and height <= 193:
            return True
    elif 'in' in hgt:
        height = int(hgt.split('in')[0])
        if height >= 59 and height <= 76:
            return True
    return False


def valid_hcl(hcl):
    if re.match('^\#[0-9a-f]{6}$', hcl):
        return True
    return False


def valid_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def valid_pid(pid):
    if re.match('^[0-9]{9}$', pid):
        return True

    return False


def part1(passports):

    man_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    opt_keys = ['cid']
    invalid_count = 0
    for passport in passports:
        for key in man_keys:
            if key not in passport:
                invalid_count += 1
                break

    print(len(passports) - invalid_count)


def part2(passports):

    man_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    opt_keys = ['cid']
    invalid_count = 0
    for passport in passports:
        has_all_keys = True
        for key in man_keys:
            if key not in passport:
                invalid_count += 1
                has_all_keys = False
                break
        if has_all_keys:
            if valid_byr(passport['byr']) and \
                    valid_iyr(passport['iyr']) and \
                    valid_eyr(passport['eyr']) and \
                    valid_hgt(passport['hgt']) and \
                    valid_hcl(passport['hcl']) and \
                    valid_ecl(passport['ecl']) and \
                    valid_pid(passport['pid']):
                # print('byr', valid_byr(passport['byr']), passport['byr'])
                # print('iyr', valid_iyr(passport['iyr']), passport['iyr'])
                # print('eyr', valid_eyr(passport['eyr']), passport['eyr'])
                # print('hgt', valid_hgt(passport['hgt']), passport['hgt'])
                # print('hcl', valid_hcl(passport['hcl']), passport['hcl'])
                # print('ecl', valid_ecl(passport['ecl']), passport['ecl'])
                # print('pid', valid_pid(passport['pid']), passport['pid'])
                # print('\n')
                continue
            else:
                # if not valid_byr(passport['byr']):
                #     print('byr', valid_byr(passport['byr']), passport['byr'])
                # if not valid_iyr(passport['iyr']):
                #     print('iyr', valid_iyr(passport['iyr']), passport['iyr'])
                # if not valid_eyr(passport['eyr']):
                #     print('eyr', valid_eyr(passport['eyr']), passport['eyr'])
                # if not valid_hgt(passport['hgt']):
                #     print('hgt', valid_hgt(passport['hgt']), passport['hgt'])
                # if not valid_hcl(passport['hcl']):
                #     print('hcl', valid_hcl(passport['hcl']), passport['hcl'])
                # if not valid_ecl(passport['ecl']):
                #     print('ecl', valid_ecl(passport['ecl']), passport['ecl'])
                # if not valid_pid(passport['pid']):
                #     print('pid', valid_pid(passport['pid']), passport['pid'])
                # print('\n')
                invalid_count += 1

    print(len(passports) - invalid_count)


with open('./d4.txt', 'r') as f:

    lines = f.readlines()

    lines = map(lambda x: x.replace('\n', ''), lines)
    lines = list(lines)

    passports = []
    passport = {}
    for line in lines:
        if (len(line) == 0):
            passports.append(passport)
            passport = {}
            continue

        for part in line.split(' '):
            if (len(part) == 0):
                continue
            key, val = part.split(':')

            if key in passport:
                print('already have', key, 'value', passport[key])

            passport[key] = val

    passports.append(passport)

    part1(passports)
    part2(passports)
