from dataclasses import dataclass
from collections import defaultdict
from functools import cmp_to_key


@dataclass
class Input:
    rules: list[tuple[int, int]]
    inputs: list[list[int]]


def part1(input: list[str]) -> None:
    inputs = _parse_input(input)

    is_lesser_map = defaultdict(set)

    for lo, hi in inputs.rules:
        is_lesser_map[hi].add(lo)

    print(sum(i[len(i) // 2] for i in inputs.inputs if _is_sorted(i, is_lesser_map)))


def _is_sorted(input: list[int], lesser_map: dict[int, set[int]]):
    for idx, i in enumerate(input[:-1]):
        if i not in lesser_map[input[idx + 1]]:
            return False
    return True


def part2(input: list[str]) -> None:
    inputs = _parse_input(input)

    is_lesser_map = defaultdict(set)

    for lo, hi in inputs.rules:
        is_lesser_map[hi].add(lo)

    def io_cmp(a: int, b: int) -> int:
        if b in is_lesser_map[a]:
            return 1
        return -1

    fixed_inputs = [
        sorted(i, key=cmp_to_key(io_cmp))
        for i in inputs.inputs
        if not _is_sorted(i, is_lesser_map)
    ]
    print(sum(i[len(i) // 2] for i in fixed_inputs))


def _parse_input(input: list[str]) -> Input:
    input_stack = input.copy()
    input_stack.reverse()

    rules: list[tuple[int, int]] = []
    inputs: list[list[int]] = []

    while (val := input_stack.pop()) != "":
        lo, hi = val.split("|")
        rules.append((int(lo), int(hi)))

    while input_stack:
        line = input_stack.pop()
        inputs.append([int(x) for x in line.split(",")])

    return Input(rules=rules, inputs=inputs)


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
