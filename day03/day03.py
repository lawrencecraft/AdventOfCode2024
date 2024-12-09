import re

def part1(input: str) -> None:
    matches = re.findall(r'mul\((\d+),(\d+)\)', input)

    print(sum(int(f) * int(s) for f,s in matches))

def part2(input: str) -> None:
    matches = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', input)

    enabled = True
    total = 0

    for m1, op1, op2 in matches:
        if m1 == "do()":
            enabled = True
            continue

        if m1 == "don't()":
            enabled = False
            continue

        if enabled:
            total += int(op1) * int(op2)

    print(total)

def main():
    with open("input", 'r') as f:
        input = f.read()

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
