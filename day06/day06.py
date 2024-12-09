from pathlib import Path
import numpy as np


def part1(input: list[str]):
    r, c = find_char(input, "^")
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    visited_map = [[False] * len(l) for l in input]
    visited_map[r][c] = True
    visited_squares = 1

    while True:
        dr, dc = directions[direction_index]

        next_row = dr + r
        next_col = dc + c

        # If we're leaving, we are done
        if not (
            next_row >= 0
            and next_col >= 0
            and next_row < len(input)
            and next_col < len(input[0])
        ):
            break

        next_square = input[next_row][next_col]

        # If free - advance
        if next_square == "." or next_square == "^":
            if not visited_map[next_row][next_col]:
                visited_map[next_row][next_col] = True
                visited_squares += 1

            r = next_row
            c = next_col

            continue

        # If not free - turn
        if next_square == "#":
            direction_index = (direction_index + 1) % len(directions)
            continue

        print(f"UNKNOWN: {next_square}")
        raise Exception("weird input")

    print(visited_squares)

    return visited_map


def part2(input: list[str], orig_visited_map: list[list[bool]]):
    start_r, start_c = find_char(input, "^")

    obstruction_locations = [
        (r, c)
        for r, l in enumerate(orig_visited_map)
        for c, v in enumerate(l)
        if v and (r, c) != (start_r, start_c)
    ]

    num_loops = 0

    mutable_grid = [[c for c in l] for l in input]

    for r, c in obstruction_locations:
        mutable_grid[r][c] = "#"
        if _does_loop(mutable_grid, start_r, start_c, r, c):
            num_loops += 1

        mutable_grid[r][c] = "."

    print(num_loops)


def _does_loop(
    modified_grid: list[str],
    starting_row: int,
    starting_col: int,
    obs_row: int,
    obs_col: int,
) -> bool:
    if (starting_row, starting_col) == (obs_row, obs_col):
        return False

    visited_map = np.zeros((len(modified_grid), len(modified_grid[0]), 4), dtype=bool)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    r, c = starting_row, starting_col

    visited_map[r][c][direction_index] = True

    while True:
        dr, dc = directions[direction_index]

        next_row = dr + r
        next_col = dc + c

        # If we're leaving, we are not looping
        if not (
            next_row >= 0
            and next_col >= 0
            and next_row < len(modified_grid)
            and next_col < len(modified_grid[0])
        ):
            # print("left grid")
            return False

        next_square = modified_grid[next_row][next_col]

        # If free - advance
        if next_square == "." or next_square == "^":
            # If we've already visited while facing this direction, we've looped
            if visited_map[next_row][next_col][direction_index]:
                return True

            visited_map[next_row][next_col][direction_index] = True
            r = next_row
            c = next_col

            continue

        # If not free - turn
        if next_square == "#":
            direction_index = (direction_index + 1) % len(directions)
            visited_map[r][c][direction_index] = True
            continue

        print(f"UNKNOWN: {next_square}")
        raise Exception("weird input")


def find_char(grid: list[str], char_to_find: str) -> tuple[int, int] | None:
    for ri, l in enumerate(grid):
        for ci, v in enumerate(l):
            if v == char_to_find:
                return ri, ci

    return None


def main():
    input_path = Path(__file__).parent / "input"
    with open(input_path, "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    orig_visited = part1(stripped_input)
    part2(stripped_input, orig_visited)


if __name__ == "__main__":
    main()
