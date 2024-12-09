import re
from collections import defaultdict

def part1(input: list[str]) -> None:
    bag_rules = [_parse_bag_line(l) for l in input]

    target_bag = 'shiny gold'

    bag_to_parent = defaultdict(set)

    for source_bag, sub_bags in bag_rules:
        for sub_bag, _ in sub_bags:
            bag_to_parent[sub_bag].add(source_bag)

    found_parents = set()
    possibilities = [target_bag]

    while possibilities:
        current_bag = possibilities.pop()
        parents = bag_to_parent[current_bag]

        for p in parents:
            if p not in found_parents:
                possibilities.append(p)
                found_parents.add(p)
    
    # found_parents.remove(target_bag)

    print(len(found_parents))



def part2(input: list[str]) -> None:
    bag_rules = dict(_parse_bag_line(l) for l in input)
    print(_calc_bag_count({}, bag_rules, 'shiny gold'))

def _calc_bag_count(bag_count_map: dict[str, int], bag_map: dict[str, list[tuple[str, int]]], bag: str) -> int:
    if bag in bag_count_map:
        return bag_count_map[bag]
    
    sub_bags = bag_map[bag]

    total_sub_bags = 0

    for sub_bag, count in sub_bags:
        # Add each bag
        total_sub_bags += count
        containing_bags = _calc_bag_count(bag_count_map, bag_map, sub_bag)

        total_sub_bags += containing_bags * count

    bag_count_map[bag] = total_sub_bags
    return total_sub_bags


def _parse_bag_line(line: str) -> tuple[str, list[tuple[str, int]]]:
    source_bag_raw, contained_raw = line.split(' contain ')
    source_bag = _extract_bag_color(source_bag_raw)

    if contained_raw == "no other bags.":
        return (source_bag, [])
    
    bag_quants = [_extract_bag_quant(b) for b in contained_raw[:-1].split(', ')]

    return (source_bag, bag_quants)

def _extract_bag_color(bag_desc: str):
    match = re.match(r'(.+) bags?', bag_desc)

    if not match:
        raise Exception(f"No match in bag desc {bag_desc}")
    
    return match.group(1)

def _extract_bag_quant(bag_quant: str) -> tuple[str, int]:
    match = re.match(r"(\d+) (.+) bags?", bag_quant)

    if not match:
        raise Exception(f"no match in bag quant {bag_quant}")
    
    return (match.group(2), int(match.group(1)))


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
