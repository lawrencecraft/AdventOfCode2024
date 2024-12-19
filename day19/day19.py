from dataclasses import dataclass
from functools import cache


@dataclass
class Input:
    tokens: list[str]
    towels: list[str]


def part1(raw_input: list[str]):
    input = _parse_input(raw_input)
    print(sum(1 if count_ways(t, tuple(input.tokens)) > 0 else 0 for t in input.towels))


def part2(raw_input: list[str]):
    input = _parse_input(raw_input)
    print(sum(count_ways(t, tuple(input.tokens)) for t in input.towels))


@cache
def count_ways(towel: str, tokens: tuple[str]):
    if not towel:
        return 1

    return sum(
        count_ways(towel[len(t) :], tokens) for t in tokens if towel.startswith(t)
    )


def _parse_input(input: list[str]) -> Input:
    tokens = input[0].split(", ")
    towels = input[2:]

    return Input(tokens=tokens, towels=towels)


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
