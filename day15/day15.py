from dataclasses import dataclass


@dataclass
class MapAndDirections:
    map: list[str]
    dirs: str


def part1(raw_input: list[str]):
    map_dirs = parse_input(raw_input)
    location = _find_guy(map_dirs.map, "@")

    mut_map = [list(m) for m in map_dirs.map]

    dir_map = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

    for d in map_dirs.dirs:
        if result := _try_move(mut_map, location, dir_map[d]):
            location = result

    score = 0
    for r, l in enumerate(mut_map):
        for c, v in enumerate(l):
            if v == "O":
                score += r * 100 + c
    print(score)


def _try_move(
    grid: list[list[str]], loc: tuple[int, int], dir: tuple[int, int]
) -> tuple[int, int] | None:
    r, c = loc
    dr, dc = dir

    val = grid[r][c]

    nextr, nextc = r + dr, c + dc

    if grid[nextr][nextc] == ".":
        grid[nextr][nextc] = val
        grid[r][c] = "."
        return nextr, nextc

    if grid[nextr][nextc] == "#":
        return None

    if grid[nextr][nextc] == "O":
        sub_result = _try_move(grid, (nextr, nextc), dir)

        if sub_result:
            grid[nextr][nextc] = val
            grid[r][c] = "."
            return nextr, nextc

    return None


def _print_grid(grid: list[list[str]]):
    for l in grid:
        print("".join(l))


def _expand_grid(square: str) -> str:
    match square:
        case "#":
            return "##"
        case "@":
            return "@."
        case ".":
            return ".."
        case "O":
            return "[]"


def part2(raw_input: list[str]):
    map_dirs = parse_input(raw_input)

    mut_map = [[i for c in l for i in _expand_grid(c)] for l in map_dirs.map]
    location = _find_guy(mut_map, "@")

    dir_map = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

    for d in map_dirs.dirs:
        # _print_grid(mut_map)
        dir = dir_map[d]

        if (result := _process_move_p2(mut_map, location, dir)):
            location = result
        # input()
    print(_score_p2(mut_map))



def _process_move_p2(
    grid: list[list[str]], location: tuple[int, int], dir: tuple[int, int]
) -> tuple[int, int] | None:
    if dir[0] == 0:
        return _process_horizontal_move(grid, location, dir[1])
    
    if _process_vertical_move(grid, set([location]), dir[0]):
        return location[0] + dir[0], location[1] + dir[1]
    
    return None
    

def _process_vertical_move(grid: list[list[str]], locations: set[tuple[int, int]], v_dir: int) -> bool:
    new_locs: set[tuple[int, int]] = set()
    for l in locations:
        r, c = l
        next_r = r + v_dir

        next_val = grid[next_r][c]

        if next_val == '#':
            return False
        
        if next_val == ']':
            new_locs.add((next_r, c - 1))
            new_locs.add((next_r, c))
        
        if next_val == '[':
            new_locs.add((next_r, c + 1))
            new_locs.add((next_r, c))

    if new_locs and not _process_vertical_move(grid, new_locs, v_dir):
        return False
    
    for l in locations:
        r, c = l
        val = grid[r][c]
        grid[r + v_dir][c] = val
        grid[r][c] = '.'

    return True


def _process_horizontal_move(
    grid: list[list[str]], location: tuple[int, int], h_dir: int
) -> tuple[int, int] | None:
    # Horizontal moves CANNOT be split - operate same as p1
    r, c = location
    nextc = c + h_dir

    val = grid[r][c]

    if grid[r][nextc] == ".":
        grid[r][c] = "."
        grid[r][nextc] = val

        return r, nextc

    if grid[r][nextc] == "#":
        return None

    if _process_horizontal_move(grid, (r, nextc), h_dir):
        grid[r][c] = "."
        grid[r][nextc] = val

        return r, nextc

def _score_p2(grid: list[list[str]]):
    score = 0
    for r, l in enumerate(grid):
        for c, v in enumerate(l):
            if v == '[':
                score += r * 100 + c

    return score

def parse_input(raw_input: list[str]):
    map = [r for r in raw_input if r.startswith("#")]
    direction_lines = "".join([r for r in raw_input if r and not r.startswith("#")])

    return MapAndDirections(map=map, dirs=direction_lines)


def _find_guy(map: list[str], char: str) -> tuple[int, int]:
    for r, l in enumerate(map):
        for c, v in enumerate(l):
            if v == char:
                return r, c

    raise Exception("not here boss")


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
