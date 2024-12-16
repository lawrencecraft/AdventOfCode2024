import heapq


def execute(raw_input: list[str]):
    for p in visit_map(raw_input):
        print(p)


def visit_map(raw_input: list[str]) -> tuple[int, int]:
    target = _find_guy(raw_input, "E")
    start = _find_guy(raw_input, "S")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    initial_state = (0, (0, start[0], start[1]), None)

    queue = [initial_state]

    visited: dict[tuple[int, int, int], int] = {}
    prev: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {
        initial_state[1]: []
    }

    winning_score: int | None = None

    while queue:
        score, current_node, prev_node = heapq.heappop(queue)

        if winning_score and score > winning_score:
            break

        (direction, r, c) = current_node

        if current_node in visited:
            if score == visited[current_node]:
                prev[current_node].append(prev_node)
            continue

        visited[current_node] = score
        if prev_node is not None:
            prev[current_node] = [prev_node]

        if (r, c) == target:
            winning_score = score
            break

        dr, dc = directions[direction]

        if raw_input[dr + r][dc + c] != "#":
            heapq.heappush(
                queue, (score + 1, (direction, r + dr, c + dc), current_node)
            )

        for i in [-1, 1]:
            next_dir = (direction + i) % len(directions)

            heapq.heappush(queue, (score + 1000, (next_dir, r, c), current_node))

    points: set[tuple[int, int]] = set()
    nodes = [k for k in prev if (k[1], k[2]) == target]

    while nodes:
        node = nodes.pop()
        points.add((node[1], node[2]))

        nodes.extend(prev[node])

    return winning_score, len(points)


def _find_guy(map: list[str], char: str) -> tuple[int, int]:
    for r, l in enumerate(map):
        for c, v in enumerate(l):
            if v == char:
                return r, c

    raise Exception("not here boss")


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    execute(stripped_input)


if __name__ == "__main__":
    main()
