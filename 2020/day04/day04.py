import re
from typing import Pattern
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

REQUIRED_PARAMS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def part1(input: list[str]) -> None:
    passports = [_load_passport(p) for p in _extract_lines(input)]

    print(sum(1 if _is_valid(p) else 0 for p in passports))


def part2(input: list[str]) -> None:
    passports = [_load_passport(p) for p in _extract_lines(input)]

    validations = {
        'byr': lambda x: _is_numeric_between(x, 1920, 2002),
        'iyr': lambda x: _is_numeric_between(x, 2010, 2020),
        'eyr': lambda x: _is_numeric_between(x, 2020, 2030),
        'hgt': lambda x: _validate_height(x),
        'hcl': lambda x: _validate_regex(x, r'#[\da-f]{6}$'),
        'ecl': lambda x: _validate_regex(x, r'(amb|blu|brn|gry|grn|hzl|oth)$'),
        'pid': lambda x: _validate_regex(x, r'\d{9}$')
    }

    valid_passports = 0

    def passes_validation(passport: dict[str, str]) -> bool:
        if not _is_valid(passport):
            return False

        for key, validator in validations.items():
            if not validator(passport[key]):
                return False

        return True

    print(sum(1 if passes_validation(p) else 0 for p in passports))


def _load_passport(input: list[str]) -> dict[str, str]:
    passport = {}
    for l in input:
        for t in l.split(' '):
            term, value = t.split(':')
            passport[term] = value

    return passport


def _extract_lines(input: list[str]):
    lines_so_far = []

    for l in input:
        if l == '':
            yield lines_so_far
            lines_so_far = []
            continue

        lines_so_far.append(l)

    yield lines_so_far


def _is_valid(passport: dict[str, str]):
    for p in REQUIRED_PARAMS:
        if p not in passport:
            return False
    return True


def _validate_height(l: str) -> bool:
    bounds = {
        'cm': (150, 193),
        'in': (59, 76)
    }
    suffix = l[-2:]

    if suffix not in bounds:
        return False

    lower, upper = bounds[suffix]
    return _is_numeric_between(l[:-2], lower, upper)


def _validate_regex(l: str, pattern: Pattern) -> bool:
    return re.match(pattern, l) is not None


def _is_numeric_between(value: str, lower: int, upper: int) -> bool:
    if not value.isdigit():
        return False

    v = int(value)

    return lower <= v <= upper


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
