import re
from dataclasses import dataclass


@dataclass
class Valve:
    id: str
    links: list[str]
    rate: int


def part1(input: list[str]):
    valves = [_parse_line(l) for l in input]
    print(valves)


def part2(input: list[str]):
    pass


def _parse_line(line: str) -> Valve:
    result = re.match(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line
    )

    id = result.group(1)
    rate = int(result.group(2))
    links = result.group(3).split(", ")

    return Valve(id=id, rate=rate, links=links)


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
