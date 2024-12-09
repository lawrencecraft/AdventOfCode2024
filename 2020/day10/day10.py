from collections import defaultdict

def part1(lines: list[str]) -> None:
    nums = [int(x) for x in lines]
    nums.append(0)
    sorted_nums = sorted(nums)

    joltages = [0, 0, 0]

    for idx, v in enumerate(sorted_nums[:-1]):
        diff = sorted_nums[idx + 1] - v - 1
        joltages[diff] += 1
    
    joltages[2] += 1
    print(joltages[0] * joltages[2])


def part2(lines: list[str]) -> None:
    nums = [int(x) for x in lines] 

    sorted_nums = sorted(nums)

    cache = defaultdict(int)

    cache[0] = 1

    for n in sorted_nums:
        cache[n] = cache[n - 1] + cache[n - 2] + cache[n - 3]

    print(cache[sorted_nums[-1]])



def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
