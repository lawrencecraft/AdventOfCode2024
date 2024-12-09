def part1(input: list[str]) -> None:
    print(_traverse(input, 3, 1))


def part2(input: list[str]) -> None:
    options = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    prod = 1

    for s in [_traverse(input, r, d) for r, d in options]:
        prod *= s

    print(prod)



def _traverse(input: list[str], right_step: int, down_step: int) -> int:
    width = len(input[0])
    seen_trees = 0
    row = 0
    column = 0

    while row < len(input):
        if input[row][column % width] == '#':
            seen_trees += 1

        row += down_step
        column += right_step

    return seen_trees


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
