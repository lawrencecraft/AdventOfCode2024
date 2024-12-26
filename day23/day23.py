from collections import defaultdict
from functools import cache


def part1(raw_input: list[str]):
    triangles, _ = find_triangles(raw_input)

    print(sum(1 for t in triangles if _is_target(t)))


def _is_target(triange: tuple[str, str, str]):
    for t in triange:
        if t.startswith("t"):
            return True

    return False


def part2(raw_input: list[str]):
    triangles, edges = find_triangles(raw_input)

    def bron_kerbosch(clique: set[str], p: set[str], x: set[str]):
        if not p and not x:
            return clique

        largest_clique = set()

        for v in list(p):
            result = bron_kerbosch(
                clique.union({v}), p.intersection(edges[v]), x.intersection(edges[v])
            )
            if len(result) > len(largest_clique):
                largest_clique = result

            p.remove(v)
            x.add(v)

        return largest_clique

    print(",".join(sorted(bron_kerbosch(set(), set(edges.keys()), set()))))


# def bron_kerbosch(neighbors, clique_vertices, possibilities, )


def find_triangles(
    raw_input: list[str],
) -> tuple[set[tuple[str, str, str]], dict[str, set[str]]]:
    edges: dict[str, set[str]] = defaultdict(set)
    all_edges: list[tuple[str, str]] = []

    for e in raw_input:
        s, d = e.split("-")

        edges[s].add(d)
        edges[d].add(s)

        all_edges.append((s, d))

    triangles: set[tuple[str, str, str]] = set()

    for s, d in all_edges:
        other_nodes = edges[s].intersection(edges[d])

        for e in other_nodes:
            triangles.add(tuple(sorted([e, s, d])))

    return triangles, edges


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
