from typing import Iterator
from collections import deque


def part1(raw_input: list[str]):
    calculate_score(raw_input, track_visited=True)


def part2(raw_input: list[str]):
    calculate_score(raw_input, track_visited=False)


def calculate_score(input: list[str], track_visited: bool):
    padded_input = _pad_input(input)
    trailheads = _get_trailheads(padded_input)

    print(sum(find_ends(padded_input, t, track_visited) for t in trailheads))


def find_ends(grid: list[str], trailhead: tuple[int, int], track_visited: bool) -> int:
    visited = [[False for _ in l] for l in grid]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # locations = deque([trailhead])
    locations = [trailhead]
    ends = 0

    while locations:
        # row, col = locations.popleft()
        row, col = locations.pop()

        if track_visited:
            if visited[row][col]:
                continue

            visited[row][col] = True

        if grid[row][col] == "9":
            ends += 1
            continue

        for dr, dc in directions:
            nextr, nextc = row + dr, col + dc

            if (
                grid[nextr][nextc].isdigit()
                and int(grid[nextr][nextc]) - int(grid[row][col]) == 1
            ):
                locations.append((nextr, nextc))

    return ends


def _get_trailheads(input: list[str]) -> Iterator[tuple[int, int]]:
    for r, l in enumerate(input):
        for c, v in enumerate(l):
            if v == "0":
                yield (r, c)


def _pad_input(input: list[str]) -> list[str]:
    padded_cols = [f".{l}." for l in input]
    return ["." * len(padded_cols[0]), *padded_cols, "." * len(padded_cols[0])]


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
