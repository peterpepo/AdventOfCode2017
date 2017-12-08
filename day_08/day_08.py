from puzzle_commons.puzzle_commons import read_puzzle_input
import os, re


def solve():
    """Advent Of Code 2017 - Day 08 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    registers = {}

    def get_register_value(register_name):
        """Returns value of a register with given name.
        Register is created with value of 0, if it doesn't exist.
        For numbers, register name casted as int is returned.
        :param register_name: name of register
        :return: [int] value of register
        """
        try:
            return int(register_name)
        except ValueError:
            if register_name not in registers:
                registers[register_name] = 0

            return registers[register_name]

    """Regexp explanation: (\w+)\s(inc|dec)\s(-?\d+)\sif\s(-?(?:\d+|\w+))\s(\S+)\s(-?(?:\d+|\w+))
    (\w+)           - name of a register to modify
    \s              - space
    (inc|dec)       - literal, increase or decrease operation
    \s              - space
    (-?\d+)         - number, optionally prefixed with minus
    \sif\s          - space if space literal
    (-?(?:\d+|\w+)) - sequence of digits / characters, optionally prefixed with minus
    \s              - space
    (\S+)           - operator, sequence of non-whitespace characters
    \s              - space
    (-?(?:\d+|\w+)) - sequence of digits / characters, optionally prefixed with minus       
    """
    instruction_pattern = r"(\w+)\s(inc|dec)\s(-?\d+)\sif\s(-?(?:\d+|\w+))\s(\S+)\s(-?(?:\d+|\w+))"

    max_value_ever = None  # Maximum value ever encountered, for Part-B

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_08_input.txt"):
        # Strip newline
        puzzle_input = puzzle_input.rstrip()

        # Parse instruction
        puzzle_instruction = re.search(instruction_pattern, puzzle_input)
        if puzzle_instruction is not None:
            register_name, operation, amount, operand_one, operator, operand_two = puzzle_instruction.group(
                1), puzzle_instruction.group(2), int(puzzle_instruction.group(3)), puzzle_instruction.group(
                4), puzzle_instruction.group(5), puzzle_instruction.group(6)

            # If the condition is evaluated as True, modify register
            if eval(str(get_register_value(operand_one)) + operator + str(get_register_value(operand_two))):
                # Flip amount, if amount is to be decreaset
                if operation == "dec":
                    amount = -amount

                # Modify the value of register
                registers[register_name] = get_register_value(register_name) + amount

        # Remember max value ever encountered, for Part-B of the puzzle
        if max_value_ever is None or registers[register_name] > max_value_ever:
            max_value_ever = registers[register_name]

    return max(registers.values()), max_value_ever
