from dataclasses import dataclass
from functools import reduce
from operator import mul

CONTAINER_WIDTH = 101
CONTAINER_HEIGHT = 103

ROUNDS=100


@dataclass
class Robot:
    velocity: tuple[int, int]
    position: tuple[int, int]


def part1(raw_input: list[str]) -> None:
   print(_calc_safety(_parse_input(raw_input), iters=ROUNDS)) 


def part2(raw_input: list[str]) -> None:
    robs = list(_parse_input(raw_input))
    print(min((_calc_safety(robs, i), i) for i in range(CONTAINER_HEIGHT * CONTAINER_WIDTH))[1])

def _calc_safety(robots: list[Robot], iters: int):
    quadrants = [[0, 0], [0, 0]]
    x_middle = (CONTAINER_WIDTH - 1) // 2
    y_middle = (CONTAINER_HEIGHT - 1) // 2

    for r in robots:
        final_x = (r.position[0] + r.velocity[0] * iters) % CONTAINER_WIDTH
        final_y = (r.position[1] + r.velocity[1] * iters) % CONTAINER_HEIGHT

        if final_x == x_middle or final_y == y_middle:
            continue

        x_quad = 0 if final_x < x_middle else 1
        y_quad = 0 if final_y < y_middle else 1

        quadrants[x_quad][y_quad] += 1

    return reduce(mul, (i for l in quadrants for i in l), 1)

def _parse_input(input: list[str]):
    for l in input:
        p, v = l.split(" ")
        yield Robot(velocity=_parse_point(v), position=_parse_point(p))


def _parse_point(l: str) -> tuple[int, int]:
    _, p = l.split("=")
    x, y = p.split(",")

    return int(x), int(y)


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
