from dataclasses import dataclass, replace


@dataclass
class Program:
    register_a: int
    register_b: int
    register_c: int
    code: list[int]


def part1(input: list[str]):
    program = parse_input(input)
    print(",".join(str(i) for i in _execute_program(program)))


def part2(raw_input: list[str]):
    program = parse_input(raw_input)
    print(_compute_quine(0, 0, program))


def _compute_quine(a: int, digit: int, program: Program) -> None | int:
    if digit == len(program.code):
        return a

    for i in range(8):
        shifted_a = (a << 3) + i
        p = replace(program, register_a=shifted_a)
        output = _execute_program(p)

        if output[0] == program.code[-(1 + digit)]:
            if result := _compute_quine(shifted_a, digit + 1, program):
                return result

    return None


def _execute_program(program: Program) -> list[int]:
    inst_pointer = 0
    output = []

    while inst_pointer < len(program.code):
        opcode = program.code[inst_pointer]
        operand = program.code[inst_pointer + 1]

        match opcode:
            case 0:  # adv
                denom = 2 ** _resolve_combo_operand(program, operand)
                program.register_a = program.register_a // denom

            case 1:  # bxl
                program.register_b = program.register_b ^ operand

            case 2:  # bst
                program.register_b = _resolve_combo_operand(program, operand) % 8

            case 3:  # jnz
                if program.register_a:
                    inst_pointer = operand
                    continue

            case 4:  # bxc
                program.register_b = program.register_b ^ program.register_c

            case 5:  # out
                value = _resolve_combo_operand(program, operand) % 8
                output.append(value)

            case 6:  # bdv
                denom = 2 ** _resolve_combo_operand(program, operand)
                program.register_b = program.register_a // denom

            case 7:  # bdv
                denom = 2 ** _resolve_combo_operand(program, operand)
                program.register_c = program.register_a // denom

        inst_pointer += 2

    return output


def _resolve_combo_operand(program: Program, value: int) -> int:
    match value:
        case 1 | 2 | 3:
            return value

        case 4:
            return program.register_a

        case 5:
            return program.register_b

        case 6:
            return program.register_c

        case _:
            raise Exception(f"Got unexpected combo operand {value}")


def parse_input(input: list[str]):
    a = input[0].split(": ")[1]
    b = input[1].split(": ")[1]
    c = input[2].split(": ")[1]

    program = input[4].split(": ")[1].split(",")

    return Program(
        register_a=int(a),
        register_b=int(b),
        register_c=int(c),
        code=[int(x) for x in program],
    )


def main():
    with open("input", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()
