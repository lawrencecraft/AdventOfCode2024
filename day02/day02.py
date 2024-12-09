def part1(lines: list[str]) -> None:
    numbers = [[int(x) for x in l.split(' ')] for l in lines]
    print(len([n for n in numbers if _is_safe(n)]))


def part2(lines: list[str]) -> None:
    numbers = [[int(x) for x in l.split(' ')] for l in lines]
    print(len([n for n in numbers if _is_safe_with_dampener(n)]))


def _is_safe_with_dampener(nums: list[int]) -> bool:
    if _is_safe(nums):
        return True

    # Dampen each number
    for i, _ in enumerate(nums):
        new_list = nums[:i] + nums[i+1:]

        if _is_safe(new_list):
            return True

    return False


def _is_safe(nums: list[int]) -> bool:
    if nums != sorted(nums) and nums != sorted(nums, reverse=True):
        return False

    for idx, val in enumerate(nums[:-1]):
        d = nums[idx + 1] - val
        if abs(d) > 3 or abs(d) < 1:
            return False

    return True


def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
