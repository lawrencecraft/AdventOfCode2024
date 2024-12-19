from collections import deque

GRID_MAX_DIM = 70

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(raw_input):
    byte_take = 1024
    print(_traverse_maze([_parse_point(p) for p in raw_input][:byte_take]))


def part2(raw_input):
    points = [_parse_point(p) for p in raw_input]

    low = 1024
    hi = len(points)

    while low != hi:
        mid = (low + hi) // 2

        if _traverse_maze(points[:mid]):
            low = mid + 1
        else:
            hi = mid

    print(points[low - 1])


def _traverse_maze(obstacle_list: list[tuple[int, int]]) -> int | None:
    obstacles = set(obstacle_list)
    visited: set[tuple[int, int]] = set()
    target = (GRID_MAX_DIM, GRID_MAX_DIM)

    visit_queue = deque([(0, (0, 0))])

    while visit_queue:
        steps, (r, c) = visit_queue.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if (r, c) == target:
            return steps

        for dr, dc in DIRECTIONS:
            next_r = r + dr
            next_c = c + dc

            if _is_ib(next_r, next_c) and (next_r, next_c) not in obstacles:
                visit_queue.append((steps + 1, (next_r, next_c)))

    return None


def _parse_point(s: str) -> tuple[int, int]:
    r, c = s.split(",")
    return int(r), int(c)


def _is_ib(r: int, c: int):
    return 0 <= r <= GRID_MAX_DIM and 0 <= c <= GRID_MAX_DIM


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
