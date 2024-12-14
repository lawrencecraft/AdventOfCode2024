def execute(raw_input: list[str]):
    padded_input = _pad_input(raw_input)
    visited = [[False for _ in l] for l in padded_input]
    part1_price = 0
    part2_price = 0

    for r, l in enumerate(padded_input):
        for c, v in enumerate(l):
            if visited[r][c]:
                continue

            if v == ".":
                continue

            area, perimeter, sides = _explore_shape(padded_input, visited, r, c)
            part1_price += area * perimeter
            part2_price += area * sides

    print(part1_price)
    print(part2_price)


def _explore_shape(
    grid: list[list[str]], visited: list[list[bool]], row: int, col: int
) -> tuple[int, int, int]:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    area = 0
    sides = 0
    perimeter = 0

    char = grid[row][col]

    coords: list[(int, int)] = [(row, col)]

    while coords:
        r, c = coords.pop()
        if visited[r][c]:
            continue

        visited[r][c] = True

        area += 1

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            next_val = grid[new_r][new_c]

            if next_val == char:
                coords.append((new_r, new_c))
            else:
                perimeter += 1

        for dr in [-1, 1]:
            for dc in [-1, 1]:
                col_equal = grid[r][dc + c] == char
                row_equal = grid[r + dr][c] == char

                if col_equal != row_equal:
                    continue

                if (not col_equal) or grid[r + dr][c + dc] != char:
                    sides += 1

    return area, perimeter, sides


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    execute(stripped_input)


def _pad_input(input: list[str]) -> list[str]:
    padded_cols = [f".{l}." for l in input]
    return ["." * len(padded_cols[0]), *padded_cols, "." * len(padded_cols[0])]


if __name__ == "__main__":
    main()
