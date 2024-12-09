def part1(input: list[str]):
    padded_grid = _pad_2d(input)

    confirmed_xmas = 0

    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]

    for i, row in enumerate(padded_grid):
        for j, _ in enumerate(row):
            for dr, dc in directions:
                if _has_word(padded_grid, i, j, "XMAS", dr, dc):
                    confirmed_xmas += 1

    print(confirmed_xmas)


def _has_word(
    grid: list[str], row: int, column: int, word: str, dr: int, dc: int
) -> bool:
    if not word:
        return True

    if grid[row][column] != word[0]:
        return False

    return _has_word(grid, row + dr, column + dc, word[1:], dr, dc)


def part2(input: list[str]):
    padded_grid = _pad_2d(input)

    confirmed_mas = 0

    for i, row in enumerate(padded_grid):
        for j, _ in enumerate(row):
            if _is_mas(padded_grid, i, j):
                confirmed_mas += 1

    print(confirmed_mas)

def _is_mas(grid, i, j):
    if grid[i][j] != "A":
        return False

    first_vertical = f"{grid[i+1][j+1]}{grid[i-1][j-1]}"
    second_vertical = f"{grid[i-1][j+1]}{grid[i+1][j-1]}"

    if first_vertical != "SM" and first_vertical != "MS":
        return False

    if second_vertical != "SM" and second_vertical != "MS":
        return False
    
    return True


def _pad_2d(grid: list[str], padding_char=".") -> list[str]:
    pad_lr = [f"{padding_char}{l}{padding_char}" for l in grid]
    return [
        padding_char * len(pad_lr[0]),
        *pad_lr,
        padding_char * len(pad_lr[0]),
    ]


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
