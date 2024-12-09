from collections import Counter


def part1(input: list[str]) -> None:
    first_list: list[int] = []
    second_list: list[int] = []

    for l in input:
        f, s = l.split('   ')

        first_list.append(int(f))
        second_list.append(int(s))

    first_sorted = sorted(first_list)
    second_sorted = sorted(second_list)

    matched_pairs = zip(first_sorted, second_sorted)

    total = sum(abs(f - s) for f, s in matched_pairs)
    print(total)


def part2(input: list[str]) -> None:
    first_list: list[int] = []
    second_list: list[int] = []

    for l in input:
        f, s = l.split('   ')

        first_list.append(int(f))
        second_list.append(int(s))

    second_counter = Counter(second_list)

    print(sum(f * second_counter[f] for f in first_list))


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
