def part1(input: list[str]) -> None:
    print(sum(len(set(''.join(s))) for s in _extract_groups(input)))
        


def part2(input: list[str]) -> None:
    print(sum(_get_intersections(g) for g in _extract_groups(input)))

def _get_intersections(group: list[str]):
    sets = [set(l) for l in group]

    return len(set.intersection(*sets))

def _extract_groups(lines: list[str]):
    current_list: list[str] = []

    for l in lines:
        if not l:
            yield current_list
            current_list = []
            continue

        current_list.append(l)
    
    if current_list:
        yield current_list

def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
