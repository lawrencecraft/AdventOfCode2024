from dataclasses import dataclass


def part1(full_input: list[str]):
    input = [int(x) for x in full_input[0]]
    disk_array = []
    total_compacted_length = 0
    for idx, x in enumerate(input):
        is_data = idx % 2 == 0
        char_to_fill = idx // 2 if is_data else "."

        disk_array.extend([char_to_fill] * x)
        total_compacted_length += x if is_data else 0

    # compact
    base_ptr = 0
    for idx, val in reversed(list(enumerate(disk_array))):
        # print(idx, val, base_ptr)
        if idx == total_compacted_length - 1:
            break

        if val == ".":
            continue

        base_ptr = next_free_space(disk_array, base_ptr)
        disk_array[idx] = "."
        disk_array[base_ptr] = val

    # print("".join(map(str, disk_array)))
    print(calc_checksum(disk_array))


def calc_checksum(disk_array: list[str | int]):
    checksum = 0

    for idx, d in enumerate(disk_array):
        if d == ".":
            continue

        checksum += idx * d

    return checksum


def next_free_space(input: list[str | int], base_ptr: int) -> int:
    while base_ptr < len(input):
        if input[base_ptr] == ".":
            return base_ptr

        base_ptr += 1

    return -1


@dataclass
class FSBlock:
    empty: bool
    length: int
    start_block: int
    id: int | None


def part2(stripped_input: list[str]):
    input = [int(x) for x in stripped_input[0]]

    blocks: list[FSBlock] = []
    start = 0
    for idx, i in enumerate(input):
        if i == 0:
            continue
        is_data = idx % 2 == 0

        blocks.append(
            FSBlock(
                empty=not is_data,
                length=i,
                id=idx // 2 if is_data else None,
                start_block=start,
            )
        )

        start += i

    for idx, d in reversed(list(enumerate(blocks))):
        if d.empty:
            continue

        for replacement_block_index, block_to_replace in enumerate(blocks):
            if not block_to_replace.empty:
                continue

            if block_to_replace.start_block > d.start_block:
                continue

            if block_to_replace.length < d.length:
                continue

            # create new block for this file
            new_blocks = blocks[:replacement_block_index]
            new_blocks.append(d)

            remaining_space = block_to_replace.length - d.length
            if remaining_space > 0:
                new_blocks.append(
                    FSBlock(
                        empty=True,
                        length=remaining_space,
                        start_block=block_to_replace.start_block + d.length,
                        id=None,
                    )
                )

            for next_block in blocks[replacement_block_index + 1 :]:
                if not next_block.empty and next_block.id != d.id:
                    new_blocks.append(next_block)
                    continue

                last_block = new_blocks[-1]

                if last_block.empty:
                    new_blocks[-1] = FSBlock(
                        empty=True,
                        length=last_block.length + next_block.length,
                        start_block=last_block.start_block,
                        id=None,
                    )
                elif next_block.empty:
                    new_blocks.append(next_block)
                else:
                    new_blocks.append(
                        FSBlock(
                            empty=True,
                            length=d.length,
                            start_block=d.start_block,
                            id=None,
                        )
                    )

            blocks = new_blocks
            break

    print(calc_block_checksum(blocks))


def _ouput_blocks(disk: list[FSBlock]):
    for d in disk:
        c = "." if d.empty else str(d.id)
        print(c * d.length, end="")

    print()

def calc_block_checksum(disk: list[FSBlock]):
    current_index = 0
    checksum = 0
    for d in disk:
        if d.empty:
            current_index += d.length
            continue

        for _ in range(d.length):
            checksum += current_index * d.id
            current_index += 1

    return checksum


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
