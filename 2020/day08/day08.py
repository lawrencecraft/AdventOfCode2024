def part1(lines: list[str]) -> None:
    visited_map = [False for _ in lines]

    acc = 0
    instruction_pointer = 0

    while True:
        if visited_map[instruction_pointer]:
            print(acc)
            return
        
        visited_map[instruction_pointer] = True

        instruction_increment = 1

        instruction = lines[instruction_pointer]
        op, val_raw = instruction.split(' ')
        val = parse_number(val_raw)

        if op == 'acc':
            acc += val

        if op == 'jmp':
            instruction_increment = val

        instruction_pointer += instruction_increment


def part2(lines: list[str]) -> None:

    visited_map = [False for _ in lines]

    acc = 0
    instruction_pointer = 0

    while True:
        if visited_map[instruction_pointer]:
            break
        
        visited_map[instruction_pointer] = True

        instruction_increment = 1

        instruction = lines[instruction_pointer]
        op, val_raw = instruction.split(' ')
        val = parse_number(val_raw)

        if op == 'acc':
            acc += val

        if op == 'jmp':
            instruction_increment = val

        instruction_pointer += instruction_increment

    candidate_instructions = [idx for idx, i in enumerate(lines) if visited_map[idx] and (i.startswith('nop') or i.startswith('jmp'))]

    for c in candidate_instructions:
        val = _run_program(lines, c)

        if val is not None:
            print(val)
            return
    
    print("NONE FOUND")

def _run_program(lines: list[str], override_index: int) -> int | None:
    visited_map = [False for _ in lines]

    acc = 0
    instruction_pointer = 0

    while instruction_pointer < len(lines):
        if visited_map[instruction_pointer]:
            return None
        
        visited_map[instruction_pointer] = True

        instruction_increment = 1

        instruction = lines[instruction_pointer]
        op, val_raw = instruction.split(' ')
        val = parse_number(val_raw)

        if op == 'acc':
            acc += val

        if (op == 'jmp' and override_index != instruction_pointer) or (op == 'nop' and override_index == instruction_pointer):
            instruction_increment = val

        instruction_pointer += instruction_increment


    return acc

def parse_number(n: str) -> int:
    base_num = int(n[1:])
    if n[0] == '-':
        return -base_num
    
    return base_num



def main():
    with open("input", 'r') as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
