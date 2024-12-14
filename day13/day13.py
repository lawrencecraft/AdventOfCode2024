import re
from dataclasses import dataclass


@dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize_loc: tuple[int, int]


def part1(input: list[str]):
    calc_score(input)


def part2(input: list[str]):
    calc_score(input, offset=10000000000000)


def calc_score(input: list[str], offset=0):
    score = 0

    for m in _parse_input(input):
        bax, bay = m.button_a
        bbx, bby = m.button_b
        px, py = m.prize_loc

        px += offset
        py += offset

        # Cramer's Rule

        det = bax * bby - bay * bbx
        det_a = px * bby - py * bbx
        det_b = bax * py - bay * px

        a_press = det_a // det
        b_press = det_b // det

        if det_a % det == 0 and det_b % det == 0:
            score += a_press * 3 + b_press

    print(score)


def _parse_input(input: list[str]):
    input_stack = list(reversed(input))

    def parse_button(button_str: str) -> tuple[int, int]:
        results = re.search(r"^.*: X.(\d+), Y.(\d+)$", button_str)
        if not results:
            print(button_str)
            raise Exception()
        return int(results.group(1)), int(results.group(2))

    while input_stack:
        yield Machine(
            button_a=parse_button(input_stack.pop()),
            button_b=parse_button(input_stack.pop()),
            prize_loc=parse_button(input_stack.pop()),
        )

        if input_stack:
            input_stack.pop()


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
