from collections import defaultdict
from itertools import islice
from typing import Iterator


def part1(raw_input: list[str]):
    items = [int(x) for x in raw_input]

    print(sum(nth(_process_round(i), 2000) for i in items))


def part2(raw_input: list[str]):
    items = [int(x) for x in raw_input]

    maps = [calc_highest_map(x) for x in items]

    consolidated_map: defaultdict[tuple[int, ...], int] = defaultdict(int)

    for m in maps:
        for key, max_val in m.items():
            consolidated_map[key] += max_val

    print(max(consolidated_map.values()))


def calc_highest_map(seed: int) -> dict[tuple[int, ...], int]:
    tuple_to_first_occurrence = {}

    for price, last_seq in islice(_make_window(seed), 1996):
        if last_seq not in tuple_to_first_occurrence:
            tuple_to_first_occurrence[last_seq] = price

    return tuple_to_first_occurrence


def nth(iterable, n, default=None):
    "Returns the nth item or a default value."
    return next(islice(iterable, n, None), default)


def _make_window(seed: int):
    round_digits = _process_round_digit(seed)

    rd_seq = [
        next(round_digits),
        next(round_digits),
        next(round_digits),
        next(round_digits),
        next(round_digits),
    ]

    for x in round_digits:
        yield rd_seq[-1], tuple(
            r - rd_seq[i - 1] for i, r in enumerate(rd_seq[1:], start=1)
        )

        rd_seq.append(x)
        rd_seq.pop(0)


def _process_round_digit(seed: int) -> Iterator[int]:
    for i in _process_round(seed):
        yield i % 10


def _process_round(seed: int) -> Iterator[int]:
    yield seed
    while True:
        seed = _calc_next_num(seed)
        yield seed


def _calc_next_num(seed: int) -> int:
    round_1 = ((seed * 64) ^ seed) % 16777216
    round_2 = ((round_1 // 32) ^ round_1) % 16777216
    return ((round_2 * 2048) ^ round_2) % 16777216


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
