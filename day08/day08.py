from collections import defaultdict
from itertools import combinations
from typing import Iterator


def part1(input: list[str]):
    antinodes: set[tuple[int, int]] = set()
    node_dict = defaultdict[str, list[tuple[int, int]]](list)

    for node_type, node_coords in _find_nodes(input):
        node_dict[node_type].append(node_coords)

    for node_type, items in node_dict.items():
        for (node1_r, node1_c), (node2_r, node2_c) in combinations(items, 2):
            row_stride = node1_r - node2_r
            col_stride = node1_c - node2_c

            antinode_a = (node1_r + row_stride, node1_c + col_stride)
            antinode_b = (node2_r - row_stride, node2_c - col_stride)

            if _in_bounds(input, antinode_a):
                antinodes.add(antinode_a)

            if _in_bounds(input, antinode_b):
                antinodes.add(antinode_b)

    print(len(antinodes))


def part2(input: list[str]):
    antinodes: set[tuple[int, int]] = set()
    node_dict = defaultdict[str, list[tuple[int, int]]](list)

    for node_type, node_coords in _find_nodes(input):
        node_dict[node_type].append(node_coords)

    for node_type, items in node_dict.items():
        for (node1_r, node1_c), (node2_r, node2_c) in combinations(items, 2):
            row_stride = node1_r - node2_r
            col_stride = node1_c - node2_c

            r, c = node1_r, node1_c

            while _in_bounds(input, (r, c)):
                antinodes.add((r, c))
                r += row_stride
                c += col_stride

            r, c = node1_r - row_stride, node1_c - col_stride
            while _in_bounds(input, (r, c)):
                antinodes.add((r, c))
                r -= row_stride
                c -= col_stride
    print(len(antinodes))


def _find_nodes(input: list[str]) -> Iterator[tuple[str, tuple[int, int]]]:
    for r, l in enumerate(input):
        for c, v in enumerate(l):
            if v != ".":
                yield (v, (r, c))


def _in_bounds(grid: list[str], point: tuple[int, int]):
    r, c = point
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
