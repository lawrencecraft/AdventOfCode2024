from functools import cache


def part1(input: list[str]):
    initial_nums = parse_input(input)

    print(sum(calc_unique(25, n) for n in initial_nums))


def part2(input: list[str]):
    initial_nums = parse_input(input)

    print(sum(calc_unique(75, n) for n in initial_nums))


@cache
def calc_unique(generations: int, num: str):
    if generations == 0:
        return 1

    if num == "0":
        return calc_unique(generations - 1, "1")

    if len(num) % 2 == 0:
        first = num[: len(num) // 2]
        second = num[len(num) // 2 :]

        return calc_unique(generations - 1, str(int(first))) + calc_unique(
            generations - 1, str(int(second))
        )

    return calc_unique(generations - 1, str(int(num) * 2024))


def parse_input(input: list[str]):
    return [x for x in input[0].split(" ")]


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
