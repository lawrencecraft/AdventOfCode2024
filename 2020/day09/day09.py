def part1(input: list[str]) -> int:
    preamble_length = 25

    nums = [int(x) for x in input]

    for idx, n in enumerate(nums[preamble_length:], start=preamble_length):
        preamble = nums[idx - preamble_length:idx]

        all_sums = set()

        for i in preamble:
            for j in preamble:
                all_sums.add(i + j)

        if n not in all_sums:
            print(n)
            return n
    print("NOT FOUND")


def part2(input: list[str], target: int):
    cum_sum = []
    nums = [int(x) for x in input]

    acc = 0
    for n in nums:
        acc += n
        cum_sum.append(acc)

    for idx_hi, i in enumerate(cum_sum):
        if i < target:
            continue

        if nums[idx_hi] == target:
            continue

        num_to_find = i - target

        for idx_lo, j in enumerate(cum_sum[:idx_hi]):
            if j == num_to_find:
                range = nums[idx_lo+1:idx_hi+1]

                print(min(range) + max(range))
                return

    
    print("done")


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    first_num = part1(stripped_input)
    part2(stripped_input, first_num)


if __name__ == "__main__":
    main()
