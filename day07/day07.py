from dataclasses import dataclass


@dataclass
class Line:
    total: int
    items: list[int]


def part1(input: list[str]) -> None:
    lines = [_parse_line(l) for l in input]

    def _walk_tree(target: int, total: int, remaining: list[int]) -> bool:
        if remaining == []:
            return target == total

        if total > target:
            return False

        current_num, rest = remaining[0], remaining[1:]

        if _walk_tree(target, current_num + total, rest):
            return True

        if _walk_tree(target, current_num * total, rest):
            return True

        return False

    print(sum(l.total for l in lines if _walk_tree(l.total, l.items[0], l.items[1:])))


def part2(input: list[str]) -> None:
    lines = [_parse_line(x) for x in input]

    def _walk_tree(target: int, total: int | None, remaining: list[int]) -> bool:
        if remaining == []:
            return target == total

        if total and total > target:
            return False

        first = remaining[0]
        rest = remaining[1:]

        addition_total = total or 0
        if _walk_tree(target, addition_total + first, rest):
            return True

        mult_total = total or 1
        if _walk_tree(target, mult_total * first, rest):
            return True

        concat_base = total or 0
        if _walk_tree(target, int(f"{concat_base}{first}"), rest):
            return True

        return False

    print(sum(l.total for l in lines if _walk_tree(l.total, None, l.items)))


def _parse_line(line: str) -> Line:
    total_raw, rest_raw = line.split(": ")

    rest = [int(x) for x in rest_raw.split(" ")]

    return Line(total=int(total_raw), items=rest)


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
