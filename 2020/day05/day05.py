def part1(input: list[str]) -> None:
    print(max(calc_seat_id(s) for s in input))


def part2(input: list[str]) -> None:
    seat_ids = [calc_seat_id(s) for s in input]
    sorted_seats = sorted(seat_ids)
    for idx, i in enumerate(sorted_seats[:-1]):
        if sorted_seats[idx+1] - i != 1:
            print(i+1)


def calc_seat_id(l: str) -> int:
    row = binary_search(l, 'F', 'B', 127)
    seat = binary_search(l, 'L', 'R', 7)
    return row * 8 + seat


def binary_search(input: str, bottom_char: str, top_char: str, max: int) -> int:
    bottom_range = 0
    top_range = max

    for i in input:
        half_range = (top_range - bottom_range) // 2
        if i == top_char:
            bottom_range = half_range + bottom_range + 1

        if i == bottom_char:
            top_range = bottom_range + half_range

        if top_range == bottom_range:
            return top_range

    raise Exception(f"Did not converge - {bottom_range} {top_range}")


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
