from collections import Counter
from dataclasses import dataclass

@dataclass
class ParsedLine:
    lower: int
    upper: int
    letter: str
    password: str

def part1(input: list[str]) -> None:
    def _is_valid(line: str) -> bool:
        p = _parse(line)

        count = Counter(p.password)
        occurrences = count[p.letter]
        return p.lower <= occurrences <= p.upper
    print(len([p for p in input if _is_valid(p)]))

def part2(input: list[str]) -> None:
    valid = 0
    
    for l in map(_parse, input):
        first_pos = l.password[l.lower - 1]
        second_pos = l.password[l.upper - 1]

        if first_pos == second_pos:
            continue

        if first_pos == l.letter or second_pos == l.letter:
            valid += 1

    print(valid)



def _parse(line: str) -> ParsedLine:
    header, password = line.split(': ')
    num_range, letter = header.split(' ')
    lower_s, upper_s = num_range.split('-')

    lower = int(lower_s)
    upper = int(upper_s) 

    return ParsedLine(lower=lower, upper=upper, letter=letter, password=password)

def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
